# TPO 2 DSSC 
# ---------------------------------------------------------------
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import math

# Bucle de ingreso de nombre de archivo
# ---------------------------------------------------------------
cont_error = 0
default="perfil.txt"
while True:
    try:
        nombre_archivo = str(input("-->Ingrese el nombre del arhivo: ") or default)
        print(nombre_archivo)
    except ValueError:
        print("Error en el ingreso del nombre")
        cont_error += 1
        if cont_error >= 3:
            nombre_archivo=default
            print(f"Valor por defecto archivo: {nombre_archivo}")
            break
        continue

    if  os.path.isfile(nombre_archivo):
        print(f"El archivo {nombre_archivo} existe!")
        break
    else:
        print(f"El nombre del archivo {nombre_archivo} es incorrecto!")
        cont_error += 1
        if cont_error >= 3:
            nombre_archivo=default
            print(f"Valor por defecto archivo: {nombre_archivo}")
            break
        continue
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Bucle de ingreso de Columna Altitud del archivo
cont_error=0
default=3
while True:
    try:
        column_alt = int(input("-->Ingrese el numero de la columna altitud: ") or default)
        print(column_alt)
    except ValueError:
        print("Error en el ingreso!")
        cont_error += 1
        if cont_error >= 3:
            column_alt=default
            print(f"Valor por defecto Columna: {column_alt}")
            break
        continue

    if column_alt < 0:
        print("Debes escribir un número positivo.")
        cont_error += 1
        if cont_error >= 3:
            column_alt=default
            print(f"Valor por defecto Columna: {column_alt}")
            break
        continue
    else:
        break
# ---------------------------------------------------------------

# Abro y leo el archivo declarado. Genero el vector con los datos del perfil de elevacion 
# ---------------------------------------------------------------
with open(nombre_archivo, newline='') as f:
    datos =csv.reader(f, delimiter='\t')
    #Cargo vector Altura
    line_count = 0
    vectorAlt= []
    for row in datos:
        if line_count == 0:
            line_count += 1
        else: 
            vectorAlt.append(float(row[column_alt]))
            line_count += 1
    print(f'Se procesaron {line_count} lineas del archivo {nombre_archivo}.\n')
#    print(f'\n{vectorAlt} \n')
# ---------------------------------------------------------------

# Bucle de ingreso de Distancia entre Torres
# ---------------------------------------------------------------
cont_error=0
default=43
while True:
    try:
        DistanciaTorres = int(input("-->Ingrese la distancia entre Torres en [Km]: ") or default )
        print(DistanciaTorres)
    except ValueError:
        print("Error en el ingreso!")
        cont_error += 1
        if cont_error >= 3:
            DistanciaTorres=default
            print(f"Valor por defecto Distancia entre Torres: {DistanciaTorres}")
            break
        continue

    if DistanciaTorres < 0:
        print("Debes escribir un número positivo.")
        cont_error += 1
        if cont_error >= 3:
            DistanciaTorres=default
            print(f"Valor por defecto Distancia entre Torres: {DistanciaTorres}")
            break
        continue
    else:
        break
# ---------------------------------------------------------------

# Bucle de ingreso de la frecuencia de trabajo
# ---------------------------------------------------------------
cont_error=0
default=4000
while True:
    try:
        Frecuencia = int(input("-->Ingrese la frecuencia de trabajo en [MHz]: ") or default )
        print(Frecuencia)
    except ValueError:
        print("Error en el ingreso!")
        cont_error += 1
        if cont_error >= 3:
            Frecuencia=default
            print(f"Valor por defecto frecuencia: {Frecuencia}")
            break
        continue

    if Frecuencia < 0:
        print("Debes escribir un número positivo.")
        cont_error += 1
        if cont_error >= 3:
            Frecuencia=default
            print(f"Valor por defecto frecuencia: {Frecuencia}")
            break
        continue
    else:
        break
# ---------------------------------------------------------------


# Ejercicio Punto A
# Determine el despeje de un enlace de RF en 4GHz entre estacines A y B distantes L distancia.
# ---------------------------------------------------------------
vectH=[]
#VectorDistancia = [i for i in range(len(vectorAlt))]
VectorDistancia=[]
a=DistanciaTorres/len(vectorAlt)
b=0
for i in range(len(vectorAlt)):
    VectorDistancia.append(b)
    b+=a

