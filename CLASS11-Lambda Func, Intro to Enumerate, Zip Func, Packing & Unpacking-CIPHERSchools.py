1+2 
"Amaan"*2
lambda a,b:a+b 

print("Hello Amaan and world")
show=print
show("something")

names=["Amaan","world",1,1.5]
for name in names:
    print(name)
for name in enumerate(names):
    print(name)
for name in enumerate(names):
    print(name[0],name[1])

a=6
b=8
temp=a
a=b
b=temp
print(a)
print(b)
a=6
b=8
a=a+b
b=a-b
a=a-b
print(a)
print(b)
a=8
b=2
a=a^b
b=a^b
a=a^b
print(a)
print(b)
a=3
b=2
a,b=b,a
print(a)
print(b)


#unpacking
a = 3
b=2
a,b=b,a
print(a)
print(b)

a=[1,2,3]
b,c,d=a
print(b,c,d)

a=1,2 #whenever we give python csv it pack it into tuple
print(a)
print(type(a))

#zip
names=["jatin","prateek","mukesh","rajesh"]
scores=[50,80,65,43]
for i,name in enumerate(names):
    score=scores[i]
    print(name,"-",score)
for name,score in zip(names,scores):
    print(name,"-",score)
