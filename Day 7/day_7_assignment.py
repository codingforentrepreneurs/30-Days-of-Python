class Animal():
    noise="grunt"
    size="large"
    hair_color="covered whole body"
    def get_noise(self):
        return self.noise
    def get_size(self,abc):
        return self.size

dog=Animal()
print(dog.get_size("big"))