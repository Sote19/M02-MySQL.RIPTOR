import random

#ESTE ES ESPECIAL PARA UNA TIENDA DE ROPA, CAMBIARLO CON VUESTROS PRODUCTOS Y TABLAS!!!

# Lista de valores para generar datos aleatorios
nombres_productos = productos_ropa = ["perro callejero", "libro antiguo", "montaña rusa", "café caliente", "lápiz afilado", "jardín floreciente", "nube blanca", "viento suave", "música relajante", "gato negro", "tormenta eléctrica", "película clásica", "playa desierta", "cascada majestuosa", "árbol frondoso", "río serpenteante", "estrella brillante", "camino polvoriento", "piano melodioso", "pastel dulce", "ola gigante", "bosque encantado", "amanecer glorioso", "bosquejo rápido", "pájaro cantor", "fuego crepitante", "libro electrónico", "silla cómoda", "guitarra acústica", "estanque tranquilo", "noche estrellada", "hierba verde", "reloj antiguo", "café con leche", "mar embravecido", "puente colgante", "pincel suave", "copo de nieve", "torre alta", "vela encendida", "jardín secreto", "otoño dorado", "rincón acogedor", "taza vacía", "pez nadador", "sombrero grande", "niebla espesa", "escalera empinada"]
colores = ["Blanco", "Negro", "Gris", "Rojo", "Azul", "Verde", "Amarillo", "Naranja", "Rosa", "Morado", "Marrón", "Beige", "Turquesa", "Celeste", "Cian", "Lila", "Fucsia", "Violeta", "Carmesí", "Cobre", "Dorado", "Plateado", "Óxido", "Topacio", "Esmeralda", "Rubí", "Zafiro", "Ámbar", "Ciruela", "Magenta", "Coral", "Áureo", "Marfil", "Ceniza", "Carmin", "Ónice", "Perla", "Aguamarina", "Terracota", "Caoba", "Púrpura", "Índigo", "Salmonete", "Verde oliva", "Malaquita", "Amaranto", "Granate", "Almendra", "Jade"]
marcas = ["Nike", "Adidas", "Puma", "Reebok", "Under Armour", "NewYorker", "Quiksilver", "Volcom", "Levis", "New Balance", "Gramy", "Lacoste", "Fila"]
descripciones = ["Una opción perfecta para aquellos que buscan comodidad y estilo en un solo producto.", "Diseñado con materiales de alta calidad para garantizar durabilidad y rendimiento.", "Con un diseño moderno y elegante que se adapta a cualquier ocasión.", "La combinación perfecta de funcionalidad y elegancia para satisfacer tus necesidades diarias.", "Este producto te ofrece confort durante todo el día, sin comprometer tu estilo.", "Experimenta la comodidad suprema con este producto diseñado pensando en tu bienestar.", "Una elección versátil que se adapta a cualquier situación, desde reuniones formales hasta salidas informales.", "Con detalles cuidadosamente elaborados que destacan su calidad y artesanía.", "Descubre la innovación en cada detalle de este producto, diseñado para satisfacer tus expectativas más altas.", "Una opción imprescindible para aquellos que valoran la calidad y el estilo en igual medida.", "Diseñado pensando en tu comodidad, este producto te acompañará en todas tus aventuras.", "Con una atención meticulosa a cada detalle, este producto te ofrece una experiencia excepcional.", "Experimenta la libertad de movimiento con este producto que se adapta a tu estilo de vida activo.", "Una opción práctica y elegante que eleva tu estilo sin esfuerzo.", "Fabricado con los mejores materiales disponibles para garantizar su durabilidad y resistencia.", "Un producto diseñado para destacar en cualquier entorno, desde la oficina hasta la vida nocturna.", "Con un diseño atemporal que nunca pasa de moda, este producto es una inversión segura.", "Diseñado para aquellos que buscan rendimiento y estilo sin compromisos.", "Descubre la versatilidad de este producto que se adapta a tu estilo personal.", "Con detalles cuidadosamente elaborados y una atención excepcional a la calidad, este producto supera todas las expectativas."]
categorias = ["7"]#"1", "2", "3", "4", "5", "6", "7 "
materiales = ["Algodón", "Poliéster", "Lino", "Seda", "Nylon", "Lana", "Spandex", "Viscosa", "Rayón", "Denim", "Cuero", "Terciopelo", "Franela", "Chifón", "Jersey", "Cachemira", "Satén", "Corduroy", "Polar", "Bambú", "Modal", "Tela vaquera", "Tafetán", "Pana", "Tul", "Tencel", "Organza", "Mezclilla", "Sarga", "Felpa"]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los 1000 registros
insert = "INSERT INTO Productos (nombre, precio, color, marca, stock, descripcion, id_categorias, materiales) VALUES\n"

for i in range(525):
    nombre = valor_aleatorio(nombres_productos)
    precio = round(random.uniform(10, 100), 2)
    color = valor_aleatorio(colores)
    marca = valor_aleatorio(marcas)
    stock = random.randint(10, 100)
    descripcion = valor_aleatorio(descripciones)
    categoria = valor_aleatorio(categorias)
    material = valor_aleatorio(materiales)
    
    # Agregar los valores al INSERT
    insert += f"('{nombre}', {precio}, '{color}', '{marca}', {stock}, '{descripcion}', '{categoria}', '{material}'),\n"

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
