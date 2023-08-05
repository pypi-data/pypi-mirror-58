import math


class RightTriangle:
    def __init__(
            self,
            a: float = None,
            b: float = None,
            c: float = None,
            a_angle: float = None,
            b_angle: float = None):
        self._a = a
        self._b = b
        self._c = c
        self._a_angle = a_angle
        self._b_angle = b_angle
        self._parameters = (a, b, c, a_angle, b_angle)

        if self._a and self._b:
            self._c = self._calculate_hypotenuse_from_legs(self._a, self._b)
            self._raise_error_if_parameter_inconsistent(c, self._c)
            self._calculate_angles()
        elif self._a and self._c:
            self._b = self._calculate_leg_from_other_leg_and_hypotenuse(
                self._a, self._c)
            self._raise_error_if_parameter_inconsistent(b, self._b)
            self._calculate_angles()
        elif self._b and self._c:
            self._a = self._calculate_leg_from_other_leg_and_hypotenuse(
                self._b, self._c)
            self._raise_error_if_parameter_inconsistent(a, self._a)
            self._calculate_angles()
        elif self._a and self._a_angle:
            self._b = self._calculate_leg_from_other_leg_and_adjacent_angle(
                self._a, self._a_angle)
            self._raise_error_if_parameter_inconsistent(b, self._b)
            self._c = self._calculate_hypotenuse_from_legs(self._a, self._b)
            self._raise_error_if_parameter_inconsistent(c, self._c)
            self._b_angle = self._calculate_acute_angle_from_other_acute_angle(
                self._a_angle)
            self._raise_error_if_parameter_inconsistent(b_angle, self._b_angle)
        elif self._b and self._a_angle:
            self._a = self._calculate_leg_from_other_leg_and_opposed_angle(
                self._b, self._a_angle)
            self._raise_error_if_parameter_inconsistent(b, self._b)
            self._c = self._calculate_hypotenuse_from_legs(self._a, self._b)
            self._raise_error_if_parameter_inconsistent(c, self._c)
            self._b_angle = self._calculate_acute_angle_from_other_acute_angle(
                self._a_angle)
            self._raise_error_if_parameter_inconsistent(b_angle, self._b_angle)
        elif self._c and self._a_angle:
            self._a = self._calculate_leg_from_hypotenuse_and_opposed_angle(
                self._c, self._a_angle)
            self._raise_error_if_parameter_inconsistent(a, self._a)
            self._b = self._calculate_leg_from_other_leg_and_hypotenuse(
                self._a, self._c)
            self._raise_error_if_parameter_inconsistent(b, self._b)
            self._b_angle = self._calculate_acute_angle_from_other_acute_angle(
                self._a_angle)
            self._raise_error_if_parameter_inconsistent(b_angle, self._b_angle)
        elif self._a and self._b_angle:
            self._a_angle = self._calculate_acute_angle_from_other_acute_angle(
                self._b_angle)
            self._raise_error_if_parameter_inconsistent(a_angle, self._a_angle)
            self._b = self._calculate_leg_from_other_leg_and_adjacent_angle(
                self._a, self._a_angle)
            self._raise_error_if_parameter_inconsistent(b, self._b)
            self._c = self._calculate_hypotenuse_from_legs(self._a, self._b)
            self._raise_error_if_parameter_inconsistent(c, self._c)
        elif self._b and self._b_angle:
            self._a_angle = self._calculate_acute_angle_from_other_acute_angle(
                self._b_angle)
            self._raise_error_if_parameter_inconsistent(a_angle, self._a_angle)
            self._a = self._calculate_leg_from_other_leg_and_opposed_angle(
                self._b, self._a_angle)
            self._raise_error_if_parameter_inconsistent(b, self._b)
            self._c = self._calculate_hypotenuse_from_legs(self._a, self._b)
            self._raise_error_if_parameter_inconsistent(c, self._c)
        elif self._c and self._b_angle:
            self._a_angle = self._calculate_acute_angle_from_other_acute_angle(
                self._b_angle)
            self._raise_error_if_parameter_inconsistent(a_angle, self._a_angle)
            self._a = self._calculate_leg_from_hypotenuse_and_opposed_angle(
                self._c, self._a_angle)
            self._raise_error_if_parameter_inconsistent(a, self._a)
            self._b = self._calculate_leg_from_other_leg_and_hypotenuse(
                self._a, self._c)
            self._raise_error_if_parameter_inconsistent(b, self._b)
        else:
            raise ValueError(f"Insufficient parameters for a RightTriangle:\n"
                             + self._parameters_to_string(*self._parameters))

    @property
    def a(self) -> float:
        return self._a

    @property
    def b(self) -> float:
        return self._b

    @property
    def c(self) -> float:
        return self._c

    @property
    def a_angle(self) -> float:
        return self._a_angle

    @property
    def b_angle(self) -> float:
        return self._b_angle

    @staticmethod
    def _calculate_leg_from_other_leg_and_hypotenuse(other_leg, hypotenuse):
        leg = math.sqrt(hypotenuse ** 2 - other_leg ** 2)
        return leg

    @staticmethod
    def _calculate_hypotenuse_from_legs(leg_a, leg_b):
        hypotenuse = math.sqrt(leg_a ** 2 + leg_b ** 2)
        return hypotenuse

    @staticmethod
    def _calculate_leg_from_other_leg_and_adjacent_angle(
            other_leg, adjacent_angle):
        leg = other_leg / math.tan(math.radians(adjacent_angle))
        return leg

    @staticmethod
    def _calculate_acute_angle_from_other_acute_angle(other_acute_angle):
        angle = 90 - other_acute_angle
        return angle

    @staticmethod
    def _calculate_leg_from_other_leg_and_opposed_angle(
            other_leg, opposed_angle):
        leg = other_leg * math.tan(math.radians(opposed_angle))
        return leg

    @staticmethod
    def _calculate_leg_from_hypotenuse_and_opposed_angle(
            hypotenuse, opposed_angle):
        leg = hypotenuse * math.sin(math.radians(opposed_angle))
        return leg

    def _calculate_angles(self):
        self._a_angle = math.degrees(math.asin(self.a / self.c))
        self._b_angle = self._calculate_acute_angle_from_other_acute_angle(
            self._a_angle)

    def _raise_error_if_parameter_inconsistent(
            self, parameter_value, expected_value):
        if (parameter_value is not None
                and parameter_value != expected_value):
            raise ValueError(f"Inconsistent parameters for a RightTriangle:\n"
                             + self._parameters_to_string(*self._parameters))

    @staticmethod
    def _parameters_to_string(a, b, c, a_angle, b_angle):
        return (f"\ta = {a}\n"
                + f"\tb = {b}\n"
                + f"\tc = {c}\n"
                + f"\ta_angle = {a_angle}\n"
                + f"\tb_angle = {b_angle}")

    def __str__(self):
        return (f"RightTriangle"
                + f"\n\ta = {self.a}"
                + f"\n\tb = {self.b}"
                + f"\n\tc = {self.c}"
                + f"\n\tA = {self.a_angle: .2f}°"
                + f"\n\tB = {self.b_angle: .2f}°")
