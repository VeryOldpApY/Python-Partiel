# Titre: Python Partiel
# Auteur: Gomis Yoann
# Date: 07/03/2023

from menu import menu

if __name__ == '__main__':
    while True:
        print("Quel exercice souhaitez-vous lancer ? (1-3)")
        exercice = input()
        if exercice.isnumeric():
            menu(int(exercice))
            