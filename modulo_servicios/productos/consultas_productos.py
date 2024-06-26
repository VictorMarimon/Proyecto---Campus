import sys
import os

sys.path.append("../..")

from datosGenerales.datos import *

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RUTA_JSON = os.path.join(project_root, "modulo_servicios", "productos", "productos.json")

def referencia_productos(categoria):
    datos = cargar_datos(RUTA_JSON)

    referencias = []

    for i in datos["productos"][0][categoria]:
        referencias.append(str(i["referencia"]))
    
    return referencias

def tipo_productos():
    datos = cargar_datos(RUTA_JSON)

    referencias = []

    for i in datos["productos"][0]:

        referencias.append(str(i))
    
    return referencias

def total_productos():
    datos = cargar_datos(RUTA_JSON)
    cantidad_productos = 0

    contador_telefonos = 0
    contador_computadores = 0
    contador_accesorios = 0
    contador_tablets = 0
    contador_electrodomesticos = 0
    

    for i in datos["productos"]:
        for llave, valor in i.items():
            for j in valor:
                if(j["eliminado"] == False):
                    cantidad_productos += 1
                    if(llave == "telefonos"):
                        contador_telefonos += 1
                    elif(llave == "computadores"):
                        contador_computadores += 1
                    elif(llave == "accesorios"):
                        contador_accesorios += 1
                    elif(llave == "tablets"):
                        contador_tablets += 1
                    elif(llave == "electrodomesticos"):
                        contador_electrodomesticos += 1
    print("")
    print(f"Total productos ofrecidos: {cantidad_productos}")
    print("")
    print(f"Telefonos: {contador_telefonos}") if contador_telefonos > 0 else contador_telefonos
    print(f"Computadores: {contador_computadores}") if contador_computadores > 0 else contador_computadores
    print(f"Accesorios: {contador_accesorios}") if contador_accesorios > 0 else contador_accesorios
    print(f"Tablets: {contador_tablets}") if contador_tablets > 0 else contador_tablets
    print(f"Electrodomesticos: {contador_electrodomesticos}") if contador_electrodomesticos > 0 else contador_electrodomesticos                

def productos_catalogo():
    datos_json = cargar_datos(RUTA_JSON)
    productos_enviados = []
    contador_productos = 0
    for llave, valor in datos_json["productos"][0].items():
        if(llave == "telefonos"):
            id=0
            for i in valor:
                if(i["eliminado"] == False and i["id"] == id):
                    productos = {}
                    contador_productos += 1
                    productos["articulo"] = "telefonos"
                    productos["referencia"] = i["referencia"]
                    productos["nombre"] = i["nombre"]
                    productos["precio"] = i["precio"]
                    productos_enviados.append(productos)
                id += 2
        elif(llave == "computadores"):
            id=0
            for i in valor:
                if(i["eliminado"] == False and i["id"] == id):
                    productos = {}
                    contador_productos += 1
                    productos["articulo"] = "computadores"
                    productos["referencia"] = i["referencia"]
                    productos["nombre"] = i["nombre"]
                    productos["precio"] = i["precio"]
                    productos_enviados.append(productos)
                id += 2
        elif(llave == "accesorios"):
            id=0
            for i in valor:
                if(i["eliminado"] == False and i["id"] == id):
                    productos = {}
                    contador_productos += 1
                    productos["articulo"] = "accesorios"
                    productos["referencia"] = i["referencia"]
                    productos["nombre"] = i["nombre"]
                    productos["precio"] = i["precio"]
                    productos_enviados.append(productos)
                id += 2
        elif(llave == "tablets"):
            id=0
            for i in valor:
                if(i["eliminado"] == False and i["id"] == id):
                    productos = {}
                    contador_productos += 1
                    productos["articulo"] = "tablets"
                    productos["referencia"] = i["referencia"]
                    productos["nombre"] = i["nombre"]
                    productos["precio"] = i["precio"]
                    productos_enviados.append(productos)
                id += 2
        elif(llave == "electrodomesticos"):
            id=0
            for i in valor:
                if(i["eliminado"] == False and i["id"] == id):
                    productos = {}
                    contador_productos += 1
                    productos["articulo"] = "electrodomesticos"
                    productos["referencia"] = i["referencia"]
                    productos["nombre"] = i["nombre"]
                    productos["precio"] = i["precio"]
                    productos_enviados.append(productos)
                id += 2
    if(contador_productos == 0):
        return("No se han registrado productos")
    return(productos_enviados)

#print(productos_catalogo())
#productos_catalogo()