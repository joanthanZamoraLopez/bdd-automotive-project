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
