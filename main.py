import os
import typer
from pendu import *

def show_title(name, color, nbr_equals):
    os.system('clear')
    page = typer.style(name, fg=color)
    print(f"|{'#' * nbr_equals * 2 + '#' * len(name)}|")
    typer.echo(f"|{'=' * nbr_equals}{page}{'=' * nbr_equals}|")
    print(f"|{'#' * nbr_equals * 2 + '#' * len(name)}|")

def home():
    show_title("MENU", "yellow", 20)
    print("1. Jouer.")
    print("2. Ajouter un mot.")
    print("3. Quitter.")
    choix = input("-> ")
    if choix == "1":
        difficulty_menu()
    elif choix == "2":
        add_word_menu()
    elif choix.lower() in ["3", "q", "quit"]:
        typer.secho("\nBye !", fg=typer.colors.BRIGHT_YELLOW)#, bg=typer.colors.YELLOW) 
        return
    else:
        home()

def add_word_menu():
    show_title("NOUVEAU MOT", "yellow", 17)
    print("Ecrivez le mot à rajouter ou la série de mots en les séparant par des espaces.")
    choix = input("-> ")
    if choix.lower() in ["q", "quit", "b", "back", "return"]:
        return home()
    try:
        choix = choix.lower()
        add_new_word(choix)
        success = typer.style("succès !", fg="bright_green")
        print(f"{' - '.join(choix.split(' '))}")
        typer.echo(f"Vos mots ont été ajouté avec {success}")
        input("(Appuyer sur Entrée pour quitter)")
        return home() 
    except:
        erreur = typer.style("Oups !", fg="red")
        typer.echo(f"{erreur} Une erreur est survenue lors de l'ajout de vos mots, veuillez réessayer...")
        input("(Appuyer sur Entrée pour recommencer)")
        return add_word_menu()

def find_occ(word: str, letter: str):
    indices = []
    for i in range(len(word)):
        if word[i] == letter:
            indices.append(i)
    return (indices)

def replace_occ(slot: str, indices: list, letter: str):
    for i in indices:
        slot = slot[:i] + letter + slot[i+1:]
    return (slot)

def play_game(word: str):
    word = word.lower()
    step = 0
    tentatives = 8
    letter = random.choice(word)
    slot = "_" * len(word)
    indices = find_occ(word, letter)
    slot = replace_occ(slot, indices, letter)
    tent_aff = typer.style(f"{tentatives}", fg="green")

    while (tentatives and slot != word):
        show_title("PENDU", "bright_magenta", 20)
        
        if tentatives > 5:
            color = "green"
        elif 5 >= tentatives >= 3:
            color = "yellow"
        else:
            color = "red"
        tent_aff = typer.style(f"{tentatives}", fg=color)
        typer.echo(f"Tentatives restantes : {tent_aff}")
        show_pendu(step, perso_color=color)
        print(slot)
        letter = input("-> ").lower()
        if len(letter) != 1:
            erreur = typer.style("Hmm !", fg="magenta")
            typer.echo(f"{erreur} Petit malin, tu peux mettre qu'une lettre...")
            input("(Appuyer sur Entrée pour continuer)")
        else:
            indices = find_occ(word, letter)
            if indices == []:
                tentatives -= 1
                step += 1
            else:
                slot = replace_occ(slot, indices, letter)

    if (slot == word):
        show_title("VICTOIRE", "bright_green", 20)
        show_pendu(step, perso_color="green")
        typer.secho(slot, fg="bright_green")
        t_aff = typer.style(f"Bravo !", fg="green")
        typer.echo(f"{t_aff} Vous avez sauvé le pendu ! Il vous restait {tent_aff} tentatives avant sa mort...")
        input("(Appuyer sur Entrée pour quitter)")
        return home()
    else:
        show_title("HE'S DEAD", "bright_red", 20)
        show_pendu(step, perso_color="red")
        empty_slot = [[i, typer.style(word[i], fg="red")] for i in range(len(slot)) if slot[i] == "_"]
        slot_aff = []
        j = 0
        for i in range(len(slot)):
            if j == len(empty_slot):
                slot_aff.append(slot[i])
            else:
                if empty_slot[j][0] == i:
                    slot_aff.append(empty_slot[j][1])
                    j += 1
                else:
                    slot_aff.append(slot[i])
        typer.echo("".join(slot_aff))

        t_aff = typer.style(f"C'est tragique !", fg="bright_red")
        typer.echo(f"{t_aff} Vous n'avez pas réussi à sauver le pendu...")
        input("(Appuyer sur Entrée pour quitter)")
        return home()

def difficulty_menu():
    show_title("JOUER", "yellow", 20)
    print("Donnez une longueur de mots [3-20] ou écrivez un mot à deviner.")
    choix = input("-> ")
    if choix.lower() in ["q", "quit", "b", "back", "return"]:
        return home()
    try:
        try:
            length = int(choix)
            if length < 3 or length > 20:
                erreur = typer.style("Erreur !", fg="red")
                typer.echo(f"{erreur} La longueur de mot que vous souhaitez est incorrecte.")
                input("(Appuyer sur Entrée pour recommencer)")
                return difficulty_menu()
        except:
            if len(choix) < 2:
                erreur = typer.style("Erreur !", fg="red")
                typer.echo(f"{erreur} Votre mot est trop court !")
                input("(Appuyer sur Entrée pour recommencer)")
                return difficulty_menu()
            word = choix
            return play_game(word)
        word = choice_random_word(length)
        if word == -1:
            erreur = typer.style("Erreur !", fg="red")
            typer.echo(f"{erreur} Aucun mot n'a été trouvé avec cette longueur, merci de réessayer.")
            input("(Appuyer sur Entrée pour recommencer)")
            return difficulty_menu()
        return play_game(word)
    except:
        erreur = typer.style("Erreur !", fg="red")
        typer.echo(f"{erreur} La valeur que vous avez entré n'est pas un nombre.")
        input("(Appuyer sur Entrée pour recommencer)")
        return difficulty_menu()
home()