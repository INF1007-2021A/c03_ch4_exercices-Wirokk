#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main() -> None:
    string = "Bonjour"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "helllo world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans {string} est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")



def is_even_len(string: str) -> bool:
    longueurstring = len(string)
    if longueurstring %2 !=1:
        return True
    else:
        return False

    

def remove_third_char(string: str) -> str:
    neword = (string[0:2]+string[3:])
    return neword


def replace_char(string: str, old_char: str, new_char: str) -> str:
    return string.replace('w','z')


def get_nb_char(string: str, char: str) -> int:
    counter = 0
    for lettre in string:
        if lettre == char:
            counter += 1
    return counter


def get_nb_words(sentence: str) -> int:
    sentence.strip()
    counter = 1
    for char in sentence:
        if char == ' ':
            counter += 1 
    return counter


if __name__ == '__main__':
    main()
