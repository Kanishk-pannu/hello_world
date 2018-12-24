#while prints a statement till the condition becomes false
x=1
while x<10:
    print(x)
    x=x+x
#x=x+x can also be written as x=+x
x=1
while x<10:
    print(x)
    x=x+x
else:
    print('x is greater than ten')

#pass:does nothin gat all
p=[4,3,22,4,5]
for x in p:
    pass
#continue:goes to the of the closest enclosing loop
lettter='kanishkp'
for l in lettter:
    if l=='a':
        continue
    print(l)
#break:it breaks out of the current closest enclosing loop
lettter='kanishkp'
for l in lettter:
    if l=='h':
       break
    print(l)
#these keywords can also be used with while