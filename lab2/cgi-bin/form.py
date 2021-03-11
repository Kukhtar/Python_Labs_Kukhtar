#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "")
text2 = form.getfirst("TEXT_2", "")
text3 = form.getfirst("if", "")
text4 = form.getfirst("lv", "")
text5 = form.getfirst("contact", "none")

if text3 == "on":
	text3 = "Ivano-Framkivsk"

if text4 == "on":
	text4 = ", Lviv"

i = 0
if text1=="":
    i = i + 1
if text2=="":
    i = i + 1
if text3=="":
    i = i + 1
if text4=="":
    i = i + 1
if text5=="":
    i = i + 1

print("Set-cookie: counter="+str(i)+";")

print("Content-type: text/html\n")
print(str(i) + " counter")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обробка даних форм</title>
        </head>
        <body>""")

print("<h1>Обробка даних форм!</h1>")
print("<p>Name: {}</p>".format(text1))
print("<p>Surname: {}</p>".format(text2))
print("<p>Cities: {}</p>".format(text3 + text4))
print("<p>Contact: {}</p>".format(text5))



print("""</body>
        </html>""")