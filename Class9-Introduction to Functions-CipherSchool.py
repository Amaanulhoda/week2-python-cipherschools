a=6
b=3
print(a+b)
print(" coming")
print(" coming")
print("coming")

print(a-b)
print(" coming")
print(" coming")
print("coming")

print(a*b)
print(" coming")
print(" coming")
print(" coming")

print(a+b)
print("loading..")
print("loading..")
print("loading..")

print(a-b)
print("loading..")
print("loading..")
print("loading..")

print(a*b)
print("loading..")
print("loading..")
print("loading..")

x=9
x="Ronaldo"
x=1.5
x=print

def show_loading():
    for i in range(3):
        print("loading...")

print(a+b)
show_loading()
print(a-b)
show_loading()
print(a*b)
show_loading()

def show_loading():
    for i in range(3):
        print("loading"+"."*(i+1))

print(a+b)
show_loading()
print(a-b)
show_loading()
print(a*b)
show_loading()


def sheldon_knock(name):
    for _  in range(3):
        print("knock knock hello",name)
sheldon_knock("penny")

def sheldon_knock(name,times=3):
    for _  in range(times):
      print("knock knock hello",name)
sheldon_knock("Ronaldo",3000)

#Return Statement
def add(a,b):
    return a+b
a=add(1,2)
print(a)