Rn=[]
AlturaMax=0
RadioFresnel=1

# Calculo de la region de Fresnel Rn(i)
# ---------------------------------------------------------------
largo=len(vectorAlt)
for i in range(largo):
    Rn.append(547.074*math.sqrt((RadioFresnel*(VectorDistancia[i])*VectorDistancia[(largo-1)- i])/(Frecuencia*DistanciaTorres)))
    # Constante 547.074 sale del ajuste de km a m multiplicado la constante n=17.3 --> 17.3*sqtr(1000)=547.074

# Calculo de la altura Maxima
# ---------------------------------------------------------------
for i in range(len(vectorAlt)):
    vectH.append(0.6*Rn[i]+vectorAlt[i])
    if vectH[i]>AlturaMax:
        AlturaMax=vectH[i]

# Imprimo la Altura Maxima
# ---------------------------------------------------------------
print(f'\nRESPUESTA EJERCICIO A')
print("La altura maxima es: {0:.2f} metros".format(AlturaMax))
 

# Imprimo Alturas de Torre A y B
# ---------------------------------------------------------------
AlturaTorreA= AlturaMax - vectorAlt[0]
AlturaTorreB= AlturaMax - vectorAlt[largo-1] 
print("La altura de la Torre A es: {0:.2f} metros".format(AlturaTorreA))
print("La altura de la Torre B es: {0:.2f} metros".format(AlturaTorreB))

# Imprimo la Cantidad de Tramos para la Torre A y B. Usando tramos de torre de 6 metros
# ---------------------------------------------------------------
CantidadTramoA= math.ceil(AlturaTorreA/6) 
CantidadTramoB= math.ceil(AlturaTorreB/6)
print(f'La cantidad de tramos de la Torre A son: {CantidadTramoA}')      
print(f'La cantidad de tramos de la Torre B son: {CantidadTramoB}')


# Grafico de la zona de Fresnel y del terreno
newRn=np.array(Rn)
#plt.plot(VectorDistancia,((0.6*Rn)+AlturaMax),'b',VectorDistancia ,(- (0.6*Rn)+AlturaMax),'b',VectorDistancia,Rn+AlturaMax,'r',VectorDistancia,- Rn+AlturaMax,'r',VectorDistancia,VectorAltura,'g')
plt.plot(VectorDistancia,((0.6*newRn)+AlturaMax),'b',VectorDistancia ,(- (0.6*newRn)+AlturaMax),'b',VectorDistancia,newRn+AlturaMax,'r',VectorDistancia,- newRn+AlturaMax,'r',VectorDistancia,vectorAlt,'g')
plt.title('Radio de Fresnel')
plt.xlabel('Distancia entre las antenas [km]')
plt.ylabel('Altura [m]') 
#Establezco limites variables para que el radio de fresnell aparezca completo
plt.ylim(0,newRn[math.ceil(largo/2)]+AlturaMax+5)
plt.xlim(0,DistanciaTorres)
plt.grid() 
plt.show()


# Ejercicio Punto B
# Determine con Excel o Matlab el margen de Fading que se posee en este mismo enlace, en donde el PIRE es de 41dbm,
# Antenas iguales, en RX y TX con ganancia de 18dBi y un receptor con potencia minima detectable de -95dbm.
# ---------------------------------------------------------------
# Ptel=32.4+20*log10(f)+20*log10(d)
# PIRE= Pt + Gt
# Prx= PIRE + Gr - Pel - Pobs - Pconec 
Pmin= -95;
PIRE=41;
Gr=18;
Patm=0;
Pobs=0;
#Calculo de la Perdida en el espacio libre
Pel=32.45+20*math.log10(Frecuencia)+20*math.log10(DistanciaTorres)
#Calculo de la Potencia recibida en el receptor
Prx=PIRE+Gr-Pel-Patm-Pobs;
# Calculo del Margen de Fadding
MF= Prx - Pmin;

#Imprimo Margen de Fadding
print(f'\n RESPUESTA EJERCICIO B')
print("El Margen de Fading es: {0:.4} dBm".format(MF))
