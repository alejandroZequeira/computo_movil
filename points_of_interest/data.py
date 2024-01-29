import json
import algorith1
with open("dataset/Records.json") as archivo:
    datos=json.load(archivo)

def formatear(data):
    datos=[]
    for d in data["locations"]:
        datos.append({
            "lat":d["latitudeE7"],
            "lon":d["longitudeE7"],
            "ts":d["timestamp"],
        })
    return datos

data=formatear(datos)
print(data[0]["ts"])

rutas=algorith1.trayectoria(data,100,5/60)
print(rutas[0])