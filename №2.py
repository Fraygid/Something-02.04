def is_valid_triangle(side1, side2, side3):
    return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)

a = float(input('Введите 1 сторону треугольника: '))
b = float(input('Введите 2 сторону треугольника: '))
c = float(input('Введите 3 сторону треугольника: '))

if is_valid_triangle(a, b, c):
    print('True - треугольник существует')
else:
    print('False - треугольник не существует')
