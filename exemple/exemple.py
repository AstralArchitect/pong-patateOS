#importer les librairies sense Hat, elle sont installés par défaut sur patateOS
from sense_hat import SenseHat

sense = SenseHat()

#afficher " Hello World " sur le sense hat
message = "Hello World"
sense.show_message(message, text_colour=(127, 127, 0), scroll_speed=0.1)
