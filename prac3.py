import sys
import time

import pygame
import paho.mqtt.client as mqtt
from threading imort*

ip_to = "127.0.0.1"
port_to = 1883
topic_to = "test/topic"

screen = pygame.display.set_mode((400, 300))

def pygame_thread():
    pygame.init()
    clock = pygame.time.Clock()
    done = False

    while not done:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()

def on_message(client, userdata, msg):
    payload = (int(x) for x in msg.payload.split(' '))
    x, y = payload
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x - 10, y - 10, x + 10, y + 10))

if __name__ == '__main__':
    #draw_a_rect()

    t1 = Thread(target=pygame_thread())
    t1.start()

    client = mqtt.Client("subscriber")
    client.on_message = on_message
    client.connect(ip_to, port_to)

    client.loop(60)