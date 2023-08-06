import os
import re
import zipfile
from urllib import request
import platform
import datetime

from bs4 import BeautifulSoup
import requests

from Check_Chromedriver.libs import deal_parse, deal_reg, deal_zip, deal_txt


def check_os():
    return platform.system()


def compare_driver():
    global local_ver
    try:
        read_ver = deal_txt.read_version(driver_mother_path)
        read_ver_code = deal_reg.reg_version_code(read_ver)
        print("chromedriver_ver : {}".format(read_ver))
        if read_ver_code == local_ver_code:
            return True
    except FileNotFoundError:
        pass


def check_local_driver():
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
    temp = deal_parse.parse_download_URL(local_ver_code)
    down_url = temp[0]
    new_version = temp[1]
    download_path = os.path.join(driver_mother_path, "chromedriver.zip")
    print("Chromedriver does not match your Chrome browser version. Downloading...")
    request.urlretrieve(down_url, download_path)
    print("Download Complete!")
    deal_zip.unzip(driver_mother_path, download_path)
    deal_zip.remove_zip(download_path)
    deal_txt.write_version(driver_mother_path, new_version)


# os_name = check_os()
local_ver = check_local_driver()
print("chromebrowser_ver : {}".format(local_ver))
local_ver_code = deal_reg.reg_version_code(local_ver)
driver_mother_path = "./chromedriver/"

if __name__ == "__main__":
    # now = datetime.datetime.now()
    main()
    # now2 = datetime.datetime.now()
    # print(now2 - now)

