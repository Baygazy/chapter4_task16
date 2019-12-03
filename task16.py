from random import shuffle

class Soldier:
    liguid_units = []
    liguid_hero_in_soldier = []
    og_units = []
    og_hero_in_soldier = []
    """
        имя, номер и команда задаются
        экземпляром класса
    """
    def __init__(self, name, number, team):
        self.name = name
        self.number = number
        self.team = team
        # print("in Soldier: ", name, number, team)
        if name.lower() == "unit" and team.lower() == "liquid":
            self.liguid_units.append(name)
            self.liguid_units.append(int(number))
            self.liguid_units.append(team)
        elif name.lower() == "unit" and team.lower() == "og":
            self.og_units.append(name)
            self.og_units.append(int(number))
            self.og_units.append(team)
        elif name.lower() != "unit":
            if team.lower() == "liquid":
                self.liguid_hero_in_soldier.append(name)
                self.liguid_hero_in_soldier.append(number)
                self.liguid_hero_in_soldier.append(team)
            else:
                self.og_hero_in_soldier.append(name)
                self.og_hero_in_soldier.append(number)
                self.og_hero_in_soldier.append(team)
        else:
            pass


    """ солдат может следовать за героем """
    def go_to_hero(self):
        print(f"Hero: {self.liguid_hero_in_soldier[0]} number: {self.liguid_hero_in_soldier[1]}")
        print(f"Soldier: {self.liguid_units[0]} number: {self.liguid_units[1]}")

class Hero(Soldier):
    liquid_hero = []
    og_hero = []
    """
        имя, номер и команда задаются
        экземпляром класса
    """
    def __init__(self, name, number, team):
        self.name = name
        self.number = number
        self.team = team
        self.level = 1
        Soldier.__init__(self, name, number, team)
        if team.lower() == "liquid":
            self.liquid_hero.append(name)
            self.liquid_hero.append(int(number))
            self.liquid_hero.append(team)
            self.liquid_hero.append(self.level)
        else:
            self.og_hero.append(name)
            self.og_hero.append(int(number))
            self.og_hero.append(team)
            self.og_hero.append(self.level)
    """
        у героя повышается  уровень
        если длина списка солдат его команды
        больше чем у команды противников
    """
    def level_up(self):
        print("liquid units:", int(len(self.liguid_units)/3))
        print("OG units:", int(len(self.og_units)/3))
        if len(self.liguid_units) > len(self.og_units):
            self.liquid_hero[-1] += 1
        elif len(self.liguid_units) < len(self.og_units):
            self.og_hero[-1] += 1
        else:
            pass
        print("Hero", self.liquid_hero[0], self.liquid_hero[-1], "level (in Liquid)")
        print("Hero", self.og_hero[0], self.og_hero[-1], "level (in OG)")

Axe = Hero('Axe', 1, 'Liquid')
Sven = Hero('Sven', 2, 'OG')

""" Создаются две команды """
team_liquid = []
team_og = []
rendom = [1, 2]
"""
    Случайным образом в разные списки (команды)
    закидываются солдаты
    с номерами и названием команды
"""
for unit in range(10, 20):
    shuffle(rendom)
    if rendom[1] == 1:
        team_liquid.append("unit" + str(-unit) + '-liquid-')
    else:
        team_og.append("unit" + str(-unit) + '-og-')

""" все солдаты вместе с номерами и названиями команд
    объединяются в одну строку str()
"""
liguid_all_units = ""
og_all_units = ""
for unit in team_liquid:
    liguid_all_units += unit
for unit in team_og:
    og_all_units += unit
"""
    в новые списки закидываем всех солдат отдельно
    разделяя символом '-'
"""
liguid_units = [i for i in liguid_all_units.split("-")]
og_units = [i for i in og_all_units.split("-")]
""" удаляяем лишние ковычки
    если они есть
"""
if liguid_units[-1] == "":
    del liguid_units[-1]
if liguid_units[0] == "":
    del liguid_units[0]
if og_units[-1] == "":
    del og_units[-1]
if og_units[0] == "":
    del og_units[0]
"""
    в цикле создаем экземпляр класса Soldier
    и закидываем каждого солдата отдельно
    в каждой итерации
"""
for i in range(int(len(liguid_units)/3)):     # делим на 3 потому что: name, number, team
    if liguid_units:
        unit = Soldier(liguid_units[0], liguid_units[1], liguid_units[2])
        del liguid_units[2], liguid_units[1], liguid_units[0]
for i in range(int(len(og_units)/3)):
    if og_units:
        unit = Soldier(og_units[0], og_units[1], og_units[2])
        del og_units[2], og_units[1], og_units[0]
Axe.level_up()
unit.go_to_hero()

