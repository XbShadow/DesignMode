
# https://www.runoob.com/design-pattern/singleton-pattern.html


# 1. 闭包方式
def singleton(cls):
    instance = {}

    def get_instance(*arg, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*arg, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class Pool(object):
    def __new__(cls, *args, **kwargs):
        print("new pool")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print("init pool")


# 类自身实现
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# 继承单例类
class Bus(Singleton):
    pass


if __name__ == '__main__':
    # 闭包
    print(Pool == Pool)
    # 类自身实现
    print(Singleton() == Singleton())
    # 继承单例类
    print(Bus() == Bus())
