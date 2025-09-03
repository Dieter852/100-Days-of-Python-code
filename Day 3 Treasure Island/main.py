print(r"""
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `====================================`
""")

print("Welcome to Treasure Island\n\n")
print("""You stand at the edge of a cursed island. The legends say a chest of gold lies hidden deep within its haunted ruins.
Few who have entered ever returned.""")

first_choice = input("Do you decide to enter the jungle or walk along the beach? type jungle or beach?\n").lower()

if first_choice == "jungle":
    print("You enter the jungle, you hear whispers between the trees.")
    second_choice = input("Do you decide to follow the whispers or carry on through the jungle? type whispers or continue?\n").lower()

    if second_choice == "continue":
        print("You ignore the whispers and push deeper into the jungle, you find a ruined stone temple.")
        third_choice = input("you open the temple door and the roof crumbles a bit. do you decide to go in and explore or look for another entrance? type explore or entrance?\n").lower()

        if third_choice == "explore":
            last_choice = input("You explore around the temple and discover a secret stairway underground, filled with spiderwebs. do you enter or keep looking around? type enter or around?\n").lower()

            if last_choice == "enter":
                print("You venture deep underground and see the treasure next to a boat and a underground river which leads outside to the ocean. . . . . WELL DONE")

            elif last_choice == "around":
                print("You decide to still have a look around and venture into a great hall, the floor collapses and you fall to your death.")

        elif third_choice == "entrance":
            print("You find a cave and a swarm of bats blinds you and you fall into a pit and die")

    elif second_choice == "whispers":
        print("You follow the whispers, a shadowy figure lures you into quicksand and you die.")

elif first_choice == "beach":
    print("You walk along the beach, you see strange footprints in the sand. they lead to a skeleton clutching a rusted sword. Suddenly, the skeleton rises and you are slain.")