"""Escribe un programa que permita al usuario ingresar el precio
de un producto y un código de descuento. El programa debe validar
si el precio es un número positivo y si el código de descuento es
válido. Los errores posibles incluyen entreadas no numéricas, 
números negativos y códigos de descuento no válidos.

Codigos de descuento : 
descuentos_validos = ["DESC10", "DESC20", "DESC30"]"""


class producto:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor


def validadorDescuento(valor, descuento):
    descuentos_validos = {"DESC10" : -0.1 , "DESC20" : -0.2 , "DESC30" : -0.3}
    if descuento == "DESC10":
        return valor + (valor * descuentos_validos.get(descuento))
    elif descuento == "DESC20":
        return valor + (valor * descuentos_validos.get(descuento))
    elif descuento == "DESC30":
        return valor + (valor * descuentos_validos.get(descuento))
    else:
        return f"El código de descuento \"{descuento}\", no es válido."


print("Bienvenido al programa que agrega productos y toma descuentos")
print("-------------------------------------------------------------")
x = 1
menu()


def main():
x += 1


def menu():
    print("Ingrese un nuevo nombre de producto y valor")
    print("para finalizar si tiene algún descuento tambien.")
    nombre = input("Nombre de producto: ")
    valor = int(input("Valor del producto: "))
    descuento = input("Codigo de descuento: ")
    

def crea_producto(nombre, valor, x):
    producto = "producto" + x
    producto = producto(nombre, valor)
        

