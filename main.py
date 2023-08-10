import json
import os
import ast
import time


##########################################################################################
# Crear Archivos
##########################################################################################



def InicializarArchivos():
    #limpiar los datos
    NuevosDatos = [
        "1/10011\n",
        "2/1000111\n",
        "3/11\n",
        "4/101111001101\n",
        "5/1001111110\n",
        "6/0\n",
        "7/0\n",
        "8/100111\n",
        "9/10001\n",
        "10/1001\n"
    ]
    
    file = open("Datos/memorias.txt", "w")
    for fila in NuevosDatos:
        file.write(fila)
    file.close()
    
    #limpiar el ac
    nuevoAc = []

    file = open("Datos/AC.txt")
    for fila in nuevoAc:
        file.write(fila)
    file.close()
    #limpiar las memorias

    nuevaMemoria = ["1250/1100101\n",
        "1251 /101000010010001000\n",
        "1252/1100101\n",
        "1253/11010111010\n",
        "1254/10000001110010000\n",
        "1255/11\n"
    ]

    file = open("Datos/memorias.txt")
    for fila in nuevaMemoria:
        file.write(fila)
    file.close()


def CrearArchivoInstrucciones():
    existe = os.path.exists("Datos/inst.txt")
    if existe:
        pass
    else:
        file = open("Datos/inst.txt", "w")
        # file.write("Lista de Usuarios")
        # file.write("\n")
        file.close()


def CrearArchivoMemorias():
    existeMe = os.path.exists("Datos/memorias.txt")
    if existeMe:
        pass
    else:
        file = open("Datos/memorias.txt", "w")
        # file.write("Registro de pacientes")
        # file.write("\n")
        file.close()


def CrearArchivoAC():
    existeAC = os.path.exists("Datos/AC.txt")
    if existeAC:
        pass
    else:
        file = open("Datos/AC.txt", "w")
        # file.write("Registro de medicos")
        # file.write("\n")
        file.close()


def CrearArchivoOperaciones():
    existeOp = os.path.exists("Datos/operaciones.txt")
    if existeOp:
        pass
    else:
        file = open("Datos/operaciones.txt", "w")
        # file.write("Registro de medicos")
        # file.write("\n")
        file.close()

def CrearArchivoDispositivos():
    existeES = os.path.exists("Datos/dispositivos.txt")
    if existeES:
        pass
    else:
        file = open("Datos/dispositivos.txt", "w")
        # file.write("Registro de medicos")
        # file.write("\n")
        file.close()

def ObtenerInst(id):
    CrearArchivoInstrucciones()
    file = open("Datos/inst.txt", "r")
    filas = file.readlines()
    filasTemporal = []

    for fila in filas:
        if int(fila[0]) == id:
            operacion = fila.split("/")
            filasTemporal.append({
                "Instruccion": operacion[1],
            })
    file.close()
    return filasTemporal


def ObtenerMemoria(id):
    CrearArchivoMemorias()
    file = open("Datos/memorias.txt", "r")
    filas = file.readlines()
    filasTemporal = []

    for fila in filas:
        memo = fila.split("/")
        puntero = memo[0]
        if puntero == id:
            memo = fila.split("/")
            filasTemporal.append({
                "variable": memo[1],
            })
    file.close()
    return filasTemporal

def ObtenerDispositivo(id):
    CrearArchivoDispositivos()
    file = open("Datos/dispositivos.txt", "r")
    filas = file.readlines()
    filasTemporal = []

    for fila in filas:
        dis = fila.split("/")
        puntero = dis[0]
        if puntero == id:
            dis = fila.split("/")
            filasTemporal.append({
                "dispositivo": dis[1],
            })
    file.close()
    return filasTemporal

