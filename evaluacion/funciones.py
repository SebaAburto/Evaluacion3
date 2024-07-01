

def Ingresar_datos(Jugadores):
    
    unJugador=[]
    
    menu1=True
    while menu1:
        tipo=""
        juegos=[]
        full_nombre=[]
        id_jugador=str(input("Ingrese su ID de jugador: "))
        if id_jugador==0:
            print("el ID no puede estar vacío.")
        else:
            unJugador.append(id_jugador)
            nombre=str(input("Escriba su nombre: "))
            if nombre=="":
                print("el nombre no puede estar vacío.")
            else:
                full_nombre.append(nombre)
                apellido=str(input("Escriba su apellido: "))
                if apellido=="":
                    print("el apellido no puede estar vacío.")
                else:
                    full_nombre.append(apellido)
                    unJugador.append(full_nombre)
                    opjuego=0
                    contador=0
                    while contador<3 and opjuego!=4:
                        print("¿En qué juegos compite?(1-3):")
                        print("""
    1) VALORANT
    2) FORTNITE
    3) FIFA
    4) Salir\n""")
                        try: 
                            opjuego=int(input("opción: "))
                            puntaje1=0
                            puntaje2=0
                            puntaje3=0
                            if opjuego==1:
                                puntaje1=int(input("Ingrese su puntaje obtenido en VALORANT: "))
                                contador+=1
                                juegos.append(puntaje1)

                            elif opjuego==2:
                                puntaje2=int(input("Ingrese su puntaje obtenido en FORNITE: "))
                                contador+=1
                                juegos.append(puntaje2)

                            elif opjuego==3:
                                puntaje3=int(input("Ingrese su puntaje obtenido en FIFA: "))
                                contador+=1  
                                juegos.append(puntaje3)  

                            elif opjuego==4:
                                break                   
                            else:
                                print("opción inválida")
                        except:
                            ("opción debe ser un número") 
                    unJugador.append(juegos)
                menutipo=True
                while menutipo:
                    try:
                        print("Seleccione su nivel(1-3): \n")
                        print("""
    1) Principiant
    2) Avanzado
    3) Experto\n""")
                        optipo=int(input("Opción: "))
                        if optipo==1:    
                            tipo="Principiante"
                            menutipo=False                  
                        elif optipo==2:    
                            tipo="Avanzado"
                            menutipo=False
                        elif optipo==3:    
                            tipo="Experto"
                            menutipo=False
                        else:
                            print("opción inválida.")
                    except:
                        print("Seleccione una opción entre 1 y 3.")
    
        unJugador.append(tipo)
        Jugadores.append(unJugador)
        menu1=False
    return Jugadores        




def mostrar_listado(Jugadores):
    if len(Jugadores)==0:
        print("No hay puntajes ingresados.")
    else:
        print("Id Jugador | ","Nombre | ","VALORANT | ","FORNITE | ","FIFA | ","Tipo |")
        print(Jugadores)
        



    


