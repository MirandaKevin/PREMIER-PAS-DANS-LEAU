# ALGO CALCUL JOUR ANNEE
# MIRANDA KEVIN

# Le but de cet exercice est de créer un programme permettant de savoir le jour de la semaine
# pour une date donnée dans le calendrier grégorien. Le calendrier grégorien adopté au
# XVIe siècle succède au calendrier Julien, en modifiant la règle pour déterminer quelle année est
# bissextile.



#---------------------------------------FONCTIONS--------------------------------------------


# Fonction qui retourne en fonction du mois entré une valeur definit
def ajouteMois(leMois):
    temp = ['0','3','3','6','1','4','6','2','5','0','3','5']
    return temp[leMois-1]


# Fonction de PREDICAT qui retourne si l'année est bissextile ou non
def bissextile(lAnnee):
    if lAnnee % 400 == 0: # Si l'année est divisible par 400
        return True
    elif lAnneeannee % 100 == 0: # Si l'année est divisible par 100
        return False
    elif lAnneennee % 4 == 0: # Si l'années est divisible par 4
        return True


# Fonction qui retourne en fonction du siecle une valeur définit
def ajouteSiecle(lAnnee):
    temp = int(lAnnee/100)
    temp *= 100
    if (temp == 1600):
        return 6
    elif (temp == 1700):
        return 4
    elif (temp == 1800):
        return 2
    elif (temp == 1900):
        return 0
    elif (temp == 2000):
        return 6
    elif (temp == 2100):
        return 4


# Fonction qui affiche la jour de la semaine en fonction de la date
def affichageFinal(monChiffre):
    if (monChiffre == 0):
        print("Le ", dateUser, " était un Dimanche !")
    elif (monChiffre == 1):
        print("Le ", dateUser, " était un Lundi !")
    elif (monChiffre == 2):
        print("Le ", dateUser, " était un Mardi !")
    elif (monChiffre == 3):
        print("Le ", dateUser, " était un Mercredi !")
    elif (monChiffre == 4):
        print("Le ",dateUser," était un Jeudi !")
    elif (monChiffre == 5):
        print("Le ", dateUser, " était un Vendredi !")
    elif (monChiffre == 6):
        print("Le ", dateUser, " était un Samedi !")


#------------------------------------------------------------------------------------------


# Recuperation de la date choisi par l'user + on test si la date est à une longeur correcte de 10 caracteres
while True:
    dateUser = input("Entrez la date au format jj/mm/aaaa : ")
    if (len(dateUser) > 10):
       print("ATTENTION DATE TROP LONGUE ")
    elif (len(dateUser) < 10):
       print("ATTENTION DATE TROP COURTE ")
    else:
       break


# On sépare notre chaine dans differentes variables Année / mois / jour
monAnnee = int(dateUser[6:10])
monMois = int(dateUser[3:5])
monJour = int(dateUser[0:2])


# ETAPE 1 : On garde les deux derniers chiffres de l'année :
deuxAnnee = int(dateUser[8:10])


# ETAPE 2 : On ajoute 1/4 de ce chiffre en ignorant le reste :
calculus = deuxAnnee/4


# ETAPE 3 : On ajoute la journée du mois :
calculus += monJour


# ETAPE 4 : Selon le mois on ajoute un chiffre definit dans la fonction ajouteMois() :
calculus += int(ajouteMois(monMois))


# ETAPE 5 : Si l'année est bissextile (vérifié par la fonction bissextile() et le mois est janvier ou février, on ôte 1 :
if ((monMois == '01') or (monMois == '02') and bissextile(monAnnee)):
    calculus -= 1


# ETAPE 6 : Selon le siècle, on ajoute un chiffre definit dans la fonction ajouteSiecle():
calculus += ajouteSiecle(monAnnee)


# ETAPE 7 : On divise la somme par 7 et on garde que le reste (ici via un modulo) :
calculus = calculus%7


# ETAPE 8 : Le reste représente le jour de la semaine recherché et est affiché via la fonction affichageFinal() :
affichageFinal(calculus)