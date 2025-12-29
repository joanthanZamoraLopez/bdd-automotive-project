class ECUSimulator:
    def __init__(self):
        self.session = "default"
        self.vin = "1HGBH41JXMN109186"

    def set_session(self, session):
        self.session = session

    def read_did(self, did):
        if did == "F190":
            return self.vin
        else:
            raise ValueError("DID not supported")
