# class Complex:
#     def __init__(self, value):
#         self.value = value
    
#     def __add__(self, other):
#         result = self.value + other.value
#         return f"Result of addition of two values is: {result}"
    
#     def __mul__(self, other):
#         rslt = self.value * other.value
#         return f"Result of multiplication of two values is: {rslt}"
    
# a = Complex(2)
# b = Complex(3)
# print(a + b)
# print(a * b)

class Complex:
    def __init__(self, real, imge):
        self.real = real
        self.imge = imge
    
    def __add__(self, other):
        if isinstance(other, Complex):
            new_real = self.real + other.real
            new_imge = self.imge + other.imge

            return Complex(new_real, new_imge)

        return NotImplemented
    
    def __str__(self):
        sign = "+" if self.imge >= 0 else "-"
        return f"Result of addition: {self.real} {sign} {self.imge}i"
    
a = Complex(2, 3)
b = Complex(4, 2)
print(a + b)