def ObtenerOperaciones():
    CrearArchivoOperaciones()
    file = open("Datos/operaciones.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        operaciones = fila.split("/")
        filasTemporal.append({"instruccion": operaciones[0],
                              "memoria1": operaciones[1],
                              "memoria2": operaciones[2],

                              })
    file.close()
    return filasTemporal


def ObtenerAC():
    CrearArchivoAC()
    file = open("Datos/AC.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        ac = fila.split("/")
        filasTemporal.append({"ac": ac[0],
                              })
    file.close()
    return filasTemporal


# ////////////////////////////////////////////////

def Conversion(bin):
    decimal = 0
    i = 0

    while (bin > 0):
        digito = bin % 10
        bin = int(bin // 10)
        decimal = decimal + digito * (2 ** i)
        i = i + 1
    # SALIDA
    return decimal


def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario



def Operaciones():
    listaOperaciones = ObtenerOperaciones()
    print(listaOperaciones)
    for elemento in listaOperaciones:
        instruccion = elemento['instruccion']
        memoria1 = elemento['memoria1']
        memoria2 = elemento['memoria2']
        inst = Conversion(int(instruccion))

        file = open("Datos/inst.txt", "r")
        filas = file.readlines()
        filasTemporal = []
        for fila in filas:
            instr = fila.split("/")
            filasTemporal.append(instr[0])

        if inst == 1:
            Inst1(memoria1)
        elif inst == 2:
            Inst2(memoria1)
        elif inst == 3:
            Inst3(memoria1)
        elif inst == 4:
            Inst4(memoria1, memoria2)
        elif inst == 5:
            Inst5(memoria1)
        elif inst == 6:
            Inst6(memoria1, memoria2)
        elif inst == 7:
            Inst7(memoria1)
        elif inst == 8:
            Inst8(memoria1)
        elif inst == 9:
            Inst9(memoria1)
        elif inst == 10:
            Inst10(memoria1, memoria2)
        elif inst == 11:
            Inst11(memoria1, memoria2)
        elif inst == 12:
            Inst12(memoria1)
        elif inst == 13:
            Inst13(memoria1, memoria2)

    else:
        print("Ya no hay isntrucciones por ejecutar :)")
    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac',
                                                                                                             '').replace(
        ':', '').replace("'", '')
    print("----------------------------------")
    print("El AC final es: ", ac_limpio  , "en decimal es: ", Conversion((int(ac_limpio))))


def EditarMemoria(id, var):
    CrearArchivoMemorias()
    file = open("Datos/memorias.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        mem = fila.split("/")
        if int(mem[0]) == id:
            filaModificada = ""
            filaModificada = filaModificada + (str(id) + "/")
            filaModificada = filaModificada + (str(var) + "/")
            filaModificada = filaModificada + ("\n")
            filasTemporal.append(filaModificada)
        else:
            filasTemporal.append(fila)
    file.close()
    file = open("Datos/memorias.txt", "w")
    for fila in filasTemporal:
        file.write(fila)
    file.close()

def EditarDispositivo(id, dis):
    CrearArchivoDispositivos()
    file = open("Datos/dispositivos.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        ae = fila.split("/")
        if int(ae[0]) == id:
            filaModificada = ""
            filaModificada = filaModificada + (str(id) + "/")
            filaModificada = filaModificada + (str(dis) )
            filaModificada = filaModificada + ("\n")
            filasTemporal.append(filaModificada)
        else:
            filasTemporal.append(fila)
    file.close()
    file = open("Datos/dispositivos.txt", "w")
    for fila in filasTemporal:
        file.write(fila)
    file.close()
##########################################################################################
# Instrucciones
##########################################################################################


# Instrucción 1 Carga de memoria 1 hacia AC
def Inst1(memoria1):
    mem1 = Conversion(int(memoria1))
    lista = ObtenerMemoria(str(mem1))
    valor_variable = lista[0]['variable']
    # Eliminar espacios en blanco y saltos de línea del valor
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')
    print('Este AC es de la inst 1', valor_limpio, "en decimal es: ", Conversion(int(valor_limpio)))
    file = open("Datos/AC.txt", "w")
    file.write(str(valor_limpio) + "/")


# Instrucción 2 Almacenar en memoria 1 desde AC

def Inst2(memoria1):
    # Almacenar en memoria 1 desde AC
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerMemoria(str(mem1))  # 1252/ 1100101
    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac',
                                                                                                             '').replace(
        ':', '').replace("'", '')
    print('Este AC es de la inst 2', ac_limpio , "en decimal es: ", Conversion(int(ac_limpio)))
    EditarMemoria(mem1, ac_limpio)


# Instrucción 3 Suma: memoria 1 + AC

def Inst3(memoria1):
    # Suma: memoria 1 + AC
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerMemoria(str(mem1))  # 1252/ 1100101
    valor_variable = lista[0]['variable']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac',
                                                                                                             '').replace(
        ':', '').replace("'", '')
    acNuevo = Conversion(int(valor_limpio)) + Conversion(int(ac_limpio))

    print('Este es el nuevo AC de la inst 3: ', decimal_a_binario(acNuevo) , "en decimal es: ", acNuevo)
    file = open("Datos/AC.txt", "w")
    file.write(str(decimal_a_binario(acNuevo)) + "/")


# Instrucción 4 Suma: memoria 1 + memoria 2 + AC
def Inst4(memoria1, memoria2):
    # Suma: memoria 1 + AC
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerMemoria(str(mem1))  # 1252/ 1100101
    valor_variable = lista[0]['variable']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    mem2 = Conversion(int(memoria2))  # 1252
    lista2 = ObtenerMemoria(str(mem2))  # 1252/ 1100101
    valor_variable2 = lista2[0]['variable']
    valor_limpio2 = valor_variable2.strip().replace(' ', '').replace('\n', '')

    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac','').replace(
        ':', '').replace("'", '')
    acNuevo = Conversion(int(valor_limpio)) + Conversion(int(valor_limpio2)) + Conversion(int(ac_limpio))
    print('Este es el nuevo AC de la inst 4:',decimal_a_binario(acNuevo) , "en decimal es: ", acNuevo)
    file = open("Datos/AC.txt", "w")
    file.write(str(decimal_a_binario(acNuevo)) + "/")


# Instrucción 5 Resta: AC – memoria 1, almacena en AC

def Inst5(memoria1):
    # Resta: AC – memoria 1, almacena en AC
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerMemoria(str(mem1))  # 1252/ 1100101
    valor_variable = lista[0]['variable']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac',
                                                                                                             '').replace(
        ':', '').replace("'", '')
    acD = Conversion(int(ac_limpio))
    memD = Conversion(int(valor_limpio))
    acNuevo =  acD - memD
    print('Este es el nuevo AC de la inst 5: ', decimal_a_binario(acNuevo) , "en decimal es: ", acNuevo)
    acDef = decimal_a_binario(acNuevo)
    aceDEFF = acDef.replace('b', '')
    file = open("Datos/AC.txt", "w")
    file.write(str(aceDEFF) + "/")


