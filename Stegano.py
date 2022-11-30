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
    for y in range(hi):
        #on boucle sur l'abscisse de la n'image
        for x in range(li):
            #on boucle sur l'ordonee de la n'image
            ri, vi, bi = pixels_invitee[x, y]
            numero_pixel_i = y * li + x
            numero_pixel_h = 4 * numero_pixel_i
            x1 = (numero_pixel_h)//lh
            x2 = (numero_pixel_h + 1)//lh
            x3 = (numero_pixel_h + 2)//lh
            x4 = (numero_pixel_h + 3)//lh
            y1 = (numero_pixel_h)%lh
            y2 = (numero_pixel_h+1)%lh
            y3 = (numero_pixel_h+2)%lh
            y4 = (numero_pixel_h+3)%lh
            rh1, vh1, bh1 = pixels_invitee[x, y]
            ri, vi, bi = pixels_invitee[x, y]
            rh1, vh1, bh1 = pixels_hote[x1, y1]
            rh2, vh2, bh2 = pixels_hote[x2, y2]
            rh3, vh3, bh3 = pixels_hote[x3, y3]
            rh4, vh4, bh4 = pixels_hote[x4, y4]
            fr1, fr2, fr3, fr4 = fusion_composantes(ri, rh1, rh2, rh3, rh4)
            fv1, fv2, fv3, fv4 = fusion_composantes(vi, vh1, vh2, vh3, vh4)
            fb1, fb2, fb3, fb4 = fusion_composantes(bi, bh1, bh2, bh3, bh4)
            newpixels[x1, y1] = (fr1, fv1, fb1)
            newpixels[x2, y2] = (fr2, fv2, fb2)
            newpixels[x3, y3] = (fr3, fv3, fb3)
            newpixels[x4, y4] = (fr4, fv4, fb4)
    img_cache.save("cachee.bmp")
    print("c'est cacher!")
        
    
    
    
    
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
    image = Image.open(chemin_image) # je précise le chemin de mon image
    largeur, hauteur = image.size # image.size retourne un tuple de 2 valeurs
    print(f"largeur = {largeur} pixels")
    print(f"hauteur = {hauteur} pixels")
    h_revele = int(largeur/4)
    l_revele = int(hauteur/4)
    print(h_revele)
    pixels = image.load() # j'ai tous les pixels de l'image grace à load()
    image_revele = Image.new("RGB", (l_revele, h_revele))
    newpixels = image_revele.load()
    for y in range(h_revele):
        #on boucle sur l'abscisse de la n'image
        for x in range(l_revele):
            #on boucle sur l'ordonee de la n'image
            r, v, b = pixels[x, y]
            numero_pixel_c = y * largeur + x
            numero_pixel_r = int(numero_pixel_c / 4)
            xr = (numero_pixel_r)//largeur
            yr = (numero_pixel_r)%largeur
            xc1 = (numero_pixel_c)//largeur
            xc2 = (numero_pixel_c + 1)//largeur
            xc3 = (numero_pixel_c + 1)//largeur
            xc4 = (numero_pixel_c + 1)//largeur
            yc1 = (numero_pixel_c)%largeur
            yc2 = (numero_pixel_c + 1)%largeur
            yc3 = (numero_pixel_c + 2)%largeur
            yc4 = (numero_pixel_c + 3)%largeur
            rc1, vc1, bc1 = pixels[xc1, yc1]
            rc2, vc2, bc2 = pixels[xc2, yc2]
            rc3, vc3, bc3 = pixels[xc3, yc3]
            rc4, vc4, bc4 = pixels[xc4, yc4]
            er = extraction_composante(rc1, rc2, rc3, rc4)
            ev = extraction_composante(vc1, vc2, vc3, vc4)
            eb = extraction_composante(bc1, bc2, bc3, bc4)
            newpixels[x, y] = (er, ev, eb)
    image_revele.save("révélé.bmp")
    print("c'est révélé!")

def extraction_composante(value1,value2,value3,value4):
    """
    Extrait les deux bits de poids faibles de <value>, et les place en bits de poids forts.
    Après test, l'ajout le plus satisfaisant est le suivant:
    On ajoute '100000' (c'est le milieu de 000000 et 111111) après les deux bits de poids fort extraits.
    Retourne un entier.
    """
    compo_h1 = bin(value1)[2:]
    compo_h2 = bin(value2)[2:]
    compo_h3 = bin(value3)[2:]
    compo_h4 = bin(value4)[2:]
    
    composante_h1=(8-len(compo_h1))*'0'+compo_h1
    composante_h2=(8-len(compo_h2))*'0'+compo_h2
    composante_h3=(8-len(compo_h3))*'0'+compo_h3
    composante_h4=(8-len(compo_h4))*'0'+compo_h4
    
    h1 = bin(value1)[6:8]
    h2 = bin(value2)[6:8]
    h3 = bin(value3)[6:8]
    h4 = bin(value4)[6:8]
    compo_i = int(h1,2)+int(h2,2)+int(h3,2)+int(h4,2)
    return (compo_i)
    # A vous de coder               
    
#dissimuler("Images/61235709.bmp","Images/Dieu.bmp",2)
reveler("cachee.bmp")