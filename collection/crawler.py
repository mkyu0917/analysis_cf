import sys
from urllib.request import Request, urlopen
from datetime import datetime


def crawling(
        url='',#주소값 받음
        encoding='utf-8',#인코딩 utf-8로
        err=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):#에러메세지
    try:
        request = Request(url) #주소값
        resp = urlopen(request)

        try:
            receive = resp.read()
            result = receive.decode(encoding)
        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace')

        return result

    except Exception as e:
        err(e)