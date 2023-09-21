import sqlite3

connect = sqlite3.connect("cars.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
                   id INTEGER PRIMARY KEY,
                   number TEXT,
                   mark VARCHAR(255),
                   model VARCHAR(255),
                   year INTEGER,
                   description TEXT,
                   status TEXT)""")


class Car:
    def __init__(self):
        self.number = None
        self.mark = None
        self.model = None
        self.year = 0
        self.description = None
        self.status = None
    
    def add_car(self, number, mark, model, year, description, status):
        self.number = number
        self.mark = mark
        self.model = model
        self.year = year
        self.description = description
        self.status = status
        cursor = connect.cursor()
        cursor.execute(f"""INSERT INTO cars(number, mark, model, year, description, status) VALUES ('{self.number}', '{self.mark}', '{self.model}', {self.year}, '{self.description}', '{self.status}')""")
        connect.commit()
        print(f"Автомобиль {self.model} успешно принят!")
    def info(self):
        cursor.execute("""
                       SELECT * FROM cars
                       """)
        cars = cursor.fetchall()
        return cars
    def info_obs(self):
            cursor.execute('''
            SELECT * FROM cars
            WHERE status = 'В ремонте'
        ''')
            cars = cursor.fetchall()
            if cars == "":
                print("_________________ Список пуст _________________")
            else:
                return cars
    def info_finish(self):
            cursor.execute('''
            SELECT * FROM cars
            WHERE status = 'Завершен'
        ''')
            cars = cursor.fetchall()
            if cars == "":
                print("_________________ Список пуст _________________")
            else:
                return cars
    
    def update(self):
        car_id = int(input("Введите ID автомобиля для обновления: "))
        mark = input("Новая марка автомобиля: ")
        model = input("Новый модель автомобиля: ")
        year = int(input("Год выпуска: "))
        number = input("Новый номер авто: ")
        description = input("Информация об авто (Причина поломки): ")
        status = input("Статус: 1 - Принят, 2 - В ремонте, 3 - Завершен ")
        if status == "1":
            cursor.execute("""UPDATE cars SET mark = ?, model = ?, year = ?, number = ?, description = ?, status = ?
                           WHERE id = ?""", (mark, model, year, number, description, 'Принят', car_id))
            connect.commit()
        elif status == "2":
            cursor.execute("""UPDATE cars SET mark = ?, model = ?, year = ?, number = ?, description = ?, status = ?
                           WHERE id = ?""", (mark, model, year, number, description, 'В ремонте', car_id))
            connect.commit()
        elif status == "3":
            cursor.execute("""UPDATE cars SET mark = ?, model = ?, year = ?, number = ?, description = ?, status = ?
                           WHERE id = ?""", (mark, model, year, number, description, 'Завершен', car_id))
            connect.commit()
        else:
            cursor.execute('''
        UPDATE cars
        SET mark = ?, model = ?, year = ?, number = ? description = ?, status = ?
        WHERE id = ?
        ''', (self.mark, self.model, self.year, self.number, self.description, self.status, car_id))
        connect.commit()

    def main(self):
        while True:
            command = input("1 - Регистрация авто, \n2 - информация об автомобилей, \n3 - Обновить данные, \n4 - Просмотр списка всех автомобилей на обслуживании, \n5 - Готовы к выдаче, \n6 - Выход:  ")
            
            if command == '1':
                mark = input("Марка автомобиля: ")
                model = input("Модель автомобиля: ")
                year = int(input("Год выпуска: "))
                number = input("Номер авто: ")
                description = input("Информация об авто (Причина поломки): ")
                status = input("Статус: 1 - Принят, 2 - В ремонте, 3 - Завершен ")
                if status == "1":
                    self.add_car(number, mark, model, year, description, 'Принят')
                elif status == "2":
                    self.add_car(number, mark, model, year, description, 'В ремонте')
                elif status == "3":
                    self.add_car(number, mark, model, year, description, 'Завершен')
            elif command == "2":
                for i in car.info():
                    print(f'\n<------------------------ ID: {i[0]} ---------------------->')
                    print(f'_____________________ Марка: {i[2]} _____________________')
                    print(f'_____________________ Модель: {i[3]} _____________________')
                    print(f'_____________________ Год выпуска: {i[4]} _____________________')
                    print(f'_____________________ Номер авто: {i[1]} _____________________')
                    print(f'_____________________ Описание: {i[5]} _____________________')
                    print(f'_____________________ Статус: {i[6]} _____________________')
            elif command == "3":
                    self.update()
            elif command == "4":
                for i in self.info_obs():
                    print(f'\n<------------------------ ID: {i[0]} ---------------------->')
                    print(f'_____________________ Марка: {i[2]} _____________________')
                    print(f'_____________________ Модель: {i[3]} _____________________')
                    print(f'_____________________ Год выпуска: {i[4]} _____________________')
                    print(f'_____________________ Номер авто: {i[1]} _____________________')
                    print(f'_____________________ Описание: {i[5]} _____________________')
                    print(f'_____________________ Статус: {i[6]} _____________________')
            elif command == "5":
                for i in self.info_finish():
                    print(f'\n<------------------------ ID: {i[0]} ---------------------->')
                    print(f'_____________________ Марка: {i[2]} _____________________')
                    print(f'_____________________ Модель: {i[3]} _____________________')
                    print(f'_____________________ Год выпуска: {i[4]} _____________________')
                    print(f'_____________________ Номер авто: {i[1]} _____________________')
                    print(f'_____________________ Описание: {i[5]} _____________________')
                    print(f'_____________________ Статус: {i[6]} _____________________')
            elif command == "6":
                print("Все данные сохранены!")
                cursor.close()
                break
            else:
                print("Выберите из списка: ")
                return self.main()

car = Car()
car.main()