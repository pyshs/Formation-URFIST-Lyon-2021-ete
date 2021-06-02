nombre_articles = 0
motcle = "Macron"
titres = [" C'est l'histoire de deux potes... Les youtubeurs  McFly et Carlito vont bientôt tourner à l'Elysée une vidéo avec Emmanuel Macron, à la suite d'un pari gagné avec le chef de l'Etat. Portrait de ces deux rois du Web. ",
 " McFly et Carlito aux portes de l'Elysée Si la vidéo des deux youtubeurs sur les gestes barrière atteint 10 millions de vues, le chef de l'Etat les recevra. Et c'est bien parti. ",
 ' Par Rosalie Lucas  Mcfly et Carlito, ministres ',
 " Macron contre  McFly et Carlito : match nul et deux gagnants Les deux youtubeurs à succès ont mis en ligne hier matin la vidéo de leur concours d'anecdotes avec le président de la République. Un coup de com déjà vu par 6,7 millions de personnes. ",
 " Devant  McFly et Carlito, Macron veut séduire les jeunes Dans la vidéo postée dimanche, il s'engage à mettre une photo des deux youtubeurs sur son bureau lors d'une prochaine prise de parole. "]
nombre_total_articles = len(titres)

if nombre_total_articles > 0:
    for i in titres:
        if motcle in i:
            print(i)
            nombre_articles+=1
else:
    print("La liste est vide")
    
proportion = 100*nombre_articles/nombre_total_articles
print("Proportion d'articles contenant le terme dans le titre : {} %".format(round(proportion,1)))