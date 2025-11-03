import json
import os
import csv
import random


# The class for keeping the data of player progress, calculating its exp\coins gaining and lvling up
# it also saves and loads the progress to the json file
class PlayerStats:
    def __init__(self, current_lvl, exp_gained, coins):
        self.current_lvl = current_lvl
        self.exp_gained = exp_gained
        self.coins = coins
        self.title = "Unranked "
        self.title_table = self.load_titles("titles.csv")
        self.update_title()

    def lvl_up(self, exp_gained):
        self.exp_gained += exp_gained
        if self.exp_gained >= 100:
            while self.exp_gained >= 100:
                self.exp_gained -= 100
                self.current_lvl += 1
                if self.current_lvl % 5 == 0:
                    self.coins += 5
                else:
                    self.coins += 3
        self.update_title()

    def coins_added(self, amount):
        self.coins += amount

    def coins_spent(self, amount):
        if self.coins - amount >= 0:
            self.coins -= amount
        else:
            print("The operation can not be processed: Not enough coins")

    def load_titles(self, filename):
        titles = {}
        with open(filename, newline="", encoding='utf-8') as csv_data:
            reader = csv.DictReader(csv_data)
            for row in reader:
                lvl = int(row["Уровень"])
                titles[lvl] = row["Титул"]
        return titles

    def update_title(self):
        eligible_levels = [lvl for lvl in self.title_table if lvl <= self.current_lvl]
        if eligible_levels:
            highest = max(eligible_levels)
            new_title = self.title_table[highest]
            if self.title != new_title:
                self.title = new_title
                print(f"Вы получили {self.current_lvl} уровень. Новый титул:{self.title}")
        else:
            self.title = "Unranked"

    def save_data(self, filename="player_data.json"):
        data = {
            "current_lvl": self.current_lvl,
            "exp_gained": self.exp_gained,
            "coins": self.coins,
            "title": self.title
        }
        with open(filename, "w") as save_file:
            json.dump(data, save_file, indent=4)
        print(f"Data was saved to {filename}")

    @classmethod
    def load_data(cls, filename="player_data.json"):
        if not os.path.exists(filename):
            print("No dave data. Creating a new save file!")
            return cls(1, 0, 0)
        with open(filename, "r") as save_file:
            data = json.load(save_file)
        return cls(data["current_lvl"], data["exp_gained"], data["coins"])

    def reset_data(self):
        self.current_lvl = 1
        self.exp_gained = 0
        self.coins = 0
        self.title = "Unranked"
        self.save_data()


# class for handling the csv files with a daily quests, challenges and store
class ActivitiesAndStore:
    def __init__(self):
        self.tables = {}

    def load_csv(self, name, filename):
        with open(filename, newline="", encoding='utf-8') as csv_data:
            reader = csv.reader(csv_data)
            data = [row for row in reader if row]
        self.tables[name] = data

    def get_random_row(self, name):
        if name not in self.tables:
            raise ValueError(f"No table named '{name} loaded.")
        return self.tables[name][random.randint(1, len(self.tables[name]) - 1)]

    def get_all_rows(self, name):
        if name not in self.tables:
            raise ValueError(f"No table named '{name} loaded.")
        return self.tables[name]

    def choose(self, table_name, field_index=None):
        if table_name not in self.tables:
            print(f"❌ Table '{table_name}' not found!")
            return None
        table = self.tables[table_name]

        print(f"📋 Доступны следующие {table_name}ы:")
        for i, row in enumerate(table):
            print(f"{i}: {row}")

        choice = input("Введите номер желаемого материала: ")
        if not choice.isdigit():
            print("❌ Нужно ввести номер!")
            return None

        choice = int(choice)
        if not (0 <= choice < len(table)):
            print("❌ Неправильный материал!")
            return None
        selected_row = table[choice]

        if field_index is not None:
            if not (0 <= field_index < len(selected_row)):
                print("❌ Нет такого поля!")
                return None
            print(f"✅ Получено экспы: {selected_row[field_index]}")
            return selected_row[field_index]
        print(f"✅ Выбран материал: {selected_row}")
        return selected_row


# This, if imported, will print any activities preloaded from csv row by row
# def print_all_rows(name):
#     i = 0
#     for row in name:
#         print(f"{i}. {row[0]} {row[1]}")
#         i += 1
