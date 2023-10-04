nombres = [2, 5, 1, 1e1, -3, 4.4]


print("Llista: ")
print(nombres[:])

print("Quants números? "+str(len(nombres)))
print("Quants 3? "+str(nombres.count(3)))
print("Quants 3 i 4? \n3: "+str(nombres.count(3))+"\n4: "+str(nombres.count(4)))

nombres.sort()
print("Nombre mes gran? "+str(nombres[-1]))

print("3 més petits? "+str(nombres[:3]))

rang = range(nombres[0], (int(nombres[-1]+1)))
diferencia = str(nombres[-1] - nombres[0])
print ("Rang: "+str(nombres[0])+":"+str(nombres[-1])+" = "+diferencia)
for i in rang:
    print (i, end=' ')
