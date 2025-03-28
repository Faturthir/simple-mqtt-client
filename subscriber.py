import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Pesan diterima: {message.payload.decode()}")

broker = "test.mosquitto.org"
topic = "iot/1101220248"

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, 1883, 60)
client.subscribe(topic)
client.loop_forever()
