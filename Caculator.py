# taking user input numbers
num1,num2=map(int,input("Enter two numbers: ").split())

# operation choice
choice = int(input("Enter you prefered operation choice: \n1 --> Addition \n2 --> Subtraction \n3 --> Multiplication \n4 --> Division\n"))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("Enter a valid input!")