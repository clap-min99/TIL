# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, len1, len2):
        self.len1 = len1
        self.len2 = len2

    def calculate_perimeter(self):
        return (2*self.len1 + 2*self.len2)

shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)