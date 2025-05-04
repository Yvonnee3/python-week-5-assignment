class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def display_info(self):
        print(f"brand {self.brand}, model {self.model}, storage {self.storage}GB ")

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}")

phone1 = Smartphone("Apple", "iPhone 13 pro max",256)
phone1.display_info()
phone1.make_call("0723478670")



   