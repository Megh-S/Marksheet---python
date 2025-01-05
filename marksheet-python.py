#marksheet
a, b,c, d = input("Name: "), input("Age: "), input("ID: "),input("Std: ")
maths = int(input("Marks scored in maths: "))
ss = int(input("Marks scored in ss: "))
sci = int(input("Marks scored in sci: "))
french = int(input("Marks scored in french: "))
spanish = int(input("Marks scored in spanish: "))
total = maths + ss + sci + french + spanish 
print("Name:", a)
print("Age:", b )
print("ID:", c)
print("Std:" , d) 
print("Maths:", maths)
print("SS:", ss)
print("Science:", sci)
print("French:", french)
print("Spanish", spanish)
print("Total:", total)
if total>=470:
    print("Grade A")
elif total>=420:
    print("Grade B")
elif total>=400:
    print("Grade C")
else:
    print("Grade D")