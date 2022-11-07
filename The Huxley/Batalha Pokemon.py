def atacar(pokemon1,pokemon2):
	attacksPokemon1 = 0
	attacksPokemon2 = 0
	p1 = pokemon1.copy()
	p2 = pokemon2.copy()
	while p1["life"] > 0:
		p1["life"] -= p2["attack"]
		attacksPokemon2 += 1
	while p2["life"] > 0:
		p2["life"] -= p1["attack"]
		attacksPokemon1 += 1

	return attacksPokemon1 <= attacksPokemon2



nBattles = int(input())
for i in range(nBattles):
	v1,v2,d1,d2 = [int(i) for i in input().split()]
	clodesPokemon = {"life":v1,"attack":d1}
	bezalielPokemon = {"life":v2,"attack":d2}

	while True:
		if atacar(clodesPokemon,bezalielPokemon): 
			bezalielPokemon["life"] -= clodesPokemon["attack"]
			#print("Clodes => Attack")
		else:
			clodesPokemon["attack"] += 50
			#print("Clodes => Buff")
		if bezalielPokemon["life"] <= 0: 
			print("Clodes")
			break
		
		clodesPokemon["life"] -= bezalielPokemon["attack"]
		#print("Bezaliel => Attack")
		if clodesPokemon["life"] <= 0: 
			print("Bezaliel")
			break