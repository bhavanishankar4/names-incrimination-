val=input('enter number')
sum=0
for ii in range(len(val)):
    sum=sum+(int(val[ii])**3)
if (int(val)==sum):
    print("the given number is armstrong number")
else:
    print("the given number is anot a armstrong number")
        
