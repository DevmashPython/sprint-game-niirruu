import msvcrt

finish=10
count1=count2=count3=0

print "print enter key to get started!"
raw_input()

while count1!=10:
    key=msvcrt.getch()
    if key=='d': 
        count1=count1+1
        print "_",        
    else:
        print "\n wrong key"
        exit()

if count1==10:
	print "\n"
while count2!=10:
    key=msvcrt.getch()
    if key=='s':     
        count2=count2+1
        print "                   |"
    else:
        print "\nwrong key"
        exit()


if count2==10 and count1==10:
    print "                    
    ",
while count3!=finish:
    key=msvcrt.getch()
    if key=='d':
        count3=count3+1
        print "_",
    else:
        print"wrong key"
        break
print "\ncompleted"        

''' 
1. Mention controls for the game before the game is started!
ex. Press D to move right
2. Mention when we are supposed to turn down or right.
3. Print time in which game is completed.
4. Print z properly
'''
