# 参考资料：https://www.jianshu.com/p/9119c85067e2

class Subject(object):
    def __init__(self):
        self._observers = []

    # observer模式中固定具有的三个函数

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    # 构造函数
    @property
    def data(self):
        return self._data

    # set
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer:
    def update(self, subject):
        print('HexViewer:Subject %s has data 0x%x' % (subject.name, subject.data))


class DecimalViewer:
    def update(self, subject):
        print('DecimalViewer:Subject %s has data %d' % (subject.name, subject.data))


data1 = Data('Data 1')
data2 = Data('Data 2')
view1 = DecimalViewer()
view2 = HexViewer()
data1.attach(view1)
data1.attach(view2)
data2.attach(view1)
data2.attach(view2)

print(u"Setting Data 1 = 10")
data1.data = 10
print(u"Setting Data 2 = 15")
data2.data = 15
print(u"Setting Data 1 = 3")
data1.data = 3
print(u"Setting Data 2 = 5")
data2.data = 5
print(u"Detach HexViewer from data1 and data2.")
data1.detach(view2)
data2.detach(view2)
print(u"Setting Data 1 = 10")
data1.data = 10
print(u"Setting Data 2 = 15")
data2.data = 15
