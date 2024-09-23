from setuptools import setup #Primera instruccion para el paquete distribuile
setup( #Funcion Setuo
    name="Paquete Calculos", #Nombre del paquete
    version="1.0",
    description="Paquete de redondeo y potencia",
    author="Freddy Mercado",
    author_email="frmercado@emcali.com.co",
    url="www.emcali.com.co",
    packages=["calculos","calculos.redondeo"]
)