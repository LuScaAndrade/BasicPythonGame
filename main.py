import os

player = {"nome": "Python", "x": 0, "y": 0}

def walk(direction):
    if direction == "d":
        player['y'] += 1
    elif direction == "a":
        player['y'] -= 1
    elif direction == "w":
        player['x'] -= 1
    elif direction == "s":
        player['x'] += 1
        
while True:
    os.system('cls')
    
    print("--------------------------------")
    for x in range(5):
        print("\n")
        for y in range(10):
            if player['x'] == x and player['y'] == y:
                print("🏇", end="")
            else:
                print("🟩",end="")
    print("--------------------------------")
    
    direction = input("Próxima direção (w,s,d,a): ")
    walk(direction)