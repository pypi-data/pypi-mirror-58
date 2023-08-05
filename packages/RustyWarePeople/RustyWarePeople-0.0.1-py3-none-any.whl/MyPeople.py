class Person:
    V=2
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def __str__(self):
        return "I am a person with the name " + self.__name

class Rusty(Person):
    
    V=1
    def __init__(self):
        super().__init__('Rusty')
    def __str__(self):
        return "I am a Rusty Coopes."
    def exceptionThrower(self,throwNow):
        if throwNow :
            try:
                raise Exception('This is my exception')
            except Exception as e :
                print(e)
            finally:
                print('finally i am here')


rsc = Rusty()
print(rsc)