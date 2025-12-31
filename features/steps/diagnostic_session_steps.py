from behave import given, when, then
from uds.uds_client import UdsClient
from behave import given, when, then
from ecu_simulator import ECUSimulator

@given('the ECU is in default session')
def step_given_ecu_default_session(context):
    context.ecu = ECUSimulator()
    context.ecu.set_session("default")

@when('I request the VIN using DID F190')
def step_when_request_vin(context):
    context.response = context.ecu.read_did("F190")

@then('the VIN should be returned correctly')
def step_then_validate_vin(context):
    assert context.response == "1HGBH41JXMN109186"

@given("la ECU está en Default Session")
def step_default_session(context):
    context.uds = UdsClient()
    context.uds.set_default_session()

@given("la ECU está en Extended Session")
def step_extended_session(context):
    context.uds = UdsClient()
    context.uds.set_extended_session()

@when('el tester envía el request UDS "{request}"')
def step_send_request(context, request):
    context.response = context.uds.send_request(request)

@then('la ECU responde con "{expected_response}"')
def step_check_response(context, expected_response):
    assert context.response == expected_response, \
        f"Esperado {expected_response}, obtenido {context.response}"

@then('la ECU responde con datos del DID "{did}"')
def step_check_did(context, did):
    assert did in context.response, \
        f"DID {did} no presente en la respuesta {context.response}"

@then("la ECU responde con seed de seguridad")
def step_check_seed(context):
    assert context.response.startswith("67 01"), \
        f"Respuesta incorrecta: {context.response}"
