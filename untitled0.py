print("hello world")

z= 3j

print(type(z))

z= int ("3")
z=3
print(type(z))


a=str("Hello world")
print(a)
print(type(a))

a = "               Hello, World! "
print(a) # returns "Hello, World!"

print(a.strip()) # returns "Hello, World!"
a = " Hello, World! "
print(a.split(",")) # returns "Hello, World!"
a=a.split(",")
print(a)

b=[]
b=a.split(",")
print(b[0])

print(a.strip()) # returns "Hello, World!"
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(len(a))



z=3
z=z<<1
#z=z>>2
print(z)

if  "y" in "hello world y ":
    print("yes")
else:
        print("no")



a = ['hey', 'bye']
print(a[0])


if  "hey" in a:
    print("hey")
    

if ('hey'=="hey"):
    print("hellO")

a = ['hey', 'bye',"apple","banana"]

print(a[0])
#print(a.pop())
print(a.remove("hey")) 
print(a.sort())       

c=a.copy()
a.clear()


a[0]="gaurang"



e=("hello","bye","banana","apple","banana")
e[0]="hsagd"

print(e.index("bye"))

if "bye" in e:
    
    print("bye")
    
    
del e[0]

del a[0]







w={"hello","bye","banana","apple","banana"}



print(w[0])

print ( "hello" in w)


w.add("add")


print(len(a))



dict = {
        "hello":"world",
        "hello1":"world1",
        "hello2":"world2"
        
        }


print(dict["hello"])


for x in dict:
    print(dict[x])
dict["hello"]="byebbye"
print(dict)



for x in dict.items():
    print(x)



dict.update({"geahskdjhaskjge":"asjdj"})

print(len(dict))
print(dict.items())

del dict



if(5 is not 5):
    print("yes")





i=1

while i<6:
    print(i)
    i+=1
    if(i==3):
        pass;
        print(i)
    print(i)


for x in range(2,60,10):
    print(x)






def rec(k):
    if k==1:
        return k;
    else:
        result=k+rec(k-1)
        return result

print(rec(5))


a=5
b=10
print(a,b)

a,b=b,a

print (a,b)



def find(a,b):
    if(a in b):
        return "true"
    else :
        return "false"

find("hello123",dict)



v=lambda a: a*5

print(v(4))


a=["hello","ehkfd"]

a.pop(0)


class boy:
    def __init__(self,name):
        print(self)
        self.name=name

p=boy("hello")
print(p.name)

del p.name

del p

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)




def greeting(a):
    print(a)



