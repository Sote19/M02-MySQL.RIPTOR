import random

# Lista de categorías y descripciones
nombre_cat = ["Camisetas", "Chaquetas", "Gorras_Gorros", "Ropa_interior", "Pantalones", "Sudaderas", "Zapatillas"]
descripcion_cat = [
    "Prendas superiores de manga corta o larga, generalmente de algodón, utilizadas como ropa casual o deportiva.",
    "Prendas exteriores que cubren el torso y los brazos, diseñadas para proteger contra el frío o la lluvia.",
    "Accesorios para la cabeza que pueden incluir sombreros con visera o sin ella, gorras de béisbol, entre otros.",
    "Prendas íntimas que se llevan debajo de la ropa exterior, como sujetadores, calzoncillos, entre otros.",
    "Prendas inferiores que cubren las piernas, como pantalones largos, cortos o faldas.",
    "Prendas superiores de manga larga con capucha, diseñadas para proporcionar comodidad y calidez.",
    "Calzado deportivo diseñado para actividades físicas como correr, caminar o entrenar."
]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los registros
insert_categoria = "INSERT INTO Categorias (nombre_cat, descripcion_cat) VALUES\n"

for nombre in nombre_cat:
    descripcion = descripcion_cat[nombre_cat.index(nombre)]
    
    # Agregar los valores al INSERT
    insert_categoria += f"('{nombre}', '{descripcion}'),\n"

# Eliminar la coma extra al final y agregar punto y coma
insert_categoria = insert_categoria[:-2] + ";"

# Imprimir el INSERT generado
print(insert_categoria)
    