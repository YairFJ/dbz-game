#### THIS IS A GAME OF DBZ ####
import os
from Character import Character

print("****BIENVENIDO A DRAGON BALL Z GAME FUSION*****")

pj_list = []
name_list = []
i = 0
menu = "0"
while menu != "4":
    print("""Eliga una de las siguientes opciones:\n
            1)CREAR PJ\n
            2)FUSIONAR PJS\n
            3)MOSTRAR PJS\n
            4)SALIR\n""")

    menu = input(" ")
    if menu == "1":
        try:
            nombre = input("Ingrese el nombre de su PJ: ")
            fuerza = int(input("Ingrese la fuerza de su PJ: "))
            velocidad = int(input("Ingrese la velocidad de su PJ: "))
            vida = int(input("Ingrese la vida de su PJ: "))
            pj_list.append(Character(nombre, fuerza, velocidad, vida))
            for pj in pj_list:
                name_list.append(pj.nombre)
            print("Su personaje ha sido creado exitosamente .....\n")
            print("Enter para continuar")
            input()
            os.system('cls')
        except:
            print("No se ha podido crear su personaje")
            print("Enter para continuar")
            input()
            os.system('cls')

    elif menu == "2":
        try: 
            print("Debe elegir a que personajes quiere fusionar: ")   
            for count, value in enumerate(pj_list):
                print(count, value)
            one = int(input("Primer personaje a fusionar(Eliga uno de la lista ingresando su n°): "))
            two = int(input("Segundo personaje a fusionar: "))
            fusion = pj_list[one] + pj_list[two]
            pj_list.append(fusion)
            print(f"""Felicidades, su fusión ha sido exitosa\n
            He aquí el personaje creado {fusion}""")
            print("Enter para continuar")
            input()
            os.system('cls')
        except:
            print(f"Ha ocurrido un error en la fusión de los pj.")
            print("Enter para continuar")
            input()
            os.system('cls')    

    elif menu == "3":
        print("Aquí una lista de los personajes existentes")
        if len(pj_list) == 0:
            print("Usted aún no ha creado ningún personaje")
        else:
            print(f"""He aquí la lista de los personajes disponibles :\n
                    {pj_list}""")
        print("Enter para continuar")
        input()
        os.system('cls')
    
    elif menu == "4":
        print("El juego ha finalizado")
        break

    else:
        print("Porfavor ,Debe ingresar un numero correcto")
        input()
        os.system('cls')




    