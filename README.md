#  Prueba Técnica de Automatización QA - Mobile, API & Eventos

Este repositorio contiene la solución a la prueba técnica de automatización, abarcando validaciones de interfaz móvil, contratos de backend y flujos de mensajería asíncrona.

## Arquitectura del Proyecto

El proyecto está diseñado bajo principios de escalabilidad y mantenibilidad, separando la lógica de negocio de los localizadores utilizando el patrón **Page Object Model (POM)** para la capa móvil.

```text
C:.
├── api-tests/
│   ├── config/       # Variables de entorno y configuraciones de API
│   └── specs/        # Scripts de validación de backend (test_api.py)
├── event-tests/
│   └── specs/        # Scripts de validación de mensajería (test_kafka.py)
├── mobile-tests/
│   ├── page-objects/ # Mapeo de elementos de UI (login_page.py)
│   └── specs/        # Flujos de prueba móviles (test_login.py)
├── docker-compose.yml # Infraestructura local de Kafka/Zookeeper
└── README.md