# Right Triangle

Simple Python package that can be used to do calculations with
right-angled triangles

## Installation

Use pip to install right-triangle.

```shell script
pip install right-triangle
```

## Usage

### The RightTriangle instance

A RightTriangle instance has 5 attributes:

1. a - the length of the first leg of the triangle
1. b - the length of the second leg of the triangle
1. c - the length of the hypotenuse of the triangle
1. a_angle - the angle opposed to leg _a_, measured in degrees
1. b_angle - the angle opposed to leg _b_, measured in degrees

You can instantiate a RightTriangle with the following information:

- The lengths of any two sides of the triangle
- One angle and the length of one side of the triangle

During the instantiation the other attributes are calculated and become
accessible.

### Example
```python
from right_triangle import RightTriangle

# Instantiate a RightTriangle with some of the attributes
rt = RightTriangle(a=3, b=4)

# The other attributes are accessible
print(rt.c)
print(rt.a_angle)
print(rt.b_angle)

# Instantiation with other attributes
rt2 = RightTriangle(c=10, a_angle=rt.a_angle)
print(rt2.a)
```
