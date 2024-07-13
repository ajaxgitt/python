import cProfile

def funcion_principal():
    # Código principal a evaluar
    r = 1 + 1
    return r

# Ejecutar cProfile para perfilar la función principal
cProfile.run('funcion_principal()')
