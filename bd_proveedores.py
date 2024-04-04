import random

# Generar el INSERT con los 20 registros
insert = "INSERT INTO Proveedor (id_categorias, contacto_prov, nombre_prov, telefono_prov, direccion_prov, electronico_prov) VALUES\n"

for i in range(20):
    # Generar número aleatorio del 1 al 7
    numero_aleatorio = random.randint(1, 7)
    
    # Restablecer las listas para que se repitan los valores
    contacto_prov = ["María López", "Juan Martínez", "Laura Sánchez", "Carlos Fernández", "Andrea Rodríguez", "Sergio González", "Ana Pérez", "Pablo Díaz", "Marta García", "Alejandro Ruiz", "Paula Torres", "Javier Moreno", "Lucia Navarro", "Diego Jiménez", "Elena Ramírez", "Daniel Ortiz", "Carmen Castro", "Marcos Herrera", "Sara Medina", "Adrián Castro"]
    nombre_prov = ["ModaStyle Distribuciones", "Tendencia Textil S.A.", "FashionEmporium Proveedores", "UrbanChic Suministros", "Elegance Couture Producers", "TrendyThreads Wholesale", "ModaVanguardia Distribución", "StyleFusion Suministros", "VogueVentures S.A.", "FashionForward Supplies", "GlamourGrove Proveedores", "CoutureConnect Distribuciones", "StreetStyle Trading Co.", "ChicWear Wholesale", "ModaExclusiva Distribución", "TrendyTrove Suministros", "CoutureCrafters S.A.", "UrbanEdge Suppliers", "FashionFocus Distribuciones", "StyleSavvy Wholesale"]
    direccion_prov = ['123 Calle Principal', '456 Avenida Central', '789 Calle Secundaria', '10 Avenida Norte', '24 Calle Este', '567 Calle Oeste', '890 Avenida Sur', '135 Calle Norte', '246 Avenida Este', '579 Calle Central', '802 Avenida Principal', '153 Calle Secundaria', '364 Avenida Norte', '697 Calle Este', '910 Avenida Oeste', '246 Calle Sur', '579 Avenida Norte', '802 Calle Este', '135 Avenida Sur', '468 Calle Oeste']
    
    # Seleccionar valores aleatorios de las listas
    contacto = random.choice(contacto_prov)
    nombre = random.choice(nombre_prov)
    telefono = random.randint(600000000, 699999999)  # Generar número aleatorio de teléfono en España
    direccion = random.choice(direccion_prov)
    email = f"{contacto.lower().replace(' ', '')}@{nombre.lower().replace(' ', '')}.com"  # Generar email combinando el nombre y el contacto
    
    # Agregar los valores al INSERT
    insert += f"({numero_aleatorio}, '{contacto}', '{nombre}', '{telefono}', '{direccion}', '{email}'),\n"

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)