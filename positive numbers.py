#WAP to print all positive numbers in a range.

#using for loop
list1 = [12, -7, 5, 64, -14]
for num in list1:
    if num >= 0:
       print(num)

#using while loop
list2 = [12, 14, -95, 3]
i = 0   
while(i < len(list2)):
    if list2[i] >= 0:
        print(list2[i]) 
    i = i + 1
     
