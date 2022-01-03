import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By

# load .env variables
load_dotenv()

# Webdriver env
CHROME_WEBDRIVER_PATH = os.getenv('CHROME_WEBDRIVER_PATH')


# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.headless = True # also works


def test_scores_service(app_url):
    """
    test_scores_service - it’s purpose is to test our web service. It will get the application
    URL as an input, open a browser to that URL, select the score element in our web page,
    check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.
    """

    #  Configuration for driver
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH, options=chrome_options)
    # get site's score
    chrome_driver.get(app_url)
    score_xpath = "//*[@id=\"score\"]"
    score = WebDriverWait(chrome_driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, score_xpath)))
    if score:
        score_value = int(chrome_driver.find_element(By.XPATH, score_xpath).text)
        if 1 <= score_value <= 1000:
            return True
    else:
        return False


def main_function():
    """
    main_function to call our tests function. The main function will return -1 as an OS exit
    code if the tests failed and 0 if they passed.
    """
    code = test_scores_service('http://127.0.0.1:5000')
    if code:
        print(0)
        return 0
    else:
        print(-1)
        os.system(exit())
        return -1


if __name__ == "__main__":
    main_function()