from behave import *


@then('네이버 검색 필드가 표시된다.')
def step_impl(context):
    context.mp.check_search_field()


@then('프로필 영역이 표시된다.')
def step_impl(context):
    context.mp.check_account_container()


@then('로그인 안내 문구가 표시된다.')
def step_impl(context):
    context.mp.check_login_info_text()


@then('로그인 버튼이 표시된다.')
def step_impl(context):
    context.mp.check_login_button()


@then('"아이디 찾기" 링크 텍스트가 표시된다.')
def step_impl(context):
    context.mp.check_find_id_text()


@then('"비밀번호 찾기" 링크 텍스트가 표시된다.')
def step_impl(context):
    context.mp.check_find_password_text()


@then('"회원가입" 링크 텍스트가 표시된다.')
def step_impl(context):
    context.mp.check_register_text()


@when('로그인 버튼을 클릭한다.')
def step_impl(context):
    context.mp.click_login_button()


@then('로그인 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_login_page_logo()


@when('네이버 카페 메뉴를 클릭한다.')
def step_impl(context):
    context.mp.click_cafe_icon()


@then('네이버 카페 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_cafe_logo()


@when('네이버 블로그 메뉴를 클릭한다.')
def step_impl(context):
    context.mp.click_blog_icon()


@then('네이버 블로그 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_blog_logo()


@when('네이버 쇼핑 메뉴를 클릭한다.')
def step_impl(context):
    context.mp.click_shopping_icon()


@then('네이버 쇼핑 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_shopping_logo()


@when('네이버 뉴스 메뉴를 클릭한다.')
def step_impl(context):
    context.mp.click_news_icon()


@then('네이버 뉴스 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_news_logo()


@when('네이버 증권 메뉴를 클릭한다.')
def step_impl(context):
    context.mp.click_stock_icon()


@then('네이버 증권 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_stock_logo()


@when('네이버 부동산 메뉴를 클릭한다.')
def step_impl(context):
    context.mp.click_real_icon()


@then('네이버 부동산 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_real_logo()


@when('네이버 지도 메뉴를 클릭한다.')
def step_impl(context):
    context.mp.click_map_icon()


@then('네이버 지도 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_map_logo()


@when('네이버 웹툰 메뉴를 클릭한다.')
def step_impl(context):
    context.mp.click_webtoon_icon()


@then('네이버 웹툰 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_webtoon_logo()


@when('네이버 날씨 링크 텍스트를 클릭한다.')
def step_impl(context):
    context.mp.click_weather_link_text()


@then('네이버 날씨 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_weather_logo()
