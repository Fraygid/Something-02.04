def convert_to_miles(km):
    return km * 0.6214

km = float(input("Введите расстояние в км: "))
miles = convert_to_miles(km)
print(f'{km} км = {miles} миль')
