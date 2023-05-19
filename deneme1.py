import time
import threading


#using Thhreads
class PhoneStation:
    def __init__(self):#Lock nesneleri oluşturdum.
        self.lady1 = threading.Lock()
        self.lady2 = threading.Lock()
        self.line1 = threading.Lock()
        self.line2 = threading.Lock()
        self.calls_completed = 0



    # Arkadaşın aramasını yapmak için bu metot kullanılır
    # Eğer Bayan 1 ve Hat 1 kullanılabilir durumdaysa, arama gerçekleştirilir.
    def call_friend(self, friend):
        if self.lady1.acquire(blocking=False) and self.line1.acquire(blocking=False):
            self._make_call(friend, "Line 1", "Lady 1")
        elif self.lady2.acquire(blocking=False) and self.line2.acquire(blocking=False):
            self._make_call(friend, "Line 2", "Lady 2")
        else:
            self._wait_and_call(friend)



    #Arama gerçekleştirme işlemini simüle etmek için kullanılır.
    def _make_call(self, friend, line, lady):
        print(f"Friend {friend} is talking on {line} with {lady}")
        time.sleep(1)  # Simulating the duration of the phone call.
        print(f"Friend {friend} has finished the call")
        self.calls_completed += 1
        self._release_line(line, lady)



    # Kullanılan hat ve bayan kilidi serbest bırakılır
    def _release_line(self, line, lady):
        if line == "Line 1":
            self.line1.release()
            self.lady1.release()
        else:
            self.line2.release()
            self.lady2.release()



    # Bekleme işlemi gerçekleştirilir.
    def _wait_and_call(self, friend):#wait operation opject.
        while True:
            if self.lady1.acquire(blocking=False):
                if self.line1.acquire(blocking=False):
                    self._make_call(friend, "Line 1", "Lady 1")
                    break
                else:
                    self.lady1.release()
            elif self.lady2.acquire(blocking=False):
                if self.line2.acquire(blocking=False):
                    self._make_call(friend, "Line 2", "Lady 2")
                    break
                else:
                    self.lady2.release()
            else:
                time.sleep(1)  # Waiting for a lady to become available.


station = PhoneStation()

# Simulating the phone calls from side A to side B.
threads = []
for friend in range(1, 7):
    for _ in range(6):
        thread = threading.Thread(target=station.call_friend, args=(friend,))
        threads.append(thread)
        thread.start()

# Wait for all threads to complete.
for thread in threads:
    thread.join()

# Checking if all calls are completed.
if station.calls_completed == 36:
    print("All phone calls have been completed.")
else:
    print("Some phone calls were not completed.")

print("-----------------The Program is Finished----------------")
