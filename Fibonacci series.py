#WAP to display the Fibonacci sequence.

n = int(input("Enter number of terms : "))

a = 0
b = 1
count = 0

if n <= 0:
   print("Invalid number")
elif n == 1:
   print("Fibonacci sequence upto",n,"term is :",a)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(a)
       c = a + b
       a = b
       b = c
       count = count + 1
  
