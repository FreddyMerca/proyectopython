import re


lista_nombres=['Ana',
               'Pedro',
               'Maria',
               'Rosa',
               'Freddy',
               'Lorena',
               'Karen',
               'Diana',
               'Liliana'
]

for elemento in lista_nombres:
    if re.findall('^[A-C]', elemento):
        print(elemento)



