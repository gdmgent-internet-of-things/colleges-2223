from numpy import matrix

z = 2 ** 2
z = 5 % 3
z = 5 // 3
z = 5 / 3
z = 5 * 3

A = matrix([
    [1, 2], 
    [3, 4]
    ])
B = matrix([
    [5, 6], 
    [7, 8]
    ])

print(A @ B)

a = 'Jannes'
b = 'Lambrecht'

print (a + b)

# vergelijking

a= 1
b = 2
c = True
print(a is b, a == b)
print(a is c, a == c)

logic = False

print('this is true' if logic else 'this is false')

if logic:
    print('this is true')
else:
    print('this is false')

# oefening 2: vraag een naam op, 
# indien de naam start met de letter a of A en langer is dan 3 letters, 
#  > print dan 'goed' 
# Anders indien hij enkel start met 'a' of 'A' 
#  > print dan 'matig'
# Anders
#  > print dan 'slecht'
#  && >  and 
#  || >  or
name = input("What is your name: " )
if (name[0] == "A" or name[0] == "a") and len(name) > 3:
	print("Goed")
elif name[0] == "A":
	print("Matig")
else:
	print("Slecht")
		



