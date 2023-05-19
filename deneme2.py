import time
from threading import Lock, Thread

class PhoneStation:
    def __init__(self):
        self.lady1 = Lock()
        self.lady2 = Lock()
        self.line1 = Lock()
        self.line2 = Lock()
        self.calls_completed = 0

    def call_friend_a(self, friend_a):
        if self.lady1.acquire(False) and self.line1.acquire(False):
            self.make_call(friend_a, "Line 1", "Lady 1")
        elif self.lady2.acquire(False) and self.line2.acquire(False):
            self.make_call(friend_a, "Line 2", "Lady 2")
        else:
            self.wait_and_call(friend_a)

    def call_friend_b(self, friend_b):
        if self.lady1.acquire(False) and self.line1.acquire(False):
            self.make_call(friend_b, "Line 1", "Lady 1")
        elif self.lady2.acquire(False) and self.line2.acquire(False):
            self.make_call(friend_b, "Line 2", "Lady 2")
        else:
            self.wait_and_call(friend_b)

    def make_call(self, friendA,friendB, line, lady):
        print(f"Friend {friendA} is talking on {line} with {lady}")
        time.sleep(1)  # Simulating the duration of the phone call.
        print(f"Friend {friendB} has finished the call")
        time.sleep(1)
        self.calls_completed += 1
        self.release_line(line, lady)

    def release_line(self, line, lady):
        if line == "Line 1":
            self.line1.release()
            self.lady1.release()
        else:
            self.line2.release()
            self.lady2.release()

    def wait_and_call(self, friend):
        while True:
            if self.lady1.acquire(False):
                if self.line1.acquire(False):
                    self.make_call(friend, "Line 1", "Lady 1")
                    break
                else:
                    self.lady1.release()
            elif self.lady2.acquire(False):
                if self.line2.acquire(False):
                    self.make_call(friend, "Line 2", "Lady 2")
                    break
                else:
                    self.lady2.release()
            else:
                time.sleep(1)  # Waiting for a lady to become available.

def main():
    station = PhoneStation()

    # Simulating the phone calls from side A to side B.
    threads_a = []
    for friend_a in range(1, 7):
        thread_a = Thread(target=station.call_friend_a, args=(friend_a,))
        threads_a.append(thread_a)
        thread_a.start()

    # Simulating the phone calls from side B to side A.
    threads_b = []
    for friend_b in range(1, 7):
        thread_b = Thread(target=station.call_friend_b, args=(friend_b,))
        threads_b.append(thread_b)
        thread_b.start()

    # Wait for all threads to complete.
    for thread_a in threads_a:
        thread_a.join()

    for thread_b in threads_b:
        thread_b.join()

    # Checking if all calls are completed.
    if station.calls_completed == 36:
        print("All phone calls have been completed.")
    else:
        print("Some phone calls were not completed.")

    print("--------------The Program is Finished--------------")

if __name__ == "__main__":
    main()
