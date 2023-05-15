import time

class PhoneStation:
    def __init__(self):
        self.lady1 = False
        self.lady2 = False
        self.line1 = False
        self.line2 = False
        self.calls_completed = 0

    def make_call(self, friend):
        while True:
            if not self.lady1:
                self.lady1 = True
                self.line1 = True
                self._establish_call(friend, "Line 1", "Lady 1")
                break
            elif not self.lady2:
                self.lady2 = True
                self.line2 = True
                self._establish_call(friend, "Line 2", "Lady 2")
                break
            else:
                time.sleep(1)

    def _establish_call(self, friend, line, lady):
        print(f"Friend {friend} is talking on {line} with {lady}")
        time.sleep(1)
        print(f"Friend {friend} has finished the call")
        self.calls_completed += 1
        self._release_line(line, lady)

    def _release_line(self, line, lady):
        if line == "Line 1":
            self.line1 = False
            self.lady1 = False
        else:
            self.line2 = False
            self.lady2 = False


station = PhoneStation()

for friend in range(1, 7):
    for _ in range(6):
        station.make_call(friend)

if station.calls_completed == 36:
    print("All phone calls have been completed.")
else:
    print("Some phone calls were not completed.")
