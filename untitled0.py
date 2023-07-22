class score ():
    def __init__(self):
        self.__score=1
    def showScore (self):
        print(self.__score)
    def updateScore (self):
        self.__score=self.__score +1
        print(self.__score)
        
player=score()
player.score=100
player.showScore()
player.updateScore()
player.updateScore()
        
        