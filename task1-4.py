# Вычислить число п c заданной точностью *d*
d = float(input('Введите d '))
def digit_after_dot_count(num:float):  #функция для подсчета количества знаков после запятой
    count = 0
    div = 1
    while True:
        if not(num*div == int(num*div)):
            count += 1
            div *= 10
        else: break
    return count
count = digit_after_dot_count(d)
print(count)
import math
print(round(math.pi, count))
