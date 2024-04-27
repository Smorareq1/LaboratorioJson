import json
import os

#Ruta donde guardar el json
ruta_archivo_json = r"C:\Users\smora\Downloads\Pruebas json\productos.json"

#Arreglo de productos
productos = [
  {
    "id": 1,
    "nombre": "Camiseta básica",
    "descripcion": "Camiseta de algodón para uso diario",
    "precio": 15.99,
    "stock": 100,
    "categoria": "Ropa"
  },
  {
    "id": 2,
    "nombre": "Pantalón vaquero",
    "descripcion": "Pantalón de mezclilla resistente",
    "precio": 29.99,
    "stock": 50,
    "categoria": "Ropa"
  },
  {
    "id": 3,
    "nombre": "Zapatillas deportivas",
    "descripcion": "Zapatillas cómodas para entrenamiento",
    "precio": 49.99,
    "stock": 75,
    "categoria": "Calzado"
  },
  {
    "id": 4,
    "nombre": "Mochila escolar",
    "descripcion": "Mochila con varios compartimentos",
    "precio": 39.99,
    "stock": 30,
    "categoria": "Accesorios"
  },
  {
    "id": 5,
    "nombre": "Reloj de pulsera",
    "descripcion": "Reloj analógico con correa de cuero",
    "precio": 79.99,
    "stock": 20,
    "categoria": "Accesorios"
  },
  {
    "id": 6,
    "nombre": "Gafas de sol",
    "descripcion": "Gafas con protección UV",
    "precio": 24.99,
    "stock": 15,
    "categoria": "Accesorios"
  },
  {
    "id": 7,
    "nombre": "Libreta de notas",
    "descripcion": "Libreta con hojas rayadas",
    "precio": 5.99,
    "stock": 80,
    "categoria": "Papelería"
  },
  {
    "id": 8,
    "nombre": "Teclado inalámbrico",
    "descripcion": "Teclado compatible con varios dispositivos",
    "precio": 39.99,
    "stock": 25,
    "categoria": "Electrónica"
  },
  {
    "id": 9,
    "nombre": "Altavoces Bluetooth",
    "descripcion": "Altavoces portátiles con conexión Bluetooth",
    "precio": 59.99,
    "stock": 40,
    "categoria": "Electrónica"
  },
  {
    "id": 10,
    "nombre": "Cámara digital",
    "descripcion": "Cámara compacta con alta resolución",
    "precio": 199.99,
    "stock": 10,
    "categoria": "Electrónica"
  },
  {
    "id": 11,
    "nombre": "Bolígrafo de tinta",
    "descripcion": "Bolígrafo de tinta negra",
    "precio": 1.99,
    "stock": 150,
    "categoria": "Papelería"
  },
  {
    "id": 12,
    "nombre": "Auriculares con cable",
    "descripcion": "Auriculares con cable jack estándar",
    "precio": 19.99,
    "stock": 60,
    "categoria": "Electrónica"
  },
  {
    "id": 13,
    "nombre": "Sudadera con capucha",
    "descripcion": "Sudadera de algodón con bolsillo canguro",
    "precio": 34.99,
    "stock": 45,
    "categoria": "Ropa"
  },
  {
    "id": 14,
    "nombre": "Lápiz de dibujo",
    "descripcion": "Lápiz con mina suave para dibujar",
    "precio": 2.49,
    "stock": 100,
    "categoria": "Papelería"
  },
  {
    "id": 15,
    "nombre": "Cepillo de dientes eléctrico",
    "descripcion": "Cepillo de dientes recargable con cabezales intercambiables",
    "precio": 49.99,
    "stock": 20,
    "categoria": "Cuidado personal"
  },
  {
    "id": 16,
    "nombre": "Mesa plegable",
    "descripcion": "Mesa portátil para uso en exteriores",
    "precio": 79.99,
    "stock": 10,
    "categoria": "Hogar"
  },
  {
    "id": 17,
    "nombre": "Lámpara de escritorio",
    "descripcion": "Lámpara LED ajustable para escritorio",
    "precio": 29.99,
    "stock": 30,
    "categoria": "Hogar"
  },
  {
    "id": 18,
    "nombre": "Cargador portátil",
    "descripcion": "Cargador externo para dispositivos móviles",
    "precio": 24.99,
    "stock": 50,
    "categoria": "Accesorios"
  },
  {
    "id": 19,
    "nombre": "Bicicleta de montaña",
    "descripcion": "Bicicleta todo terreno con cambios",
    "precio": 399.99,
    "stock": 5,
    "categoria": "Transporte"
  },
  {
    "id": 20,
    "nombre": "Cámara de seguridad",
    "descripcion": "Cámara IP para monitoreo remoto",
    "precio": 129.99,
    "stock": 15,
    "categoria": "Camara"
  }
] 
# Convertir el arreglo de productos a un archivo JSON
with open(ruta_archivo_json, "w") as archivo_json:
    json.dump(productos, archivo_json, indent=2)

# Función para cargar los productos desde el archivo JSON
def cargar_productos():
    # Verificar si el archivo JSON existe
    if os.path.exists(ruta_archivo_json):
        # Cargar datos desde el archivo JSON
        with open(ruta_archivo_json, "r") as archivo_json:
            productos = json.load(archivo_json)
    else:
        productos = []

    return productos

# Funciones para filtrar y ordenar productos
def filtrar_productos_categoria(categoria):
    # Filtrar productos por categoría
    productos_filtrados = [producto for producto in productos if producto["categoria"] == categoria]

    return productos_filtrados

#Funciones para filtrar y ordenar productos

def filtrar_productos_stock_mayorA0(stock_minimo):
    # Filtrar productos por stock mayor a un valor mínimo
    productos_filtrados = [producto for producto in productos if producto["stock"] > stock_minimo]

    return productos_filtrados

def filtrarPorPrecio(precio_maximo):
    # Filtrar productos por precio menor a un valor máximo
    productos_filtrados = [producto for producto in productos if producto["precio"] < precio_maximo]
    return productos_filtrados


def ordenar_productos(criterio):
    # Ordenar productos según criterio
    productos_ordenados = sorted(productos, key=lambda x: x[criterio])

    return productos_ordenados


# Arreglo leido de json
productos = cargar_productos()

#uso
productos_filtradosCategoria= filtrar_productos_categoria(categoria="Transporte")
print("Productos filtrados por categoría y precio máximo:")
for producto in productos_filtradosCategoria:
    print(producto)

productos_filtradosStock = filtrar_productos_stock_mayorA0(stock_minimo=50)
print("\nProductos filtrados por stock mayor a 50:")
for producto in productos_filtradosStock:
    print(producto)

productos_filtradosPrecio = filtrarPorPrecio(precio_maximo=20)
print("\nProductos filtrados por precio menor a 20:")
for producto in productos_filtradosPrecio:
    print(producto)

productos_ordenados = ordenar_productos(criterio="precio")
print("\nProductos ordenados por precio ascendente:")
for producto in productos_ordenados:
    print(producto)