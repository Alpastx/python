from multipledispatch import dispatch
#python -m venv 44
#cd 44
#pip install multipledispatch
class Example:
    @dispatch(int)
    def area(self, a):
        return a * a
    
    @dispatch(int, int)
    def area(self, a, b):
        return a * b

obj = Example()
print('Area of square:', obj.area(10))
print('Area of rectangle:', obj.area(10, 20))
