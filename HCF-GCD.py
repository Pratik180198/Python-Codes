num1=int(input("Enter  1st number: "))
num2=int(input("Enter  2nd number: "))
if num1>num2:
    lower=num2
else:
    lower=num1
for i in range(2,lower):
    if num1 % i == 0 and num2 % i == 0:
        hcd=i
print(hcd)