# Instrucción 6 Resta: AC – memoria 1, almacena en memoria 2

def Inst6(memoria1, memoria2):
    # Resta: AC – memoria 1, almacena en memoria 2
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerMemoria(str(mem1))  # 1252/ 1100101
    valor_variable = lista[0]['variable']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    mem2 = Conversion(int(memoria2))  # 1252

    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac',
                                                                                                             '').replace(
        ':', '').replace("'", '')
    mem_nueva = Conversion(int(ac_limpio)) - Conversion(int(valor_limpio))
    print("Esta es el nuevo valor de la memoria", mem1, ' : ', mem_nueva, " en decimal es: ", decimal_a_binario(mem_nueva))
    EditarMemoria(mem2, decimal_a_binario(mem_nueva))


# Instrucción 7 Multiplicación: memoria 1 x AC, almacena en AC
def Inst7(memoria1):
    # Multiplicación: memoria 1 x AC, almacena en AC
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerMemoria(str(mem1))  # 1252/ 1100101
    valor_variable = lista[0]['variable']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac',
                                                                                                             '').replace(
        ':', '').replace("'", '')
    acNuevo = Conversion(int(ac_limpio)) * Conversion(int(valor_limpio))
    print('Este es el nuevo AC de la inst 7', decimal_a_binario(acNuevo) , "en decimal es: ", acNuevo)
    file = open("Datos/AC.txt", "w")
    file.write(str(decimal_a_binario(acNuevo)) + "/")


# Instrucción 8 Carga de AC desde ES
def Inst8(memoria1):
    #8-0004-0000
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerDispositivo(str(mem1))  # 1252/ 1100101
    valor_variable = lista[0]['dispositivo']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    acNuevo = valor_limpio
    print('Este es el nuevo AC de la inst 8', acNuevo , "en decimal es: ", Conversion(int(acNuevo)))
    file = open("Datos/AC.txt", "w")
    file.write(str(acNuevo)+ "/")

