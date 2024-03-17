import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import undetected_chromedriver as uc
import asyncio
from bbbb import check
import os
import shutil


def do_click_robot(driver, timeout):
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(timeout)
    try:
        # driver.switch_to.frame(0)
        # print("new-window")
        # driver.window_new()
        # # driver.execute_script("window.open('');")
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
        # driver.get(
        #     "https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-N3JQxh1vIZe9tECk0Pg")
        #
        # time.sleep(timeout)
        print("checkbox")
        driver.switch_to.frame(0)
        element = WebDriverWait(driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="challenge-stage"]/div/label/input'))
        )
        # element.click()
        # driver.find_element(By.CSS_SELECTOR, 'input["type=checkbox"]').click()
        driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input').click()
        time.sleep(20)
        driver.switch_to.default_content()
        return True
    except:
        driver.switch_to.default_content()
        print("no checkbox")
        return False


def do_click_list_error(driver, timeout):
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "kQAmfF"))
        )
        print("error")
        driver.refresh()
        return True
    except:
        print("no error")
        return False


def do_click(driver, timeout):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "time-slot-19-00"))
    )
    js4 = "arguments[0].scrollIntoView();"
    driver.execute_script(js4, element)
    # element.location_once_scrolled_into_view
    elements = driver.find_elements(By.CLASS_NAME, "time-slot-19-00")
    # driver.execute_script(js4, elements[0])
    time.sleep(1)
    driver.execute_script("arguments[0].click();", elements[0])
    print("点击1")
    # element.click()
    element2 = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ldyyOy"))
    )
    js4 = "arguments[0].scrollIntoView();"
    driver.execute_script(js4, element2)
    time.sleep(1)
    print("点击2")

    elements = driver.find_elements(By.CLASS_NAME, "ldyyOy")
    # driver.execute_script(js4, elements[0])
    time.sleep(1)
    driver.execute_script("arguments[0].click();", elements[0])
    # element2.click()
    time.sleep(3)

    try:

        # element3 = WebDriverWait(driver, timeout).until(
        #     EC.element_to_be_clickable((By.ID, "name"))
        # )
        # print("点击3")
        # element3.send_keys("黃思諭")
        # element4 = WebDriverWait(driver, timeout).until(
        #     EC.element_to_be_clickable((By.ID, "phone"))
        # )
        # print("点击4")
        # element4.send_keys("976347629")

        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "jmEJIc"))
        )
    except:
        driver.refresh()
        return False
    print("点击3")
    js4 = "arguments[0].scrollIntoView();"
    driver.execute_script(js4, element)
    return True
    # time.sleep(3)
    # element = WebDriverWait(driver, timeout).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "sc-hHLeRK"))
    # )
    # print("点击3")
    # js4 = "arguments[0].scrollIntoView();"
    # driver.execute_script(js4, element)


def do_click2(driver, timeout):
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

    # element.location_once_scrolled_into_view
    elements = driver.find_elements(By.CLASS_NAME, "sc-hHLeRK")
    # driver.execute_script(js4, elements[0])
    # time.sleep(1)
    driver.execute_script("arguments[0].click();", elements[0])
    print("点击1")
    # element.click()
    element2 = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "ldyyOy"))
    )
    time.sleep(1)
    print("点击2")
    element2.click()


# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# desired_capabilities = DesiredCapabilities.CHROME
# desired_capabilities["pageLoadStrategy"] = "none"
async def xxx(userinfo_dict, error_count):
    print(1)
    chrome_options = uc.ChromeOptions()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-popup-blocking")
    # chrome_options.add_argument("--profile-directory=Default")
    # chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument("--disable-plugins-discovery")
    # chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument('--no-first-run')
    # chrome_options.add_argument('--no-service-autorun')
    # chrome_options.add_argument('--no-default-browser-check')
    # chrome_options.add_argument('--password-store=basic')
    # chrome_options.add_argument('--remote-debugging-port=13888')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.set_capability('pageLoadStrategy', 'none')
    chrome_options.debugger_address = "127.0.0.1:13888"
    driver = uc.Chrome(options=chrome_options,
                       # executable_path='chromedriver', version_main=103
                       # desired_capabilities=desired_capabilities
                       )
    driver.get(
        "https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-N3JQxh1vIZe9tECk0Pg")

    # driver.set_page_load_timeout(30)
    # driver.maximize_window()

    # driver.minimize_window()
    while True:
        # print(error_count)
        if error_count:
            if 1 in error_count:
                del error_count[1]
            # driver.delete_all_cookies()
            # Open a new window
            print("error_count")
            driver.refresh()
            # if do_click_robot(driver, 10):
            #     continue
            if do_click_list_error(driver, 1):
                continue
            if do_click(driver, 20):
                continue
            # print(f"userinfo_dict:{userinfo_dict}")

        else:
            # Open a new window
            # driver.window_new()
            # # driver.execute_script("window.open('');")
            # driver.close()
            # driver.switch_to.window(driver.window_handles[0])
            # driver.get(
            #     "https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-N3JQxh1vIZe9tECk0Pg")

            try:
                element = WebDriverWait(driver, 2).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "jmEJIc"))
                )
            except:
                print(f"not in finish page")
                # if do_click_robot(driver, 10):
                #     continue
                if do_click_list_error(driver, 1):
                    continue
                if do_click(driver, 30):
                    continue

            element = WebDriverWait(driver, 1000).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "jmEJIc"))
            )
            while True:

                if error_count: break
                if userinfo_dict[1]:
                    # for k, v in userinfo_dict.items():
                    #     if v:
                    element.click()
                    print("点击1")
                    raise Exception(666)
                await asyncio.sleep(0.01)

    # time.sleep(10)

    # print("查找元素")
    #
    # # <button data-cy="book-now-time-slot-box-19-00" class="sc-bZnhIo kRPfep time-slot time-slot-19-00
    # # button data-cy="book-now-action-button" class="sc-hHLeRK ldyyOy py-0 w-full"
    # # <button type="submit" data-cy="submit" class="sc-hHLeRK jmEJIc
    #
    # element = WebDriverWait(driver, 1000).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "time-slot-19-00"))
    # )
    # print("点击1")
    # element.click()
    # element2 = WebDriverWait(driver, 1000).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "ldyyOy"))
    # )
    # print("点击2")
    # element2.click()
    # element3 = WebDriverWait(driver, 1000).until(
    #     EC.element_to_be_clickable((By.ID, "name"))
    # )
    # print("点击3")
    # element3.send_keys("aaa")
    # element4 = WebDriverWait(driver, 1000).until(
    #     EC.element_to_be_clickable((By.ID, "phone"))
    # )
    # print("点击4")
    # element4.send_keys("931212121")
    #
    # # button class time-slot-19-00
    # # button class ldyyOy
    # # button class jmEJIc
    # cookies = driver.get_cookies()
    #
    # print(cookies)
    time.sleep(10000)


ug = 'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 OPR/10.3.2843.400'


def clear_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            else:
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Error deleting {file_path}. Reason: {e}')


async def yyy(userinfo_dict, error_count):
    print(1)
    while True:
        clear_directory(r'D:/tmp/c1')
        time.sleep(5)
        print("update -header")
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--user-data-dir=D:\\tmp\\c1")
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--disable-popup-blocking")
        # chrome_options.add_argument("--profile-directory=Default")
        # chrome_options.add_argument("--ignore-certificate-errors")
        # chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument(f'--user-agent={ug}')
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--proxy-server=127.0.0.1:9090")
        # chrome_options.add_argument('--no-first-run')
        # chrome_options.add_argument('--no-service-autorun')
        # chrome_options.add_argument('--no-default-browser-check')
        # chrome_options.add_argument('--password-store=basic')
        # chrome_options.add_argument('--remote-debugging-port=13888')
        # chrome_options.add_argument(f'--user-agent={ug}')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.set_capability('pageLoadStrategy', 'none')
        # chrome_options.debugger_address = "127.0.0.1:13888"
        # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36
        driver = uc.Chrome(options=chrome_options, user_multi_procs=True,
                           # executable_path='chromedriver', version_main=103
                           # desired_capabilities=desired_capabilities
                           )
        driver.get(
            "https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-N3JQxh1vIZe9tECk0Pg")

        time.sleep(10000)
        while True:
            while True:
                if do_click_robot(driver, 15):
                    driver.refresh()
                    continue
                break
            driver.delete_all_cookies()
            # await asyncio.sleep(1)
            print("check")
            await asyncio.sleep(15)

            if await check():
                break
            else:
                print("refresh")
                driver.refresh()

        driver.close()
        break
        #
        # # driver.set_page_load_timeout(30)
        # # driver.maximize_window()
        # await asyncio.sleep(10000)
    time.sleep(10)
    clear_directory(r'D:/tmp/c1')
