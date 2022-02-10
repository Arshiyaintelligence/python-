from sqlalchemy import true


lst = list((4,)*4)
print(lst)
print(bool("hello"),bool(100000))



def check(num):
    return(bool(num % 2 == 0))

num = 22
if  check(num):
    print('Even')
else:
    print('odd')


