from behave import *
from base.BasePage import BasePage
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage
from pages.WeatherPage import WeatherPage
import config.config as config

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import WebDriverException

# 브라우저 타입 리스트
browser_type = ["Chrome", "Firefox", "Edge", "Safari"]


@given(f'{browser_type[0]} 브라우저를 통해 NAVER URL에 접속한다.')
def step_impl(context):
    try:
        if not hasattr(context, 'driver'):
            if config.REMOTE_RUN is True:
                remote_run_browser(context)
            else:
                local_run_browser(context)

        context.driver.get(config.BASE_URL)
        context.driver.implicitly_wait(5)
    except WebDriverException:
        print("WebDriverException 예외 발생 : webdriver를 초기화하지 못했습니다.")
    except AttributeError as e:
        print(f"속성 오류 발생 : {e}. 'driver' 속성이 정의되지 않았습니다.")


def local_run_browser(context):
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()
    context.driver = webdriver.Chrome(service=service, options=options)


def remote_run_browser(context):
    options = Options()
    options.set_capability("browserName", "chrome")
    options.add_argument("--start-maximized")
    try:
        context.driver = webdriver.Remote(command_executor=config.SELENIUM_GRID_URL, options=options)
    except Exception as error:
        print(f"{error} 에러 발생")


@given('테스트 환경을 초기화한다.')
def step_impl(context):
    try:
        context.bs = BasePage(context.driver, context)
        context.mp = MainPage(context.driver, context)
        context.lp = LoginPage(context.driver, context)
        context.wp = WeatherPage(context.driver, context)
    except Exception as e:
        print(f"초기화 오류 발생 : {e}. 페이지 및 요소 초기화에 실패했습니다.")
