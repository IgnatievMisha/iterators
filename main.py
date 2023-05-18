#example1
lst=[1,2,3,4,5,6,6]
print(iter(lst))



#example2
class MyIterator():
    def __init__(self, data):
        self.data=data
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.data):
            raise StopIteration
        value=self.data[self.index]
        self.index+=1
        return value
for num in MyIterator(lst):
    print(num)


#example3
def my_generator(data):
    for item in data:
        yield item

for num in my_generator(lst):
    print(num)



#example4
def calc():
    def add(a, b):
        return a+b
    def sub(a, b):
        return a-b
    def mult(a, b):
        return a*b
    def div(a, b):
        return a/b
    return add, sub, mult, div
add, sub, mult, div = calc() #zamikannya
print(div(3, 1))