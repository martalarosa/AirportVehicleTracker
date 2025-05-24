''' данный код реализует систему для создания и управления различными типами транспортных средств, которые могут быть использованы в аэропорту. 
каждое транспортное средство генерируется со случайными параметрами, такими как объём топлива, дни стоянки, расположение, количество пассажиров и т.д.
программа предоставляет графический интерфейс для фильтрации и сортировки транспортных средств по различным характеристикам.
генерируются случайные данные для различных типов транспортных средств. 
транспортные средства пользователем выборочно фильтруются по всевозможным параметрам и сортируются по выбранным характеристикам.
визуализация данных происходит с помощью графического интерфейса Tkinter. 
в архитектуре реализован паттерн "Итератор" для последовательного перебора и фильтрации транспортных средств с возможностью задания собственных условий обхода. '''

import tkinter as tk
import random
from tkinter import ttk

# класс-итератор
class VehicleIterator:
    def __init__(self, vehicles):
        self._vehicles = vehicles
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._vehicles):
            result = self._vehicles[self._index]
            self._index += 1
            return result
        raise StopIteration

# базовый класс для всех транспортных средств
class Vehicle:
    def __init__(self, type_name, category, fuel_volume=0, days=0, current_day=0, location=0, cargo_weight=0, seats=0, passengers=0, rockets=0, 
                 required_position=0, gas_station=0):
        self.type = type_name   # конкретный тип
        self.category = category   # обобщённый тип
        self.fuel_volume = fuel_volume
        self.days = days
        self.current_day = current_day
        self.location = location
        self.cargo_weight = cargo_weight
        self.seats = seats
        self.passengers = passengers
        self.rockets = rockets
        self.required_position = required_position
        self.gas_station = gas_station

class LightPlane(Vehicle):
    def __init__(self, fuel_volume, days, current_day, location):
        super().__init__("Лёгкий самолёт", "Летательный аппарат", fuel_volume=fuel_volume, days=days, current_day=current_day, location=location)

class CargoPlane(Vehicle):
    def __init__(self, fuel_volume, days, current_day, location, cargo_weight):
        super().__init__("Грузовой самолёт", "Грузовое транспортное средство", fuel_volume=fuel_volume, days=days, current_day=current_day, 
                         location=location, cargo_weight=cargo_weight)

class PassengerPlane(Vehicle):
    def __init__(self, fuel_volume, days, current_day, location, seats, passengers):
        super().__init__("Пассажирский самолёт", "Пассажирское транспортное средство", fuel_volume=fuel_volume, days=days, current_day=current_day, 
                         location=location, seats=seats, passengers=passengers)

class LightHelicopter(Vehicle):
    def __init__(self, fuel_volume, days, current_day, location):
        super().__init__("Лёгкий вертолет", "Летательный аппарат", fuel_volume=fuel_volume, days=days, current_day=current_day, location=location)

class AttackHelicopter(Vehicle):
    def __init__(self, fuel_volume, days, current_day, location, rockets):
        super().__init__("Лёгкий вертолет", "Ударное транспортное средство", fuel_volume=fuel_volume, days=days, current_day=current_day, 
                         location=location, rockets = rockets)

class Fighter(Vehicle):
    def __init__(self, fuel_volume, days, current_day, location, rockets):
        super().__init__("Истребитель", "Ударное транспортное средство", fuel_volume=fuel_volume, days=days, current_day=current_day, 
                         location=location, rockets = rockets)

class Tanker(Vehicle):
    def __init__(self, fuel_volume, days, current_day, location, rockets, required_position, gas_station):
        super().__init__("Бензовоз", "Наземное транспортное средство", fuel_volume=fuel_volume, days=days, current_day=current_day, 
                         location=location, required_position=required_position, gas_station=gas_station)
        
class Bus(Vehicle):
    def __init__(self, fuel_volume, location, seats, passengers, required_position):
        super().__init__("Автобус", "Пассажирское транспортное средство", fuel_volume=fuel_volume, location=location, seats=seats, 
                         passengers=passengers, required_position=required_position)

