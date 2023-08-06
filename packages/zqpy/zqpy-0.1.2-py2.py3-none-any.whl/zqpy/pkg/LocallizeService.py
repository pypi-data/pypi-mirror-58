from FileService import FileServiceClass
class LocallizeServiceClass(object):
    def __init__(self, path = None):
        self.File = FileServiceClass()
        self.localData = {}
        self.ChangeData(path)

    def ChangeData(self, path=None):
        #filePath = "./Locallize.txt"
        if path!=None:
            filePath = path
        if path != None:
            self.localData = self.File.SpliteContentKV(filePath)
                
    def Get(self, key):
        return self.localData.get(key or "NoLocallize",'{}{}'.format(str(key)," 没有写入到文本"))