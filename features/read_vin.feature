Feature: Read VIN from ECU

  Scenario: Read VIN using ReadDataByIdentifier
    Given the ECU is in default session
    When I request the VIN using DID F190
    Then the VIN should be returned correctly