# функция для генерации случайных значений и создания транспортных средств
def generate_vehicle(vtype):
    # случайные значения для необходимых параметров
    fuel_volume = round(random.uniform(0, 50), 1)
    days = random.randint(0, 10)
    current_day = random.randint(0, days)
    location = random.randint(0, 200)
    
    if vtype == LightPlane:
        return LightPlane(fuel_volume, days, current_day, location)
    elif vtype == CargoPlane:
        cargo_weight = round(random.uniform(0, 50), 1)
        return CargoPlane(fuel_volume, days, current_day, location, cargo_weight)
    elif vtype == PassengerPlane:
        seats = random.randint(0, 50)
        passengers = random.randint(0, seats)
        return PassengerPlane(fuel_volume, days, current_day, location, seats, passengers)
    elif vtype == LightHelicopter:
        return LightHelicopter(fuel_volume, days, current_day, location)
    elif vtype == AttackHelicopter:
        rockets = random.randint(0, 6)
        return AttackHelicopter(fuel_volume, days, current_day, location, rockets)
    elif vtype == Fighter:
        rockets = random.randint(0, 6)
        return Fighter(fuel_volume, days, current_day, location, rockets)
    elif vtype == Tanker:
        required_position = random.randint(0, 200)
        gas_station = random.choice(["Заправлен", "Не заправлен"])
        return Tanker(fuel_volume, days, current_day, location, rockets=0, required_position=required_position, gas_station=gas_station)
    elif vtype == Bus:
        seats = random.randint(0, 50)
        passengers = random.randint(0, seats)
        required_position = random.randint(0, 200)
        return Bus(fuel_volume, location, seats, passengers, required_position)

vehicles_list = []
vehicles_classes = [LightPlane, CargoPlane, PassengerPlane, LightHelicopter, AttackHelicopter, Fighter, Tanker, Bus]

# генерация всех транспортных средств
def generate_vehicles():
    global vehicles_list
    vehicles_list = [generate_vehicle(random.choice(vehicles_classes)) for _ in range(20)]

# отображение транспортных средств в текстовом поле
def display_vehicles(v_list):
    text_area.config(state=tk.NORMAL)
    text_area.delete("1.0", tk.END)
    iterator = VehicleIterator(v_list)  # создаём итератор
    for v in iterator:
        for attr, val in v.__dict__.items():
            text_area.insert(tk.END, f"{attr}: {val}\n")
        text_area.insert(tk.END, "-" * 20 + "\n")
    text_area.config(state=tk.DISABLED)

def generate_and_display():
    generate_vehicles()
    display_vehicles(vehicles_list)

