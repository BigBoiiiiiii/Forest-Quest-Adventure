import random
import time

player = {
    "health": 100,
    "inventory": [],
    "name": "Hero"
}

def print_pause(text, delay=1):
    print(text)
    time.sleep(delay)

def intro():
    print_pause("\n🌲 You wake up in a cold, dark forest...")
    print_pause("You have nothing but your fists and your will to survive.")
    print_pause("You hear noises nearby — something's watching.")
    forest_entrance()

def forest_entrance():
    print_pause("\nYou see two paths ahead:")
    print_pause("1. A dark trail leading deeper into the forest.")
    print_pause("2. A broken fence leading to an abandoned cabin.")

    choice = input("Choose: 'trail' or 'cabin': ").lower()
    if choice == "trail":
        forest_trail()
    elif choice == "cabin":
        cabin_scene()
    else:
        print_pause("You hesitate too long. A beast attacks from the shadows!")
        take_damage(30)
        forest_entrance()

def forest_trail():
    print_pause("\nThe trail is muddy. You trip on a root and scrape your knee.")
    take_damage(10)

    print_pause("You see something shiny in the dirt.")
    if "rusty knife" not in player["inventory"]:
        print_pause("You found a rusty knife!")
        player["inventory"].append("rusty knife")
    
    print_pause("Suddenly, a wild boar charges at you!")
    action = input("Do you 'fight' or 'run'?: ").lower()
    if action == "fight":
        if "rusty knife" in player["inventory"]:
            print_pause("You stab the boar and scare it off. That was close!")
        else:
            print_pause("You try to punch the boar. Bad idea.")
            take_damage(40)
    elif action == "run":
        print_pause("You escape, but not before it grazes you.")
        take_damage(20)
    else:
        print_pause("You freeze up and take the hit.")
        take_damage(30)
    
    print_pause("You find a path that leads to a tower.")
    tower_scene()

def cabin_scene():
    print_pause("\nThe cabin creaks as you enter...")
    print_pause("You find a medkit on the table.")
    player["health"] = min(100, player["health"] + 30)
    print_pause(f"Your health is now {player['health']}.")

    print_pause("There’s a trapdoor. You open it and climb down...")
    sewer_scene()

def tower_scene():
    print_pause("\nYou reach an ancient tower.")
    if "tower key" not in player["inventory"]:
        print_pause("The door is locked. You need a key.")
        print_pause("A nearby skeleton holds something shiny...")
        print_pause("You grab the key — and wake something up.")
        print_pause("A skeleton knight attacks!")
        fight_enemy("Skeleton Knight", 50)
        player["inventory"].append("tower key")
        print_pause("You unlock the tower door and enter.")
    
    print_pause("Inside is a glowing portal.")
    end_game("portal")

def sewer_scene():
    print_pause("\nYou walk through a damp tunnel. It's disgusting.")
    print_pause("You hear whispers. You’re not alone.")
    action = input("Do you 'sneak' or 'run'?: ").lower()
    if action == "sneak":
        chance = random.randint(1, 10)
        if chance <= 7:
            print_pause("You sneak past the danger. Nice!")
        else:
            print_pause("You trip and alert a monster!")
            fight_enemy("Sewer Fiend", 40)
    else:
        print_pause("You run blindly and fall into a pit.")
        take_damage(30)

    print_pause("You find a ladder leading up to a tower.")
    tower_scene()

def fight_enemy(name, damage):
    print_pause(f"\n⚔️ You fight the {name}!")
    if "rusty knife" in player["inventory"]:
        print_pause(f"You slash the {name} with your rusty knife!")
        print_pause(f"You win but take {damage//2} damage.")
        take_damage(damage // 2)
    else:
        print_pause(f"You fight barehanded... risky!")
        print_pause(f"You take {damage} damage.")
        take_damage(damage)

def take_damage(amount):
    player["health"] -= amount
    print_pause(f"💔 You took {amount} damage. Health: {player['health']}")
    if player["health"] <= 0:
        end_game("death")

def end_game(outcome):
    if outcome == "death":
        print_pause("\n💀 You collapse from your injuries. Game over.")
    elif outcome == "portal":
        print_pause("\n🌌 You step into the portal and escape the cursed forest!")
        print_pause("You're free. For now...")
        print_pause("🎉 YOU WIN!")
    else:
        print_pause("Unknown ending... you broke the timeline.")

    again = input("Play again? yes/no: ").lower()
    if again == "yes":
        reset_game()
    else:
        print_pause("Thanks for playing!")

def reset_game():
    player["health"] = 100
    player["inventory"] = []
    intro()

# Start the game
intro()