# Instrucción 9 Guardar en ES desde AC
def Inst9(memoria1):

    dis1 = Conversion(int(memoria1))  # 1
    lista = ObtenerDispositivo(str(dis1))  # 1/ 1100101
    valor_variable = lista[0]['dispositivo']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac',
                                                                                                             '').replace(
        ':', '').replace("'", '')
    print('Este AC es de la inst 9: ', ac_limpio , "en decimal es: ", Conversion(int(ac_limpio)))
    EditarDispositivo(dis1, ac_limpio)

# Instrucción 10 Suma: memoria 1 + memoria 2, almacena en memoria 1
def Inst10(memoria1, memoria2):
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerMemoria(str(mem1))  # 1252/ 1100101
    valor_variable = lista[0]['variable']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    mem2 = Conversion(int(memoria2))  # 1252
    lista2 = ObtenerMemoria(str(mem2))  # 1252/ 1100101
    valor_variable2 = lista2[0]['variable']
    valor_limpio2 = valor_variable2.strip().replace(' ', '').replace('\n', '')

    mem_nueva = Conversion(int(valor_limpio)) + Conversion(int(valor_limpio2))
    print("Esta es el nuevo valor de la memoria", mem1, ' : ', mem_nueva, " en decimal es: ",
          decimal_a_binario(mem_nueva))
    EditarMemoria(mem1, decimal_a_binario(mem_nueva))

# Instrucción 11 Multiplicación: memoria 1 x AC, almacena en memoria 2
def Inst11(memoria1, memoria2):
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerMemoria(str(mem1))  # 1252/ 1100101
    valor_variable = lista[0]['variable']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    mem2 = Conversion(int(memoria2))  # 1252

    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac',
                                                                                                             '').replace(
        ':', '').replace("'", '')
    mem_nueva = Conversion(int(valor_limpio)) * Conversion(int(ac_limpio))
    print("Esta es el nuevo valor de la memoria", mem2, ' : ', mem_nueva, " en binario es: ",
          decimal_a_binario(mem_nueva))
    EditarMemoria(mem2, decimal_a_binario(mem_nueva))

# Instrucción 12 División: AC divide memoria 1, almacena en AC
def Inst12(memoria1):
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerMemoria(str(mem1))  # 1252/ 1100101
    valor_variable = lista[0]['variable']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac',
                                                                                                             '').replace(
        ':', '').replace("'", '')
    acNuevo = Conversion(int(ac_limpio)) / Conversion(int(valor_limpio))
    print('Este es el nuevo AC de la inst 12: ', decimal_a_binario(int(acNuevo)) , "en decimal es: ", acNuevo)
    file = open("Datos/AC.txt", "w")
    file.write(str(decimal_a_binario(int(acNuevo))) + "/")

# Instrucción 13 División: AC divide 1, almacena en memoria 2
def Inst13(memoria1, memoria2):
    mem1 = Conversion(int(memoria1))  # 1252
    lista = ObtenerMemoria(str(mem1))  # 1252/ 1100101
    valor_variable = lista[0]['variable']
    valor_limpio = valor_variable.strip().replace(' ', '').replace('\n', '')

    mem2 = Conversion(int(memoria2))  # 1252
    lista2 = ObtenerMemoria(str(mem2))  # 1252/ 1100101
    valor_variable2 = lista2[0]['variable']
    valor_limpio2 = valor_variable2.strip().replace(' ', '').replace('\n', '')

    ac = ObtenerAC()  # 1100101
    ac_semilimpio = ac[0]['ac']
    ac_limpio = ac_semilimpio.replace(' ', '').replace('\n', '').replace('[{', '').replace('}]', '').replace('ac',
                                                                                                           '').replace(
        ':', '').replace("'", '')
    memNueva = Conversion(int(ac_limpio)) / Conversion(int(valor_limpio))
    print("Esta es el nuevo valor de la memoria", mem1, ' : ', memNueva, " en binario es: ",
          decimal_a_binario (memNueva))
    EditarMemoria(mem2, decimal_a_binario(memNueva))

while 1 == 1:
    print("----------------Bienvenido--------------")
    CrearArchivoInstrucciones()
    CrearArchivoMemorias()
    CrearArchivoAC()
    CrearArchivoOperaciones()
    CrearArchivoDispositivos()
    Operaciones()
    break

