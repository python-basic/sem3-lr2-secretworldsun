"""
Яхимович Анастасия 
ИВТ 2 курс 
Группа 1.1
Задание: Вычисление площади треугольника по формуле Герона
"""

def geron_sq(a,b,c):
    p = (a+b+c)/2
    import math
    s = math.sqrt((p-a)*(p-b)*(p-c)*p)
    return s

def main():
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    print(geron_sq(a,b,c))

main()
