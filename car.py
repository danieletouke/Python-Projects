class Car:

    def __init__(self,make,model,year,speed,color):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        self.color = color

    def enjoyment(self):
        print("I love the 0 - 60 in " + self.model + " in " , self.speed ,  " seconds!!!")

    def caution(self):
        print("Please drive responsably\nThanks!!!")

my_new_dream = Car("Lexus", "LFA Successor", 2024,2,"white")

print(my_new_dream.make)
print(my_new_dream.speed)

print(my_new_dream.caution())
print(my_new_dream.enjoyment())

print(type(my_new_dream))