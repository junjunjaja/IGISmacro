from ProcRate import Koribor
from ProcTBond import KofiaBond
from ProcFBond import FBond

import json

# selenium crawl
kb = KofiaBond()
kb_data = kb.run()

koribor = Koribor()
s = koribor.get_koribor_df()
j = koribor.get_koribor_json()
koribor_data = koribor.process_json(j)

fb = FBond()
fb_data = fb.run()

# whole data
to_be_json = dict()
to_be_json.update(**kb_data)
to_be_json.update(**koribor_data)
to_be_json.update(**fb_data)

# save it to JSON
with open('./asset/macro.json', 'w') as file:
    json.dump(to_be_json, file)

