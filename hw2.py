# Name: Travis Wagner
# Evergreen Login: wagtra12
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###
from hw2_test import n
print n
num=0
i=1

while i < n + 1:
    num = num + i
    i =i + 1

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"
print num
# ... write your code and comments here (and remove this line)


###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"
for n in range(2,11):
    print 1.0/n
# N is values 1-10 divided by 1.0 to get it to decimal representation.


###
### Problem 3
###

print "Problem 3 solution follows:"
n = 10
triangular = 0
for i in range(1,n+1):
    triangular = + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2
# ... write your code and comments here (and remove this line)

###
### Problem 4
###


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"
n = 10
fact = 1
for i in range(1,n+1):
    fact = fact * i
print fact   
# ... write your code and comments here (and remove this line)

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

n = 10
fact = 1
ctr = n

for j in range(1, n +1): 
    for i in range(1, ctr + 1):
        fact = fact * i
    print fact
    fact = 1                #reset fact to 1
    ctr= ctr - 1            # set ctr to go down by 1

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

n = 10
ctr = n
t= 1
for j in range(1, 11): 
    fact = 1
    for i in range(1, j+ 1):
        fact = fact * i
    t= t + (1.0 / fact)
print t                 
   
###
### Collaboration
###

# Colabs- Daniel Wagner, Jordan Rawls, Travis Goodroad, kahea (tutor)

###
### Reflection
###

# This assignment has taken me over a span of 3 nights of probably between 1-2 hours plus 1 hour tutor session.
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
