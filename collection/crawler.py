import sys
from urllib.request import Request, urlopen
from datetime import datetime


def crawling(
        url='',#주소값 받음
        encoding='utf-8',#인코딩 utf-8로
        proc=lambda html: html, #람다는 마지막값을 꼭 리턴함
        store=lambda html: html,
        err=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):#에러메세지
    try:
        request = Request(url) #주소값
        resp = urlopen(request)

        try:
            receive = resp.read()
            result = store(proc(receive.decode(encoding))) #저장된 결과값을 리턴

            #if store is not None: #저장이 되면 결과값저장
            #    store(result)

        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace') #replace 공백제거?

        return result

    except Exception as e:
        err(e)