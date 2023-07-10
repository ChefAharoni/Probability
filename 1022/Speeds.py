def arc_length(s, r):
    """
    The radian measure Theta of a rotation is the ratio of the distance 'S', travelled by a point at a radius 'R' from
    the center of rotation to the length of the radius 'R'.
    @param s: Distance travelled
    @param r: Radius from the center of rotation.
    @return:
    """
    theta = s / r
    return theta


def linear_speed(s, t):
    """
    Linear speed is defined to be the distance travelled per unit of time. If we use 'V' for linear speed,
    'S' for distance, and 'T' for time then: V=(S/T)
    @param s:
    @param t:
    @return:
    """
    v = s / t
    return v


def angular_speed(theta, t):
    """
    Angular speed is defined to be the amount of rotation per unit of time. The greek letter Omega is generally used
    for angular speed. Thus for a rotation 'Theta' and time 'T', we have angular speed defined as: Omega=(Theta/T)
    @param theta:
    @param t:
    @return:
    """
    omega = theta / t
    return omega


def linear_in_angular_speed(r, omega):
    """
    Linear Speed in Terms of Angular Speed - the linear speed 'V', of a point of distance 'R', from the center of
    rotation is given by v=r*omega; Where omega is the angular speed in radians per unit of time.
    @param r:
    @param omega:
    @return:
    """
    v = r * omega
    return v
