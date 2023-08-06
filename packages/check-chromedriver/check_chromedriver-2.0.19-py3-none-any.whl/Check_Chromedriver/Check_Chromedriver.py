import os
import re
import zipfile
from urllib import request
import platform
import datetime

from bs4 import BeautifulSoup
import requests

try:
    from libs import deal_parse, deal_reg, deal_zip, deal_txt
except Exception:
    from Check_Chromedriver.libs import deal_parse, deal_reg, deal_zip, deal_txt


def check_os():
    return platform.system()


def compare_driver():
    try:
        driver_ver = deal_txt.read_version(driver_mother_path)
        driver_ver_code = deal_reg.reg_version_code(driver_ver)
        print("chromedriver_ver : {}".format(driver_ver))
        if driver_ver_code == browser_ver_code:
            return True
    except FileNotFoundError:
        pass


def check_browser_ver():
    try:
        ver_path = "C:/Program Files (x86)/Google/Chrome/Application"
        for i in os.listdir(ver_path):
            if deal_reg.is_version(i):
                return i
    except Exception:
        print("You do not have Chrome browser.")


def make_dir():
    try:
        os.makedirs(driver_mother_path)
    except OSError as e:
        if e.errno != 17:
            raise


def main():
    if compare_driver():
        # print chromedriver version
        return
    make_dir()
    temp = deal_parse.parse_download_URL(browser_ver_code)
    down_url = temp[0]
    new_version = temp[1]
    download_path = os.path.join(driver_mother_path, "chromedriver.zip")
    print("Chromedriver does not match your Chrome browser version. Downloading...")
    request.urlretrieve(down_url, download_path)
    print("Download Complete!")
    deal_zip.unzip(driver_mother_path, download_path)
    deal_zip.remove_zip(download_path)
    deal_txt.write_version(driver_mother_path, new_version)


driver_mother_path = "./chromedriver/"

if not os.path.isfile("./chromedriver/chromedriver.exe"):
    os.rmdir("./chromedriver/")

browser_ver = check_browser_ver()
print("chromebrowser_ver : {}".format(browser_ver))
browser_ver_code = deal_reg.reg_version_code(browser_ver)

if __name__ == "__main__":
    # now = datetime.datetime.now()
    main()
    # now2 = datetime.datetime.now()
    # print(now2 - now)

