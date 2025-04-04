Proyek ini cocok untuk memahami dasar komunikasi MQTT dalam aplikasi IoT.

## Persyaratan
Pastikan Anda memiliki Python 3.x dan pustaka `paho-mqtt` terinstal:

```bash
pip install paho-mqtt
```

## Cara Penggunaan

### 1. Menjalankan Publisher
Script publisher akan mengirim pesan ke broker MQTT:

```bash
python publisher.py
```

Isi dari `publisher.py`:

```python
import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
topic = "iot/1101220248"

client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    pesan = input("Masukkan pesan yang akan dikirim: ")
    client.publish(topic, pesan)
    print(f"Pesan terkirim: {pesan}")
```

### 2. Menjalankan Subscriber
Subscriber akan menerima dan mencetak pesan yang diterima dari topik MQTT:

```bash
python subscriber.py
```

Isi dari `subscriber.py`:

```python
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
```

## Kontribusi
Silakan fork repository ini, buat perubahan yang diperlukan, lalu ajukan pull request jika ingin berkontribusi.

## Lisensi
Proyek ini menggunakan lisensi MIT.

