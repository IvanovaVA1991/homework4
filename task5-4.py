# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
from task44 import createEquation
def myEquation():
    file1 = createEquation()
    equation = {}   #создаем словарь
    file1 = file1.replace(' + ', ' +').replace(' - ', ' -').split()[:-2]  # преобразовали уравнение, убрали 2 последних знака
    for i in range(len(file1)):
            file1[i] = file1[i].replace('+', '').split('x^') 
            equation[int(file1[i][1])] = int(file1[i][0])   # в словарь сложили в качестве ключа степень, значчение - коэффициент
    return equation
final = {}
equation1 = myEquation()
equation2 = myEquation()
print(equation1)
print(equation2)
for i in range(max(len(equation1), len(equation2)), -1, -1):   # выбираем максимальную длину
        first = equation1.get(i)
        second = equation2.get(i)
        if first != None or second != None:
                final[i] = (first if first != None else 0) + (second if second != None else 0)
print(final)
total = []
for k in range(len(final)):
        for i, j in final.items():
                total.append(str(j) + 'x^' + str(i))
        break
print(total)
for i in range(len(total)):
        total[i] = total[i].replace('x^0', '').replace('x^1', 'x')
totalEq = '+'.join(total) + '=0'
print(totalEq)
with open('file5.txt', 'w') as data:
    data.write(totalEq)
