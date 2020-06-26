#!/usr/bin/python3.7

import cgi, cgitb , datetime

# Lecture des données formulaire
form = cgi.FieldStorage() 
xnom = form.getvalue('nom')
xprenom  = form.getvalue('prenom')
xville = form.getvalue('ville')
xcomment = form.getvalue('comment')

# Création du fichier si n'existe pas et ouverture en mode append 
gb=open("/home/ginf2021/yelhouari/public_html/guest.html","a")

# Ecriture des informations dans le fichier avec balisage HTML
gb.write('<div> <hr />')
gb.write ("<p><em>Date</em>: "+str(datetime.date.today())+"<br />\n")
gb.write ("<em>De</em>: <strong>"+str(xnom)+", ")
gb.write(str(xprenom)+"</strong><br />")
gb.write ("<em>Adresse</em>: "+str(xville)+"</p>\n")
gb.write("<blockquote>")
gb.write (str(xcomment)+"</blockquote></div>")

gb.close()

# Sortie sur UA de l'accusé de réception
print ("Content-type: text/html; charset=UTF-8\n")
a = """
<!DOCTYPE html>
<html>
<head>
<title>Merci!...</title>
</head>
<body>
"""
print(a)
print ("<p> Merci %s %s </p>" % (xnom, xprenom));
a = """
<p> Votre message a été transmis </p>
<p><em> Au revoir </em></p>
</body>
</html>
"""
print(a)
