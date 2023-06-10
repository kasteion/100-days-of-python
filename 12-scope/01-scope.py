################### Scope ####################

enemies = 1


def increase_enemies(enemies):
    enemies += 2
    print(f"enemies inside function: {enemies}")


increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

# Global Scope
player_health = 10
player = {"health": player_health}


# Local Scope
def drink_potion(npc):
    potion_strength = 2
    print(player_health)
    npc["health"] += potion_strength
    print(potion_strength)


an_array = [1, 2, 3, 5, 4]


def array_function(arr):
    arr.remove(5)
    return sum(arr)


print(array_function(an_array))
drink_potion(player)
print(player)
print(an_array)

enemies = 2

PI = 3.14159
URL = "https://example.com"


def increase_enemies():
    global enemies
    enemies = 1


print("Enemies: ", enemies)
increase_enemies()
print("Enemies: ", enemies)
