num1=float(input("Enter First Number:"))
num2=float(input("Enter Second Number:")) 

print("Arithmetic Operators")
print("Addition:",num1+num2)
print("Subtraction:",num1-num2)
print("Multiplication:",num1*num2)
print("Division:",num1/num2)
print("Modulus:",num1%num2)
print("Exponent:",num1**num2)
print("Floor Division:",num1//num2)

print("Assignment Operators")
a=num1
a+=num2
print("After +=: ",a)
a-=num2
print("After -=: ",a)
a*=num2
print("After *=: ",a)
a/=num2
print("After /=: ",a)
a%=num2
print("After %=: ",a)

print("Comparison Operators")
print(num1,"==",num2,":",num1==num2)
print(num1,"!=",num2,":",num1!=num2)
print(num1,">",num2,":",num1>num2)
print(num1,"<",num2,":",num1<num2)
print(num1,">=",num2,":",num1>=num2)
print(num1,"<=",num2,":",num1<=num2)

print("Logical Operators")
print("num1 > 0 and num2 > 0:",num1>0 and num2>0)
print("num1 > 0 or num2 > 0:",num1>0 or num2>0)
print("not(num1 > 0):",not(num1>0))

print("Identity Operators")
x=num1
y=num2
print("x is y:",x is y)
print("x is not y:",x is not y)

print("Membership Operators")
list1=[1,2,3,4,5]
print(num1,"in list1:",num1 in list1)
print(num2,"not in list1:",num2 not in list1)