
a=int(input("enter a number"))
if a%2==0:
  print("even")
else:
  print("odd")

a=int(input("enter a number: "))
count=0
for i in range(2,a):
  if(a%i==0):
     print("not prime")
     count=count+1
if(count==0):
 print("prime")
    Write a program to display the last digit of a number.


num=int(input("Enter a number:"))
last_digit=num%10
print(f"Last digit of the number is:{last_digit}")
     
Enter a number:987
Last digit of the number is:7
Write a program to check whether the last number (given by the user) is odd or even


num=int(input("Enter a number:"))
a=num%2
if a==0:
  print(f"{num} is even")
else:
  print(f"{num} is odd")
     
Enter a number:25
25 is odd
Write a program to check whether the person is eligible to vote or note


num=int(input("Enter a number:"))
if num>=18:
  print("You are eligible to vote")
else:
  print("You are not eligible to vote")
     
Enter a number:19
You are eligible to vote
Write a program to display the grade according to the percentage of mark


num=int(input("Enter a number:"))
if num>=80:
  print("Grade A")
elif num>=60:
  print("Grade B")
elif num>=40:
  print("Grade C")
else:
  print("Grade D")
     
Enter a number:75
Grade B
Write a program to display the day in a week according to the number entered by the user


monday,tuesday,wednesday,thursday,friday,saturday,sunday=1,2,3,4,5,6,0
num=int(input("Enter a number:"))
if num%7==1:
  print("monday")
elif num%7==2:
  print("tuesday")
elif num%7==3:
  print("wednesday")
elif num%7==4:
  print("thursday")
elif num%7==5:
  print("friday")
elif num%7==6:
  print("saturday")
else:
  print("sunday")
     
Enter a number:678
saturday
Write a program to check whether the number entered is 3 digits or not


num=int(input("Enter a number:"))
if num>=100 and num<=999:
  print("The number is 3 digits")
else:
  print("The number is not 3 digits")
     
Enter a number:9080
The number is not 3 digits
Write a program to check whether the entered number is positive or not


num=int(input("Enter a number:"))
if num>=0:
  print("number is positive")
else:
  print("number is negative")
     
Enter a number:9
number is positive
Write a program to check whether the entered number is divisible by 8 and 9


num=int(input("Enter a number:"))
a=num%8
b=num%9
if a==0 and b==0:
  print("The number is divisible by 8 and 9")
else:
  print("The number is not divisible by 8 and 9")
     
Enter a number:89
The number is not divisible by 8 and 9
Write a program to find the largest of three number


n1=int(input("Enter a number 1:"))
n2=int(input("Enter a number 2:"))
n3=int(input("Enter a number 3:"))
if n1>n2 and n1>n3:
  print(f"{n1} is the largest number")
elif n1n3:
  print(f"{n2} is the largest number")
else:
  print(f"{n3} is the largest number")
     
Enter a number 1:67
Enter a number 2:78
Enter a number 3:43
78 is the largest number
Write a program to check whether the entered character is vowel or not


ch=input("Enter a character:")
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
  print("The character is a vowel")
else:
  print("The character is not a vowel")
     
Enter a character:n
The character is not a vowel
Write a program to print the following number pattern using a loop. 1 1 2 1 2 3 1 2 3 4 1 2 3 4 5


for i in range(1,6):
  for j in range(1,i+1):
    print(j,end=" ")
  print()
     
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
Calculate the sum of all numbers from 1 to a given number (If the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10))


num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
  sum=sum+i
print(f"The sum of all numbers from 1 to {num} is {sum}")
     
Enter a number:25
The sum of all numbers from 1 to 25 is 325
Write a program to display only those numbers from a list [12, 75, 150, 180, 145, 525, 50] that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)
     
75
150
145
Write a program to count the total number of digits in a number using a while loop. (The number is 75869, so the output should be 5.)


number=int(input("Enter a number:"))
count = 0
while number != 0:
    number //= 10
    count += 1
print("Total number of digits:", count)
     
Enter a number:9090
Total number of digits: 4
Write a program to print list [10, 20, 30, 40, 50] in reverse order using a loop


list =[10, 20, 30, 40, 50]
rev_list=[i for i in list[::-1]]
print(rev_list)
     
[50, 40, 30, 20, 10]
Display numbers from -10 to -1 using for loop


for i in range(-10,0,1):
  print(i,end=",")
     
-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,
Write a program to print Fibonacci series up to 10 terms


n=10
n1,n2=0,1
print(n1,n2,end=" ")
for i in range(n-2):
 n3=n1+n2
 print(n3,end=" ")
 n1,n2=n2,n3
     
0 1 1 2 3 5 8 13 21 34 
Write a program to use the loop to find the factorial of a given number.


num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"The factorial of {num} is {fact}")
     
Enter a number: 5
The factorial of 5 is 120
Write a program to print reverse a given integer number (Input: 76542 output: 24567)


num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
print("Reversed number:", rev)

     
Enter a number: 76542
Reversed number: 24567

