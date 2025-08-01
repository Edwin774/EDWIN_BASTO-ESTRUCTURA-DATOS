lista_numeros = []

tuplas_pares = ()
tuplas_impares = ()


def agregar_par(num1, num2):
    """Agrega un par [num1, num2] a la lista principal."""
    lista_numeros.append([num1, num2])

def insertar_par(pos, num1, num2):
    """Inserta un par en una posición específica."""
    if 0 <= pos <= len(lista_numeros):
        lista_numeros.insert(pos, [num1, num2])
    else:
        print("Posición fuera de rango.")

def eliminar_ultimo():
    """Elimina el último par ingresado."""
    if lista_numeros:
        lista_numeros.pop()
    else:
        print("Lista vacía.")

def eliminar_por_posicion(pos):
    """Elimina el par ubicado en una posición específica."""
    if 0 <= pos < len(lista_numeros):
        lista_numeros.pop(pos)
    else:
        print("Posición inválida.")

def eliminar_par_valor(par):
    """Elimina un par específico si existe."""
    if par in lista_numeros:
        lista_numeros.remove(par)
    else:
        print("El par no está en la lista.")

def buscar_par(par):
    """Busca un par y devuelve su índice."""
    try:
        return lista_numeros.index(par)
    except ValueError:
        return -1

# -------------------- FUNCIONES PARA TUPLAS --------------------

def crear_tupla_pares(valores):
    """Crea una tupla solo con números pares."""
    global tuplas_pares
    tuplas_pares = tuple([n for n in valores if n % 2 == 0])

def crear_tupla_impares(valores):
    """Crea una tupla solo con números impares."""
    global tuplas_impares
    tuplas_impares = tuple([n for n in valores if n % 2 != 0])

def modificar_valor_tupla(tupla_tipo, posicion, nuevo_valor):
    """Modifica un valor en una tupla (pares o impares), creando una nueva."""
    global tuplas_pares, tuplas_impares
    if tupla_tipo == 'par':
        if 0 <= posicion < len(tuplas_pares):
            lista_temp = list(tuplas_pares)
            lista_temp[posicion] = nuevo_valor
            tuplas_pares = tuple(lista_temp)
    elif tupla_tipo == 'impar':
        if 0 <= posicion < len(tuplas_impares):
            lista_temp = list(tuplas_impares)
            lista_temp[posicion] = nuevo_valor
            tuplas_impares = tuple(lista_temp)

def eliminar_valor_tupla(tupla_tipo, valor):
    """Elimina un valor de una tupla (pares o impares), creando una nueva."""
    global tuplas_pares, tuplas_impares
    if tupla_tipo == 'par':
        if valor in tuplas_pares:
            lista_temp = list(tuplas_pares)
            lista_temp.remove(valor)
            tuplas_pares = tuple(lista_temp)
    elif tupla_tipo == 'impar':
        if valor in tuplas_impares:
            lista_temp = list(tuplas_impares)
            lista_temp.remove(valor)
            tuplas_impares = tuple(lista_temp)
