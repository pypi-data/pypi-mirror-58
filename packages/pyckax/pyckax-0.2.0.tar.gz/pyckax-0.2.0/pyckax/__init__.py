from .page import Page
from .work import Work, Worker

class Picker:
    '''
    采集器
    '''

    def __init__(self):
        '''
        '''
        self.able = True
        self.links = {}
        self.targets = []
        self.processes = []

    def set_able(self, able):
        self.able = able

    def add_target(self, link):
        '''
        添加目标链接。
        '''
        if link not in self.links:
            self.links[link] = 0
            self.targets.append(link)
        self.links[link] += 1
        return self

    def pick(self, process):
        '''
        开始采集
        '''
        while self.able and len(self.targets) > 0:
            url = self.targets.pop()
            worker = Worker(process)
            result = worker.work(url)
            if None != result:
                if not result.able:
                    break
                for link in result.links:
                    self.add_target(link)
        return self
