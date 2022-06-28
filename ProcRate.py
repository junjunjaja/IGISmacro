import c as const

import pandas as pd
import requests

from typing import List, Dict
from datetime import datetime, timedelta


class Koribor:
    def __init__(self):
        self.ctx = self.get_html()

    @staticmethod
    def get_html() -> str:
        r = requests.get(const.KFB_KORIBOR)
        res = r.content.decode('utf-8', 'ignore')
        r.close()
        return res  # although detected as utf-8, it raise error

    def parse_html(self) -> List:
        # read off "제일 최근 공시"
        yst = datetime.now() - timedelta(days=1)
        yst = yst.strftime("%Y-%m-%d")

        # find <td> </td>
        table_start = self.ctx.find(f"<td>{yst}</td>")
        table_ctx = self.ctx[table_start:]
        table_end = table_ctx.find("</tr>")
        table_ctx = self.ctx[table_start : (table_start + table_end)]

        table_ctx = table_ctx.replace("\n", "").replace("\t", "")

        # parse it
        t = table_ctx.split("</td>")
        t = list(map(lambda x: x.replace("<td>", ""), t))
        t = list(map(lambda x: x.rstrip().lstrip(), t))

        return t

    def get_koribor_df(self) -> pd.DataFrame:
        col = ["DATE", "1W", "1M", "2M", "3M", "6M", "12M", "_"]
        d = self.parse_html()
        return pd.DataFrame([d], columns= col)

    def get_koribor_json(self) -> Dict:
        d = self.parse_html()
        col = ["d", "1w", "1m", "2m", "3m", "6m", "12m", "_"]

        res = {
            "date": d[0],
            "data": list()
        }
        for k, v in zip(col[1:], d[1:]):
            if k == "_":
                continue
            res["data"].append({k: v})

        return res


if __name__ == "__main__":
    koribor = Koribor()
    s = koribor.get_koribor_df()
    j = koribor.get_koribor_json()
