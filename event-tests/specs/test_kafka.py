import json
import time
from kafka import KafkaProducer, KafkaConsumer

def test_telemetry_event():
    topic_name = "qa_telemetry_events"
    bootstrap_servers = ['localhost:9092']

    try:
        producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

        evento_enviado = {
            "event_type": "user_login",
            "platform": "android",
            "timestamp": int(time.time()),
            "status": "success"
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
            if message.value.get("event_type") == "user_login":
                mensaje_recibido = message.value
                break

        assert mensaje_recibido is not None, "Fallo: No se encontró el evento en Kafka."
        assert mensaje_recibido["platform"] == "android", "Fallo: Plataforma incorrecta."
        assert mensaje_recibido["status"] == "success", "Fallo: Estado incorrecto."

        print("¡BONUS TRACK COMPLETADO! Evento producido, consumido y validado con éxito.")

    except Exception as e:
        print(f"Ocurrió un error con Kafka: {e}")
        print("Asegúrate de tener un servidor Kafka ejecutándose en el puerto 9092.")

if __name__ == "__main__":
    test_telemetry_event()