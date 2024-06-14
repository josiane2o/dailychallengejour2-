# #exemple 1: lister les lettres qui constituent le mot balais
# #letter = "balais"
# #for letter in "balais":
# #    print(letter)

# # mot = "poisson"

# # for letter in mot:
# #     print(letter)



# #fruits = ["banane","orange","papaye","citron","pomme","ananas"]
# #for lister in fruits:
# #    print(lister)


# # sport = ["football","vitesse","saut","lancer du poids"]
# # for lister in sport:
# #         print(lister)


# # exemple: valeur d un nombre courent

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1


# #  Exercice

# # Imprimez les nombres de 1 à 10 en utilisant la boucle while






#numbers = range(4,19)

#for number in numbers:
#    print(number)
    
# Exercice

# Acceptez un nombre de l'utilisateur et imprimez sa table de multiplication

# user_number = int(input("entrer un nombre"))
# print(f"voici votre nombre : {user_number} ")
# for i in range (1, 11):
#     result = user_number*i
#     print(f"{user_number} * {i} = {result}")

#Instructions
# Défi 1
# Demandez à l'utilisateur un number et un length.
# Créez un programme qui imprime une liste de multiples 
# de numberjusqu'à ce que la longueur de la liste atteigne length.
# Exemples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]



# Demandez à l'utilisateur un number et un length.
# number = int(input("entrer mon numero"))
# length = int(input("entrer la taille de la liste"))

# Créez un programme qui imprime une liste de multiples 
# de numberjusqu'à ce que la longueur de la liste atteigne length

# nb = number
# my_liste =[]
# multiple = number
# while len(my_liste) < length:
#     my_liste.append(nb)
#     nb += number

# nb = number
# my_liste =[9]
# multiple = number
# while len(my_liste) < length:
#     my_liste.append(nb)
#     nb += number
# print(my_liste)



# #Défi 2
# Écrivez un programme qui demande une chaîne à l'utilisateur et affiche une nouvelle chaîne en supprimant toutes les lettres consécutives en double.
# Exemples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Les chaînes finales n'incluront pas de mots avec des lettres doubles (par exemple « passage », « loterie »).

mot = input("entrer votre mot\n")
result = ''
for i in mot :
    if i not in result:
        result += i 
print(result)         



