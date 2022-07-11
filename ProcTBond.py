import c as const

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime
from typing import List, Dict
import time


class KofiaBond:
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
        self.browser.get(const.KOFIA_BOND_INFO)
        time.sleep(5)

    @staticmethod
    def process_rows(row: str) -> (str, List):
        splitter = ["일", "월", "년"]
        # split rows
        split_candidate = list()
        for sp in splitter:
            split_candidate.append(row.rfind(sp))
        split_with = splitter[
            split_candidate.index(max(split_candidate))
        ]

        space = row.split(split_with)
        return space[-1].rstrip().lstrip().split(' ')  # return only the value

    def search_rows(self) -> Dict:
        dt = datetime.now().strftime("%Y%m%d")
        columns = [
            "TODAYAM", "TODAYPM", "DELTA",
            "YESTERDAY", "YEARHIGH", "YEARLOW"
        ]
        columns_keys = list(const.ASSET.keys())
        res = {
            "date": dt,
            "data": dict()
        }
        for i in range(1, 19):
            r = self.browser.find_element(
                by=By.XPATH,
                value=const.ROW.format(i)
            )
            r = self.process_rows(r.text)

            # input data
            res["data"][columns_keys[i - 1]] = list()
            for k, v in zip(columns, r):
                res["data"][columns_keys[i - 1]].append(
                    {k: v}
                )
        time.sleep(1)
        return res

    @staticmethod
    def process_json(data: dict):
        dt = data['date']
        asset = data['data'].keys()
        result = dict()
        for k in asset:
            result[k.lower()] = [{
                "date": dt,
                "value": float(data['data'][k][1]['TODAYPM'])
            }]
        return result

    def run(self):
        self.browse()
        d = self.search_rows()
        self.browser.close()
        j = self.process_json(d)
        return j


if __name__ == "__main__":
    kb = KofiaBond()
    kb.run()
