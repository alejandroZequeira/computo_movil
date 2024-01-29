from math import sqrt
from datetime import datetime
def distance(p1,p2):
    return sqrt((p2["lat"]-p1["lat"])**2 + (p2["lon"]-p1["lon"])**2)

def timeDiference(p1,p2):
    fecha1 = datetime.fromisoformat(p1["ts"].replace("Z", "+00:00"))
    fecha2 = datetime.fromisoformat(p2["ts"].replace("Z", "+00:00"))
    diferencia = fecha2 - fecha1
    diferencia_en_horas = diferencia.total_seconds() / 3600
  #  print(diferencia_en_horas)
    return abs(diferencia_en_horas)

def sumar_Lon_lat(p,Rmin,Rmax,parameter):
    suma=0
    if parameter=="lat":
        for a in range(Rmin,Rmax):
            suma  += p[a]["lat"]
    if parameter=="lon":
        for a in range(Rmin,Rmax):
            suma  += p[a]["lon"]
    return suma

def trayectoria(points,Od,Ot):
    n=len(points)
    i=1
    ruta=[] 
    while i<n:
        j=i+1
        while j<n:
            if distance(points[i],points[j])>=Od:
                if timeDiference(points[i],points[j])>=Ot:
                    subTrayoterySize=j-i+1
                    point={
                        "lat":sumar_Lon_lat(points,i,j,"lat")/subTrayoterySize,
                        "lon":sumar_Lon_lat(points,i,j,"lon")/subTrayoterySize,
                        "at":points[i]["ts"],
                        "dt":points[j]["ts"]
                           }
                    ruta.append(point)
                i=j
                break
            j=j+1
    return ruta