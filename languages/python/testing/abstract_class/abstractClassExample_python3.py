from abc import  ABC,abstractmethod
 
class AbstractClassExample(ABC):  # extend from ABC is compulsary
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass

class derivedClass(AbstractClassExample):
    
    # def __init__(self,value):
    #     super.__init__(value)
    def do_something(self):
        return self.value + 42    


x = derivedClass(10)
print (x.do_something())