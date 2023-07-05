# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
import random

stuff = {'food': random.randint(1,5), 'sleeping bag': random.randint(2,4), 'tent': random.randint(4,6), 'flint': random.randint(1,2) , 'water': random.randint(2,4), 'medicine': random.randint(2,4), 'shoes':random.randint(1,4),'clothes':random.randint(1,4)}

print(stuff)
def backpack(capacity: int, stuff: dict) -> list[str]:
    packaging_option = []
    summary = []
    for key, value in stuff.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option


print(backpack(18, stuff))