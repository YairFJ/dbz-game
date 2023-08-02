#### THIS IS A GAME OF DBZ ####
import os
from Character import Character

print("****BIENVENIDO A DRAGON BALL Z GAME FUSION*****")

pj_list = []
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
            pj_list.append(Character(nombre, fuerza, velocidad, vida)) # Acá estamos agregamos el objeto de la clase Character a una lista
            print("Su personaje ha sido creado exitosamente .....\n")
            print("Enter para continuar")
            input()
            os.system('cls') # Limpiamos la cosnsola
        except:
            print("No se ha podido crear su personaje")
            print("Enter para continuar")
            input()
            os.system('cls')

    elif menu == "2":
        try: 
            print("Debe elegir a que personajes quiere fusionar: ")   
            for count, value in enumerate(pj_list):  # Aca estamos enumerando los elementos de la lista atravez de la función enumerate para que el usuario pueda elegir uno
                print(count, value)
            one = int(input("Primer personaje a fusionar(Eliga uno de la lista ingresando su n°): ")) # Almacenamos el primer pj que eligió el usuario
            two = int(input("Segundo personaje a fusionar: ")) # Almacenamos el primer pj que eligió el usuario
            fusion = pj_list[one] + pj_list[two]  #En esta variable guardamos la fusión de los personajes que eligio el usuario anteriormente
            pj_list.append(fusion) # Agregamos el personaje a la lista de personajes
            print(f"""Felicidades, su fusión ha sido exitosa\n
            He aquí el personaje creado {fusion}""") # Mostramos el personaje ya fusionado junto con sus propiedades 
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
        if len(pj_list) == 0: # A travez del método len() podemos contar los elementos de la lista(En este caso si no hay ningun elemento imprimiremos los siguiente)
            print("Usted aún no ha creado ningún personaje")
        else:
            print(f"""He aquí la lista de los personajes disponibles :\n
                    {pj_list}""")  # Acá estamos mostrando la lista con los personajes ya creados anteriormente
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




    