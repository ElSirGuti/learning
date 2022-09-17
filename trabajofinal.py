#                                             Programa realizado por: ====> Andrés Gutierrez
#                                                            Seccion: ====> 10312
#                                                              Curso: ====> Programacion II
#                                                           Proyecto: ====> Calculadora Cientifica

## Una empresa de desarrollo de sofware te ha contratado para programar un calculadora basada en lineas
## de comandos (CLI) para un proyecto de uno de sus clientes que es una institucion cientifica

## Esta calculadora cientifica debe contar con los siguientes modulos a programar:
## ====>  Consola de comando 
## ====>  Perimetro de un rectangulo
## ====>  Calcular El Tiempo Tiempo
## ====>  Volumen de un cubo




## Modulo 1: ===> Perimetro de un rectangulo(prectangulo): Calcular el perimetro de un rectangulo.
## Formula:  ===> (2 x base) + (2 x altura)
def prectangulo(base,altura):
    return (2*base)+(2*altura)

## Modulo 2: ===> Volumen de una piramide(vpiramide): Calcular el volumen de una piramide.
## Formula:  ===> (1/3) x base x altura

def vpiramide(base,altura):
    return (1/3) * base * altura

## Modulo 3: ===> Calcular el tiempo(ctiempo):solicita al usuario una cantidad en horas y regresa su
## equivalente dias, minutos y segundos.

### Para realizar esta operacion lo haremos con tres modulos:

### Modulo 3.1: Transformar las horas a dias 
### Formula: ===> Horas/24
def ctiempo(horas):
    return horas/24

### Modulo 3.2: Transformar las horas a minutos
##  Formula: ===> Horas x 60
def cminutos(horas):
    return horas * 60

### Modulo 3.3: Transformar las horas a segundos
### Formula: ===> Horas x 3600
def csegundos(horas):
    return  horas * 3600

## Modulo 4: ===> Volumen de un cubo: Calcular el volumen de un cubo
## Formula: ====> Lado x Lado x Lado
def vcubo(lado):
    return lado**3


######### Principal ###########

def main():
    config = open("configuracion.txt", "r")
    lineas = config.read().splitlines()

    rutaerrores = lineas[0].split('=')[1]
    rutahistorial = lineas[1].split('=')[1]
    prectanguloact = lineas[2].split('=')[1] == "act"
    vpiramideact = lineas[3].split('=')[1] == "act"
    ctiempoact = lineas[4].split('=')[1] == "act"
    vcuboact = lineas[5].split('=')[1] == "act"

    errores = []
    historial = []
    archivoerror = open(rutaerrores, 'r')
    for linea in archivoerror.readlines():
        errores.append(linea)
    archivoerror.close()

    archivohistorial = open(rutahistorial, 'r')
    for linea in archivohistorial:
        historial.append(linea)
    archivohistorial.close()

    
##################################################################################################################
    while True:
        print ("====== Bienvenidos A Nuestra Calculadora Cientifica =======" + "\n" )
        print ("==>  Por Favor Escriba En Comando Para Realizar Una Operacion :"  )
        print(" prectangulo ===>  Perimetro De Un Rectangulo")
        print(" vpiramide   ===>  Volumen De Una Piramide")
        print(" ctiempo     ===>  Trasformar horas a dias,minutos y segundos")
        print(" vcubo       ===>  Volumen de un cubo")  
        print(" salir           ===>  Salir " + "\n")

        print("==========  OPCIONES  ============ "+ "\n" )
        print ("===> Errores")
        print ("===> Historial")

        command = input("")
###################################################################################################################

        try:
            if command == "prectangulo" and prectanguloact:

                
                base = float(input("Base ==>"))
                altura = float(input("Altura ==>"))
                
                result = prectangulo(base,altura)
                print("El Perimetro Del Rectangulo Es: " ,prectangulo(base,altura))
 
                historial.append("Perimetro rectangulo. Base: " + str(base) + ". Altura: " + str(altura) + ". Resultado: " + str(result))
               
                print("======   Presione ENTER para continuar   ======")
                command = input("")
                if command == "":
                    continue
                
##########################################################################################################################################

               
            elif command == "vpiramide" and vpiramideact:

                base = float(input("Base ==>"))
                altura = float(input("Altura ==>"))
                
                print("El Volumen De La Piramide Es: " ,vpiramide(base,altura))
                result = vpiramide(base, altura)
                
                
                historial.append("Volumen piramide. Radio: " + str(base) + ". Altura: " + str(altura) + ". Resultado: " + str(result))

                print("======   Presione ENTER para continuar   ======")
                command = input("")
                if command == (""):
                    continue 

        
                
##########################################################################################################################################

            elif command == "ctiempo" and ctiempoact:

                horas = float(input("Horas : "))
                print("Dias: ", ctiempo(horas))
                print("Minutos: ",cminutos(horas))
                print("Segundos:", csegundos(horas))

            
                dias = ctiempo(horas)
                minutos = cminutos(horas)
                segundos = csegundos(horas)
                
                
                historial.append("Tiempo . dias: " + str(dias) + ". minutos : " + str(minutos) + ". segundos: " + str(segundos))

                print("======   Presione ENTER para continuar   ======")
                command = input("")
                if command == (""):
                    continue 
###########################################################################################################################################
                
            elif command == "vcubo" and vcuboact:
                
                lado = float(input("Lados: "))
                print("El volumen del cubo es: ",vcubo(lado))
                result = vcubo(lado)
                
                historial.append("Volumen cubo. lado: " + str(lado) + ". Resultado: " + str(result))

                print("======   Presione ENTER para continuar   ======")
                command = input("")
                if command == (""):
                    continue
                
###########################################################################################################################################


        
            elif command == "errores":
                for error in errores:
                    print(error)
                    continue
            elif command == "historial":
                for operacion in historial:
                    print(operacion)
                    continue
            elif command == "salir":
                
                print ("======   Gracias Por Usar Nuestra Calculadora   ======")
                break
                
            else:
                print("Comando no valido")
                continue
        except Exception as error:
            print("Ha ocurrido un error, intente de nuevo")
            errores.append(str(error))
            archivoerror = open("errores.txt", "a")
            archivoerror.write(str(error) + "\n")
            archivoerror.close()
    
    archivohistorial = open(rutahistorial, "a")
    for operacion in historial:
        archivohistorial.write(operacion + "\n")
    archivohistorial.close()

main()
