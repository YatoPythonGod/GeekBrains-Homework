class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_mass(self, thick_asp=5, m_asp=25):
        mass = self._length * self._width * thick_asp * m_asp
        return f'{mass / 1000:.0f} т.' if mass//1000 else f'{mass} кг.'


m = Road(5000, 20)
print(m.calculation_mass())
print(m.calculation_mass(3))
