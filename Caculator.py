# taking user input numbers
num1,num2=map(int,input("Enter two numbers: ").split())

# operation choice
choice = int(input("Enter you prefered operation choice: \n1 --> Addition \n2 --> Subtraction \n3 --> Multiplication \n4 --> Division\n"))
if choice==1:
    print(num1+num2)
elif choice==2:
    if num1 < num2:
        print("First number should be greater than second")
    else:
        print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    if num2==0:
        print("Error!, you cannot divide anything by zero")
    else:
        print(num1/num2)
else:
    print("Enter a valid input!")
