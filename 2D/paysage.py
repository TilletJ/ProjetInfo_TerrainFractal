from sommet import Sommet


class Paysage:

    def __init__(self, som_gauche, som_milieu, som_droit):
        self.liste_sommets = Sommet([som_gauche, som_milieu, som_droit])

    def affine(self, fraction=1/2):
        som = self.liste_sommets
        while som is not None and som.next is not None:
            som.creer_sommet(fraction)
            som = som.next.next

    def save(self, nom_fichier):
        with open(nom_fichier, 'w') as f:
            som = self.liste_sommets
            while som is not None:
                f.write(str(som))
                f.write("\n")
                som = som.next

    def __str__(self):#TODO
        string = ""
        for sommet in self.liste_sommets:
            string+= str(sommet) +"\n"
        return string