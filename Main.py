from characters.Devourer import Devourer
from characters.Maruzensky import Maruzen
from characters.Zen import Zen
from characters.Giga import Giga
from characters.JAD import JAD
from characters.Minos import Minos
from characters.Pol import Pol
from characters.Sed import Sed
from gui.Guides import guide

def interface():
    while True:
        try:
            choice = int(input("""
1. 1 Player
2. 2 Player
3. Guides
4. Exit
Choose an option: 
"""))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice. Enter 1-4.")
        except ValueError:
            print("Enter a number.")


def menu():
    while True:
        try:
            choice_one = int(input("""
Choose a character for Player 1
1. Maruzen
2. Zen
3. Devourer
4. J.A.D.
5. Giga
6. Minos
7. Pol
> """))
            if choice_one in [1, 2, 3, 4, 5, 6, 7]:
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a number.")

    while True:
        try:
            choice_two = int(input("""
Choose a character for Player 2
1. Maruzen
2. Zen
3. Devourer
4. J.A.D.
5. Giga
6. Minos
7. Pol
"""))
            if choice_two in [1, 2, 3, 4, 5, 6, 7]:
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a number.")

    return [choice_one, choice_two]

#============================================
# HANDLES MOVE & COOLDOWN LOGIC
#============================================

def get_move(player):
    while True:
        try:
            print("\nChoose action:")

            for i in range(1, 5):
                cd = player.cooldowns.get(i, 0)

                if cd > 0:
                    print(f"{i}. Skill {i-1 if i>1 else 'Basic Atk'} (CD: {cd}) ❌")
                else:
                    print(f"{i}. Skill {i-1 if i>1 else 'Basic Atk'} (Ready) ✅")

            move = int(input("> "))

            if move not in [1,2,3,4]:
                print("Invalid choice.")
                continue

            if player.cooldowns.get(move, 0) > 0:
                print("That skill is on cooldown! Choose another.")
                continue

            return move

        except ValueError:
            print("Enter a number.")

#=========================================
# BATTLE HANDLER
#==========================================
def battle(p1, p2):

    turn = 1

    while p1.is_alive() and p2.is_alive():

        print("\n" + "="*40)
        print(f"TURN {turn}")
        print("="*40)

        current = p1 if turn % 2 == 1 else p2
        enemy = p2 if turn % 2 == 1 else p1

        current.turn_counter += 1

        current.check_transformation()

        print(current.stats())
        print(current.status())

        move = get_move(current)

        move = current.debuff_checker(move, enemy)
        result = current.use_skill(move, enemy)

        if result is True:
            continue

        current.reduce_cooldowns()

        current.end_turn_checks()
        current.reduce_effects()

        # Apply end-of-turn DoT effects (Bleeding, etc.) on the enemy
        enemy.end_of_round_effects(current)

        current.first_turn = False

        turn += 1

    print("\n" + "="*40)


    if p1.is_alive():
        print("PLAYER 1 WINS!")
    else:
        print("PLAYER 2 WINS!")

#===========================================
# MAIN
#===========================================

CHARACTER_MAP = {
    1: Maruzen,
    2: Zen,
    3: Devourer,
    4: JAD,
    5: Giga,
    6: Minos,
    7: Pol,
    8: Sed,
}

def main():
    while True:
        c = interface()

        if c == 1:
            print("1 Player mode is not yet implemented.")

        elif c == 2:
            choice = menu()

            p1 = CHARACTER_MAP[choice[0]]()
            p2 = CHARACTER_MAP[choice[1]]()

            print(f"\nPlayer 1 chose {p1.Name}")
            print(f"Player 2 chose {p2.Name}")

            battle(p1, p2)
            break

        elif c == 3:
            guide()

        elif c == 4:
            print("Exiting...")
            break



if __name__ == "__main__":
    main()
