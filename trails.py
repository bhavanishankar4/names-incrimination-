name=input('enter your name')
times=int(input('enter the number of times to repeat:'))


print("method:1 prints on the same line")
print('') if times <=0 else print((name+' ')*times)
      

#print on seperate lines
print("method 2: print on separate lines")
print('')if times <=0 else print(times*(name+'\n'))
