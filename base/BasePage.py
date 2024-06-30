# import os
# import time
# import allure
# import utilities.CustomLogger as log
# import config.config as config
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
# from allure_commons.types import AttachmentType
# from traceback import print_stack

# waitTime = config.WAIT_TIME
# BASE_DIR = os.getcwd()
# logger = log.custom_logger(name=__name__)


# class BasePage:

#     def __init__(self, driver, context):
#         self.driver = driver
#         self.context = context

#     def write_log(self, locator, text):
#         """
#         로그 및 스크린샷을 기록
#         :return:
#         """
#         print_stack()
#         logger.info(locator + text)
#         self.take_screenshot_allure(locator)
#         self.save_screenshot_to_file()

#     def save_screenshot_to_file(self):
#         """
#         웹 페이지의 스크린샷을 저장하고, 이미지 이름 포맷 지정 및 해당 파일 경로를 반환하는 함수
#         이미지는 reports 디렉토리 하위에 모두 저장됨
#         :return:
#         """
#         image_file_name = str(self.context.tags).strip("{}'") + '_' + f'{time.strftime("%Y%m%d_%H%M%S")}' + '.png'
#         image_file_path = os.path.join(BASE_DIR + "/reports", image_file_name)
#         self.context.image_file_path = image_file_path
#         self.driver.save_screenshot(image_file_path)
#         logger.info(f'{image_file_path} : 저장됨')
#         return image_file_path

#     def take_screenshot_allure(self, text):
#         """
#         스크린샷을 저장하고, allure 리포트에 첨부하는 함수
#         :param text:
#         :return:
#         """
#         allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

#     def web_driver_wait(self, locator):
#         """
#         요소가 표시될 때까지 waitTime 만큼 대기하는 함수
#         :param locator:
#         :return:
#         """
#         try:
#             WebDriverWait(self.driver, waitTime).until(
#                 EC.presence_of_element_located((By.XPATH, locator))
#             )
#         except TimeoutException:
#             self.write_log(locator, f" TimeoutException 발생 : 엘리먼트를 최대 {waitTime}초 만큼 기다렸지만 찾을 수 없습니다.")

#     def switch_to_window(self, number):
#         """
#         새 창이 열렸을 때, 해당 윈도우로 포커스
#         :param number:
#         :return:
#         """
#         self.driver.switch_to.window(self.driver.window_handles[number])

#     def highlight(self, element, effect_time, color, border):
#         """
#         엘리먼트 상호작용할 때, 하이라이팅 적용
#         :param element: 포커스 할 요소
#         :param effect_time: 효과 지속 시간
#         :param color: 테두리 효과 컬러 코드
#         :param border: 테두리 굵기
#         :return:
#         """
#         driver = element._parent

#         def apply_style(s):
#             driver.implicitly_wait(waitTime)
#             driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
#         original_style = element.get_attribute('style')
#         apply_style(f"border: {border}px solid {color};")
#         time.sleep(effect_time)
#         if config.PASS_SCREENSHOT is True:
#             self.take_screenshot_allure("")
#         apply_style(original_style)

#     def find_element(self, locator):
#         """
#         엘리먼트가 화면에 표시되는 지 확인하고, 이를 element 변수에 할당하여 반환
#         :param locator:
#         :return:
#         """
#         self.web_driver_wait(locator)
#         try:
#             element = self.driver.find_element(by=By.XPATH, value=locator)
#             self.highlight(element, 0.1, "#FF0000", 5)
#             return element
#         except NoSuchElementException as e:
#             self.write_log(locator, f" NoSuchElementException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 DOM에서 찾을 수 없습니다. 상세 정보 - {e}")
#             assert False

#     def is_displayed(self, locator):
#         """
#         엘리먼트가 화면에 표시되는 지 확인
#         (XPATH 경로를 인자로 받음)
#         :param locator:
#         :return:
#         """
#         self.web_driver_wait(locator)
#         try:
#             element = self.driver.find_element(by=By.XPATH, value=locator)
#             element.is_displayed()
#             self.highlight(element, 0.1, "#FF0000", 5)
#             return True
#         except NoSuchElementException as e:
#             self.write_log(locator, f" NoSuchElementException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 DOM에서 찾을 수 없습니다. 상세 정보 - {e}")
#             assert False
#         except StaleElementReferenceException as e:
#             self.write_log(locator, f" StaleElementReferenceException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트와의 참조가 더 이상 유효하지 않습니다. 상세 정보 - {e}")
#             assert False

