a=int(input("Enter  1st number: "))
b=int(input("Enter  2nd number: "))

greater=max(a,b)    #Maximum lcm value

for i in range(greater,a*b+1):  #Loop from greater value to maximum which is product of the two numbers
    if i%a==0 and i%b==0:  
        lcm=i
        break       #Break out of the loop once the first divisible value is encountered

print(lcm)  #print the value