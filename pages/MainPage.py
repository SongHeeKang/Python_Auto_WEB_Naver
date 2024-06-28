from base.BasePage import BasePage
import pages.PageElements as pe
import utilities.CustomLogger as cl


class MainPage(BasePage):
    def __init__(self, driver, context):
        super().__init__(driver, context)
        self.driver = driver
        self.context = context

    def check_search_field(self):
        BasePage.is_displayed(self, pe.naver_search_field)
        cl.allure_logs("검색 필드 표시 확인")

    def check_account_container(self):
        BasePage.is_displayed(self, pe.account_container)
        cl.allure_logs("프로필 컨테이너 영역 표시 확인")

    def check_login_info_text(self):
        BasePage.is_displayed(self, pe.login_info_text)
        cl.allure_logs("로그인 정보 텍스트 표시 확인")

    def check_login_button(self):
        BasePage.is_displayed(self, pe.login_button)
        cl.allure_logs("로그인 버튼 표시 확인")

    def check_find_id_text(self):
        BasePage.is_displayed(self, pe.login_find_id)
        cl.allure_logs("아이디 찾기 버튼 텍스트 표시 확인")

    def check_find_password_text(self):
        BasePage.is_displayed(self, pe.login_find_password)
        cl.allure_logs("비밀번호 찾기 버튼 텍스트 표시 확인")

    def check_register_text(self):
        BasePage.is_displayed(self, pe.login_register)
        cl.allure_logs("회원가입 버튼 텍스트 표시 확인")

    def click_login_button(self):
        BasePage.click_element(self, pe.login_button)
        cl.allure_logs("로그인 버튼 클릭")

    def check_login_page_logo(self):
        BasePage.is_displayed(self, pe.login_page_logo)
        cl.allure_logs("로그인 페이지 로고 표시 확인")

    def click_cafe_icon(self):
        BasePage.click_element(self, pe.service_icon_type_cafe)
        BasePage.switch_to_window(self, 1)
        cl.allure_logs("카페 아이콘 클릭")
        
    def check_cafe_logo(self):
        BasePage.is_displayed(self, pe.cafe_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.cafe_title)
        cl.allure_logs("카페 로고 표시 - 카페 페이지 접근 확인")

    def click_blog_icon(self):
        BasePage.click_element(self, pe.service_icon_type_blog)
        BasePage.switch_to_window(self, 1)
        cl.allure_logs("블로그 아이콘 클릭")

    def check_blog_logo(self):
        BasePage.is_displayed(self, pe.blog_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.blog_title)
        cl.allure_logs("블로그 로고 표시 - 블로그 페이지 접근 확인")

    def click_shopping_icon(self):
        BasePage.click_element(self, pe.service_icon_type_shopping)
        BasePage.switch_to_window(self, 1)
        cl.allure_logs("쇼핑 아이콘 클릭")

    def check_shopping_logo(self):
        BasePage.is_displayed(self, pe.shopping_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.shopping_title)
        cl.allure_logs("쇼핑 로고 표시 - 쇼핑 페이지 접근 확인")

    def click_news_icon(self):
        BasePage.click_element(self, pe.service_icon_type_news)
        BasePage.switch_to_window(self, 1)
        cl.allure_logs("뉴스 아이콘 클릭")

    def check_news_logo(self):
        BasePage.is_displayed(self, pe.news_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.news_title)
        cl.allure_logs("뉴스 로고 표시 - 뉴스 페이지 접근 확인")

    def click_stock_icon(self):
        BasePage.click_element(self, pe.service_icon_type_stock)
        BasePage.switch_to_window(self, 1)
        cl.allure_logs("주식 아이콘 클릭")

    def check_stock_logo(self):
        BasePage.is_displayed(self, pe.stock_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.stock_title)
        cl.allure_logs("주식 로고 표시 - 주식 페이지 접근 확인")

    def click_real_icon(self):
        BasePage.click_element(self, pe.service_icon_type_real)
        BasePage.switch_to_window(self, 1)
        cl.allure_logs("증권 아이콘 클릭")

    def check_real_logo(self):
        BasePage.is_displayed(self, pe.real_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.real_title)
        cl.allure_logs("증권 로고 표시 - 증권 페이지 접근 확인")

    def click_map_icon(self):
        BasePage.click_element(self, pe.service_icon_type_map)
        BasePage.switch_to_window(self, 1)
        cl.allure_logs("지도 아이콘 클릭")

    def check_map_logo(self):
        BasePage.is_displayed(self, pe.map_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.map_title)
        cl.allure_logs("지도 로고 표시 - 지도 페이지 접근 확인")

    def click_webtoon_icon(self):
        BasePage.click_element(self, pe.service_icon_type_webtoon)
        BasePage.switch_to_window(self, 1)
        cl.allure_logs("웹툰 아이콘 클릭")

    def check_webtoon_logo(self):
        BasePage.is_displayed(self, pe.webtoon_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.webtoon_title)
        cl.allure_logs("웹툰 로고 표시 - 웹툰 페이지 접근 확인")

    def click_weather_link_text(self):
        BasePage.click_element(self, pe.weather_link_text)
        BasePage.switch_to_window(self, 1)
        cl.allure_logs("날씨 링크 텍스트 클릭")

    def check_weather_logo(self):
        BasePage.is_displayed(self, pe.weather_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.weather_title)
        cl.allure_logs("날씨 페이지 이동")
