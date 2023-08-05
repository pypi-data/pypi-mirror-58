import re
from urllib import request
from .page import Page

class Work:
    '''
    工作
    '''

    def __init__(self):
        '''
        '''
        self.able = True
        self.links = []

    def set_able(self, able):
        '''
        '''
        self.able = able

    def add_link(self, link):
        '''
        添加链接
        '''
        self.links.append(link)


class Worker:
    '''
    作业器
    '''

    def __init__(self, method):
        '''
        '''
        self.method = method

    def work(self, url):
        '''
        作业，获取页面内容并调用处理程序。
        '''
        try:
            with request.urlopen(url) as response:
                page = Page(response)
                return self.method(page)
        except Exception as e:
            print(e)



