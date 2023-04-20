# Angle in Radians × 180°/π = Angle in Degrees
import math

def rad_to_deg (radian):
    degree = (radian * (180 / math.pi))
    # print(degree)
    print('The degrees of a radian of ' + str(radian) + ' is ' + str(degree))

rad_to_deg(45)