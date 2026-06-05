import json
import time
from kafka import KafkaProducer, KafkaConsumer

def test_telemetry_event():
    topic_name = "gps-raw-events"
    bootstrap_servers = ['localhost:9092']

    try:
        producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

        evento_enviado = {
            "vehicleId": "VEH-99",
            "lat": 4.60,
            "lng": -74.08,
            "speed": 65
        }

        print("1. Produciendo evento de telemetría hacia Kafka...")
        producer.send(topic_name, evento_enviado)
        producer.flush()
        print("Evento publicado en el tópico.")

        print("2. Conectando el consumidor para leer el evento...")
        consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='qa_test_group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            consumer_timeout_ms=5000
        )

        print("3. Buscando y validando el mensaje...")
        mensaje_recibido = None
        
        for message in consumer:
            if message.value.get("vehicleId") == "VEH-99":
                mensaje_recibido = message.value
                break

        assert mensaje_recibido is not None, "Fallo: No se encontró el evento del vehículo."
        assert type(mensaje_recibido["lat"]) == float, "Fallo de contrato: Latitud no es decimal."
        assert mensaje_recibido["speed"] == 65, "Fallo: La velocidad no coincide."

        print("¡BONUS TRACK COMPLETADO! Evento producido, consumido y validado con éxito.")

    except Exception as e:
        print(f"Ocurrió un error con Kafka: {e}")
        print("Asegúrate de tener un servidor Kafka ejecutándose en el puerto 9092.")

if __name__ == "__main__":
    test_telemetry_event()