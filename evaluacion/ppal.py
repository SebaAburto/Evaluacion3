import funciones as f


Jugadores=[]


op=0
while op!=4:
    print("""********** SISTEMA DE PUNTAJES eShirlitos **********\n
    1.Registrar puntajes torneo
    2.Listar los todos puntajes
    3.Imprimir por Tipo
    4.Salir\n""")
    print("*"*50,"\n")
    op=int(input("Opción: "))
    try:
        if op==1:
            f.Ingresar_datos(Jugadores)
        elif op==2:
            f.mostrar_listado(Jugadores)
        elif op==3:
            print(".")
        elif op==4:
            print("Saliendo...")
        else:
            print("Opción fuera de rango.")
    except:
        print("Opción debe ser un número.")
        
        
    
