import time
import threading

try:
    import explorerhat
    hardware = True
except:
    hardware = False

DIST_PER_ROTATION_M = (2.0 * 3.1415 * 19.0) / 100.0


class Elliptical(object):
    def _read_sensor():
        return explorerhat.input.three.read()

    def _hardware_loop(self):
        while True:
            start_time = time.time()
            while _read_sensor():
                pass
            while _read_sensor() == False:
                pass
            end_time = time.time()
            diff = end_time - start_time
            self.speed_RPM = (60 / diff)
            self.num_rotations += 1

    def __init__(self):
        self.num_rotations = 0
        self.speed_RPM = 0
        if hardware:
            threading.Thread(target=self._hardware_loop()).start()

    def get_speed(self):
        return self.speed_RPM

    def get_distance(self):
        return self.num_rotations * DIST_PER_ROTATION_M
