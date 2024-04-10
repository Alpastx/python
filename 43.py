class a :
    def display(self, n,c):
        print(f"Name: {n}\nClass: {c}")
    def display(self, c,n):
        print(f"Class: {n}\nName: {c}")
a1 = a()
a1.display("alp", 10)
a1.display(10, "alp")