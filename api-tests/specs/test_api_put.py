import requests
from jsonschema import validate, ValidationError

producto_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "price": {"type": "number"}
    },
    "required": ["id", "title", "price"]
}

def test_crear_producto():
    url_post = "https://dummyjson.com/products/add"
    url_put = "https://dummyjson.com/products/1"
    #url = "https://dummyjson.com/products/agregar_producto_falso"
    payload = {
        "title": "Zapatos QA Automation",
        "price": 120
    }
    headers = {"Content-Type": "application/json"}
   
    print("Prueba PUT")
    try:
        print("1. Ejecutando petición PUT...")
        
        put_response = requests.put(url_put, json=payload, headers=headers)
        
        print(f"2. Validacion estado HTTP (Recibido: {put_response.status_code})...")
        assert put_response.status_code in [200, 201], f"Fallo: Estado incorrecto {put_response.status_code}"
        
        put_tiempo_respuesta = put_response.elapsed.total_seconds()
        print(f"3. Validando SLA de tiempo (Recibido: {put_tiempo_respuesta} segundos)...")
        assert put_tiempo_respuesta < 1.5, f"Fallo: La API es muy lenta ({put_tiempo_respuesta}s)"
        
        print("4. Validando contrato JSON Schema...")
        put_datos_recibidos = put_response.json()
        validate(instance=put_datos_recibidos, schema=producto_schema)
        
        print("2.1 Validando cabeceras de respuesta...")
        content_type = put_response.headers.get("Content-Type", "")
        assert "application/json" in content_type, f"Fallo: la cabecera Content-Type no es JSON. Recibido: {content_type}"
        
        print("¡PRUEBA DE API PASADA CON ÉXITO!")
                
    except AssertionError as error_asercion:
        print(f"Prueba fallida por aserción: {error_asercion}")
    except ValidationError as error_contrato:
        print(f"Prueba fallida, el contrato no coincide: {error_contrato.message}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    test_crear_producto()