#!/usr/bin/python3.7

import cgi, cgitb , datetime,os

# Lecture des données formulaire
form=cgi.FieldStorage()
xnom=form.getvalue('nom')
xprenom=form.getvalue('prenom')
xemail=form.getvalue('email')
xcomment=form.getvalue('comment')
xnavigateur=form.getvalue('navigateur')
ip=""
for key in os.environ.keys():
	if key=="REMOTE_ADDR":
		ip=os.environ[key]

# Création du fichier si n'existe pas et ouverture en mode append 
gb=open("/home/ginf2021/yelhouari/public_html/guest.html","a")

# Ecriture des informations dans le fichier avec balisage HTML
gb=open("/home/ginf2021/yelhouari/public_html/guest.html","a")
gb.write("<div class='guest'><hr/>")
gb.write("<p>Post ,le "+str(datetime.date.today())+"</p>")
gb.write("<p><strong>Nom</strong> : "+str(xnom)+" "+str(xprenom)+"</p>\n")
gb.write("<p><strong>Email</strong> : "+str(xemail)+" </p>\n")
gb.write("<p><strong>Message</strong> :"+str(xcomment)+" </p>\n")
gb.write("<p>Vous utilisez le navigateur : "+str(xnavigateur)+"</p>")
gb.write("<p>Connecté  à partir de : "+str(ip)+"</p></div>")
gb.close()


# Sortie sur UA de l'accusé de réception
print("Content-type:text/html; charset=UTF-8")
print()
a="""
<!DOCTYPE html>
<html>
<head><title>Confirmation</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:ital@1&display=swap" rel="stylesheet">
<style>
h1
{
	text-align:center;
	position:absolute;
	left:35%;
	top:20%;
}
body
{
	font-family: 'Nunito', sans-serif;
	background:url(../ImageArticle/background.jpg);
background-size:cover;
background-repeat:no-repeat;
}
a{
	text-decoration: none;
	color:black;
text-align:center;
	

}
a:hover
{
	color:white;
	background: black;
}
.test
{
position:absolute;
	left:35%;
	top:30%;
}
</style>
</head>
<body>

<h1>Nous avons envoye votre message</h1>
<div class="test">
<p><a href="../guest.html"><img src="../ImageArticle/back.png"/> Voir le livre d'or</a></p>
<p><a href="../index.html"><img src="../ImageArticle/home.png"/> Acceuil</a></p>
</div>
</body>
</html>"""
print(a)
