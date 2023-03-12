import math

def coord_distance(position_one:[int,int] ,position_two:[int,int] ) -> int:
    ## c^2 = a^2 + c^2
    postion_one_x = position_one[0] #150
    position_two_x = position_two[0] #130
    postion_one_y = position_one[1] #30
    position_two_y = position_two[1] #15
    a = postion_one_y-position_two_y
    b = postion_one_x-position_two_x
    cSquared = a*a + b*b
    c = math.sqrt(cSquared)

def speed(distance:int ) -> float:
    METERS_PER_MINUTE = 4996541
    print(meters_per_minute)
    return distance/meters_per_minute


