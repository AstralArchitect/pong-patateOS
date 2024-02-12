import threading
from random import randint
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

# Initialisez toutes les variables globales
message = "pong..."
sense.show_message(message, text_colour=(127, 127, 0), scroll_speed=0.1)
sense.clear()
ballx = 4
bally = 3
youx = 0
youy = [3, 4]
ennemix = 7
ennemiy = [3, 4]
mx = 0
my = 0
temps = 1
a = 0
sense.set_pixel(0, 7, 0, 65, 65)
sense.set_pixel(1, 7, 0, 65, 65)
sense.set_pixel(2, 7, 0, 65, 65)
sense.set_pixel(3, 7, 0, 65, 65)
sense.set_pixel(4, 7, 0, 65, 65)
sense.set_pixel(5, 7, 0, 65, 65)
sense.set_pixel(6, 7, 0, 65, 65)
sense.set_pixel(7, 7, 0, 65, 65)
sense.set_pixel(0, 0, 0, 65, 65)
sense.set_pixel(1, 0, 0, 65, 65)
sense.set_pixel(2, 0, 0, 65, 65)
sense.set_pixel(3, 0, 0, 65, 65)
sense.set_pixel(4, 0, 0, 65, 65)
sense.set_pixel(5, 0, 0, 65, 65)
sense.set_pixel(6, 0, 0, 65, 65)
sense.set_pixel(7, 0, 0, 65, 65)
sense.set_pixel(youx, youy[0], 127, 127, 0)
sense.set_pixel(youx, youy[1], 127, 127, 0)
# Définissez la fonction afficher()
def renderyou():
    sense.set_pixel(youx, youy[0], 127, 127, 0)
    sense.set_pixel(youx, youy[1], 127, 127, 0)

def renderball():
    sense.set_pixel(ballx, bally, 0, 127, 0)
    sense.set_pixel(ennemix, ennemiy[0], 127, 127, 0)
    sense.set_pixel(ennemix, ennemiy[1], 127, 127, 0)

sleep(0.5)

# Définissez la fonction move()
def move():
    global a
    while(a == 0):
        events = sense.stick.get_events()
        for event in events:
            if event.action == "pressed" and event.direction == "up":
                if not (youy[1] < 3):
                    sense.set_pixel(youx, youy[0], 0, 0, 0)
                    sense.set_pixel(youx, youy[1], 0, 0, 0)
                    youy[0] = youy[0] - 1
                    youy[1] = youy[1] - 1
                    renderyou()
            elif event.action == "pressed" and event.direction == "down":
                if not (youy[1] > 5):
                    sense.set_pixel(youx, youy[0], 0, 0, 0)
                    sense.set_pixel(youx, youy[1], 0, 0, 0)
                    youy[0] = youy[0] + 1
                    youy[1] = youy[1] + 1
                    renderyou()

move_thread = threading.Thread(target=move)
move_thread.start()

# Définissez la fonction ball()
def ball():
    global a, temps, my, ennemix, ennemiy, youx, youy, ballx, bally, mx
    while (a == 0):
        sense.set_pixel(ballx, bally, 0, 0, 0)
        sense.set_pixel(ennemix, ennemiy[0], 0, 0, 0)
        sense.set_pixel(ennemix, ennemiy[1], 0, 0, 0)
        if mx == 0:
            ballx = ballx + 1
        elif mx == 1:
            ballx = ballx - 1
        if my == 0:
            bally = bally + int(randint(0, 1))
        elif my == 1:
            bally = bally - int(randint(0, 1))
        if bally < 3 or bally == 3:
            ennemiy[0] = bally
            ennemiy[1] = bally + 1
            renderball()
            sleep(temps)
        else:
            ennemiy[0] = bally - 1
            ennemiy[1] = bally
            renderball()
            sleep(temps)
        if ballx == 6:
            mx = 1
        elif (ballx == 1 and bally == youy[1]) or (ballx == 1 and bally == youy[0]):
            mx = 0
        elif (ballx == 1 and not(bally == youy[1])) or (ballx == 1 and not(bally == youy[0])):
            mx = 0
            message = "Vous avez perdu !"
            sense.show_message(message, text_colour=(127, 0, 0), scroll_speed=0.1)
            a = 1
            break
        if bally == 6:
            my = 1
        elif temps < 0.05:
            my = 1
            message = "Vous avez gagne !"
            sense.show_message(message, text_colour=(70, 127, 70), scroll_speed=0.1)
            a = 1
            break
        elif bally == 1:
            my = 0
            temps = temps - 0.05

ball_thread = threading.Thread(target=ball)
ball_thread.start()