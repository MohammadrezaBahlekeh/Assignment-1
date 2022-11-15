Firstname = input("Please enter your Firstname : ")
Lastname = input("Please enter your Lastname : ")

print("Now enter your grades")

G1 =float(input("First grade = ")) 
G2 =float(input("Second grade = ")) 
G3 =float(input("Third grade = ")) 

Avg = (G1+G2+G3)/3

if Avg>=17:
    print(Firstname+" "+Lastname+" Your Status is Great")

elif 17> Avg >=12:
    print(Firstname+" "+Lastname+" Your Status is Normal")

elif Avg < 12:
    print(Firstname+" "+Lastname+" Your Status is Fail")

