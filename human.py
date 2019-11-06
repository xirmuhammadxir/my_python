class Human:
    def __init__(self, new_name='Магомед'):
        self._name = new_name
        print(f'Родился новый человек... {self._name}')
        self._years = 0

    def eating(self):
        print(f"{self._name} ест...")
        
    def sleeping(self):
        print(f"{self._name} спит...")

    def working(self):
        print(f"{self._name} работает...")
        
    def relaxing(self):
        print(f"{self._name} отдыхает...")

    def growing(self):
        print(f"{self._name} отмечает день рождения...")
        self._years +=1

class Life:
    def life(self, human, years=70):
        while years:            
            human.growing()
            human.eating()
            human.sleeping()
            human.working()
            human.relaxing()
            years -= 1
        
petr = Human('Магомед')
life_petr = Life()
life_petr.life(petr)
