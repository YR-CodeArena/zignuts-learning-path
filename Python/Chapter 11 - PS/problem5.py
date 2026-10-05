class Vector:
    def __init__(self, row1column1, row1column2, row2column1, row2column2):
        self.row1column1 = row1column1
        self.row1column2 = row1column2
        self.row2column1 = row2column1
        self.row2column2 = row2column2
    
    def __add__(self, other):
        new_row1column1 = self.row1column1 + other.row1column1
        new_row1column2 = self.row1column2 + other.row1column2
        new_row2column1 = self.row2column1 + other.row2column1
        new_row2column2 = self.row2column2 + other.row2column2

        return Vector(new_row1column1, new_row1column2, new_row2column1, new_row2column2)
    def __mul__(self, other):
        new_row1column1 = self.row1column1 * other.row1column1
        new_row1column2 = self.row1column2 * other.row1column2
        new_row2column1 = self.row2column1 * other.row2column1
        new_row2column2 = self.row2column2 * other.row2column2

        return Vector(new_row1column1, new_row1column2, new_row2column1, new_row2column2)

v1 = Vector(2, 3, 1, 4)
v2 = Vector(1, 4, 5, 2)

print(v1 + v2)
print(v1 * v2)