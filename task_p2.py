# продуктивность я высчитал в процентном соотношении: 100% = 40 часов
# зарплаты работников цеха и замены секретарши маленькие из-за того что в задании дано количество часов только за неделю
class Manager:

    def __init__(self, name, num, time, wage):
        self.name = name
        self.num = num
        self.time = time
        self.wage = wage

    def wages(self):
        print(f'Имя - {self.name}, заработная плата - {self.wage}, номер - {self.num}')
        return self.wage

    def productivity(self):
        dct = {f'{self.name}': self.time * 100 / 40}
        return dct


class Secretary(Manager):
    pass


class Seller(Manager):
    def __init__(self, name, num, time, wage, count_of_sales):
        super().__init__(name, num, time, wage)
        self.count_of_sales = count_of_sales

    def wages(self):
        sum_of_wage = 0
        print(f'Имя - {self.name}, заработная плата - {self.wage + 50 * self.count_of_sales}, номер - {self.num}')
        sum_of_wage += (self.wage + 50 * self.count_of_sales)
        return sum_of_wage


class ShopWorker:
    def __init__(self, name, num, time):
        self.name = name
        self.num = num
        self.time = time

    def wages(self):
        sum_of_wage = 0
        count = 0
        for i in self.name:
            print(f'Имя - {i}, заработная плата - {self.time[count] * 100}, номер - {self.num[count]}')
            sum_of_wage += (self.time[count] * 100)
            count += 1
        return sum_of_wage

    def productivity(self):
        dct = {}
        count = 0
        for i in self.time:
            dct[f'{self.name[count]}'] = i * 100 / 40
            count += 1
        return dct


class ReplaceSecretary(Secretary):
    def __init__(self, name, num, time):
        super().__init__(name, num, time, wage=0)

    def wages(self):
        print(f'Имя - {self.name}, заработная плата - {self.time * 100}, номер - {self.num}')
        return self.time * 100


def sum_of_wages(*args):
    return print(f'Общая сумма оплаты персонала - {sum(args)}')


def rating(*args):
    dct = {}
    dct_rang = {}
    for i in args:
        for key, value in i.items():
            dct[f'{key}'] = value
    sorted_lst = sorted(dct.values())
    for key, value in dct.items():
        if sorted_lst[len(sorted_lst)-1] == value:
            dct_rang['Самый продуктивный работник'] = key
        elif sorted_lst[0] == value:
            dct_rang['Самый непродуктивный работник'] = key
    return dct_rang


m = Manager(name='Барсбек Канаткулов', num=1, time=18, wage=45000)
sec = Secretary(name='Алымкул Тилекбаев', num=2, time=38, wage=20000)
sel = Seller(name='Айпери Шалымбекова', num=3, time=38, wage=20000, count_of_sales=38)
sh = ShopWorker(name=['Бакыт Рустамов', 'Алтынай Ширинбаева'], num=[4, 5], time=[25, 40])
r = ReplaceSecretary(name='Жанара Рыскулова', num=6, time=33)
sum_of_wages(m.wages(), sec.wages(), sel.wages(), sh.wages(), r.wages())
print(rating(m.productivity(), sec.productivity(), sel.productivity(), sh.productivity(), r.productivity()))