import time
import threading


class PhoneStation:
    def __init__(self):
        self.ladies = [threading.Lock() for _ in range(6)]
        self.lines = [threading.Lock() for _ in range(2)]
        self.calls_completed = 0

    def call_friend(self, friend):
        for i in range(2):
            if self.ladies[i].acquire(blocking=False) and self.lines[i].acquire(blocking=False):
                self._make_call(friend, f"Line {i+1}", f"Lady {i+1}")
                return
        self._wait_and_call(friend)

    def _make_call(self, friend, line, lady):
        print(f"Friend {friend} is talking on {line} with {lady}")
        time.sleep(1)
        print(f"Friend {friend} has finished the call")
        self.calls_completed += 1
        self._release_line(line, lady)

    def _release_line(self, line, lady):
        line_index = int(line.split()[-1]) - 1
        lady_index = int(lady.split()[-1]) - 1
        self.lines[line_index].release()
        self.ladies[lady_index].release()

    def _wait_and_call(self, friend):
        while True:
            for i in range(2):
                if self.ladies[i].acquire(blocking=False) and self.lines[i].acquire(blocking=False):
                    self._make_call(friend, f"Line {i+1}", f"Lady {i+1}")
                    return
            time.sleep(1)


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
