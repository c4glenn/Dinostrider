import time
try:
    import explorerhat
except:
    pass

DIST_PER_ROTATION = (2.0 * 3.1415 * 19.0) / 100.0


class elliptical(object):
    def __init__(self):
        self.num_rotations = 0
        self.distance_m = 0
        self.speed_RPM = 0

    def read_sensor():
        return explorerhat.input.three.read()

    def get_value(self):
        try:
            while True:
                start_time = time.time()
                while read_sensor():
                    pass
                while read_sensor() == False:
                    pass
                end_time = time.time()
                diff = end_time - start_time
                self.speed_RPM = (60 / diff)
                self.num_rotations += 1
                self.distance_m = num_rotations * DIST_PER_ROTATION_M
                return ([self.speed_RPM, self.distance_m])
                print("{0} RPM - {1} m".format(
                    int(speed_RPM), self.distance_m))

        except:
            return ([321, 321])
