# !/usr/bin/python3
# -- coding utf-8 --


class Commodity(object):
    def price(self):
        return 0

    def __repr__(self):
        return "{} price is {}".format(self.__class__.__name__, self.price())


class Candy(Commodity):
    def price(self):
        return 1


class Pencil(Commodity):
    def price(self):
        return 2


class CommodityFactory(object):
    @staticmethod
    def create_commodity(commodity_type):
        if commodity_type == "Candy":
            return Candy()
        if commodity_type == "Pencil":
            return Pencil()


def main():
    candy = CommodityFactory.create_commodity("Candy")
    print(candy)
    pencil = CommodityFactory.create_commodity("Pencil")
    print(pencil)


if __name__ == '__main__':
    main()
