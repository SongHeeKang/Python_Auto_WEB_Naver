# import logging
# import os
# import allure


# def custom_logger(name):
#     """
#     Test_log.log 파일을 reports 디렉토리 하위에 생성하고, 로그 기록을 지원하는 함수
#     :param name:
#     :return:
#     """
#     log_dir = os.path.join(os.getcwd(), "reports")
#     if not os.path.exists(log_dir):
#         os.makedirs(log_dir)

#     log_file = os.path.join(log_dir, "test_error_log.log")

#     formatter = logging.Formatter(
#         fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
#     )
#     handler = logging.FileHandler(log_file)
#     handler.setFormatter(formatter)

#     logger = logging.getLogger(name)
#     logger.setLevel(logging.DEBUG)
#     logger.addHandler(handler)

#     return logger


# def allure_logs(text):
#     """
#     allure 리포트의 테스트 케이스에 로그 메시지를 기록하는 함수
#     :param text:
#     :return:
#     """
#     with allure.step(text):
#         pass



import inspect
import logging

import allure


def custom_logger():
    # 1.) This is used to get the  class / method name from where this customLogger method is called
    logName = inspect.stack()[1][3]

    # 2.) Create the logging object and pass the logName in it
    logger = logging.getLogger(logName)

    # 3.) Set the Log level
    logger.setLevel(logging.DEBUG)

    # 4.) Create the fileHandler to save the logs in the file under reports folder.
    fileHandler = logging.FileHandler("reports/Logs.log", mode='a')

    # 5.) Set the logLevel for fileHandler
    fileHandler.setLevel(logging.DEBUG)

    # 6.) Create the formatter in which format do you like to save the logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # 7.) Set the formatter to fileHandler
    fileHandler.setFormatter(formatter)

    # 8.) Add file handler to logging
    logger.addHandler(fileHandler)

    #  9.) Finally return the logging object

    return logger


# Allure Report log method

def allure_logs(text):
    with allure.step(text):
        pass