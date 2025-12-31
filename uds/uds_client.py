class UdsClient:

    def __init__(self):
        self.session = "default"
        self.security_unlocked = False

    def set_default_session(self):
        self.session = "default"

    def set_extended_session(self):
        self.session = "extended"

    def send_request(self, request):

        # Diagnostic Session Control
        if request == "10 03" and self.session == "default":
            self.session = "extended"
            return "50 03"
        if request.startswith("10"):
            return "7F 10 12"

        # ECU Reset
        if request == "11 01":
            if self.session == "extended":
                return "51 01"
            return "7F 11 7E"

        # Read DID
        if request == "22 F1 90":
            return "62 F1 90 56 49 4E"
        if request.startswith("22"):
            return "7F 22 31"

        # Write DID
        if request.startswith("2E"):
            return "7F 2E 33"

        # Security Access
        if request == "27 01":
            return "67 01 AB CD"
        if request.startswith("27 02"):
            return "7F 27 35"

        # Routine Control (long processing)
        if request.startswith("31"):
            return "7F 31 78"

        return "7F 10 11"
