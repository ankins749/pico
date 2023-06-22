import random

pacientes=[]

def menuprincipal():
    print('Menu registro de pacientes|')
    print('1 -   registro de paciente ')
    print('2 -   busqueda por rut     ')
    print('3 -   lista por tratamiento')
    print('4 -       SALIR            ')

def registro_de_paciente():
    rut=input('ingresa el rut del paciente(sin guion ni puntos): ')
    while len(rut) <8 or len(rut) > 9 or not rut.isalnum():
        print('Rut invalido, debe tener entre 8 a 9 caracteres numericos.')
        rut=input('ingresa el rut del paciente(sin guion ni puntos): ')

    nombre=input('ingrese el nombre del paciente: ')
    while not nombre:
        print('nombre invalido.')
        nombre=input('ingrese el nombre del paciente: ')  
    edad=input('ingresa la edad del paciente: ')
    while not edad.isdigit() or int (edad)<12:
        print('edad invalida solo mayores de 12 años')
        edad=input('ingresa la edad del paciente: ')

    tratamiento= input('ingresa el tratamiento del paciente (1)=blanqueamiento, (2)=tratamiento de conducto,(3)=implante dental:')
    while tratamiento not in ['1','2','3']:
        print('tratamiento invalido debe ser (1),(2),(3)')
        tratamiento= input('ingresa el tratamiento del paciente (1)=blanqueamiento, (2)=tratamiento de conducto,(3)=implante dental:')

    paciente={'rut':rut, 'nombre':nombre, 'edad': int(edad),'tratamiento':tratamiento }
    pacientes.append(paciente)
    print('registrado exitosamente')

def index():
    rut=input('ingresa el rut del paciente(sin guion ni puntos): ')
    encontrado= False
    for paciente in pacientes:
        if paciente ['rut']==rut:
            print('info del paciente')
            print('rut:',paciente['rut'])
            print('nombre:',paciente['nombre'])
            print('edad:',paciente['edad'])
            print('tratamiento:',paciente['tratamiento'])
            encontrado=True
            break

    if not encontrado:
        print('el paciente no forma parte del registro')        

def listado():
    print("¿Qué reportes desea generar?")
    print("1. Blanqueamiento")
    print("2. Tratamiento Conducto")
    print("3. Implante Dental")
    opcion= input ('ingresa el numero de la opcion deseada')
    while opcion not in ['1','2','3']:
         print('opcion invalida ingresa algunos de los numero ya descritos (1),(2),(3)')
         opcion= input ('ingresa el numero de la opcion deseada: ')
    
    tratamiento= ''
    if opcion=='1':
        tratamiento= 'blanqueamiento'
    elif opcion=='2':
        tratamiento= 'tratamiento de conducto'
    elif opcion=='3':
        tratamiento= 'implante dental'
    report_ge=0
    for paciente in pacientes:
        if paciente ['tratamiento']== opcion:
            ses_pend=random.randint(1,5)
            print('Reporte medico dental: ')
            print('sr/a',paciente['nombre'])
            print('rut',paciente['rut'])
            print('tratamiento',tratamiento)
            print('faltan',ses_pend,'sesiones por completar')
            report_ge +=1
    print('se generaron',report_ge,'reportes de',tratamiento)
#menu principal
while True:
    menuprincipal()
    opcion=input('ingresa el numero de la opcion: ')

    if opcion=='1':
        registro_de_paciente()
    elif opcion=='2':
        index()
    elif opcion=='3':
        listado()
    elif opcion=='4':
        print('buen dia')
        break
    else:
        print('ingresa una opcion valida')