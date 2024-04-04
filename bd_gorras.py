import random

# Lista de valores para generar datos aleatorios
talla_gorr = ["6 3/8", "6 1/2", "6 3/4", "6 7/8", "7", "7 1/8", "7 1/4", "7 3/8", "7 1/2", "7 5/8", "7 3/4", "7 7/8", "8", "8 1/8"]
cierre_gorr = ["Correa ajustable", "Snapback", "Velcro", "Hebilla metálica", "Cierre de plástico", "Elástico", "Cierre a presión", "Cinta de tela", "Cierre magnético", "Botón de presión"]
visera_gorr = ['Gorras de béisbol', 'Gorras planas (snapback)', 'Gorras de camionero (truckers)', 'Gorras de visera curva', 'Gorras de visera plana']

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los registros y el contador
insert = "INSERT INTO Gorras_Gorros (id_producto, talla_gorr, visera_gorr, cierre_gorr) VALUES\n"
contador = 2251

for i in range(275):
    talla = valor_aleatorio(talla_gorr)
    cierre = valor_aleatorio(cierre_gorr)
    visera = valor_aleatorio(visera_gorr)
    
    # Agregar los valores al INSERT
    insert += f"({contador}, '{talla}', '{visera}', '{cierre}'),\n"
    contador += 1

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
