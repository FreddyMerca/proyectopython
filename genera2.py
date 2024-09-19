#COn generador
def numpares(limite):

    num=1

    while num<limite:

        yield num*2
        num=num+1

parnum=numpares(10)

print(next(parnum))
print(next(parnum))
print(next(parnum))
