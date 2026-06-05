# Prueba Tecnica Ingeniero QA Automatizacion

**Autor:** Miguel Angel Diaz Baquero

Este repositorio contiene la solución al reto técnico de automatización de pruebas, cubriendo tres capas fundamentales del ciclo de desarrollo de software: **Mobile UI (End-to-End), API REST (Integración) y Mensajería de Eventos (Kafka).**

## Arquitectura y Patrones de Diseño

El proyecto está diseñado bajo principios de Clean Architecture y escalabilidad:
*   **Page Object Model (POM):** Separación estricta entre la lógica de negocio (casos de prueba) y la representación de la interfaz de usuario (localizadores y acciones).
*   **Driver Factory / Singleton:** Centralización de las `Capabilities` de Appium para cumplir con el principio DRY (Don't Repeat Yourself) y facilitar el mantenimiento multiplataforma.
*   **Aserciones Duras y Contratos:** Validación rigurosa de JSON Schemas, códigos de estado HTTP y tipos de datos en la mensajería asíncrona.

## Stack Tecnológico

*   **Lenguaje:** Python 3
*   **Mobile UI:** Appium, Selenium WebDriver, UiAutomator2
*   **API Testing:** Requests, JSONSchema
*   **Eventos/Mensajería:** Apache Kafka, `kafka-python`, Docker Compose

## Requisitos Previos

Para ejecutar este proyecto en un entorno Windows, asegúrate de contar con las siguientes herramientas instaladas y configuradas:

1.  **Python 3.14+** (Añadido al PATH).
2.  **Appium Server** v2.x (Ejecutándose en `http://127.0.0.1:4723`).
3.  **Appium UiAutomator2 Driver** instalado.
4.  Un emulador de **Android Studio** o dispositivo físico activo (Ej. `emulator-5554`).
5.  **Docker Desktop** ejecutándose (requerido para levantar el broker local de Kafka).

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio:**
```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd <NOMBRE_DE_LA_CARPETA>