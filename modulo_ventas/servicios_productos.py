import sys

sys.path.append("..")

from modulo_servicios.productos.consultas_productos import productos_catalogo
from modulo_servicios.servicios.consultas_servicios import servicios_catalogo
from datosGenerales.datos import *

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_ventas/registro.json"
RUTA_JSON_VENTAS = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_ventas/ventas.json"

def actualizar_registro():
    datos = cargar_datos(RUTA_JSON)
    for i in datos:
            datos["productos"] = productos_catalogo()
            datos["servicios"] = servicios_catalogo()
            guardar_datos(datos, RUTA_JSON)

def leer_registos():
    datos = cargar_datos(RUTA_JSON)
    cantidad_productos = 0
    cantidad_servicios = 0
    for llave,valor in datos.items():
        if(llave == "servicios"):
            print("CATALOGO SERVICIOS")
            for j in valor:
                cantidad_servicios += 1
                print("")
                print(f"Servicio No. {cantidad_servicios}")
                print("")
                print(f"Tipo: {j["articulo"]}")
                print(f"Referencia: {j["referencia"]}")
                print(f"Nombre: {j["nombre"]}")
                print(f"Precio: {j["precio"]}")
                print("")
        elif(llave == "productos"):
            print("CATALOGO PRODUCTOS")
            for j in valor:
                cantidad_productos += 1
                print("")
                print(f"Producto No. {cantidad_productos}")
                print("")
                print(f"Tipo: {j["articulo"]}")
                print(f"Referencia: {j["referencia"]}")
                print(f"Nombre: {j["nombre"]}")
                print(f"Precio: {j["precio"]}")
                print("")

def compras_usuarios():
    datos = cargar_datos(RUTA_JSON_VENTAS)
    compras_totales = []
    for i in datos["ventas"]:
        if(i["categoria"] == "servicios"):
            compras = {}
            compras["documento_usuario"] = i["documento_usuario"]
            compras["cantidad_servicios"] = i["cantidad"]
            encontrado = False
            for servicio in compras_totales:
                if servicio["documento_usuario"] == compras["documento_usuario"]:
                    servicio["cantidad_servicios"] += i["cantidad"]
                    encontrado = True
                    break

            if not encontrado:
                compras_totales.append(compras)
    return compras_totales