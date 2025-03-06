
            time.sleep(0.2)




    else:
        print()
        print("     sorry ! your guess was absolutely INCORRECT")
        print(f" you picked {press2} while computer (AI) picked  {ai_man} ")

    ok = str(input("""
    press ENTER to see what two computers(AI) picked   """))
    print()
    if ai_man == real_human:
        print(" woOW ! The two AI guessed correctly ")
        print(f"First AI picked  {ai_man} ")
        print(f"Second AI picked  {real_human}")
        print("Artificial intelligent are supper 🗼🗼🗼")
        print()
        print()

    else:
        print(" The Two AI guessed and picked different option 😂🤣🤣🤣")
        print(f"   First AI picked  {ai_man} ")
        print(f"   Second AI picked  {real_human}")
    print()
    print(" .........GAME ENDS...........")
    print()

    play_again = str(input(" do you want to play again (Yes / No) > ")).capitalize()
    if play_again != "Yes":
        break
print()
print("                 Wait !")
for ty in ("......................................."):
    print(ty,end="")
    time.sleep(0.1)
print()
for gb in (" The Game is being exited now bye bye"):
    print(gb , end="")
    time.sleep(0.3)
print()
okay = str(input("""
           Press 'ENTER' To Close tha page
               """))

