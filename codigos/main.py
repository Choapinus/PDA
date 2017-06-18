from automata import get_adn, automata

if __name__ == '__main__':
	#variables
	adn = get_adn() #retorna una lista
	result = [] #ingresaremos los resultados del automata
	string = '' #inicializamos la variable
	contador = {'alzheimer': 0, 'parkinson': 0, 'epilepsia': 0} #contador de cada enfermedad
	keys = list(contador.keys()) 
	#keys del diccionario contador parseado a list (.keys() retorna un dict_keys) para poder ser indexado
	#end variables

	#begin	
	for i in range(len(adn)): #obtenemos los resultados
		result.append(automata(adn[i])) #recordar que se retorna un dict, asi que es una lista de dicts

	#a cada dict en la lista result le obtenemos su key (respectiva enfermedad)
	#con esta key ubicamos a cada enfermedad dentro de la variable contador
	#e incrementamos en uno su valor respectivo a key
	for element in result:
		#element = {'enfermedad':'bool'}
		key = list(element.keys())[0] #key siempre sera un solo elemento, por lo que accedemos a su valor con [0]	
		if(element[key]): #verificamos que el valor de la enfermedad es True
			contador[key] += 1 #incrementamos el valor del contador con la enfermedad respectiva

	#calculamos los porcentajes de tener cada enfermedad
	for enfermedad in contador:
		contador[enfermedad] = contador[enfermedad]*100/len(adn)

	#preparamos el string a ser impreso en el archivo de salida
	for deep in keys:
		#deep because deep purple
		string += 'Individuo con {}% de tener {} \n'.format(contador[deep], deep)

	try: #por si algo sale mal
		salida = open('salida.txt', 'w') #abrimos el archivo destino
		salida.write(string) #escribimos el string preparado
		salida.close() #cerramos el archivo
	except Exception:
		print('No se pudo abrir el archivo indicado, saliendo')
		exit()



	"""
	#programa con opciones para ver como funciona
	opc = 9999 #OVER 9000!!
	while(True):
		print('Ingrese 0 para salir.')
		opc = input('Usted posee {} elementos. Ingrese un numero dentro de ese rango: '.format(len(adn)))
		if(int(opc) == 0):
			break
		print('Ha elegido {}: {}'.format(opc, adn[int(opc)-1]))
		result = automata(adn[int(opc)-1])
		#print(result)
		print('Enfermedad reconocida \'{}\', resultado: {}\n'.format(list(result.keys())[0], list(result.values())[0]))
	"""