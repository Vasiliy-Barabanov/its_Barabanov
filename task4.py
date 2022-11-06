import os
import paho.mqtt.client as mqtt


def read_and_publish(path):
    client = mqtt.Client("publisher")
    client.connect('127.0.0.1', 1883)
    f = open(path, "r")

    lines = f.readlines()
    for line in lines:
        client.publish('test/topic', line)


v = []


def print_avg(vt):
    if (len(v) == 1):
        print(v[0] * 0.6)
    if (len(v) == 2):
        print(v[1] * 0.6 + v[0] * 0.3)
    if (len(v) == 3):
        print(v[2] * 0.6 + v[1] * 0.3 - v[0] * 0.1)


def on_message(client, userdata, msg):
    if (len(v) == 3):
        v.pop(0)
        v.append(float(msg.payload))
        print_avg(v)
    else:
        v.append(float(msg.payload))
        print_avg(v)


def subscribe_and_print():
    client = mqtt.Client("subscriber")
    client.on_message = on_message
    client.connect("127.0.0.1", 1883)

    client.loop(60)


if __name__ == '__main__':
    read_and_publish("text.txt")
    subscribe_and_print()