def es_bisiesto(anio):
    """
    Función que determina si un año es bisiesto o no.
    Un año es bisiesto si es divisible por 4 pero no por 100, 
    o si es divisible por 400.
    
    :param anio: Un número entero que representa el año a verificar.
    :return: True si el año es bisiesto, False si no lo es.
    """
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False
print(es_bisiesto(2000))  # Debe imprimir True
print(es_bisiesto(2004))  # Debe imprimir True
print(es_bisiesto(1900))  # Debe imprimir False
print(es_bisiesto(2001))  # Debe imprimir False
