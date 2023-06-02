import lib.lib


class MyLibrary(lib.lib.Base):
    # 通过继承可以改写2、4的内容
    def step2(self):
        return True

    def step4(self):
        print("App step4()")


a = MyLibrary()
lib.lib.run(a)
