from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

import time

travel = 'https://commons.wikimedia.org/w/index.php?title=Special:ListFiles&limit=500&user=Designermadsen'
home = 'https://commons.wikimedia.org/wiki/Main_Page'


red_url = 'https://commons.wikimedia.org/wiki/'
lengthOfRed = len(red_url)

Found = []


def print_result():
    global Found, lengthOfRed

    print('size:')
    print(len(Found))

    for e in Found:
        print(e[lengthOfRed:])


def is_in_found( value ):
    global Found

    for e in Found:
        if str(e) == str(value):
            return True

    return False


def file_format_png(link):
    StrVal = str(link).lower()

    if '.png' in StrVal:
        return True

    return False


def file_format_jpeg(link):
    StrVal = str(link).lower()

    if '.jpeg' in StrVal:
        return True

    if '.jpg' in StrVal:
        return True

    return False


def only_file(link):
    StrVal = str(link).lower()

    if 'file:' in StrVal:
        return True

    return False


def find_links(driver):
    global lengthOfRed, Found
    found_elements = driver.find_elements(By.TAG_NAME, 'a')

    for e in found_elements:
        href = e.get_attribute('href')

        if not href is None:
            if only_file(href):
                sliced = str(href)

                if not is_in_found( sliced ):
                    Found.append( sliced )


def main():
    global travel

    DriverService = Service(ChromeDriverManager().install())
    Driver = webdriver.Chrome(service=DriverService)

    Driver.get(travel)
    stop = False

    while not stop:
        found = Driver.find_elements(By.TAG_NAME, 'a')

        find_links(Driver)
        time.sleep(5)

        # Get State
        for eF in found:
            if eF.get_attribute( 'class' ) == 'oo-ui-buttonElement-button':
                if eF.text == 'Next page':
                    if eF.get_attribute('aria-disabled') == 'true':
                        stop = True
                        break
                    else:
                        eF.click()
                        break

    print_result()



if __name__ == '__main__':
    main()