Feature: Servicios UDS básicos sobre CAN

  Background:
    Given la ECU está en Default Session


  Scenario: Read VIN using ReadDataByIdentifier
    Given the ECU is in default session
    When I request the VIN using DID F190
    Then the VIN should be returned correctly

  # -------------------------
  # Diagnostic Session Control
  # -------------------------

  Scenario: Cambiar a sesión extendida
    When el tester envía el request UDS "10 03"
    Then la ECU responde con "50 03"

  Scenario: Subfunción inválida en Diagnostic Session
    When el tester envía el request UDS "10 FF"
    Then la ECU responde con "7F 10 12"

  # -------------------------
  # ECU Reset
  # -------------------------

  Scenario: ECU Reset en sesión extendida
    Given la ECU está en Extended Session
    When el tester envía el request UDS "11 01"
    Then la ECU responde con "51 01"

  Scenario: ECU Reset no permitido en Default Session
    When el tester envía el request UDS "11 01"
    Then la ECU responde con "7F 11 7E"

  # -------------------------
  # Read Data By Identifier
  # -------------------------

  Scenario: Leer DID VIN correctamente
    When el tester envía el request UDS "22 F1 90"
    Then la ECU responde con datos del DID "F1 90"

  Scenario: Leer DID no soportado
    When el tester envía el request UDS "22 AA BB"
    Then la ECU responde con "7F 22 31"

  # -------------------------
  # Write Data By Identifier
  # -------------------------

  Scenario: Escritura de DID sin seguridad
    When el tester envía el request UDS "2E F1 91 01"
    Then la ECU responde con "7F 2E 33"

  # -------------------------
  # Security Access
  # -------------------------

  Scenario: Solicitar seed de seguridad
    When el tester envía el request UDS "27 01"
    Then la ECU responde con seed de seguridad

  Scenario: Enviar key incorrecta
    When el tester envía el request UDS "27 02 00 00"
    Then la ECU responde con "7F 27 35"

  # -------------------------
  # Timing
  # -------------------------

  Scenario: Respuesta pendiente por procesamiento largo
    When el tester envía el request UDS "31 01 FF 00"
    Then la ECU responde con "7F 31 78"
