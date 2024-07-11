import time,os,random,csv


trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos= []
trabajadores_y_sueldo=[]
total_sueldos=[]
promedio_s=[]
media_geometrica=[]
datos_csv=[]


def validar_opciones(opciones):
    while True:
        try:
            opc = int(input("Ingrese una opcion: "))
            if opc in opciones:
                return opc
            else:
                print("ERROR,dene ingresar una opcion valida!")
        except:
            print("ERROR,debe ingresar la opcion en valor numerico!")


def asignar_sueldos():

    os.system("cls")
   
    SJuan_P =random.randint(300000,2500000)
    SMaria_G = random.randint(300000,2500000)
    SCarlos_L= random.randint(300000,2500000)
    SAna_M = random.randint(300000,2500000)
    SPedro_R = random.randint(300000,2500000)
    SLaura_H = random.randint(300000,2500000)
    SMiguel_S = random.randint(300000,2500000)
    SIsabel_G = random.randint(300000,2500000)
    SFrancisco_D =random.randint(300000,2500000)
    SElena_F =random.randint(300000,2500000)


    Juan_P = ["Juan Pérez",SJuan_P]
    Maria_G = ["María García",SMaria_G]
    Carlos_L= ["Carlos López",SCarlos_L]
    Ana_M = ["Ana Martínez",SAna_M]
    Pedro_R = ["Pedro Rodríguez",SPedro_R]
    Laura_H = ["Laura Hernández",SLaura_H]
    Miguel_S = ["Miguel Sánchez",SMiguel_S]
    Isabel_G = ["Isabel Gómez",SIsabel_G]
    Francisco_D =["Francisco Díaz",SFrancisco_D]
    Elena_F = ["Elena Fernández",SElena_F]

    trabajadores_y_sueldo.append(Juan_P)
    trabajadores_y_sueldo.append(Maria_G)
    trabajadores_y_sueldo.append(Carlos_L)
    trabajadores_y_sueldo.append(Ana_M)
    trabajadores_y_sueldo.append(Pedro_R)
    trabajadores_y_sueldo.append(Laura_H)
    trabajadores_y_sueldo.append(Miguel_S)
    trabajadores_y_sueldo.append(Isabel_G)
    trabajadores_y_sueldo.append(Francisco_D)
    trabajadores_y_sueldo.append(Elena_F)
    sueldos.append(SJuan_P)
    sueldos.append(SMaria_G)
    sueldos.append(SCarlos_L)
    sueldos.append(SAna_M)
    sueldos.append(SPedro_R)
    sueldos.append(SLaura_H)
    sueldos.append(SMiguel_S)
    sueldos.append(SIsabel_G)
    sueldos.append(SFrancisco_D)
    sueldos.append(SElena_F)
    total= SJuan_P+SMaria_G+SCarlos_L+SAna_M+SPedro_R+SLaura_H+SMiguel_S+SIsabel_G+SFrancisco_D+SElena_F
    prome= total / 10

    MG = (SJuan_P*SMaria_G*SCarlos_L*SAna_M*SPedro_R*SLaura_H*SMiguel_S*SIsabel_G*SFrancisco_D*SElena_F)**1/10
    total_sueldos.append(total)
    promedio_s.append(prome)
    media_geometrica.append(MG)
    
   
    print("Sueldos generados!!!")
    time.sleep(3)
 
    
def clasificar_sueldos():
    os.system("cls")
    if not (trabajadores_y_sueldo):
        print("No se han encontrado datos, debe crear los sueldos!")
        time.sleep(3)
    else:
        sueldos_bajos=[]
        sueldos_medios=[]
        sueldos_altos=[]
        for x in trabajadores_y_sueldo:
            if x[1] < 800000:
                I = [x[0],x[1]]
                sueldos_bajos.append(I)
            elif x[1] >=800000 and x[1] < 2000000:
                I = [x[0],x[1]]
                sueldos_medios.append(I)
            else:
                I = [x[0],x[1]]
                sueldos_altos.append(I)

        print(f"Sueldos menores a $800.000= {len(sueldos_bajos)}")
        print("Nombre empleado  Sueldo")
        for o in sueldos_bajos:
            print(o)
        print("")
        print(f"Sueldos entre $800.000 y $2.000.000= {len(sueldos_bajos)}")
        print("Nombre empleado  Sueldo")
        for v in sueldos_medios:
            print(v)
        print("")
        print(f"Sueldos superiores a $2.000.000= {len(sueldos_bajos)}")
        print("Nombre empleado  Sueldo")
        for c in sueldos_altos:
            print(c)
        print("\n\n")
        print(f"TOTAL SUELDOS: {total_sueldos}")
        time.sleep(5)
    

def ver_estaisticas():
    os.system("cls")
    if not (trabajadores_y_sueldo):
        print("No se han encontrado datos, debe crear los sueldos!")
        time.sleep(3)
    else:
        menor_sueldo=sueldos[0]
        mayor_sueldo=sueldos[0]
        for x in sueldos:
            
            if x < menor_sueldo:
                menor_sueldo = x
        for x in sueldos:
            if x > mayor_sueldo:
                mayor_sueldo=x
        print(f"Sueldo mas alto: {mayor_sueldo}\n")
        print(f"Sueldo mas bajo: {menor_sueldo}\n")
        print(f"Promedio de sueldos: {promedio_s}\n")
        print(f"Media geometrica: {media_geometrica}")

    time.sleep(3)
def descuento_salud(x):
    descuento= (x*7)//100
    total_desc = x - descuento
    
    return total_desc
def descuento_AFP(x):
    descuento= (x*12)//100
    total_desc = x - descuento
 
    return total_desc

def sueldo_liquido(x):
    descuento1= (x*7)//100
    descuento2= (x*12)//100
    total_desc = x - descuento1-descuento2
  
    return  total_desc

def reporte_sueldos():
    os.system("cls")
    if not (trabajadores_y_sueldo):
        print("No se han encontrado datos, debe crear los sueldos!")
        time.sleep(3)
    else:
        print("Nombre Empleado     Sueldo Base     Descuento salud     Descuento AFP   Sueldo liquido")
        for x in trabajadores_y_sueldo:
            descuento_AF=descuento_AFP(x[1])
            descuento_SA=descuento_salud(x[1])
            sueldo_li=sueldo_liquido(x[1])
            datos = print(f"{x[0]}\t{x[1]}\t{descuento_SA}\t{descuento_AF}\t{sueldo_li}")
            datos_csv.append(datos)
          

        with open("Reporte Sueldos.csv","w",newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow("Nombre Empleado     Sueldo Base     Descuento salud     Descuento AFP   Sueldo liquido")
            for L in trabajadores_y_sueldo:
                escritor.writerow(L)
    time.sleep(5)
