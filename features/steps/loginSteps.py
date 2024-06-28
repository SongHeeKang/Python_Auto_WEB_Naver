from behave import *
import base64


@when('"{id}" 및 "{password}" 입력한다.')
def step_impl(context, id, password):
    if id == "<empty>":
        id = ""
    if password == "<empty>":
        password = ""
    context.lp.input_id(id)
    decrypted_password = base64.b64decode(password).decode('utf-8')
    context.lp.input_password(decrypted_password)


@when('로그인 페이지에서 로그인 버튼을 클릭한다.')
def step_impl(context):
    context.lp.click_login_page_button()


@then('로그인에 실패하고 "{error_message}" 표시된다.')
def step_impl(context, error_message):
    context.lp.check_error_message(error_message)