class Devices:
    def __init__(self, software, price, hardware, type ):
        self.software = software
        self.price = price
        self.harware = hardware
        self.type = type
class Smartphones(Devices):
    def __init__(self, software, price, hardware, type, pixels):
        Devices.__init__(self, software, price, hardware, type)
        self.pixels = pixels
    def __str__(self):
        return f"{self.software, self.price, self.harware, self.type, self.pixels}"
dev_1 = ("IOS", 1000, "Apple A15 Bionic", "casual", 12)

class Laptop(Devices):
    def __init__(self, software, price, hardware, type, videocard):
        Devices.__init__(self, software, price, hardware, type)
        self.videocard = videocard
    def __str__(self):
        return f"{self.software, self.price, self.harware, self.type, self.videocard}"
dev_2 = ("IOS", 3000, "Apple M1 Pro", "для дома, бизнеса","built-in")

class Ultrabook:
    def __init__(self,weight):
        self.weight = weight

class GamingLP(Laptop, Ultrabook):
    def __init__(self, software, price, hardware, type, videocard,  weight, amountcooler):
        Laptop.__init__(self, software, price, hardware, type)
        Ultrabook. __init__(self,weight)
        self.amountcooler = amountcooler
        return f"{self.software, self.price, self.harware, self.type, self.videocard,  self.weight, self.amountcooler}"
dev_3 =  ("Windows", 1300, "Intel Core i5-11400H", "for games", "discrete", 3.7,3 )
print(dev_1, dev_2, dev_3)



