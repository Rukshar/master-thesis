from flatten_json import flatten
import json
import pandas as pd

jsondata = json.load(open('database_final.json'))

dic = jsondata['userProfile'].values()

dic_flattened = (flatten(d) for d in dic)
df = pd.DataFrame(dic_flattened)
print df 
# df.to_csv('testcsv.csv', encoding='utf-8')