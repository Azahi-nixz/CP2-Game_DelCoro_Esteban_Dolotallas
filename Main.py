from Devourer import Devourer
from Maruzensky import Maruzen
from Zen import Zen
from Giga import Giga
from JAD import JAD

def interface():
    choice = int(input("""
1. 1 Player
2. 2 Player
3. Guides
4. Exit
Choose an option: 
"""))
    return choice


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
6. JK
7. Icanfixher
8. SeanJii
9. Taracoffee
10. CollectorBaddie
11. Igop                                  
> """))

            if choice_one in [1,2,3,4,5,6,7,8,9, 10, 11]:
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
6. JK
7. Icanfixher
8. SeanJii
9. Taracoffee
10. CollectorBaddie
11. Igop                                                
> """))

            if choice_two in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
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

def main():

    choice = menu()

    if choice[0] == 1:
        p1 = Maruzen()
    if choice[0] == 2:
        p1 = Zen()
    if choice[0] == 3:
        p1 = Devourer()
    if choice[1] == 4:
        p1 = JAD()
    if choice[1] == 5:
        p1 = Giga()

    if choice[1] == 1:
        p2 = Maruzen()
    if choice[1] == 2:
        p2 = Zen()
    if choice[1] == 3:
        p2 = Devourer()
    if choice[1] == 4:
        p2 = JAD()
    if choice[1] == 5:
        p2 = Giga()
    print(f"\nPlayer 1 chose {p1.Name}")
    print(f"Player 2 chose {p2.Name}")

    battle(p1, p2,)


if __name__ == "__main__":
    main()