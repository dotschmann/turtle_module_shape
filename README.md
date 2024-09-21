# turtle_module_shape
Using turtle module to create different shapes example polygons and flowers

## equilateral triangle
base length, side length have the same value and internal angles are the same.
if you use the left-return (.lt), you use the external angle (180-60) of the input
Hence it is easy to use the for_range method to lop through 3 times to get the triangle.

## isosceles triangle
use the desired angle(θ) and base-length (b) to calculate the side-length (s) of the triangle.
<s = b / (2 * cos(θ))>

## polygon
use the formular <total_angle = (n - 2) * 180°> to calculate the total internal angle and then divide by number of sides (n)
to find each angle value <per_angle = total_angle / n>

## tri_polygon
the idea is to divde the internal of polygon into triangle equal to the number of sides. 
