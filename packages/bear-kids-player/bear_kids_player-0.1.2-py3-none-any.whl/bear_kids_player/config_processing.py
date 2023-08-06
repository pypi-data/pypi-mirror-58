# -*- coding: utf-8 -*-
import pandas as pd


def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1",'Ture')

def get_config(path= 'config.csv'):
    df = pd.read_csv(path,encoding='utf-8')
    d = df.set_index('parameter').T.to_dict('list')
    for i in d:
        if d[i][1] == 'double':
            d[i] = float(d[i][0])
        elif d[i][1] == 'list':
            d[i] = list(d[i][0].split(" "))
        elif d[i][1] == 'bool':
            d[i] = str2bool(d[i][0])
        elif d[i][1] == 'string':
            d[i] = str(d[i][0])
    return d



if __name__=="__main__":
    d = get_config()
    print(d)
    # path= 'config.csv'
