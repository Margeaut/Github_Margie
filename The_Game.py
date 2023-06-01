#FERLA Margaux & BETTE Angie - THE GAME

#--------------------------------------------------------
# ------------------------ IMPORTS ----------------------
#--------------------------------------------------------

from random import choice

#--------------------------------------------------------
# ----------------------- FONCTIONS ---------------------
#--------------------------------------------------------

def deroulement_tour(tour_actuel, mains, pioche,cartes):
    """permet de faire tourner le tour automatiquement sans surcharger le code"""
    #pour chaque carte que le joueur souhaite poser, demander laquelle et le tas choisi
    for i in range(cartes):
        carte=int(input("Quelle carte allez-vous jouer ? "))
        tas=input("Sur quelle pile ? ")
        #conditions pour poser une carte sur les tas :
        #si choix pile ascendante: il faut que la carte soit > à la dernière carte de la pile croissante
        #si choix pile descendante: il faut que le carte soit < à la dernière carte de la pile
        while (((tas=="Asc1" or tas=="Asc2") and (carte<globals()[tas][-1] and (carte+10)!=globals()[tas][-1])) or ((tas=="Desc1" or tas=="Desc2") and (carte>globals()[tas][-1] and (carte-10)!=globals()[tas][-1]))) : 
            print("\nVous ne savez pas jouer ! Relisez les règles")
            carte=int(input("Choissisez une nouvelle carte : "))
            tas=input("Sur quelle pile ? ")
        
        #enlève la carte qui vient d'être posée et on l'ajoute au tas choisi
        mains[tour_actuel].remove(carte)
        globals()[tas].append(carte)
        print("Main du joueur",tour_actuel+1,":",mains[tour_actuel])
    
    print("\nVous pouvez piocher krobi'un !")
    
    #si la pioche est vide, on ne pioche pas de carte
    if len(pioche)!=0:
        for i in range(cartes):
            piocher=choice(pioche)
            mains[tour_actuel].append(piocher)
            pioche.remove(piocher) #i[j] est la carte sélectionnée par le random
            if len(pioche)==0:
                #au moment où la pioche est vidée
                print("\n--- Pioche vidée ! --- \n")
                break
        
    print("\nNouvelle main du joueur",tour_actuel+1,":",mains[tour_actuel])


def cartes_jouees(num_joueur,mains):
    """permet de retourner le nombre de cartes que le joueur souhaite poser"""
    print("Main du joueur",tour_actuel+1,' : \t',mains[tour_actuel])
    cartes_jouees=int(input("Combien de cartes allez-vous jouer ? "))
    return cartes_jouees


def Plateau(pile1,pile2,pile3,pile4):
    """ affiche le plateau de jeu (les 4 tas) """
    print(' {:>12} \t {}'.format("(1)",("(2)")))
    print('↑  {:10} \t {}\n'.format(pile1[-1],pile2[-1]))
    print('↓  {:10} \t {}'.format(pile3[-1],pile4[-1]))



#--------------------------------------------------------
# ------------------ DEBUT DE LA PARTIE -----------------
#--------------------------------------------------------

print("------- T H E   G A M E -------")
#Affichage des règles lors du lancement du jeu
regles=input("\nSouhaites-vous consulter les règles du jeu (O ou N) ? ")
if regles=="O":
    regle=open('Regles_TheGame.txt','r') #mettre le fichier txt dans le même dossier que le file python
    print("\n")
    for ligne in regle:
        print(ligne)
    regle.close()

#Initialisation du nombre de joueurs
nbr_joueurs=int(input("Combien de joueurs vont jouer ? "))
#Tant que le nbr de joueurs est supérieur à 5, le jeu ne commence pas
while nbr_joueurs>5 :
    print("Vous êtes trop, entretuez-vous")
    nbr_joueurs=int(input("Combien de joueurs vont jouer ? "))

#Initialisation des listes (yen a tro & qd c trop c tropico)
#Listes pour poser les cartes
Asc1=[1]
Asc2=[1]
Desc1=[100]
Desc2=[100]

#Mains des joueurs
pioche=[i for i in range(2,99)] #de 2 à 99
if nbr_joueurs==1 :
    nbr_cartes=8
elif nbr_joueurs==2 : 
    nbr_cartes=7
elif nbr_joueurs>2 :
    nbr_cartes=6

#Distribution des cartes
mains=[[] for i in range(nbr_joueurs)] #crée les x mains dans une même liste
for i in mains :
    for j in range(nbr_cartes):
        i.append(choice(pioche))
        pioche.remove(i[j]) #i[j] est la carte sélectionnée par le random
        
#Initialisation du tour
tour=[i for i in range(0,nbr_joueurs)]
tour_actuel=0

#Affichage du plateau
Plateau(Asc1,Asc2,Desc1,Desc2)

#Tant que les conditions de fin de partie ne sont pas remplies, le tour des joueurs tourne en boucle
while tour_actuel!=len(tour):
    for i in tour :
        cartes=cartes_jouees(tour_actuel, mains)
        #Fin de partie quand la pioche est vide
        if len(pioche)==0 : 
            if cartes==0:
                score=len(pioche)+sum(len(i) for i in mains)
                print('Score : ',score)
                print("Fin de la partie")
                tour_actuel=len(tour)
                break
        #Fin de partie quand la pioche n'est pas vide
        else :
            if cartes<2:
                score=len(pioche)+sum(len(i) for i in mains)
                print('Score : ',score)
                print("Fin de la partie")
                tour_actuel=len(tour)
                break
        
        deroulement_tour(tour_actuel, mains, pioche,cartes) #récupère le nb de carte jouées
        Plateau(Asc1,Asc2,Desc1,Desc2)
        
        #Boucle des tours
        if tour_actuel==max(tour):
            tour_actuel=0
        else :
            tour_actuel+=1
            
        
        
            
    









