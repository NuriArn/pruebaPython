clientes={}

def listar_clientes(tipo_clientes):
    for clave, valor in clientes.items():
        if tipo_clientes=='VIP':
            if valor['vip']:
                print(clave, valor)
        else:
            print(clave, valor)



texto='''
Seleccione entre las opciones del Menú \n
1.Añadir un cliente\n
2.Eliminar Cliente\n
3.Mostrar datos de un Cliente\n
4.Listar Clientes \n
5.Listar Clientes VIP\n
6.Terminar
'''



def listarClientes(tipo_cliente)
print('Los clientes VIP registrados son:')
        listar_clientes('VIP')
    opcion = input(texto)


opcion=input(texto)
while opcion!='6':
    if opcion=='1':
        dni=input('Ingrese el DNI del cliente: ')
        nombre=input('Ingrese el nombre del cliente: ')
        direccion=input('Ingrese la direccion del cliente: ')
        telefono=input('Ingrese el telefono del cliente: ')
        email=input('Ingrese el email del cliente: ')
        vip=input('Es un cliente VIP? (S/N): ')
        datos_persona={'nombre':nombre,'direccion':direccion,'telefono':telefono,'email':email,'vip':vip.upper()=='S'}
        clientes[dni]=datos_persona
    if opcion=='2':
        dni=input('Ingrese el DNI del cliente que desea eliminar:')
        if dni in clientes:
            del clientes[dni]
        else:
            print("El DNI ingresado no existe")
    if opcion=='3':
        dni=input('Ingrese el DNI del cliente que desea consultar:')
        if dni in clientes:
            print('DNI'+dni)
            for clave,valor in clientes[dni].items():
                print(clave + ':', valor)
        else:
            print("El DNI ingresado no existe")
    if opcion=='4':
        print('Los clientes registrados son:')
        listar_clientes('')

    if opcion=='5':
        print('Los clientes VIP registrados son:')
        listar_clientes('VIP')
    opcion = input(texto)