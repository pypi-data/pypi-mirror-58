import os
import re
import zipfile
from urllib import request

from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options


class Check_Chromedriver:
    def __init__(self, path="./chromedriver/"):
        self.BASE_URL = "https://chromedriver.chromium.org/"
        self.driver_mother_path = path
        self.driver_path = os.path.join(self.driver_mother_path, "chromedriver.exe")

    def check_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        try:
            cur_path = os.getcwd()
            # print(cur_path)
            raw_version = os.popen(
                "{}/chromedriver/chromedriver -v".format(cur_path)
            ).read()
            version = self.parse_driver_version_from_driver(raw_version)
            read_version = self.read_version()
            if version != read_version:
                return False
            return True
        except Exception:
            return False

    def parse_driver_version_from_driver(self, raw_version):
        p = re.compile("ChromeDriver (.*) .*")
        m = p.search(raw_version)
        return m.group(1)

    def make_dir(self):
        try:
            os.makedirs(self.driver_mother_path)
        except OSError as e:
            if e.errno != 17:
                raise

    def parse_download_URL(self):
        base_req = self.get_to_URL(self.BASE_URL)
        base_soup = BeautifulSoup(base_req.content, "html.parser")

        driver_version = self.parse_driver_version(base_soup)
        download_url = "/".join(
            [
                "https://chromedriver.storage.googleapis.com",
                driver_version,
                "chromedriver_win32.zip",
            ]
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
        href = li[1].select_one("a")["href"]
        version = self.regrex_version(href)
        # https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_win32.zip
        return version

    def regrex_version(self, href):
        p = re.compile(".*path=(.*)/")
        m = p.search(href)
        return m.group(1)

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
        parse_return = self.parse_download_URL()
        down_url = parse_return[0]
        latest_version = parse_return[1]
        download_path = os.path.join(self.driver_mother_path, "chromedriver.zip")
        print("Downloading...")
        request.urlretrieve(down_url, download_path)
        print("Download Complete!")
        self.unzip(download_path)
        self.remove_zip(download_path)
        self.write_version(latest_version)


if __name__ == "__main__":
    cc = Check_Chromedriver()
    cc.main()
