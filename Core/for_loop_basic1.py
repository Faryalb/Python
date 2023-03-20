# Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(100):
    if i % 5:
        print("Coding")
    elif i % 10:
        print("Coding Dojo")
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
count = 0
for i in range(0,500001,2):
    count += i 
    print(count)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018,0,-4):
    print(i)

# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive line
lowNum = 3
highNum = 7
mult = 12
for i in range(lowNum,highNum):
    if i % mult:
        print(i)
