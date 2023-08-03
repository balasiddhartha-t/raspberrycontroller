from django.apps import AppConfig
import RPi.GPIO as GPIO
import pygame
import threading

pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

def run_on_startup():
    print("################# Joystick thread initialized #####################.")
    # For all the connected joysticks
    for i in range(0, pygame.joystick.get_count()):
        # Create a Joystick object in our list
        joysticks.append(pygame.joystick.Joystick(i))
        # Initialize the appended joystick
        joysticks[-1].init()
        # Print a statement telling the name of the controller
        print("Detected joystick", joysticks[-1].get_name())

        while keepPlaying:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    # Button press event handling
                    if event.button == 0:
                        print('stop event called')
                        GPIO.output(3, False)
                        GPIO.output(5, False)
                        GPIO.output(8, False)
                        GPIO.output(10, False)
                elif event.type == pygame.JOYAXISMOTION:
                    # Axis motion event handling
                    axis_x = joysticks[0].get_axis(0)  # X-axis index is 0
                    axis_y = joysticks[0].get_axis(1)  # Y-axis index is 1
                    axis_z = joysticks[0].get_axis(2)  # Z-axis index is 2 (if available)
                    print("X-axis:", axis_x, " Y-axis:", axis_y, " Z-axis:", axis_z)
                    if  axis_x > 0.5:
                        print("Rotating right")
                        # commands for right
                        GPIO.output(3, True)
                        GPIO.output(5, False)
                        GPIO.output(8, False)
                        GPIO.output(10, False)
                    elif axis_x <= -1.0:
                        print("Rotating left")
                        # commands for left
                        GPIO.output(3, False)
                        GPIO.output(5, False)
                        GPIO.output(8, True)
                        GPIO.output(10, False)
                    elif axis_y > 0.5 :
                        print("Going Forward")
                        # forward
                        GPIO.output(3, False)
                        GPIO.output(5, True)
                        GPIO.output(8, False)
                        GPIO.output(10, True)
                    elif axis_y < -0.5 :
                        print("Going Backward")
                        # backward
                        GPIO.output(3, True)
                        GPIO.output(5, False)
                        GPIO.output(8, True)
                        GPIO.output(10, False)

class RaspberrysiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'raspberrysite'

    def ready(self):
        # Code to run when Django is initialized
        startup_thread = threading.Thread(target=run_on_startup)
        startup_thread.start()
        