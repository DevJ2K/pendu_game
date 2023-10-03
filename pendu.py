import typer
import time
import os
import random

# def show_pendu(step: int):
    # dimensions = 10
    # box_color = "bright_blue"
    # box_vert = typer.style("|", fg=box_color)

    # struct_color = "yellow"
    # typer.secho("_" * dimensions, fg=box_color)
    # if step == 0:
    #     for i in range(8):
    #         typer.echo(f"{box_vert}{' ' * (dimensions - 2)}{box_vert}")

    # elif step == 1:
    #     for i in range(7):
    #         typer.echo(f"{box_vert}{' ' * (dimensions - 2)}{box_vert}")

    #     struct = typer.style(" _ _", fg=struct_color)
        
    #     typer.echo(f"{box_vert}{struct}{' ' * (dimensions - 6)}{box_vert}")

    # typer.secho(f"|{'_' * (dimensions - 2)}|", fg=box_color)

def space(nb: int):
    return ' ' * nb

def show_elt(show: str, step: int, i: int):
    return show if step > i else ' '

def show_pendu(step: int, struct_color: str = "yellow", box_color: str = "bright_blue", perso_color: str = "bright_green"):
    dimensions = 13

    box_vert = typer.style("|", fg=box_color)

    struct_hor = typer.style("_", fg=struct_color)
    struct_vert = typer.style("|", fg=struct_color)
    struct_diag = typer.style("/", fg=struct_color)
    p = [
        typer.style("(", fg=perso_color),
        typer.style(")", fg=perso_color),
        typer.style("_", fg=perso_color),
        typer.style("|", fg=perso_color),
        typer.style("\\", fg=perso_color),
        typer.style("/", fg=perso_color)
    ]
    typer.secho("_" * dimensions, fg=box_color)
    typer.echo(f"{box_vert}{space(2) if step > 2 else space(dimensions - 6)}{show_elt(struct_hor * (dimensions - 7), step, 2)}{space(3)}{box_vert}")
    typer.echo(f"{box_vert}{space(2)}{show_elt(struct_vert, step, 1)}{show_elt(struct_diag, step, 3)}{space(3)}{show_elt(struct_vert, step, 3)}{space(3)}{box_vert}")
    typer.echo(f"{box_vert}{space(2)}{show_elt(struct_vert, step, 1)}{space(3)}{show_elt(p[0], step, 4)}{show_elt(p[2], step, 4)}{show_elt(p[1], step, 4)}{space(2)}{box_vert}")
    typer.echo(f"{box_vert}{space(2)}{show_elt(struct_vert, step, 1)}{space(3)}{show_elt(p[4], step, 6)}{show_elt(p[3], step, 5)}{show_elt(p[5], step, 6)}{space(2)}{box_vert}")
    typer.echo(f"{box_vert}{space(2)}{show_elt(struct_vert, step, 1)}{space(4)}{show_elt(p[3], step, 5)}{space(3)}{box_vert}")
    typer.echo(f"{box_vert}{space(2)}{show_elt(struct_vert, step, 1)}{space(3)}{show_elt(p[5], step, 7)} {show_elt(p[4], step, 7)}{space(2)}{box_vert}")
    typer.echo(f"{box_vert}{space(2)}{show_elt(struct_vert, step, 1)}{space(dimensions - 5)}{box_vert}")
    typer.echo(f"{box_vert}{space(1)}{show_elt(struct_hor, step, 0)}{show_elt(struct_vert, step, 1)}{show_elt(struct_hor, step, 0)}{space(dimensions - 6)}{box_vert}")


    typer.secho(f"|{'_' * (dimensions - 2)}|", fg=box_color)

def vanilla_pendu():
    print("_____________")
    print("|  ______   |")
    print("|  |/   |   |")
    print("|  |   (_)  |")
    print("|  |   \\|/  |")
    print("|  |    |   |")
    print("|  |   / \\  |")
    print("|  |        |")
    print("| _|_       |")
    print("|___________|")

def choice_random_word(length: int):
    with open("mots", encoding="utf-8", mode="r") as f:
        mots = f.read().splitlines()
        good_length = [mot for mot in mots if len(mot) == length]
    try:
        word = (random.choice(good_length))
        return (word)
    except:
        return (-1)

def add_new_word(words: str):
    series = words.split()
    with open("mots", encoding="utf-8", mode="r") as f:
        all_words = f.read().splitlines()

    for word in series:
        if word not in all_words:
            all_words.append(word)

    all_words.sort()
    with open(file="mots", encoding="utf-8", mode="w") as f:
        for i in range(len(all_words)):
            f.write(all_words[i])
            if i + 1 < len(all_words):
                f.write("\n")

if __name__ == "__main__":
    os.system("clear")
    # show_pendu(2)
    for i in range(9):
        os.system("clear")
        print(f"étape : {i}".capitalize())
        show_pendu(i)
        time.sleep(1)