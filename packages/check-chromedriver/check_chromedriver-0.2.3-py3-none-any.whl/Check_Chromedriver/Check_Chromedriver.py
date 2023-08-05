import os
import re
import zipfile
from urllib import request
import platform

from bs4 import BeautifulSoup
import requests


class Check_Chromedriver:
    def __init__(self, path="./chromedriver/"):
        self.os_name = self.check_os()
        self.BASE_URL = "https://chromedriver.chromium.org/"
        self.driver_mother_path = path
        temp = self.parse_download_URL()
        self.down_url = temp[0]
        self.new_version = temp[1]

    def check_os(self):
        return platform.system()

    def parse_download_URL(self):
        if self.os_name == "Linux":
            down_name = "chromedriver_linux64.zip"
        else:
            down_name = "chromedriver_win32.zip"
        base_req = self.get_to_URL(self.BASE_URL)
        base_soup = BeautifulSoup(base_req.content, "html.parser")

        driver_version = self.parse_driver_version(base_soup)
        download_url = "/".join(
            ["https://chromedriver.storage.googleapis.com", driver_version, down_name,]
        )
        return download_url, driver_version

    def get_to_URL(self, url):
        req = requests.get(url)
        if req.status_code == 200 and req.ok:
            return req
        else:
            print("request error")

    def parse_driver_version(self, soup):
        # print(soup)
        li = soup.select(".sites-layout-tile.sites-tile-name-content-1 > div li")
        href = li[0].select_one("a")["href"]
        version = self.regrex_version(href)
        # https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_win32.zip
        return version

    def regrex_version(self, href):
        p = re.compile(".*path=(.*)/")
        m = p.search(href)
        return m.group(1)

    def check_driver(self):
        try:
            cur_path = os.getcwd()
            read_version = self.read_version()
            if self.new_version != read_version:
                return False
            return True
        except Exception:
            return False

    def make_dir(self):
        try:
            os.makedirs(self.driver_mother_path)
        except OSError as e:
            if e.errno != 17:
                raise

    def unzip(self, download_path):
        try:
            with zipfile.ZipFile(download_path) as zf:
                zf.extractall(path=self.driver_mother_path)
        except Exception as e:
            print(e)

    def remove_zip(self, download_path):
        os.remove(download_path)

    def write_version(self, latest_version):
        with open(self.driver_mother_path + "/version.txt", "wt") as f:
            f.write(latest_version)

    def read_version(self):
        with open(self.driver_mother_path + "/version.txt", "rt") as f:
            result = f.read()
        return result

    def main(self):
        if self.check_driver():
            # print chromedriver version
            return
        self.make_dir()
        download_path = os.path.join(self.driver_mother_path, "chromedriver.zip")
        print("Downloading...")
        request.urlretrieve(self.down_url, download_path)
        print("Download Complete!")
        self.unzip(download_path)
        self.remove_zip(download_path)
        self.write_version(self.new_version)


if __name__ == "__main__":
    cc = Check_Chromedriver()
    cc.main()
    # print(cc.check_os())
