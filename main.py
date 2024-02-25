a = int(input(">"))
b = input()
c = int(input())
if b == "+" :
    history = f" {print(a + c)},{print(str(a), b ,str(c))}"
elif b == "-" :
    history = f" {print(a - c)},{print(str(a), b ,str(c))}"
elif b == "*" :
   history = f" {print(a * c)},{print(str(a), b ,str(c))}"
elif b == "/" :
    history = f" {print(a / c)},{print(str(a), b ,str(c))}"
else:
    print("bug")

def  add(*args):
    s=0
    for i in args:
        s+=i
    print(s)
def  sub():
    a=int(input())
    b=int(input())
    print(a-b)
print('1.add\n2.sub\nmul\ndiv')
x=int(input())
if x==1:
    add()
if x==2:
    sub()





