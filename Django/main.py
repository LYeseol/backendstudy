# import urllib.request
#
# url ='https://www.google.com'
#
# request = urllib.request.Request(url)
#
# response = urllib.request.urlopen(request)
#
# # html = response.read()
# print(html)
from urllib.request import urlopen
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
    def handle_startendtag(self, tag, attrs):
        if tag!='img':
            return
        if not hasattr(self, 'result'):
            self.result =[]
        for name,value in attrs:
            if name =='src':
                self.result.append(value)


def parse_image(data):
    parser = ImageParser()
    #html parser 상속된 feed
    parser.feed(data)
    #중복 제거
    dataset = set(x for x in parser.result)
    return dataset

def main():
    url ='https://hongong.hanbit.co.kr/%EC%9E%A5%EA%B3%A0django%EC%9D%98-%ED%8A%B9%EC%A7%95%EA%B3%BC-%EC%9E%A5%EA%B3%A0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EC%84%A4%EC%B9%98%ED%8C%8C%EC%9D%B4%EC%8D%AC-3-x-%EB%B2%84%EC%A0%84-%EC%9E%A5/'
    with urlopen(url) as f:
        charset = f.headers.get_params('charset')[1][1]

        data = f.read().decode(charset)

    dataset = parse_image(data)
    print('\n>>>>>>>>>Fetch Images from ', url)
    print('\n'.join(sorted(dataset)))

if __name__ == '__main__':
    main()