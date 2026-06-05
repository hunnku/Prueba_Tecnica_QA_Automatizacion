# 🤖 Bitácora de Uso de Inteligencia Artificial (AI Usage)

Durante el desarrollo de esta prueba técnica, se utilizó la inteligencia artificial de **Gemini** bajo un enfoque de *Pair Programming* (programación en pareja), actuando como mentor técnico para la estructuración de la arquitectura, resolución de problemas (troubleshooting) y validación estricta de requisitos.

A continuación, se detallan los casos de uso específicos y los prompts clave utilizados en el proceso:

## 1. Estructuración Inicial de la Arquitectura
Para garantizar desde el día uno que el proyecto tuviera una jerarquía de carpetas escalable y profesional, se utilizó a Gemini para generar el esqueleto inicial del proyecto.

**Prompt utilizado:**
> *"con base en la siguiente esquema genera los archivos necesarios para abarcar todo el proyecto tecnico qa de automatizacion el cual se llevara acabo con python por el momento el contenido de los documentos van vacios"*

**Resultado:** Se generó la estructura base separando lógicamente las carpetas `api-tests`, `event-tests` y `mobile-tests`, sentando las bases para el trabajo modular.

## 2. Refactorización y Aplicación Estricta del Patrón POM
Durante el desarrollo del flujo End-to-End de compra (`test_buy.py`), el código comenzó a concentrarse en un solo archivo masivo (antipatrón *God Object*). Se le pidió a la IA que analizara los localizadores y separara la lógica para cumplir estrictamente con el patrón Page Object Model (POM).

**Prompt utilizado:**
> *"en la aplicacion buy_page.py estoy armando un proceso pero necesito que se conserve la logica de trabajo POM asi que separa el contenido para cada pantalla, esta comentado que id voy a usar por cada uno, separalos en archivos"*

**Resultado:** La IA ayudó a segmentar el flujo en 6 archivos independientes (`catalog_page.py`, `product_page.py`, `cart_page.py`, etc.), mejorando drásticamente la mantenibilidad y limpieza del código.

## 3. Resolución de Problemas (Troubleshooting de Infraestructura)
Uno de los mayores retos enfrentados durante la automatización móvil fue el manejo del ciclo de vida de la aplicación. 
* **El Problema:** Al ejecutar el test de Login, todo funcionaba correctamente, pero al intentar ejecutar la prueba de compra inmediatamente después, la aplicación se cerraba de forma abrupta en el emulador.
* **La Solución:** Se consultó a la IA sobre este comportamiento, y ayudó a identificar que se trataba de un conflicto con las *Capabilities* de Appium (específicamente el manejo del estado con `dontStopAppOnReset` y el cierre de sesión en los bloques `finally`). Esto permitió estabilizar la ejecución de las pruebas garantizando un "estado conocido" al inicio de cada script.

## 4. Auditoría y Validación de Requisitos Técnicos
Antes de dar por finalizado el proyecto, se utilizó a Gemini como auditor externo para realizar un cruce entre el código desarrollado y el documento PDF de requerimientos de la prueba.

**Prompt utilizado:**
> *"con base en la estructura y contenido del proyecto realiza una compraracion critica de los puntos a tener en cuenta que estan en el documento pdf, realiza una evaluacion y con el resultado genera un informa en txt donde mencione todos los hayasgos prositivos, negativos y faltantes"*

**Resultado:** Esta auditoría permitió identificar pequeños detalles faltantes, garantizando así un 100% de cumplimiento frente a la rúbrica de evaluación.

---
**Conclusión:** La integración de IA en este proyecto no se utilizó para generar código a ciegas, sino como una herramienta de validación de arquitectura, cumplimiento de requerimientos y optimización de flujos de trabajo, reflejando las habilidades analíticas esperadas en un rol Senior de QA Automation.