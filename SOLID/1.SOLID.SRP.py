# SOLID

# Принципы дизайна, представленные Робертом Мартином.

# SRP - Single Responcebility Princple (принцип единой ответственности).
# Так же встречается как SOC (разделение ответственностей).

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # Это нарушение принципа 'SRP', т.к. этот метод относится ко
    # вторичной ответственности. Необходимо вынести в отдельный класс.
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    # Это нарушение принципа 'SRP', т.к. этот метод относится ко
    # вторичной ответственности. Необходимо вынести в отдельный класс.
    def load(self, filename):
        pass

    # Это нарушение принципа 'SRP', т.к. этот метод относится ко
    # вторичной ответственности. Необходимо вынести в отдельный класс.
    def load_from_web(self, uri):
        pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


# создание журнала и добавление записей в журнал.
j = Journal()
j.add_entry("I am learning the principles of 'SOLID'.")
j.add_entry("I am learning the first principle of 'SOLID' \
which is called 'SRP'.")
print(f'Journal.entries:\n{j}')

# сохранение данных в журнал (файл с именем 'journal.txt').
# такой подход не нарушает принципа 'SRP'
file = r'D:\Python\Code\journal.txt'
PersistenceManager.save_to_file(j, file)

# чтение журнала из файла.
with open(file) as fh:
    print(fh.read())

# Одним из антипаттернов является God_Object (Всемогущий_Объект). Это
# происходит, если разработчик собирает ВСЕ возможные методы в одном
# классе. Принцип 'SRP' не позволяет создавать God_Object.
