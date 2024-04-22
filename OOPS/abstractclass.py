from abc import ABC,abstractmethod

class abstract(ABC):
    def abst():
        pass

    def prints():
        print("this is printed from the abstract class")

class news(abstract):
    def abst():
        print("abstract class is implemented")


news.abst()
news.prints()