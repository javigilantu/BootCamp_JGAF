"""
__name__:
1.tiene ese valor de "__main__" si se ejecta dentro de su fichero.
2. tienen el valor de __name si se esta ejecitando fuera del fichero
"""
from a import x
import numpy as np

#Code
x()

print("-----------")
print("Ejecución de 'name&main'")

if __name__ == "__main__": # el archivo que se ejecuta tiene como valor main, siendo main una variable que existe en todos los valores de python 
    print("name de 'name&main':")
    print(__name__)
    print("EQ")
print("Fin de ejecución de 'name&main'")
print("----------")