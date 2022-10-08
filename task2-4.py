# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number = int(input('Введите число '))
def find_counter(number):   #список множителей
    listDiv = []
    for i in range(number):        
        for div in range(1, number+1):
            if number%div == 0:
                listDiv.append(div)
        break
    return(listDiv)
listDiv = find_counter(number)
print(listDiv)
for i in range(len(listDiv)):
    if len(find_counter(listDiv[i])) > 2:
        listDiv[i] = 1
listDiv = list(set(listDiv))
print(listDiv)

