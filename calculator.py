
# Calculator
print("Welocme to the Calculator.This is made by Arqam Shaikh",  )
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division" , "\n" )


print("Enter first number")
n1 =int(input())
print("Enter second number")
n2 = int(input())
print("what u want to do ( + , - , / , *)")
n3 = (input())


# if n1== 56 and n2 == 9 and n3=='+':
#     print("77")
if n3=='+':
    print(n1 + n2)
if n3=='-':
    print(n1 - n2)
if n3=='/':
    print(n1 / n2)
if n3=='*':
    print(n1 * n2)
if n3=='':
    print("Plz enter what u want to do")
