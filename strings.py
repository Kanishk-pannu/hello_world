#using /n 
print("hello world \nmy name is kanishk and a I like to code")
#using \t
print("hello world \tmy name is kanishk and a I like to code")
#using len function
a='hello my name is kanishk pannu'
len(a)
#using indexing grabbing something of a string
sting1='hello world this kanishk pannu'
sting1[-5]
sting1[6]
#using slicing or grabbing a subsection
sting1[0:5:2]
#variable[starting:ending:step]
#the ending should be one index more than where you want to end
#strings in python are immutable
#strings concatnation is the addition of strings
l='kanishk'
print(l+'pannu')
k='hello world its nice outside!'
print(k*3)
#using formatting 1
a="let's play then"
print(f'the weather is nice outside {a}')
#using formatting 2
print('the weather is nice outside {}'.format(a))
#formatting of floats
k=100/777
print('the result is {:1.4f}'.format(k))