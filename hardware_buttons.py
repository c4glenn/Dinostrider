try:
    import explorerhat
    HARDWARE = True
except ImportError:
    HARDWARE = False


class Button(object):
    def __init__(self, port):
        self.port = port

    def _read_sensor(self):
        if self.port == 1:
            return explorerhat.input.one.read()
        if self.port == 2:
            return explorerhat.input.two.read()
        if self.port == 3:
            return explorerhat.input.three.read()
        return explorerhat.input.four.read()

    def get_state(self):
        if HARDWARE:
            return self._read_sensor()
        return 0
