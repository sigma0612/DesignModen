from abc import abstractmethod


class Library:
    # 定义抽象类
    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass

    @abstractmethod
    def step4(self):
        pass

    @abstractmethod
    def step5(self):
        pass


def run(lib: Library):
    # template核心：一个操作中的算法的骨架（run）稳定，子类不改变run中的结构即可重写该算法的某些特定步骤
    lib.step1()

    # 例如对step2的值修改会影响是否执行step3，以及step4的执行内容
    if lib.step2():
        lib.step3()

    for i in range(4):
        lib.step4()

    lib.step5()


class Base(Library):
    # Base中已经实现了Library中的1、3、5接口，表明这些内容是稳定的
    def step1(self):
        print("Base step1()")

    def step3(self):
        print("Base step3()")

    def step5(self):
        print("Base step5()")
