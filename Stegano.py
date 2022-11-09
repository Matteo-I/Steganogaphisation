from PIL import Image

def dissimuler(chemin_hote, chemin_invitee):
    """
    chemin_hote(string) : chemin de l'image hôte
    chemin_invitee(string) : chemin de l'image invitée
    Enregistre l'image résultante sous le nom 'fusion.bmp'
    """
    # A vous de coder               
    pass

def fusion_composantes(composante_hote, composante_invitee):
    """
    composante_hote(entier) : composante (R, V ou B)
    composante_invitee(entier) : composante (R, V ou B)
    retourne la composante fusionnée sous forme d'entier 
    """
    # A vous de coder               
    pass
    
 
def reveler(chemin_image):
    """
    chemin_image(string) : chemin de l'image
    sauvegarde l'image sous le nom 'extraction.bmp'
    """
    # A vous de coder               
    pass

def extraction_composante(value):
    """
    Extrait les deux bits de poids faibles de <value>, et les place en bits de poids forts.
    Après test, l'ajout le plus satisfaisant est le suivant:
    On ajoute '100000' (c'est le milieu de 000000 et 111111) après les deux bits de poids fort extraits.
    Retourne un entier.
    """
    # A vous de coder               
    pass
