import re
from urllib import parse
from bs4 import BeautifulSoup

class Page:
    '''
    页面类
    '''

    CHARSET_PATTERN = r"charset\s*=\s*['\"]?([\w-]+)['\"]?"
    LINK_PATTERN = r"https?://.+"

    def __init__(self, response):
        '''
        通过响应结果初步分析页面
        '''
        self.response = response
        self.data = response.read()
        self.url = response.geturl()
        self.links = None
        self.charset = None
        self.content = None
        self.document = None

    def get_charset(self):
        '''
        获取字符集
        '''
        if None == self.charset:
            content = self.data.decode('ascii', 'ignore')
            m = re.search(self.CHARSET_PATTERN, content, re.M|re.I)
            if None != m:
                self.charset = m.group(1)
        return self.charset

    def get_content(self):
        '''
        获取 HTML 内容
        '''
        if None == self.content:
            charset = self.get_charset()
            self.content = self.data.decode(charset)
        return self.content

    def get_document(self):
        '''
        获取文档 BS4 对象
        '''
        if None == self.document:
            content = self.get_content()
            self.document = BeautifulSoup(content, 'html.parser')
        return self.document

    def get_links(self, pattern=None):
        '''
        获取该页面的链接
        '''
        if None == self.links:
            self.links = []
            document = self.get_document()
            for a in document.find_all('a'):
                href = a.get('href')
                link = parse.urljoin(self.url, href)
                if re.match(self.LINK_PATTERN, link):
                    self.links.append(link)
        if None == pattern:
            return self.links
        return [link for link in self.links if re.match(pattern, link)]
