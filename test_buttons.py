import time
import threading

try:
    import explorerhat
    hardware = True
except:
    hardware = False


class Button(object):
    def __init__(self, port):
        self.port = port
        self.state = False
        self.thread = None
        # if hardware:
        # self.thread = threading.Thread(target=self._hardware_loop)
        # self.thread.stopped = False
        # self.thread.start()

    def _read_sensor(self):
        if self.port == 1:
            return explorerhat.input.one.read()
        if self.port == 2:
            return explorerhat.input.two.read()
        if self.port == 3:
            return explorerhat.input.three.read()
        if self.port == 4:
            return explorerhat.input.four.read()

    def _hardware_loop(self):
        while not self.thread.stopped:
            while self._read_sensor():
                if self.thread.stopped:
                    return
                self.state = True
            while self._read_sensor() == False:
                if self.thread.stopped:
                    return
                self.state = False

    def get_state(self):
        if hardware:
            return self._read_sensor()
        return self.state

    def stop(self):
        if hardware:
            self.thread.stopped = True


if __name__ == "__main__":
    elliptical = Button('two')
