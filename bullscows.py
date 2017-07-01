#!/usr/bin/python3
import random
def passw(numDigits):
    # Returns a string that is numDigits long, made up of unique random digits.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return int(secretNum)
passw = passw(4)

## parse() is a broken function as of Python3.  MUSTFIX. 
#def parse(code):
#	a = code/1000
#	b = (code/100) - (a*10)
#	c = (code/10) - ((code/100)*10)
#	d = code - ((code/10)*10)
#	return a,b,c,d

on = 0
while (on != 4):
	on = 0
	present = 0
	guess=int(input("Guess the 4-digit code:"))
	# inserting str here is a hacky solution; Python3 broke expected behavior of parse() function above (disabled), and list won't accept int input, so int guess and int passwd are converted to strings and then passed to list.  VERY HACKY, MUSTFIX.  
	a,b,c,d = list(str(guess))
	A,B,C,D = list(str(passw))
	while a==b or b==c or c==d or a==c or a==d or b==d:
		print("No digits can repeat!")
		guess=int(input("Guess the 4-digit code:"))
		a,b,c,d = list(str(guess))
	if a==A:
		on+=1
	if b==B:
		on+=1
	if c==C:
		on+=1
	if d==D:
		on+=1
	if a==B or a==C or a ==D:
		present+=1
	if b==A or b==C or b==D:
		present+=1
	if c==A or c==B or c==D:
		present+=1
	if d==A or d==B or d==C:
		present+=1
	present = present
	if on==4:
		print("You guessed correctly!")
	else:
		print("Number of digits in the right place:",on)
		print("Number of digits guessed correctly but in the wrong place:",present)
