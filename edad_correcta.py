def validar_edad():
    try:
        edad = int(input("Edad: "))
    except:
        return "El dato ingresado no es valido", edad
    else:
        if 17 < edad < 66:
            return "Su edad esta dentro del rango valido para votar", edad
        elif 18 > edad :
            return "Es demasiado joven para...", edad
        else:
            return "Estas pasado, viejo", edad
    


print("Ingrese su edad para saber si debe o no votar")
while True:    
    mensaje, edad = validar_edad()
    print(mensaje, edad)
    if edad == 0:
        break
