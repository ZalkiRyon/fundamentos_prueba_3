cargos = ["ceo", "desarrollador", "analista de datos"]
empleados = []
list_analista = []
list_desarolla= []
list_ceo= []

def numeros(a):
    return "{:,}".format(a).replace(",", ".")
    #${numeros(i[2])}

def menu_principal():    
    while True:
        print("="*20, "Menú Principal", "="*20)
        print("1. Registrar trabajador")
        print("2. Listar los todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("0. Salir del Programa")
        try:
            op_menu_p = int(input("Elija una opción ->"))
            if op_menu_p == 1:
                registro_user()
            if op_menu_p == 2:    
                if empleados == []:
                    print("No hay trabajadores registrados aún.")        
                lista_trabajadores()
            if op_menu_p == 3:
                if empleados == []:
                    print("No hay trabajadores registrados aún.")
                else:                              
                    planilla_sueldos()
            if op_menu_p == 0:
                print("Gracias por usar nuestro sistema.")
                break
        except:
            print("Ingrese un valor valido")

def planilla_sueldos():    
    while True:
        print("==========Plantilla de sueldos==========")
        print("1. Imprimir todos los trabajadores")
        print("2. Imprimir todos los CEO")
        print("3. Imprimir todos los Desarrolladores")
        print("4. Imprimir todos los Analistas de Datos")
        print("0. Salir")
        try:
            op_planilla = int(input("Indique la opción deseada -> "))
            if op_planilla == 0:
                break
            if op_planilla == 1:
                for i in empleados:
                    print(f"Nombre: {i[0].title()} // Cargo: {i[1].title()} // Sueldo Bruto: ${numeros(i[2])} // Des. Salud: ${numeros(i[3])} // Des. AFP: ${numeros(i[4])} // Liquido a pagar: ${numeros(i[5])}")
            if op_planilla == 2:
                for i in list_ceo:
                    print(f"Nombre: {i[0].title()} // Cargo: {i[1].title()} // Sueldo Bruto: ${numeros(i[2])} // Des. Salud: ${numeros(i[3])} // Des. AFP: ${numeros(i[4])} // Liquido a pagar: ${numeros(i[5])}")
                    if list_ceo == {}:
                        print("No hay trabajadores registrados con este cargo")
            if op_planilla == 3:
                for i in list_desarolla:
                    print(f"Nombre: {i[0].title()} // Cargo: {i[1].title()} // Sueldo Bruto: ${numeros(i[2])} // Des. Salud: ${numeros(i[3])} // Des. AFP: ${numeros(i[4])} // Liquido a pagar: ${numeros(i[5])}")
                    if list_desarolla == {}:
                        print("No hay trabajadores registrados con este cargo")
            if op_planilla == 4:
                for i in list_analista:
                    print(f"Nombre: {i[0].title()} // Cargo: {i[1].title()} // Sueldo Bruto: ${numeros(i[2])} // Des. Salud: ${numeros(i[3])} // Des. AFP: ${numeros(i[4])} // Liquido a pagar: ${numeros(i[5])}")
                    if list_analista == {}:
                        print("No hay trabajadores registrados con este cargo")
        except:
            print("Ingrese un valor valido")
      
def registro_user():        
    while True:
        nombre= input("Ingrese nombre del trabajador-> ").lower()
        if nombre == "":
            print("Es necesario ingresar un nombre")
            break
        cargo = input("Ingrese el cargo del trabajador\n (CEO, Desarrollador o Analista de Datos) -> ").lower()
        if cargo not in cargos:
            print("El cargo debe corresponder a una de la opciones indicadas")  
            break                                              
        try:
            sueldo_bruto=int(input("Ingrese sueldo bruto del trabajador ->$"))
            if sueldo_bruto < 459999:
                print("El valor debe ser sobre el minimo legal")  
                break
        except:
            print("El valor debe ser númerico")
            break 

        salud = int(0.07 * sueldo_bruto)
        afp = int(0.12 * sueldo_bruto)
        liquido = sueldo_bruto - salud - afp
        empleados.append((nombre, cargo, sueldo_bruto, salud, afp, liquido))   
        if cargo == "ceo":
            list_ceo.append((nombre, cargo, sueldo_bruto, salud, afp, liquido))  
        if cargo == "desarrollador":
            list_desarolla.append((nombre, cargo, sueldo_bruto, salud, afp, liquido))   
        if cargo == "analista de datos":
            list_analista.append((nombre, cargo, sueldo_bruto, salud, afp, liquido))
        print("Trabajador registrado Correctamente")       
        break

def lista_trabajadores ():
    for i in empleados:
        print(f"Nombre: {i[0].title()} // Cargo: {i[1].title()} // Sueldo Bruto: ${numeros(i[2])}")
      
menu_principal()  