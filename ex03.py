from random import sample

nombres = []
#nombres = [2, 5, 1, 1e1, -3, 4.4]

#for n in range(5):
nombres = sample(range(-3, 11), 5)

print("Llista: ")
print(nombres[:])

print("Quants números? "+str(len(nombres)))
print("Quants 3? "+str(nombres.count(3)))
print("Quants 3 i 4? \n3: "+str(nombres.count(3))+" vegades\n4: "+str(nombres.count(4))+" vegades")

nombres.sort()
print("Nombre mes gran? "+str(nombres[-1]))

print("3 més petits? "+str(nombres[:3]))

diferencia = str(nombres[-1] - nombres[0])
print ("Rang: "+ diferencia)