if __name__ == '__main__':
    # создание окна и других элементов интерфейса
    window = tk.Tk()
    window.title("ТС аэропорта")

    generate_button = tk.Button(window, text="Сгенерировать 20 ТС", command=generate_and_display)
    generate_button.grid(row=0, column=0, padx=5, pady=5)

    # выпадающий список для фильтрации по типу (обобщённый тип)
    type_label = tk.Label(window, text="Тип:")
    type_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    type_options = ["Все", "Летательный аппарат", "Грузовое транспортное средство", "Пассажирское транспортное средство", 
                    "Ударное транспортное средство", "Наземное транспортное средство"]
    type_var = tk.StringVar()
    type_var.set(type_options[0])
    type_combo = ttk.Combobox(window, textvariable=type_var, values=type_options, state="readonly")
    type_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    # элементы управления для сортировки
    sort_label = tk.Label(window, text="Сортировка:")
    sort_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    sort_options = ["Нет", "Тип", "Объём топлива", "Дни стоянки", "Текущий день стоянки", "Расположение", "Вес груза", 
                    "Количество мест", "Количество пассажиров", "Количество ракет", "Требуемое положение"]
    sort_var = tk.StringVar()
    sort_var.set(sort_options[0])
    sort_combo = ttk.Combobox(window, textvariable=sort_var, values=sort_options, state="readonly")
    sort_combo.grid(row=0, column=3, padx=5, pady=5, sticky="w")
    desc_var = tk.BooleanVar()
    desc_check = tk.Checkbutton(window, text="По убыванию", variable=desc_var)
    desc_check.grid(row=0, column=4, padx=5, pady=5, sticky="w")

    # поля для фильтрации по числовым параметрам (min / max)
    label_fuel = tk.Label(window, text="Объём топлива:")
    label_fuel.grid(row=2, column=0, padx=5, pady=2, sticky="e")
    label_fuel_from = tk.Label(window, text="от")
    label_fuel_from.grid(row=2, column=1, padx=2, sticky="e")
    fuel_min_var = tk.StringVar()
    fuel_min_entry = tk.Entry(window, textvariable=fuel_min_var, width=5)
    fuel_min_entry.grid(row=2, column=2, padx=2, sticky="w")
    label_fuel_to = tk.Label(window, text="до")
    label_fuel_to.grid(row=2, column=3, padx=2, sticky="e")
    fuel_max_var = tk.StringVar()
    fuel_max_entry = tk.Entry(window, textvariable=fuel_max_var, width=5)
    fuel_max_entry.grid(row=2, column=4, padx=2, sticky="w")

    label_days = tk.Label(window, text="Дни стоянки:")
    label_days.grid(row=3, column=0, padx=5, pady=2, sticky="e")
    label_days_from = tk.Label(window, text="от")
    label_days_from.grid(row=3, column=1, padx=2, sticky="e")
    days_min_var = tk.StringVar()
    days_min_entry = tk.Entry(window, textvariable=days_min_var, width=5)
    days_min_entry.grid(row=3, column=2, padx=2, sticky="w")
    label_days_to = tk.Label(window, text="до")
    label_days_to.grid(row=3, column=3, padx=2, sticky="e")
    days_max_var = tk.StringVar()
    days_max_entry = tk.Entry(window, textvariable=days_max_var, width=5)
    days_max_entry.grid(row=3, column=4, padx=2, sticky="w")

    label_cur = tk.Label(window, text="Текущий день стоянки:")
    label_cur.grid(row=4, column=0, padx=5, pady=2, sticky="e")
    label_cur_from = tk.Label(window, text="от")
    label_cur_from.grid(row=4, column=1, padx=2, sticky="e")
    cur_min_var = tk.StringVar()
    cur_min_entry = tk.Entry(window, textvariable=cur_min_var, width=5)
    cur_min_entry.grid(row=4, column=2, padx=2, sticky="w")
    label_cur_to = tk.Label(window, text="до")
    label_cur_to.grid(row=4, column=3, padx=2, sticky="e")
    cur_max_var = tk.StringVar()
    cur_max_entry = tk.Entry(window, textvariable=cur_max_var, width=5)
    cur_max_entry.grid(row=4, column=4, padx=2, sticky="w")

    label_loc = tk.Label(window, text="Расположение:")
    label_loc.grid(row=5, column=0, padx=5, pady=2, sticky="e")
    label_loc_from = tk.Label(window, text="от")
    label_loc_from.grid(row=5, column=1, padx=2, sticky="e")
    loc_min_var = tk.StringVar()
    loc_min_entry = tk.Entry(window, textvariable=loc_min_var, width=5)
    loc_min_entry.grid(row=5, column=2, padx=2, sticky="w")
    label_loc_to = tk.Label(window, text="до")
    label_loc_to.grid(row=5, column=3, padx=2, sticky="e")
    loc_max_var = tk.StringVar()
    loc_max_entry = tk.Entry(window, textvariable=loc_max_var, width=5)
    loc_max_entry.grid(row=5, column=4, padx=2, sticky="w")

    label_cargo = tk.Label(window, text="Вес груза:")
    label_cargo.grid(row=6, column=0, padx=5, pady=2, sticky="e")
    label_cargo_from = tk.Label(window, text="от")
    label_cargo_from.grid(row=6, column=1, padx=2, sticky="e")
    cargo_min_var = tk.StringVar()
    cargo_min_entry = tk.Entry(window, textvariable=cargo_min_var, width=5)
    cargo_min_entry.grid(row=6, column=2, padx=2, sticky="w")
    label_cargo_to = tk.Label(window, text="до")
    label_cargo_to.grid(row=6, column=3, padx=2, sticky="e")
    cargo_max_var = tk.StringVar()
    cargo_max_entry = tk.Entry(window, textvariable=cargo_max_var, width=5)
    cargo_max_entry.grid(row=6, column=4, padx=2, sticky="w")

    label_seats = tk.Label(window, text="Количество мест:")
    label_seats.grid(row=7, column=0, padx=5, pady=2, sticky="e")
    label_seats_from = tk.Label(window, text="от")
    label_seats_from.grid(row=7, column=1, padx=2, sticky="e")
    seats_min_var = tk.StringVar()
    seats_min_entry = tk.Entry(window, textvariable=seats_min_var, width=5)
    seats_min_entry.grid(row=7, column=2, padx=2, sticky="w")
    label_seats_to = tk.Label(window, text="до")
    label_seats_to.grid(row=7, column=3, padx=2, sticky="e")
    seats_max_var = tk.StringVar()
    seats_max_entry = tk.Entry(window, textvariable=seats_max_var, width=5)
    seats_max_entry.grid(row=7, column=4, padx=2, sticky="w")

    label_pass = tk.Label(window, text="Количество пассажиров:")
    label_pass.grid(row=8, column=0, padx=5, pady=2, sticky="e")
    label_pass_from = tk.Label(window, text="от")
    label_pass_from.grid(row=8, column=1, padx=2, sticky="e")
    pass_min_var = tk.StringVar()
    pass_min_entry = tk.Entry(window, textvariable=pass_min_var, width=5)
    pass_min_entry.grid(row=8, column=2, padx=2, sticky="w")
    label_pass_to = tk.Label(window, text="до")
    label_pass_to.grid(row=8, column=3, padx=2, sticky="e")
    pass_max_var = tk.StringVar()
    pass_max_entry = tk.Entry(window, textvariable=pass_max_var, width=5)
    pass_max_entry.grid(row=8, column=4, padx=2, sticky="w")

    label_rockets = tk.Label(window, text="Количество ракет:")
    label_rockets.grid(row=9, column=0, padx=5, pady=2, sticky="e")
    label_rockets_from = tk.Label(window, text="от")
    label_rockets_from.grid(row=9, column=1, padx=2, sticky="e")
    rockets_min_var = tk.StringVar()
    rockets_min_entry = tk.Entry(window, textvariable=rockets_min_var, width=5)
    rockets_min_entry.grid(row=9, column=2, padx=2, sticky="w")
    label_rockets_to = tk.Label(window, text="до")
    label_rockets_to.grid(row=9, column=3, padx=2, sticky="e")
    rockets_max_var = tk.StringVar()
    rockets_max_entry = tk.Entry(window, textvariable=rockets_max_var, width=5)
    rockets_max_entry.grid(row=9, column=4, padx=2, sticky="w")

    label_req = tk.Label(window, text="Требуемое положение:")
    label_req.grid(row=10, column=0, padx=5, pady=2, sticky="e")
    label_req_from = tk.Label(window, text="от")
    label_req_from.grid(row=10, column=1, padx=2, sticky="e")
    req_min_var = tk.StringVar()
    req_min_entry = tk.Entry(window, textvariable=req_min_var, width=5)
    req_min_entry.grid(row=10, column=2, padx=2, sticky="w")
    label_req_to = tk.Label(window, text="до")
    label_req_to.grid(row=10, column=3, padx=2, sticky="e")
    req_max_var = tk.StringVar()
    req_max_entry = tk.Entry(window, textvariable=req_max_var, width=5)
    req_max_entry.grid(row=10, column=4, padx=2, sticky="w")

    # таблица для отображения результатов
    columns = ["Тип", "Объём топлива", "Дни стоянки", "Текущий день стоянки", "Расположение", "Вес груза", "Мест", "Пассажиров", 
               "Ракет", "Требуемое положение", "Состояние заправки"]
    tree = ttk.Treeview(window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.grid(row=12, column=0, columnspan=5, padx=5, pady=5)

    text_area = tk.Text(window, width=100, height=15)
    text_area.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

    scroll = tk.Scrollbar(window, command=text_area.yview)
    scroll.grid(row=1, column=5, sticky="ns")

    text_area.config(yscrollcommand=scroll.set)

    # функция применения фильтров и сортировки
    def apply_filter():
        global vehicles_list
        filtered = vehicles_list
        # фильтрация по обобщенному типу транспорта
        cat = type_var.get()
        if cat != "Все":
            filtered = [v for v in filtered if v.category == cat]
        # числовые фильтры: функция для получения границ интервала
        def get_min_max(min_str, max_str):
            min_val = None
            max_val = None
            if min_str.strip() != "":
                try:
                    min_val = int(min_str.strip())
                except:
                    try:
                        min_val = float(min_str.strip())
                    except:
                        min_val = None
            if max_str.strip() != "":
                try:
                    max_val = int(max_str.strip())
                except:
                    try:
                        max_val = float(max_str.strip())
                    except:
                        max_val = None
            return min_val, max_val
        # фильтр по объёму топлива
        min_val, max_val = get_min_max(fuel_min_var.get(), fuel_max_var.get())
        if min_val is not None or max_val is not None:
            if min_val is None: min_val = float('-inf')
            if max_val is None: max_val = float('inf')
            filtered = [v for v in filtered if min_val <= v.fuel_volume <= max_val]
        # фильтр по дням стоянки
        min_val, max_val = get_min_max(days_min_var.get(), days_max_var.get())
        if min_val is not None or max_val is not None:
            if min_val is None: min_val = float('-inf')
            if max_val is None: max_val = float('inf')
            filtered = [v for v in filtered if min_val <= v.days <= max_val]
        # фильтр по текущему дню стоянки
        min_val, max_val = get_min_max(cur_min_var.get(), cur_max_var.get())
        if min_val is not None or max_val is not None:
            if min_val is None: min_val = float('-inf')
            if max_val is None: max_val = float('inf')
            filtered = [v for v in filtered if min_val <= v.current_day <= max_val]
        # фильтр по расположению
        min_val, max_val = get_min_max(loc_min_var.get(), loc_max_var.get())
        if min_val is not None or max_val is not None:
            if min_val is None: min_val = float('-inf')
            if max_val is None: max_val = float('inf')
            filtered = [v for v in filtered if min_val <= v.location <= max_val]
        # фильтр по весу груза
        min_val, max_val = get_min_max(cargo_min_var.get(), cargo_max_var.get())
        if min_val is not None or max_val is not None:
            if min_val is None: min_val = float('-inf')
            if max_val is None: max_val = float('inf')
            filtered = [v for v in filtered if min_val <= v.cargo_weight <= max_val]
        # фильтр по количеству мест
        min_val, max_val = get_min_max(seats_min_var.get(), seats_max_var.get())
        if min_val is not None or max_val is not None:
            if min_val is None: min_val = float('-inf')
            if max_val is None: max_val = float('inf')
            filtered = [v for v in filtered if min_val <= v.seats <= max_val]
        # фильтр по количеству пассажиров
        min_val, max_val = get_min_max(pass_min_var.get(), pass_max_var.get())
        if min_val is not None or max_val is not None:
            if min_val is None: min_val = float('-inf')
            if max_val is None: max_val = float('inf')
            filtered = [v for v in filtered if min_val <= v.passengers <= max_val]
        # фильтр по количеству ракет
        min_val, max_val = get_min_max(rockets_min_var.get(), rockets_max_var.get())
        if min_val is not None or max_val is not None:
            if min_val is None: min_val = float('-inf')
            if max_val is None: max_val = float('inf')
            filtered = [v for v in filtered if min_val <= v.rockets <= max_val]
        # фильтр по требуемому положению
        min_val, max_val = get_min_max(req_min_var.get(), req_max_var.get())
        if min_val is not None or max_val is not None:
            if min_val is None: min_val = float('-inf')
            if max_val is None: max_val = float('inf')
            filtered = [v for v in filtered if min_val <= v.required_position <= max_val]
        # сортировка списка в соответствии с выбранным полем
        sort_field = sort_var.get()
        rev = desc_var.get()
        if sort_field != "Нет":
            if sort_field == "Тип":
                filtered.sort(key=lambda x: x.type, reverse=rev)
            elif sort_field == "Объём топлива":
                filtered.sort(key=lambda x: x.fuel_volume, reverse=rev)
            elif sort_field == "Дни стоянки":
                filtered.sort(key=lambda x: x.days, reverse=rev)
            elif sort_field == "Текущий день стоянки":
                filtered.sort(key=lambda x: x.current_day, reverse=rev)
            elif sort_field == "Расположение":
                filtered.sort(key=lambda x: x.location, reverse=rev)
            elif sort_field == "Вес груза":
                filtered.sort(key=lambda x: x.cargo_weight, reverse=rev)
            elif sort_field == "Количество мест":
                filtered.sort(key=lambda x: x.seats, reverse=rev)
            elif sort_field == "Количество пассажиров":
                filtered.sort(key=lambda x: x.passengers, reverse=rev)
            elif sort_field == "Количество ракет":
                filtered.sort(key=lambda x: x.rockets, reverse=rev)
            elif sort_field == "Требуемое положение":
                filtered.sort(key=lambda x: x.required_position, reverse=rev)
        # обновление таблицы
        for row in tree.get_children():
            tree.delete(row)
        for v in filtered:
            tree.insert("", "end", values=(v.type, v.fuel_volume, v.days, v.current_day, 
                                           v.location, v.cargo_weight, v.seats, v.passengers, v.rockets, v.required_position, v.gas_station))

    filter_button = tk.Button(window, text="Применить", command=apply_filter)
    filter_button.grid(row=15, column=4, padx=5, pady=5, sticky="e")

    apply_filter()
    window.mainloop()
