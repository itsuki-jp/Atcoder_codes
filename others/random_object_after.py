class person:
    def __init__( self, FamilyName, FirstName, age, org ):
        self.FamilyName = FamilyName
        self.FirstName = FirstName
        self.age = age
        self.org = org

    def show_info( self ):
        print(f"{self.FamilyName} {self.FirstName}, {self.age}歳 出身地:{self.org}")


p1 = person("Fudai", "Taro", 20, "Osaka")
p2 = person("Ichidai", "Hanako", 21, "Kyoto")
p1.show_info()
p2.show_info()
