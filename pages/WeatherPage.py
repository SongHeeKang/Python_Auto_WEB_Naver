from base.BasePage import BasePage
import pages.PageElements as pe
import utilities.CustomLogger as cl


class WeatherPage(BasePage):
    def __init__(self, driver, context):
        super().__init__(driver, context)
        self.driver = driver
        self.context = context

    def check_weather_home_tap(self):
        BasePage.is_displayed(self, pe.weather_home_tap)
        text = BasePage.get_element_text(self, pe.weather_home_tap)
        # BasePage.assert_text("홈", text)
        # cl.allure_logs(f"네이버 날씨 페이지 - {text} 탭 표시 확인")
        title = self.driver.title
        BasePage.assert_text(title, pe.weather_title)
        cl.allure_logs(f"네이버 날씨 페이지 - 탭 표시 확인")

    def check_weather_compare_tap(self):
        BasePage.is_displayed(self, pe.weather_compare_tap)
        text = BasePage.get_element_text(self, pe.weather_compare_tap)
        BasePage.assert_text("예보비교", text)
        cl.allure_logs(f"네이버 날씨 페이지 - {text} 탭 표시 확인")

    def check_weather_air_tap(self):
        BasePage.is_displayed(self, pe.weather_air_tap)
        text = BasePage.get_element_text(self, pe.weather_air_tap)
        BasePage.assert_text("미세먼지", text)
        cl.allure_logs(f"네이버 날씨 페이지 - {text} 탭 표시 확인")

    def check_weather_map_tap(self):
        BasePage.is_displayed(self, pe.weather_map_tap)
        text = BasePage.get_element_text(self, pe.weather_map_tap)
        BasePage.assert_text("지도", text)
        cl.allure_logs(f"네이버 날씨 페이지 - {text} 탭 표시 확인")
