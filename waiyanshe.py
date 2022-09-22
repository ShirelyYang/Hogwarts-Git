import test_json

from pip._vendor import requests


def getbookid():
    postdata = '{"business_id":"200020","level":0,"name":"","page_no":0,"page_size":500,"pic_book_type":0,"series_id":4}'
    url = 'http://res.nse.unischool.cn/api/resource/picbookmanage/getpicbooklist'
    data = test_json.dumps(test_json.loads(postdata))
    header = {"Content-Type": "application/json","Authorization":"6202871185152ddfae82e99fcb8110cab4c32e12727e9f7fd82edf9fdbe6039b","Scope":"com.fltrp.shzy.web","Host":"res.nse.unischool.cn"}
    r = requests.post(url, headers=header, data=data)
    resu = test_json.loads(r.text)['data']
    print(test_json.loads(r.text))
    for i in range(0,len(resu)):
        id = resu[i]['id']
        print (resu[i])
        with open('/Users/snhao/Downloads/picid.txt', 'a') as f:
            f.write(str(id) + '\n')
        #id = json.loads(resu[i])['id']
    return
getbookid()

def addversion():
    with open('/Users/snhao/Downloads/picid.txt', 'r') as f:
        for line in f.readlines():

            id = line.strip()
            print(id)
            postdata = '{"business_id":"200020","id":"'+id+'"}'
            url = 'http://res.nse.unischool.cn/api/resource/picbookmanage/addpicbookversion'
            header = {"Content-Type": "application/json",
                      "Authorization": "6202871185152ddfae82e99fcb8110cab4c32e12727e9f7fd82edf9fdbe6039b",
                      "Scope": "com.fltrp.shzy.web", "Host": "res.nse.unischool.cn"}
            data = test_json.dumps(test_json.loads(postdata))
            r = requests.post(url, headers=header, data=data)
            resu = test_json.loads(r.text)
            print(resu)