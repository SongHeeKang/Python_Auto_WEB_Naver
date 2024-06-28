from behave import when, then


@then('네이버 날씨 홈 탭이 표시된다.')
def step_impl(context):
    context.wp.check_weather_home_tap()


@then('네이버 날씨 예보비교 탭이 표시된다.')
def step_impl(context):
    context.wp.check_weather_compare_tap()


@then('네이버 날씨 미세먼지 탭이 표시된다.')
def step_impl(context):
    context.wp.check_weather_air_tap()


@then('네이버 날씨 지도 탭이 표시된다.')
def step_impl(context):
    context.wp.check_weather_map_tap()