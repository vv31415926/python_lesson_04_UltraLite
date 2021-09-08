'''
Написать любую функцию без параметров и функцию с параметрами
Написать любую функцию с возвращаемым значением и без него
Написать любую lambda функцию
'''

def hi():
    print('Всем привет!')

def summa( a,b ):
    return a+b

fLambda = lambda x,y: x+y

hi()
print( summa(3,2) )
print( fLambda(3,2) )




