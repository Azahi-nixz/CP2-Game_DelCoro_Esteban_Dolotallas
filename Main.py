from Maruzensky import Maruzen

global Characters
global turns
Characters = ["Maruzen"]


def menu():

    while True:
        try:
            choice_one = int(input("""
Choose a character for Player 1
1. Maruzen
> """))

            if choice_one == 1:
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
> """))

            if choice_two == 1:
                break
            else:
                print("Invalid choice.")

        except ValueError:
            print("Enter a number.")

    return [choice_one, choice_two]


# =====================================
# BATTLE SYSTEM
# =====================================

def battle(player_1, player_2, choice):

    def reduce_cd(cd1, cd2, cd3):
        cd1 = max(cd1 - 1, 0)
        cd2 = max(cd2 - 1, 0)
        cd3 = max(cd3 - 1, 0)
        return cd1, cd2, cd3

    def get_move():
        while True:
            try:
                move = int(input("Choose action: "))
                if move in [1,2,3,4]:
                    return move
                else:
                    print("Choose between 1-4.")
            except ValueError:
                print("Enter a number.")

    turns = 1

    cd1 = player_1.skill1_cd()
    cd2 = player_1.skill2_cd()
    cd3 = player_1.skill3_cd()

    p2_cd1 = player_2.skill1_cd()
    p2_cd2 = player_2.skill2_cd()
    p2_cd3 = player_2.skill3_cd()

    # =====================================
    # MARUZEN PREDICTION EFFECT
    # =====================================

    def maruzen_exclusive(self, enemy, prediction):

        print("\nPrediction phase!")

        move = get_move()

        if move == prediction:
            enemy.Hp -= enemy.Atk
            self.Sanity -= 20
            print("Prediction successful!")
        else:
            self.Hp -= enemy.Atk
            self.Sanity -= 40
            print("Prediction failed!")

    # =====================================
    # MAIN BATTLE LOOP
    # =====================================

    while player_1.is_alive() and player_2.is_alive():

        print("\n" + "="*40)
        print(f"TURN {turns}")
        print("="*40)

        # =====================================
        # PLAYER 1
        # =====================================

        if turns % 2 != 0:

            print("\nPlayer 1 Turn")
            print(player_1.stats())

            print(f"""
1. Basic Attack
2. Skill 1 - {player_1.is_cooldown(cd1)}
3. Skill 2 - {player_1.is_cooldown(cd2)}
4. Skill 3 - {player_1.is_cooldown(cd3)}
""")

            move = get_move()

            match move:

                case 1:
                    bonus = player_1.basic_attack()
                    cd1, cd2, cd3 = reduce_cd(cd1, cd2, cd3)

                    if bonus:
                        continue

                case 2:
                    if cd1 != 0:
                        print("Skill 1 is on cooldown!")
                        continue

                    player_1.skill_1(player_2)
                    cd1 = player_1.skill1_cd()
                    cd1, cd2, cd3 = reduce_cd(cd1, cd2, cd3)

                case 3:
                    if cd2 != 0:
                        print("Skill 2 is on cooldown!")
                        continue

                    player_1.skill_2(player_2)
                    cd2 = player_1.skill2_cd()
                    cd1, cd2, cd3 = reduce_cd(cd1, cd2, cd3)

                case 4:
                    if cd3 != 0:
                        print("Skill 3 is on cooldown!")
                        continue

                    prediction = player_1.skill_3()

                    if choice[0] == 1:
                        maruzen_exclusive(player_1, player_2, prediction)
                        turns += 1

                    cd3 = player_1.skill3_cd()
                    cd1, cd2, cd3 = reduce_cd(cd1, cd2, cd3)

        # =====================================
        # PLAYER 2
        # =====================================

        else:

            print("\nPlayer 2 Turn")
            print(player_2.stats())

            print(f"""
1. Basic Attack
2. Skill 1 - {player_2.is_cooldown(p2_cd1)}
3. Skill 2 - {player_2.is_cooldown(p2_cd2)}
4. Skill 3 - {player_2.is_cooldown(p2_cd3)}
""")

            move = get_move()

            match move:

                case 1:
                    player_2.basic_attack()
                    p2_cd1, p2_cd2, p2_cd3 = reduce_cd(p2_cd1, p2_cd2, p2_cd3)

                case 2:
                    if p2_cd1 != 0:
                        print("Skill 1 is on cooldown!")
                        continue

                    player_2.skill_1(player_1)
                    p2_cd1 = player_2.skill1_cd()
                    p2_cd1, p2_cd2, p2_cd3 = reduce_cd(p2_cd1, p2_cd2, p2_cd3)

                case 3:
                    if p2_cd2 != 0:
                        print("Skill 2 is on cooldown!")
                        continue

                    player_2.skill_2(player_1)
                    p2_cd2 = player_2.skill2_cd()
                    p2_cd1, p2_cd2, p2_cd3 = reduce_cd(p2_cd1, p2_cd2, p2_cd3)

                case 4:
                    if p2_cd3 != 0:
                        print("Skill 3 is on cooldown!")
                        continue

                    prediction = player_2.skill_3()

                    if choice[1] == 1:
                        maruzen_exclusive(player_2, player_1, prediction)
                        turns += 1

                    p2_cd3 = player_2.skill3_cd()
                    p2_cd1, p2_cd2, p2_cd3 = reduce_cd(p2_cd1, p2_cd2, p2_cd3)

        print("\n--- Status ---")
        print(player_1.stats())
        print(player_2.stats())

        turns += 1

    print("\n" + "="*40)

    if player_1.is_alive():
        print("PLAYER 1 WINS!")
    else:
        print("PLAYER 2 WINS!")

    print("="*40)


# =====================================
# MAIN
# =====================================

def main():

    choice = menu()

    if choice[0] == 1:
        player_1 = Maruzen()

    if choice[1] == 1:
        player_2 = Maruzen()

    print(f"\nPlayer 1 chose {player_1.Name}")
    print(f"Player 2 chose {player_2.Name}")

    battle(player_1, player_2, choice)


if __name__ == "__main__":
    main()