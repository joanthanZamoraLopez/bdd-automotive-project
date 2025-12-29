Este proyecto es un ejemplo básico de automatización de pruebas BDD (Behavior Driven Development) utilizando Behave (Cucumber en Python), enfocado en el contexto automotriz.

Simula una prueba funcional donde un tester automatizado valida la lectura del VIN desde una ECU usando el servicio UDS ReadDataByIdentifier (DID F190).

El objetivo es demostrar:

Uso de BDD con Gherkin

Automatización en Python

Estructura profesional de proyecto QA

Buenas prácticas para entornos automotrices

bdd-automotive-project/
│
├── ecu_simulator.py
│
├── features/
│   ├── read_vin.feature
│   └── steps/
│       └── read_vin_steps.py
│
├── requirements.txt
└── README.md