#     def click_element(self, locator):
#         """
#         엘리먼트를 찾고, 클릭
#         (XPATH 경로를 인자로 받음)
#         :param locator:
#         :return:
#         """
#         self.web_driver_wait(locator)
#         try:
#             element = self.driver.find_element(by=By.XPATH, value=locator)
#             self.highlight(element, 0.1, "#FF0000", 5)
#             element.click()
#             return True
#         except NoSuchElementException as e:
#             self.write_log(locator, f" NoSuchElementException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 DOM에서 찾을 수 없습니다. 상세 정보 - {e}")
#             assert False
#         except ElementClickInterceptedException as e:
#             self.write_log(locator, f" ElementClickInterceptedException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 클릭할 수 없습니다. 상세 정보 - {e}")
#             assert False
#         except StaleElementReferenceException as e:
#             self.write_log(locator, f" StaleElementReferenceException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트와의 참조가 더 이상 유효하지 않습니다. 상세 정보 - {e}")
#             assert False
#         except ElementNotInteractableException as e:
#             self.write_log(locator, f" ElementNotInteractableException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트는 현재 상호작용할 수 없는 상태입니다. 상세 정보 - {e}")
#             assert False

#     def input_element(self, locator, text):
#         """
#         엘리먼트를 찾고, 데이터 입력
#         (XPATH 경로와 입력할 데이터를 인자로 받음)
#         :param locator:
#         :param text:
#         :return:
#         """
#         self.web_driver_wait(locator)
#         try:
#             element = self.driver.find_element(by=By.XPATH, value=locator)
#             element.send_keys(text)
#             self.highlight(element, 0.1, "#FF0000", 5)
#             return True
#         except NoSuchElementException as e:
#             self.write_log(locator, f" NoSuchElementException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 DOM에서 찾을 수 없습니다. 상세 정보 - {e}")
#             assert False
#         except StaleElementReferenceException as e:
#             self.write_log(locator, f" StaleElementReferenceException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트와의 참조가 더 이상 유효하지 않습니다. 상세 정보 - {e}")
#             assert False
#         except ElementNotInteractableException as e:
#             self.write_log(locator, f" ElementNotInteractableException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트는 현재 상호작용할 수 없는 상태입니다. 상세 정보 - {e}")
#             assert False

#     def get_element_text(self, locator):
#         """
#         locator 의 텍스트를 문자열로 크롤링하는 함수.
#         :param locator:
#         :return:
#         """
#         self.web_driver_wait(locator)
#         try:
#             element = self.driver.find_element(by=By.XPATH, value=locator)
#             text = element.text
#             # self.highlight(element, 0.1, "#FF0000", 5)
#             return text
#         except NoSuchElementException as e:
#             self.write_log(locator, f" NoSuchElementException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트를 DOM에서 찾을 수 없습니다. 상세 정보 - {e}")
#             assert False
#         except StaleElementReferenceException as e:
#             self.write_log(locator, f" StaleElementReferenceException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트와의 참조가 더 이상 유효하지 않습니다. 상세 정보 - {e}")
#             assert False
#         except ElementNotInteractableException as e:
#             self.write_log(locator, f" ElementNotInteractableException 발생 : 지정한 XPATH '{locator}'에 해당하는 엘리먼트는 현재 상호작용할 수 없는 상태입니다. 상세 정보 - {e}")
#             assert False

#     @staticmethod
#     def assert_text(expected, result):
#         """
#         인자로 받은 result 와 expected 가 같은지 비교
#         :param expected: 예상결과
#         :param result:  실제값
#         :return:
#         """
#         assert result == expected, "예상 텍스트(Expected) : " + expected + "\n 실제 텍스트(result) : " + result




import os

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.CustomLogger as log
import config.config as config
import time
from traceback import print_stack

waitTime = config.SELENIUM_WAIT_TIME
BASE_DIR = os.getcwd()
logger = log.custom_logger()


