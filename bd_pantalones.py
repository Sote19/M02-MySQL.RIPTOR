import random

# Lista de valores para generar datos aleatorios
talla_pant = ["36", "38", "40", "42", "44", "46", "48", "50", "52", "54", "56", "XS", "S", "M", "L", "XL", "XXL", "XXXL"]
cierre_pant = ["Cremallera", "Botón", "Gancho y ojal", "Cinturón ajustable", "Elástico en la cintura", "Corchete", "Cierre de velcro", "Cierre de cordón", "Botones a presión", "Cierre magnético"]
corte_pant = ['Corte recto', 'Corte ajustado (skinny)', 'Corte slim', 'Corte bootcut', 'Corte flare', 'Corte boyfriend', 'Corte relaxed', 'Corte tapered', 'Corte cropped', 'Corte de pierna ancha (wide leg)']
bolsillo_pant = ["1", "0"]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los registros y el contador
insert = "INSERT INTO Pantalones (id_producto, talla_pant, cierre_pant, corte_pant, bolsillo_pant) VALUES\n"
contador = 2801

for i in range(1150):
    talla = valor_aleatorio(talla_pant)
    cierre = valor_aleatorio(cierre_pant)
    corte = valor_aleatorio(corte_pant)
    bolsillo = valor_aleatorio(bolsillo_pant)
    
    # Agregar los valores al INSERT
    insert += f"({contador}, '{talla}', '{cierre}', '{corte}', '{bolsillo}'),\n"
    contador += 1

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
