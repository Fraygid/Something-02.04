def get_middle_point(x1, y1, x2, y2):
    middle_x = (x1 + x2) / 2
    middle_y = (y1 + y2) / 2
    return middle_x, middle_y

x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))

mid_x, mid_y = get_middle_point(x1, y1, x2, y2)
print(f'Середина отрезка: ({mid_x}; {mid_y})')
