email=False
miEmail=input("Introduce tu Email: ")

for i in miEmail:
    
    if (i=="@"):
        email=True

if email==True:
    print("Email es correcto")
else: 
    print("Email no es correcto")

