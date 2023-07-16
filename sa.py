
from calculation import addition, subtract, multiply, division
if __name__=="_main_":
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    operator= input("enter the operator:\
                    \n1:addition: +n\
                    \n2:subtraction:- \
                    \n3:multiply:* \
                    \n4:division: / \
                    \n5:square:^\
                    \n6:root:^^")
    if operator =="+":
         print("addition:",addition(num1,num2))
    elif operator =="-":
         print("subtraction:",subtract(num1,num2))
    elif operator =="*":
         print("multiplication:",multiply(num1,num2))
    elif operator =="/":
         print("division:",division(num1,num2))
    elif operator =="^":
         print("square:",square (num1))
    elif operator =="^^":
         print (" root:",squareroot (num1))         
    else:
         print("invalid operator")     






                   

                   
            
        
