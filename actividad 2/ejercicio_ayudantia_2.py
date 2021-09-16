# Ayudantía 2

# Ejercicio 1
# Resultado esperado
# Film;Opening Weekend;Worldwide Gross;Budget

# Comienza escribiendo aquí tu código
# Abre el archivo, carga los datos e imprime la primera línea

with open('datos_peliculas.csv') as open_file:
    # file = []
    file = open_file.readlines()
    print(file[0])
    open_file.close()

# No olvides cerrar el archivo

###############################################

# Ejercicio 2
# Resultado esperado
# The To-Do List;1579402;3566225;1.5

# Funciones recomendadas
# split --> Separar una línea (string) en una lista
# replace --> Reemplazar un caracter por otro dentro de un string
# No olvides considerar los \n dentro de tu código

# Escribe tu código acá

datos_listos = []
for fila in file:
    fila = fila.replace('\n', '')
    film, opening_weekend, worldwide_gross, budget = fila.split(';')
    opening_weekend = opening_weekend.replace('.', '')
    worldwide_gross = worldwide_gross.replace('.', '').replace(',', '')
    budget = budget.replace(',', '.')

    t = True
    for col in (film, opening_weekend, worldwide_gross, budget):
        if col == '' or col == '-':
            t = False
            break
    if t:
        datos_listos.append(f'{film};{opening_weekend};{worldwide_gross};{budget}')

###############################################

# Ejercicio 3
# Funciones recomendadas
# join --> Unir los elementos de una lista en un string
# No olvides cerrar el archivo

# Escribe tu código acá

with open('datos_peliculas_procesados.csv', 'w') as open_file:
    open_file.write('\n'.join(datos_listos))








