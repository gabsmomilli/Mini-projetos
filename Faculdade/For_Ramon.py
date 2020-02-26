import emoji
nome = str(input("oi, qual seu nome? "))
while True:
    if nome == "ramon" or nome == "Ramon":
        print(emoji.emojize(f"{nome}, te amo :heart:", use_aliases=True))
    else:
        print("suave " + nome)
        break