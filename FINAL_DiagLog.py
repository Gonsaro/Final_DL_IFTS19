#GONZALO ROGET

despertar={1:"si",2:"no"}
parte1={1:"Llamar al trabajo y decir que te sentis mal",
        2:"Te duchas para despertarte y salis",
        3:"Te cambias con lo que tenes a mano y salis corriendo"}
opc_parte1={1:"Optas por la salida mas fácil. Te metés en la cama y volves a dormir como si nada.",
            2:"Ya estás llegando tarde asi que hora mas hora menos, mejor tomarselo con calma.",
            3:"No te gusta llegar tarde asi que salis a los tumbos."}
transporte={1:"1: Bicicleta, es la más rápida. Tardás 40 minutos pero llegas bastante transpirado.",
            2:"2: Subte Linea D, Tardas 45 minutos pero tenés que caminar unas cuadras desde tu casa y hasta el trabajo aunque es lo más rapido en transporte publico.",
            3:"3: Colectivo Linea 29. Tardas 50 minutos y tenés que caminar hasta la parada. Es lo mas lento pero te deja a una cuadra del trabajo"}
opc_tranqui={1: "Te bañaste al pedo porque llegas todo sudado a la oficina.",
            2:"Llegas a la boca del subte y te encontras con que esta cerrada. Tomas bicicleta o colectivo",
            3:"Te olvidaste que además del tiempo de viaje en bondi también tenes que esperarlo. Llegas 3 horas tarde al trabajo. Sos inimputable hermano."}
opc_apurado={1:"Llegas todo chivado a la oficina, por suerte siempre tenés un desodorante en la mochila para disimular.",
            2:"Terminas llegando 2 horas tarde, pero en la oficina no te dicen nada. Zafaste.",
            3:"El colectivo tarda una eternidad! Corriste al pedo porque terminas llegando mas de dos horas tarde y vas a tener que quedarte despues de hora para compensar."}

def validarInicio(valores):
	inicio=str(input("¿Te querés despertar?\nsi/no\n"))	
	while inicio not in valores.values():
		inicio = input("Opcion invalida\nVuelva a ingresar alguna opcion\n")
	return inicio

opc_tranqui[2]==False
def boole():
    if opc_tranqui[2]==True:
        print("Cual vas a elegir: 1 o 3")

inicio=validarInicio(despertar)	
if inicio != str(despertar[1]):
    print("zZz zZz zZz")
    exit()

if inicio == str(despertar[1]):
    print("""Abris los ojos y el sol te pega en la cara. Confundido y sin entender mucho"""
    """ agarras el celular y miras la hora: 10 de la mañana! 3 notificaciones de alarma perdida """
    """te indican que te quedaste dormido, y ya estás llegando una hora tarde minimo al trabajo,"""
    """ que querés hacer?\n""")
    for i in parte1:
        print(i, ":",parte1[i])

def opciones_transporte():
        print("Para llegar al trabajo tenes 3 opciones: ")
        print(transporte[1])
        print(transporte[2])
        print(transporte[3])

        print("Cual vas a elegir: ")


        

parte1=str(input())
if parte1 == str(1):
        print(opc_parte1[1])
        exit()
elif parte1 == str(2):
        print(opc_parte1[2])
        opciones_transporte()
        transporte=str(input())
        if transporte == str(1):
                print(opc_tranqui[1])       
        elif transporte == str(2):
                print(opc_tranqui[2])
                print("Cual vas a elegir: 1 o 3")
                transporte=str(input())
                if transporte == str(1):
                    print(opc_tranqui[1])
                elif transporte == str(3):
                    print(opc_tranqui[3])
                elif transporte == str(3):
                        print(opc_tranqui[3])
elif parte1 == str(3):
        print(opc_parte1[3])
        opciones_transporte()
        transporte=str(input())
        if transporte == str(1):
            print(opc_apurado[1])       
        elif transporte == str(2):
            print(opc_apurado[2])
        elif transporte == str(3):
                    print(opc_apurado[3])        