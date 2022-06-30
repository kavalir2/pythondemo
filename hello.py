# print("hello")
# name="sahithi"
# print(name) 
# print("name")

studentname =input("enter the name ")
studentrollnumber =input("enter the roll number ")
studentage=input("enter the age ")
print(type(studentage))
studentage=int(studentage)
print(type(studentage))
print(studentname,studentrollnumber,studentage)
if (studentage>=18):
	print("major")
else:
	print("minor")
for i in range(0,100,2):
	print(i,end=' ')