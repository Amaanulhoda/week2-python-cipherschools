a=5 #assuming
print("value of a is %d" % (a)) 
print("value of a is {}".format(a))
print("value of a is {} {}".format(a,2))

a,b,c=1,2,3
print("a = {}, b = {}, c = {}".format(a,b,c))
#If we want correct order
#Give index
print("a = {2}, b = {1}, c = {0}".format(c,b,a))
name="Mohammad Amaanul Hoda"
company="TCS"
print("name = {name} company = {company}".format(name=name,company=company))
print("Hello I am {name} and I work at {company}".format(name=name,company=company))
print("Hello {name} Welcome to my Instagram".format(name=name,company=company))

print(f"name = {name}")
print(f"name = {10/3}")

print("a\nb")
print(len("a\nb")) 
print(r"a\nb") 
for i in "a\nb":
    print(i)
for i in r"a\nb":
    print(i)
    

#strip
a="    jatin   "
print(a.strip()) 
#Removes spaces from both side

#split
b="1,2,3,4,5"
print(b.split(",")) 
#Returns List

c="MESSI"
print(c.replace("S","Z"))
print(c.count("I"))
