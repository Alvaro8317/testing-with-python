my_list_of_heros: list = ["Spiderman", "Ironman", "Batman", "Superman", "Omniman"]
my_list_of_heros_2 = []

for hero in my_list_of_heros:
    my_list_of_heros_2.append(hero)

my_list_of_heros_2.append("Rogue")
print("my_list_of_heros 1: ", my_list_of_heros)
print("my_list_of_heros 2: ", my_list_of_heros_2)

my_list_of_heros_3 = [f"new-{hero}" for hero in my_list_of_heros_2]
my_list_of_heros_3.append("Black widow")
print("my_list_of_heros 3: ", my_list_of_heros_3)

my_list_of_heros_4 = [hero for hero in my_list_of_heros_3 if "u" in hero]
print("my_list_of_heros 4: ", my_list_of_heros_4)

my_list_of_heros_5: list = []
for hero in my_list_of_heros_3:
    if "u" in hero:
        my_list_of_heros_5.append(hero)

print("my_list_of_heros 5: ", my_list_of_heros_5)