class BasePage:

    def __init__(self,driver,context):
        self.driver = driver
        self.context = context

    def web_driver_wait_presence(self, by_selector, locator):
        try:
            WebDriverWait(self.driver, waitTime).until(
                EC.presence_of_element_located((by_selector, locator))
            )
        except TimeoutException:
            self.write_log(locator, "The element was not found in time")

    def web_driver_wait_clickable(self, by_selector, locator):
        try:
            WebDriverWait(self.driver, waitTime).until(
                EC.element_to_be_clickable((by_selector, locator))
            )
        except TimeoutException:
            self.write_log(locator, "The element was not found in time")
            
    def actionChains(self):
        return ActionChains(self.driver)

    def save_screen_shot_tofile(self):
        image_file_name = str(self.context.tags).strip("{}'") + '_' + f'{time.strftime("%Y%m%d_%H%M%S")}' + '.png'
        image_file_path = os.path.join(BASE_DIR + "/reports", image_file_name)
        self.context.image_file_path = image_file_path
        self.driver.save_screenshot(image_file_path)
        logger.info(f'{image_file_path} saved')
        return image_file_path


    def take_screenshotoallure(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def find_element(self, by_selector, locator):
        self.web_driver_wait_presence(by_selector, locator)
        try:
            element = self.driver.find_element(by=by_selector, value=locator)
            self.highlight(element, 0, "red", 3)
            logger.info(f"Found element with locator: {locator}")
            return element
        except NoSuchElementException:
            self.write_log(locator, "Element Not Found")
            assert False

    def is_displayed(self, by_selector, locator):
        max_retries = 3  # 최대 재시도 횟수
        attempts = 0

        while attempts < max_retries:
            try:
                self.web_driver_wait_presence(by_selector, locator)
                element = self.driver.find_element(by=by_selector, value=locator)
                if element.is_displayed():
                    self.highlight(element, 0, "red", 3)
                    logger.info("Displayed locator value " + locator)
                    return True
                break # 요소 찾으면 탈출
            except NoSuchElementException:
                self.write_log(locator, "No Displayed locator value, retry. ")
                time.sleep(1)
                attempts += 1
            except StaleElementReferenceException:
                self.write_log(locator, "Not Staled locator value, retry. ")
                time.sleep(1)  # 재시도 전에 대기
                attempts += 1  # 재시도 횟수 증가

        if attempts == max_retries:
            self.write_log(locator, f"{attempts}번 재시도했지만 요소를 찾을 수 없습니다.")
            assert False  # 모든 재시도가 실패한 경우

    def is_enabled(self, by_selector, locator):
        self.web_driver_wait_presence(by_selector, locator)
        try:
            element = self.driver.find_element(by=by_selector, value=locator)
            element.is_enabled()
            self.highlight(element, 0, "red", 3)
            logger.info("Enabled locator value " + locator)
            return True
        except NoSuchElementException:
            self.write_log(locator, "No Enabled locator value ")
            assert False

    def click_element(self, by_selector, locator):
        """
        엘리먼트를 클릭하는 메서드
        간헐적으로 클릭하지 못하는 경우, click_element_js 메서드를 이용해 대체 가능
        :param by_selector:
        :param locator:
        :return:
        """
        self.web_driver_wait_clickable(by_selector, locator)
        try:
            element = self.driver.find_element(by=by_selector, value=locator)
            self.highlight(element, 0.1, "red", 3)
            element.click()
            return True
        except NoSuchElementException:
            self.write_log(locator, "Unable to Click with locator value ")
            assert False

    def click_element_js(self, by_selector, locator):
        """
        Selenium 의 click() 메서드를 이용하는 경우, 간헐적으로 클릭하지 못하는 Exception 을 방지하고자 작성한 메서드
        Javascript 을 이용한 클릭 액션 수행
        :param by_selector:
        :param locator:
        :return:
        """
        self.web_driver_wait_clickable(by_selector, locator)
        actions = self.actionChains()
        element = self.driver.find_element(by=by_selector, value=locator)
        actions.move_to_element(element).perform()

    def write_log(self, locator, text):
        '''
        로그와 스크린샷을 기록해준다.
        :param locator:
        :param text: 기록할 메세지
        :return:
        '''
        print_stack()
        logger.info(text + locator)
        self.take_screenshotoallure(locator)
        self.save_screen_shot_tofile()



    def get_element_text(self, by_selector, locator):
        '''
        locator 의 text를 가져온다.
        :param locator:
        :return:
        '''
        text = ''
        self.web_driver_wait_presence(by_selector, locator)
        try:
            element = self.driver.find_element(by=by_selector, value=locator)
            text = element.text
            self.highlight(element, 0, "red", 3)
            return text

        except NoSuchElementException:
            self.write_log(locator, "Unable to locator value " + text)
            assert False

    def get_element_attribute(self, by_selector, locator, value):
        '''
        locator 의 속성값을 가져온다.
        :param locator:
        :param value: 얻어올 value
        :return: attribute 값
        '''
        text = ''
        self.web_driver_wait_presence(by_selector, locator)
        try:
            element = self.driver.find_element(by=by_selector, value=locator)
            text = element.get_attribute(value)
            # self.highlight(element, 0, "red", 3)
            return text

        except NoSuchElementException:
            self.write_log(locator, "Unable to sent key with locator value " + text)
            assert False

    def excute_script_window_open(self):
        self.driver.execute_script('window.open("%s");' % config.FIRESCOUT_PAGE_URL)

    def switch_to_window(self, handle_number):
        '''
        handle_number 로 스위치 한다.
        :param handle_number:
        :return:
        '''
        self.driver.switch_to.window(self.driver.window_handles[handle_number])

    def refresh_page(self):
        self.driver.refresh()
        self.driver.implicitly_wait(5)

    def clear_input_field(self, by_selector, locator):
        self.web_driver_wait_presence(by_selector, locator)
        element = self.driver.find_element(by=by_selector, value=locator)
        element.clear()