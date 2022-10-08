# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
pathWrite = 'homework4\\file2.txt'
from random import randint as rI
def createEquation():
    degree = int(input("Введите максимальную степень многочлена: "))
    equation = ''

    for d in range(degree, -1, -1): # проходим в обратную сторону от максимального
        coef = rI(0,100)
        print(coef)
        if d == degree:
            if coef > 0:
                equation += str(coef) + 'x^' + str(d)
            if coef < 0:
                equation += '-' + str(abs(coef)) + 'x^' + str(d)
        else:
            if coef > 0:
                equation += ' + ' + str(coef) + 'x^' + str(d)
            if coef < 0:
                equation += ' - ' + str(abs(coef)) + 'x^' + str(d)

    return equation + ' = 0'
eq1 = createEquation()
result1 = eq1.replace('x^1', 'x').replace('x^0', '').replace('1x^', 'x^')
print(result1)
eq2 = createEquation()
result2 = eq2.replace('x^1', 'x').replace('x^0', '').replace('1x^', 'x^')
print(result2)
with open(pathWrite, 'w') as data:
    data.write(result1)
    data.write('\n')
    data.write(result2)
