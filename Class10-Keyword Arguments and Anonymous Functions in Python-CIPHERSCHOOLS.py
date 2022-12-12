print(1,2,3,4,5,sep=",")

#Positional Arguments
#Mapping w.r.t position
def func(m,n,o):
    print(m)
    print(n)
    print(o)
func(1,2,3)

#keyworded arguments
def func(m,n,o):
    print(m)
    print(n)
    print(o)
func(m=1,n=2,o=3)

def func(m):
    print(m)
#func() ---> Raise error
func(1)



def hello():
    print("Hello world !")
hello 
hello()
a=1
a=hello
a()

# Everything in python language is a object,
# even functions

print(type(a))
hello=2
print(hello) #hello is no longer a function
a() #a is still a function

def b():
    print("Hi")
def b():
    print("Bye")

# *args **kwargs
'''print can except any number of arguments'''

#required arguments
def func(m,n):
    print(m,n)
func(1,2)

#default arguments
def func(m=1,n=2):
    print(m,n)
func()
func(1)
func(1,2)

#optional arguments
def func(*m):
    print(*m)
func(1,2,3,4)

#required keyworded only arguments
def func(m,n,*o):
    print(m)
    print(n)
    print(o)
func(1,2,3,4,"jatin",1.5)


#default keyworded only arguments
def func(a,b,*c,d,e="jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1,2,3,4,5,6,7,d=8)


#lambda is always a one liner function, it can only contain a single expression inside it
a=lambda a,b: a+b #Expression that return a function
print(a(1,2))

a=1
b=2
c=print(a,b)
print(c) #return None
