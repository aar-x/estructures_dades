compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }

compra.update({"Plàtans": {"Qty": 1, "€": 0.27}})

print("Fruites:", end=' ')
for x in compra:
	print(x, end =' ')

cost = compra["Peres"]["€"]*compra["Peres"]["Qty"]
print("\nCost total peres: "+str(cost)+'€')

quantitat = 0
for x in compra:
	quantitat = quantitat + compra[x]["Qty"]
print("Quantitat total: "+str(quantitat)+' fruites')

print('Fruita més cara: ', end = ' ')
maxim = 0
fruita = ''

for x, y in compra.items():
    if y['€'] > maxim:
        maxim = y['€']
        fruita = x
print (fruita, str(maxim)+'€')
