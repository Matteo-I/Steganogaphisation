from PIL import Image

def dissimuler(chemin_hote, chemin_invitee,nbit=2):
    """
    chemin_hote(string) : chemin de l'image hôte
    chemin_invitee(string) : chemin de l'image invitée
    Enregistre l'image résultante sous le nom 'fusion.bmp'
    """
    # A vous de coder
    img_hote = Image.open(chemin_hote) # chemin image hote
    img_invitee = Image.open(chemin_invitee) #chemin image invitee
    pixels_hote = img_hote.load()
    pixels_invitee = img_invitee.load()
    lh, hh = img_hote.size
    li, hi = img_invitee.size
    img_cache = Image.new('RGB', (lh, hh))
    newpixels = img_cache.load()
    for y in range(hi-2):
        #on boucle sur l'abscisse de la n'image
        for x in range(li):
            #on boucle sur l'ordonee de la n'image
            ri, vi, bi = pixels_invitee[x, y]
            numero_pixel_i = y * li + x
            numero_pixel_h = 4 * numero_pixel_i
            xh = numero_pixel_h//lh
            yh = numero_pixel_h%lh
            rh1, vh1, bh1 = pixels_invitee[x, y]
            ri, vi, bi = pixels_invitee[x, y]
            rh1, vh1, bh1 = pixels_hote[xh, yh]
            rh2, vh2, bh2 = pixels_hote[xh+1, yh]
            rh3, vh3, bh3 = pixels_hote[xh+2, yh]
            rh4, vh4, bh4 = pixels_hote[xh+3, yh]
            fr1, fr2, fr3, fr4 = fusion_composantes(ri, rh1, rh2, rh3, rh4)
            fv1, fv2, fv3, fv4 = fusion_composantes(vi, vh1, vh2, vh3, vh4)
            fb1, fb2, fb3, fb4 = fusion_composantes(bi, bh1, bh2, bh3, bh4)
            newpixels[x, y] = (fr1, fv1, fb1)
            newpixels[x+1, y] = (fr2, fv2, fb2)
            newpixels[x+2, y] = (fr3, fv3, fb3)
            newpixels[x+3, y] = (fr4, fv4, fb4)
    img_cache.save("cachee.bmp")
        
    
    
    
    
def fusion_composantes(composante_invitee, composante_hote1,composante_hote2,composante_hote3,composante_hote4):
    # On enleve le 'ob' et on converti en binaire
    compo_invitee = bin(composante_invitee)[2:]
    # On pass la veleur du pixel sur 8 bits
    compo_invitee=(8-len(compo_invitee))*'0'+compo_invitee    
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

def extraction_composante(value1,value2,value3,value4):
    """
    Extrait les deux bits de poids faibles de <value>, et les place en bits de poids forts.
    Après test, l'ajout le plus satisfaisant est le suivant:
    On ajoute '100000' (c'est le milieu de 000000 et 111111) après les deux bits de poids fort extraits.
    Retourne un entier.
    """
    compo_h1 = bin(value1)[2:][6:8]
    compo_h2 = bin(value2)[2:][6:8]
    compo_h3 = bin(value3)[2:][6:8]
    compo_h4 = bin(value4)[2:][6:8]
    
    nb= 0
    return 0
    # A vous de coder               
    
dissimuler("Images/61235709.bmp","Images/Dieu.bmp",2)
