
year = int(input("Ingrese año: "))

leap = False
    
    # Write your logic here
if year%4==0 and year%400==0 and year%100!=0:
      leap=True
      print("leap year")

else:
      leapeap=False
      print("Not leap year")