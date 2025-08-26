print(" ----- Simple Calculator----")
print("Operation:")
print("1.Addition (+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")

num1 = float(input("Enter First Number:"))
num2= float(input ("Enter Second Number:"))
choice = input("Choose operation (*,/,-,+): ")

if choice == '+':
  result= num1+num2
  print("Result:",result ) 

  
elif choice == '-':
  result= num1 -num2
  print("Result:",result )  
  
 
elif choice == '*':
  result= num1 * num2
  print("Result:",result ) 

  
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation choice!")
  
  
  
  

                   
