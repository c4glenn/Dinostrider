import time
import threading

try:
    import explorerhat
    HARDWARE = True
except ImportError:
    HARDWARE = False

DIST_PER_ROTATION_M = (2.0 * 3.1415 * 19.0) / 100.0


class Elliptical(object):
    def _read_sensor(self):
        return explorerhat.input.three.read()

    def _hardware_loop(self):
        while not self.thread.stopped:
            start_time = time.time()

            print(self._read_sensor())
            while self._read_sensor() >= 0.5:
                pass
            while self._read_sensor() <= 0.5:
                pass

            while self._read_sensor():
                if self.thread.stopped:
                    return
            while not self._read_sensor():
                if self.thread.stopped:
                    return

            end_time = time.time()
            diff = end_time - start_time
            self.speed_RPM = (60 / diff)
            self.num_rotations += 1

    def __init__(self):
        self.num_rotations = 0
        self.speed_RPM = 0  #pylint:disable=invalid-name
        self.thread = None
        if HARDWARE:
            self.thread = threading.Thread(target=self._hardware_loop)
            self.thread.stopped = False
            self.thread.start()

    def get_speed(self):
        return self.speed_RPM

    def get_distance(self):
        return self.num_rotations * DIST_PER_ROTATION_M

    def stop(self):
        if HARDWARE:
            self.thread.stopped = True


if __name__ == "__main__":
    ELLIPTICAL = Elliptical()
    print("Init finished")
    while True:
        print("Speed: {0} Distance {1}".format(
            int(ELLIPTICAL.get_speed()), int(ELLIPTICAL.get_distance())))
        time.sleep(1)
