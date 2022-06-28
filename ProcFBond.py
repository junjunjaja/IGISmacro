import c as const

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime
from typing import List, Dict
import time


class FBond:
    def __init__(self):
        # initialize selenium
        chrome = webdriver.ChromeOptions()
        chrome.add_experimental_option(
            'useAutomationExtension',
            False
        )
        # open chrome browser
        self.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome
        )

    def browse(self):
        self.browser.get(const.SHINHAN_FIN)
        time.sleep(5)

    @staticmethod
    def process_rows(row: str) -> Dict:
        columns = ["date", "CD91D", "FB6M", "FB1Y", "FB3Y", "KR3Y"]
        r = row.split(' ')
        res = {
            "date": r[0],
            "data": list()
        }
        for k, v in zip(columns[1:], r[1:]):
            res["data"].append({k: v})
        return res

    def search_rows(self) -> Dict:
        r = self.browser.find_element(
            by=By.XPATH,
            value=const.T
        )
        return self.process_rows(r.text)

    def run(self):
        self.browse()
        d = self.search_rows()
        print(d)  # result file


if __name__ == "__main__":
    fb = FBond()
    fb.run()
