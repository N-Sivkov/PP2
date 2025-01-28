#dictionaries
a = {"species": "dog", "breed": "bullterier", "years": 10}
#alternative way: a = dict(species = "dog", breed = "bullterier", years = 10)
#ordered after 3.7; unordered pre-3.7; no duplicates allowed

b = a["breed"] # == b = a.get("breed")
print(b)

x = a.keys() #all the keys as a list
x = a.values() #all the values as a list
x = a.items() #a list of key:value pairs
#both connected with the dictionary and update with it

a["species"] = "cat"
#alternatively, if multiple changes are required:
a.update({"breed": "siam", "years": 7, "weight": 5, "paws": 4})
#if a nonexistent key:value is provided, it will be added

a.pop("weight") #== del a["model"] (will delete the whole dictionary if left without arguments)
a.popitem() #deletes the last inserted item
b = a.copy()
a.clear()