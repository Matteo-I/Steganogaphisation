from PIL import Image

def dissimuler(chemin_hote, chemin_invitee):
    """
    chemin_hote(string) : chemin de l'image hôte
    chemin_invitee(string) : chemin de l'image invitée
    Enregistre l'image résultante sous le nom 'fusion.bmp'
    """
    # A vous de coder               
    pass
    
    
def fusion_composantes(composante_invitee, composante_hote1,composante_hote2,composante_hote3,composante_hote4):
    # On enleve le 'ob' et on converti en binaire
    compo_invitee = bin(composante_invitee)[2:]
    # On pass la veleur du pixel sur 8 bits
    compo_invitee=(8-len(compo_invitee))*'0'+composante_invitee
    # On recupere  les bits dela comp invitee
    compo_invitee1 = compo_invitee[0:2]
    compo_invitee2 = compo_invitee[2:4]
    compo_invitee3 = compo_invitee[4:6]
    compo_invitee4 = compo_invitee[6:8]
    
    compo1 = int(compo_invitee1,2) + composante_hote1
    compo2 = int(compo_invitee2,2) + composante_hote2
    compo3 = int(compo_invitee3,2) + composante_hote3
    compo4 = int(compo_invitee4,2) + composante_hote4
    
    return(compo1,compo2,compo3,compo4)
    
    
    
    
 
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
