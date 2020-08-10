class cat:

    def __init__(self,age,heigt):
        self.age=age
        self.heigt=heigt

    def showage(self):
        print(self.age)

class whitecat(cat):

    def __init__(self,largopelo,age,heigt):
        super().__init__(age,heigt)
        self.largopelo=largopelo

michi = cat(23,123)
#michi.showage()

michiwhite =whitecat(25,34,1231)
michiwhite.showage()