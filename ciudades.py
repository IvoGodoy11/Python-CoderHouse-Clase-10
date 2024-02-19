ciudades_info = {
    'Paris': {
        'Pais': 'Francia',
        'Poblacion': 2187526,
        'Puntos_de_Interes': ['Torre Eiffel', 'Louvre', 'Catedral de Notre-Dame']
    },
    'Nueva York': {
        'Pais': 'Estados Unidos',
        'Poblacion': 8398748,
        'Puntos_de_Interes': ['Estatua de la Libertad', 'Central Park', 'Times Square']
    },
    'Tokio': {
        'Pais': 'Japón',
        'Poblacion': 13929286,
        'Puntos_de_Interes': ['Torre de Tokio', 'Templo Senso-ji', 'Palacio Imperial']
    },
    "Londres" : {
        "País" : "Inglaterra",
        "Población" : 8982000,
        "Puntos_de_Interés" : ["Torre del reloj Big Ben", "La Abadia de Westminster", "Rueda de obserbación London Eye"]
    }
}

def ciudades(nombre):
    return ciudades_info.get(nombre, "La ciudad no se encuentra en la base de datos")


print("Busque uno de los 4 grandes, París, Nueva york, Japón o Londres")
ciudad = input("Qué ciudad desea buscar? ").title()
#ciudad = ciudad.capitalize()
print(ciudad)
a = ciudades(ciudad)
print(a)
