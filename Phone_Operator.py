import time

class PhoneStation:
    def __init__(self):
        self.lady1_busy = False
        self.lady2_busy = False
        self.line1_busy = False
        self.line2_busy = False
        self.calls_completed = 0

    def call_friend(self, friend):
        if not self.lady1_busy and not self.line1_busy:
            self.lady1_busy = True
            self.line1_busy = True
            self._make_call(friend, "Line 1", "Lady 1")
        elif not self.lady2_busy and not self.line2_busy:
            self.lady2_busy = True
            self.line2_busy = True
            self._make_call(friend, "Line 2", "Lady 2")
        else:
            self._wait_and_call(friend)

    def _make_call(self, friend, line, lady):
        print(f"Friend {friend} is talking on {line} with {lady}")
        time.sleep(1)  # Simulating the duration of the phone call
        print(f"Friend {friend} has finished the call")
        self.calls_completed += 1
        if line == "Line 1":
            self.line1_busy = False
            self.lady1_busy = False
        else:
            self.line2_busy = False
            self.lady2_busy = False

    def _wait_and_call(self, friend):
        while True:
            if not self.lady1_busy:
                self.lady1_busy = True
                self._make_call(friend, "Line 1", "Lady 1")
                break
            elif not self.lady2_busy:
                self.lady2_busy = True
                self._make_call(friend, "Line 2", "Lady 2")
                break
            else:
                time.sleep(1)  # Waiting for a lady to become available


station = PhoneStation()

# Simulating the phone calls from side A to side B
for friend in range(1, 7):
    for _ in range(6):
        station.call_friend(friend)

# Checking if all calls are completed
if station.calls_completed == 36:
    print("All phone calls have been completed.")
else:
    print("Some phone calls were not completed.")

