def calcul(num1, operator, num2):
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    elif operator == "%":
        print(num1%num2)
        
calcul(5,"+",2)
calcul(5,"-",2)
calcul(5,"*",2)
calcul(5,"/",2)
calcul(5,"%",2)