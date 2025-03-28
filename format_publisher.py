import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
topic = "iot/1101220248"

client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    asal = input("Masukkan kelas asal: ")
    hobi = input("Masukkan hobi: ")
    pesan = f"nama: {nama}; nim: {nim}; asal: {asal}; hobi: {hobi}"
    client.publish(topic, pesan)
    print(f"Pesan terkirim: {pesan}")
