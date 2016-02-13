# -*- coding: utf-8 -*-
#algoritmo de insertion sort

from tqdm import tqdm

def insertionSort(arreglo):
	if len(arreglo) <= 1:
		print "El arreglo ya está ordenado"
		return
	for x in tqdm(range(1,len(arreglo))):
		key = arreglo[x]
		indice = x 
		while indice > 0 and key < arreglo[indice - 1] :
			arreglo[indice] = arreglo[indice-1]
			indice = indice-1
		arreglo[indice] = key
	return arreglo	
		

salir = 0
valores = []
while salir != 1:
	try:
		numeros = int(raw_input("Escribe los números: "))
		valores.append(numeros)
   	except:
   		print "Iniciando Algoritmo"
   		salir = 1

print insertionSort(valores)   