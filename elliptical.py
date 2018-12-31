import time
import explorerhat

def read_sensor():
   return explorerhat.input.three.read()

DIST_PER_ROTATION_M = ((2.0 * 3.1415 * 19.0) / 100.0)
num_rotations = 0

while True:
     start_time = time.time()
     while read_sensor():
        pass
     while read_sensor()== False:
        pass
     end_time = time.time()
     diff = end_time- start_time
     speed_RPM = (60/ diff)
     num_rotations += 1
     distance_m = num_rotations * DIST_PER_ROTATION_M
     print("{0} RPM - {1} m".format(int(speed_RPM), distance_m))
