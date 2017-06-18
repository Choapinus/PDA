from Stack import Stack

def get_adn():
	file = input('Ingrese archivo de texto: ') #archivo.txt
	try:
		opened_file = open(file, 'r') #abrir en modo lectura
		adn = opened_file.read() #leer su contenido
		opened_file.close() #cerrar archivo
		adn = adn.split(' ') #separar por los espacios que contenga
		#print(adn) #debug
		return adn #list of adn
	except FileNotFoundError: #si no encuentra el archivo
		print('No se ubica el archivo \"' + file +'\". Saliendo.')
		exit() #pos salir
	except Exception: #en caso de cualquier cosa hahaha
		print('Unexpected Error')
		exit()


def automata(adn):
	#lenguajes aceptados
	#L(M) = {A^n  C^2n T^n G^3n / n >= 1} Alzheimer
	#L(M) = {T^2n C^n  A^n G^2n / n >= 1} Parkinson
	#L(M) = {T^2n C^n  G^n A^3n / n >= 1} Epilepsia	

	pila = Stack() #stack infinito
	n = 0
	j = 0
	park = False #flag para parkinson
	
	#L(M) = {A^n  C^2n T^n G^3n / n >= 1} Alzheimer
	if(adn[0] == 'A'): #si la primera letra es A, es alzheimer
		for i in range(len(adn)):
			if(adn[i] == 'A'):
				n += 1 #sera nuestro n para insertar en la pila segun el lenguaje
				pila.push(adn[i]) #pusheamos los primeros elementos
			elif(adn[i] == 'C'): #si llega a la C, termina el ciclo, ya tenemos nuestra n en base a T
				break

		#reglas
		for i in range(n*2): #C^2n
			pila.push('C')
		for i in range(n):	#T^n
			pila.push('T')
		for i in range(n*3): #G^3n
			pila.push('G')
			
		#comenzamos a consumir la pila y a comparar el adn
		#primero, volteamos el adn debido a que al insertar en la pila, se voltean los datos
		adn = ''.join(reversed(adn))
		while(not pila.isEmpty()): #mientras no este vacia la pila
			aux = pila.pop()
			if(aux == adn[j]): #si la comparacion es exitosa con el elemento de la pila, se avanza el adn
				j += 1 			 #y aux se da por consumido
			else:					 #si al menos un elemento no coincide, no se acepta
				return {'alzheimer': False} #retornamos un dict con la enfermedad identificada y false
		if(pila.isEmpty()):	 #si la pila se consumio con exito, retornamos la enfermedad y true
			return {'alzheimer': True}


	else: #casos para parkinson o epilepsia
		for i in range(len(adn)):
			if(adn[i] == 'T'):
				n += 1 #mismo proceso que lo anterior, identificamos T
				pila.push(adn[i]) #y pusheamos su valor, incrementando y obteniendo nuestra n
			elif(adn[i] == 'C'): #si llega a C, break
				break
		#print('n: {}'.format(n)) #debug

		#L(M) = {T^2n C^n  A^n G^2n / n >= 1} Parkinson
		if(adn[n+int(n/2)] == 'A'): #ubicamos la A de algun modo. Si se encuentra, es parkinson
			#n+int(n/2) = T^2n + C^n = indice de A
			park = True #si se encuentra la A, es parkinson (flag = true)
			for i in range(int(n/2)): #recordar que nuestra n viene como T^2n
				pila.push('C')			  #por lo tanto, se debe adecuar la n a las reglas impuestas
			for i in range(int(n/2)): #se me olvido como hacer la division entera, asi que parseamos a int
				pila.push('A')
			for i in range(n):
				pila.push('G')
			#end


		#L(M) = {T^2n C^n G^n A^3n / n >= 1} Epilepsia	
		else:
			#recordar que el n viene como 2n
			park = False #de por si el flag ya es falso, pero prefiero no perderme
			for i in range(int(n/2)): #mismo proceso que las condiciones anteriores
				pila.push('C')
			for i in range(int(n/2)):
				pila.push('G')
			for i in range(int(n/2)*3):
				pila.push('A')
		
		#comenzamos a consumir la pila y a comparar el adn
		#recordar que volteamos el adn debido a que al insertar en la pila todo se voltea
		adn = ''.join(reversed(adn))
		
		if(park): #si se identifico parkinson (si park = True, then...)
			while(not pila.isEmpty()): #mientras la pila no este vacia
				aux = pila.pop() #consumimos sus elementos
				if(aux == adn[j]): #si la comparacion es exitosa
					j += 1			 #avanzamos por el adn
				else:
					return {'parkinson': False} #sino, retornamos la enfermedad identificada y false como dict
			if(pila.isEmpty()): #si se consumio toda la pila con exito
				return {'parkinson': True} #retornamos la enfermedad y true
		
		else: #si se identifico epilepsia
			while(not pila.isEmpty()): #mientras la pila no este vacia
				aux = pila.pop() #consumimos sus elementos
				if(aux == adn[j]): #si la comparacion es exitosa
					j += 1 			 #avanzamos por el adn
				else: #sino
					return {'epilepsia': False} #retornamos la enfermedad y false como dict
			if(pila.isEmpty()): #si la pila se consumio con exito
				return {'epilepsia': True} #la enfermedad fue bien identificada y retornamos true