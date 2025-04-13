# Parent class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Encapsulated attribute

    # Public method
    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    # Public method
    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    # Encapsulation: Getter method
    def get_storage(self):
        return self.__storage

    # Encapsulation: Setter method
    def set_storage(self, storage):
        if storage > 0:
            self.__storage = storage
        else:
            print("Invalid storage size!")

# Child class inheriting from Smartphone
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_color):
        super().__init__(brand, model, storage)
        self.strap_color = strap_color

    # New method for the child class
    def track_steps(self, steps):
        print(f"{self.brand} {self.model} has tracked {steps} steps today!")

    # Polymorphism: Overriding method
    def make_call(self, number):
        print(f"{self.brand} Smartwatch is calling {number} via Bluetooth...")

        # Create objects
phone = Smartphone("Samsung", "Galaxy S21", 128)
watch = Smartwatch("Apple", "Watch Series 6", 32, "Black")

# Test methods
phone.make_call("0712345678")
phone.send_message("0712345678", "Hello there!")
print(f"Phone storage: {phone.get_storage()} GB")

watch.make_call("0798765432")
watch.track_steps(5000)
print(f"Watch strap color: {watch.strap_color}")
print(f"Watch storage: {watch.get_storage()} GB")