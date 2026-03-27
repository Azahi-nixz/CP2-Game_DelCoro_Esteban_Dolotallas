from Maruzensky import Maruzen


# ===============================
# MENU
# ===============================
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
6. Julian
7. Icanfixher
8. Lolicon
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
6. Julian
7. Icanfixher
8. Lolicon
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


# =====================================
# BATTLE SYSTEM
# =====================================

def battle(player_1, player_2, choice):

    def reduce_cd(cd1, cd2, cd3):
        cd1 = max(cd1 - 1, 0)
        cd2 = max(cd2 - 1, 0)
        cd3 = max(cd3 - 1, 0)
        return cd1, cd2, cd3


    def get_move(player):

        # SABOTAGE DEBUFF CHECK
        if player.has_debuff("Sabotage"):
            print("You are sabotaged! Only Basic Attack allowed!")
            input("Press Enter to attack...")
            return 1

        while True:

            try:
                move = int(input("Choose action: "))

                if move in [1,2,3,4]:
                    return move

                else:
                    print("Choose between 1-4.")

            except ValueError:
                print("Enter a number.")


    # ==============================
    # COOLDOWN
    # ==============================

    turns = 1

    cd1 = player_1.skill1_cd()
    cd2 = player_1.skill2_cd()
    cd3 = player_1.skill3_cd()

    p2_cd1 = player_2.skill1_cd()
    p2_cd2 = player_2.skill2_cd()
    p2_cd3 = player_2.skill3_cd()


    # ==============================
    # MARUZEN PREDICTION SYSTEM
    # ==============================

    def maruzen_prediction(self, enemy, prediction):

        print("\nPrediction phase!")

        move = get_move(enemy)

        if move == prediction:
            enemy.Hp -= enemy.Atk
            self.Sanity -= 20
            print("Prediction successful!")
        else:
            self.Hp -= enemy.Atk
            self.Sanity -= 40
            print("Prediction failed!")


    # ==============================
    # MAIN LOOP
    # ==============================

    while player_1.is_alive() and player_2.is_alive():

        print("\n" + "="*40)
        print(f"TURN {turns}")
        print("="*40)

        # ==============================
        # PLAYER 1
        # ==============================

        if turns % 2 != 0:

            print("\nPlayer 1 Turn")

            print(player_1.stats())
            print(player_1.status())

            print(f"""
1. Basic Attack
2. Skill 1 - {player_1.is_cooldown(cd1)}
3. Skill 2 - {player_1.is_cooldown(cd2)}
4. Skill 3 - {player_1.is_cooldown(cd3)}
""")

            move = get_move(player_1)

            match move:

                case 1:

                    bonus = player_1.basic_attack(player_2)

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
                        maruzen_prediction(player_1, player_2, prediction)

                    cd3 = player_1.skill3_cd()

                    cd1, cd2, cd3 = reduce_cd(cd1, cd2, cd3)



        # ==============================
        # PLAYER 2
        # ==============================

        else:

            print("\nPlayer 2 Turn")

            print(player_2.stats())
            print(player_2.status())

            print(f"""
1. Basic Attack
2. Skill 1 - {player_2.is_cooldown(p2_cd1)}
3. Skill 2 - {player_2.is_cooldown(p2_cd2)}
4. Skill 3 - {player_2.is_cooldown(p2_cd3)}
""")

            move = get_move(player_2)

            match move:

                case 1:

                    player_2.basic_attack(player_1)

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
                        maruzen_prediction(player_2, player_1, prediction)

                    p2_cd3 = player_2.skill3_cd()

                    p2_cd1, p2_cd2, p2_cd3 = reduce_cd(p2_cd1, p2_cd2, p2_cd3)


        # ==============================
        # END OF TURN
        # ==============================

        print("\n--- Status ---")

        print(player_1.stats())
        print(player_2.stats())

        # reduce buff/debuff duration
        player_1.reduce_effects()
        player_2.reduce_effects()

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
