import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
topic = "iot/1101220248"

client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    pesan = input("Masukkan pesan yang akan dikirim: ")
    client.publish(topic, pesan)
    print(f"Pesan terkirim: {pesan}")
