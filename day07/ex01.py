class Car():
    def carInfo(self, model, year, company, smog, oilPrice, oilName):
        self.model = model
        self.year = year
        self.company = company
        self.smog = smog
        self.oilPrice = oilPrice
        self.oilName = oilName
        return print(f"모델명 :{self.model}, 연식: {self.year}, 제조사 : {self.company}, \n배기량 :{self.smog}, 연비 : {self.oilPrice}, 연료 : {self.oilName}")


car1 = Car()
car1.carInfo("베뉴", "2022", "현대", "1598", "13.7", "가솔린")
