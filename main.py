"""
C'est mon petit code à moi, on touche pas à mon ptit code, c'est mon petit code
"""
#### Imports et définition des variables globales
#import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire
xf
    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf8') as file:
        return [list(map(int, line.strip().split(';'))) for line in file.readlines()]


def get_list_k(data, k):
    """
    Retourne la k-ème liste
    """
    if 0<=k<len(data):
        return data[k]
    return None


def get_first(l):
    """
    Retourne le premier élément de la liste
    """
    return l[0]


def get_last(l):
    """
    Retourne le dernier élément de la liste
    """
    return l[-1]


def get_max(l):
    """
    Retourne la valeur max de la liste
    """
    return max(l)


def get_min(l):
    """
    Retourne la valeur min de la liste
    """
    return min(l)


def get_sum(l):
    """
    Retourne la somme de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
    Permet l'utilisation des fonctions secondaires
    """
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
