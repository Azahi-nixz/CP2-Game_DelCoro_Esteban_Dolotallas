
from Maruzensky import Maruzen
from Zen import Zen
def menu():

    while True:
        try:
            choice_one = int(input("""
Choose a character for Player 1
1. Maruzen
2. Giga
3. Jexikun
4. Leah
5. Trish
6. JK
7. Icanfixher
8. SeanJii
9. Taracoffee
10. CollectorBaddie
11. Igop                                  
> """))

            if choice_one == 1:
                break

            elif choice_one == 2:
                break

            elif choice_one == 3:
                break

            elif choice_one == 4:
                break

            elif choice_one == 5:
                break

            elif choice_one == 6:
                break

            elif choice_one == 7:
                break

            elif choice_one == 8:
                break

            elif choice_one == 9:
                break

            elif choice_one == 10:
                break

            elif choice_one == 11:
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
2. Giga
3. Jexikun
4. Leah
5. Trish
6. JK
7. Icanfixher
8. SeanJii
9. Taracoffee
10. CollectorBaddie
11. Igop                                                
> """))

            if choice_two == 1:
                break

            elif choice_two == 2:
                break

            elif choice_two == 3:
                break

            elif choice_two == 4:
                break

            elif choice_two == 5:
                break

            elif choice_two == 6:
                break

            elif choice_two == 7:
                break

            elif choice_two == 8:
                break

            elif choice_two == 9:
                break

            elif choice_two == 10:
                break

            elif choice_two == 11:
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Enter a number.")

    return [choice_one, choice_two]

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


def main():

    choice = menu()

    if choice[0] == 1:
        p1 = Maruzen()
    if choice[0] == 2:
        p1 = Zen()

    if choice[1] == 1:
        p2 = Maruzen()
    if choice[1] == 2:
        p2 = Zen()

    print(f"\nPlayer 1 chose {p1.Name}")
    print(f"Player 2 chose {p2.Name}")

    battle(p1, p2,)


if __name__ == "__main__":
    main()