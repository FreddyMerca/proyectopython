
email=input("Ingrese un email : ")
cant_arr=email.count("@")
pos_arr=email.find("@")
pos_arr2=email.endswith("@")


if "@" in email and cant_arr==1 and pos_arr!=0 and pos_arr2==False:
    print("Mail Correcto") 
else:
    print("Mail Incorrecto")



    
