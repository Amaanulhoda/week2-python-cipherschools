#Tuples

a=[1,2,3]
a[0]=100
a[2]=200
print(a)

a=(1,2,3,4)
print(type(a))
#a[0]=1--->immutable

a=(1,2,3,4)
print(type(a))
def func(*args):
    print(type(args))
func(1,2,3,4)

a=5
b=9
a,b=b,a
c=a,b
print(type(c))
def sum_diff(a,b):
    s=a+b
    d=a-b
    return s,d
c=sum_diff(10,5)
print(type(c))

s,d=sum_diff(10,5)
print(s,d) #unpack iterables

a=1,2,3,4,5
print(type(a))

print(list(a))
print(tuple(a))

#list() and tuple() take iterable as a argument

print(list(range(0,5)))

#Dictionaries

a=dict()
a={
    "name":"Amaanul Hoda",
    1:"something",
    (1,2):"Tuple key what?"
    }
  #Can't index with list--->Unhashable type  
print(a["name"])


#dictionaries are mutable but keys are immutable

a={
    "name":"Amaanul",
    "company":"TCS",
    "college":"LPU"
}
#print(a["marks"])--->Key Error
key="marks"
if key in a:
    print(a[key])
else:
    print("Key doesn't exists")

