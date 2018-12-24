#range would produce a range of integers|the first says start,stop,step size
x=[2,4,6,8]
for x in range(2,20,2):
    print(x)
#another way 
list(range(2,20,2))
#using enumarate
id=1
for x in 'abcdefghijklmno':
    print(f'the letter {x} is at {id}th position')
    id+=1

id ='abcdefghijklmnopqrstuvwxyz'
for word in enumerate(id,1):
    print(word)

#another way 
id ='abcdefghijklmnopqrstuvwxyz'
for word,l in enumerate(id,1):
    print(word)
    print(l)
    print('\n')
#using zip
list1=[1,2,3,4]
list2=['a','b','c','d']
for thing in zip(list1,list2):
    list(thing)
    print(thing)
#list makes anything a list

#in is used to check if something is in a datat structure
print(2 in [1,3,4,5,6])
#min function 
list1=[9,6,4,67,5,2,5,7,5,3,7,9,3,2,7,8]
print(min(list1))
#max function
print(max(list1))