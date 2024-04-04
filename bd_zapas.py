import random

# Lista de valores para generar datos aleatorios
talla_zapa = ["36", "36.5", "37", "37.5", "38", "38.5", "39", "39.5", "40", "40.5", "41", "41.5", "42", "42.5", "43", "43.5", "44", "44.5", "45", "45.5", "46", "46.5", "47", "47.5", "48", "48.5", "49", "49.5", "50"]
material_suela_zapa = ['Goma', 'Caucho', 'Poliuretano', 'EVA (Etileno acetato de vinilo)', 'TPR (Caucho termoplástico)', 'Cuero', 'Crepé', 'Neopreno', 'PVC (Policloruro de vinilo)', 'Tela', 'Cork (Corcho)', 'Metal', 'Plástico', 'Fibra de carbono', 'Espuma', 'Sintético']

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los registros y el contador
insert = "INSERT INTO Zapatillas (id_producto, talla_zapa, material_suela_zapa) VALUES\n"
foren_key = 4476

for i in range(525):
    talla = valor_aleatorio(talla_zapa)
    suela = valor_aleatorio(material_suela_zapa)
    
    # Agregar los valores al INSERT
    insert += f"({foren_key}, '{talla}', '{suela}'),\n"
    foren_key += 1

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
