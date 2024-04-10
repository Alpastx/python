class Degree:
    def getDegree(self):
        print("I got a degree")

class Postgraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate ")

class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")

post = Postgraduate()
grad = Undergraduate()

post.getDegree()
grad.getDegree()
