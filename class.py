class Person:

    def __init__(self, name, age, birth=15):
        self.name = name
        self.age = age
        self.birth = birth

    def birth(self, today):
        if self.birth >= today:
            self.age += 1

    def profile(self):
        profile = [self.name, self.age, self.birth]
        print(profile)
        return profile


A = Person("taro", 10, 5)
A.birth(3)
A.profile()
