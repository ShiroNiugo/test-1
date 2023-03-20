print("*" * 15, " Калькулятор ", "*" * 15) 
print("Для выхода введите q в качестве знака операции") 


while 1: 
    x, y = 0, 0
    s = input("Знaк (+,-,*,/,%,//,**): ") 
    if s == 'q': break
    if s in ('+','-','*','/','%','//','**'):
        while 1:
            tempX = (input ("х="))
            if tempX in ('0','1','2','3','4','5','6','7','8','9'):
                x = float(tempX)
                break
        while 1:
            tempY = (input ("y="))
            if tempY in ('0','1','2','3','4','5','6','7','8','9'):
                y = float(tempY)
                break
        if s == '+': 
            print("%.2f" % (x+y)) 
        elif s == '-': 
            print("%.2f" % (x-y)) 
        elif s == '*': 
            print("%.2f" % (x*y)) 
        elif s == '%': 
            print("%.2f" % (x%y))
        elif s == '//': 
            print("%.2f" % (x//y))  
        elif s == '**': 
            print("%.2f" % (x**y))
        elif s == '/': 
            if у != 0: 
                print("%.2f" % (x/y)) 
            else: 
                print("Деление на ноль!") 
        else: 
            print("Неверный знак операции!")