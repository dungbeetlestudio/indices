import requests
import lxml
import json
import os
from datetime import datetime
import indices_db as db

def gather(id):
    try:
        r = requests.get(f'https://cn.investing.com/common/modules/js_instrument_chart/api/data.php',
            params={
                'chart_type':'area',
                'pair_id': id,       #指数编号
                'pair_id_for_news': id, 
                'pair_interval': 300, #采样间隔，5分钟
                'candle_count': 120, 
                'period':'1-day',    #采样范围，1天内
                'events':'no',
                'volume_series':'no'
            },
            headers={
                'Host': 'cn.investing.com',
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56',
                'X-Requested-With': 'XMLHttpRequest',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://cn.investing.com/indices/shanghai-composite',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Cookie': 'PHPSESSID=46gec1q4g2ol0k2fjln8bmh6n3; geoC=CN; adBlockerNewUserDomains=1612161483; StickySession=id.17140744051.657cn.investing.com; logglytrackingsession=21eb119d-9265-409a-a211-ec6de44217ca; _ga=GA1.2.1501807068.1612161485; _gid=GA1.2.1853720465.1612161485; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1612161485; __gads=ID=19c6c0be20c5654b:T=1612161485:S=ALNI_MaHjImwcCy_k72Uj5aioe0Rdul1qg; adsFreeSalePopUp=3; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2240820%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A27%3A%22%2Findices%2Fshanghai-composite%22%3B%7D%7D%7D%7D; _VT_content_1995735_2=1; __atuvc=1%7C5; __atuvs=6017a341acce1b60000; nyxDorf=MTBmN2QsM2s%2FYD0vMmBlZT5tZiNkYjA0MzI%3D; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1612161859; outbrain_cid_fetch=true'
            })

        val = r.json()
        index_name = val['attr']['symbol']
        
        import re
        time = datetime.fromtimestamp(int(re.search(r'\d+',val['html']['chart_last_update']).group()) / 1000)

        print(f'gather {id}-{index_name} {time.date()}')
        os.makedirs(f'db/indices/{index_name}',exist_ok=True)
        index_data = []

        for timestamp,index in val['candles']:
            time = datetime.fromtimestamp(timestamp / 1000)
            index_data.append([time.strftime('%Y-%m-%d %H:%M:%S'),index])
        with open(f'db/indices/{index_name}/{time.date()}.json','w') as f:
            json.dump(index_data,f,indent=4,ensure_ascii=False)
    except Exception as e:
        print(e)
        pass

from multiprocessing import Process
if __name__ == '__main__':
    for id in db.ids:
        Process(target=gather,args=[id]).start()