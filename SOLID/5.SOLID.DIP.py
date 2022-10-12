# SOLID

# Принципы дизайна, представленные Робертом Мартином.

# DIP - Dependency Inversion Principle (принцип инверсии зависимостей).

from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Prerson:
    def __init__(self, name):
        self.name = name


# class Relationships:
#     def __init__(self):
#         self.relations = []

#     def add_parent_and_child(self, parent, child):
#         self.relations.append(
#             (parent, Relationship.PARENT, child)
#         )
#         self.relations.append(
#             (child, Relationship.CHILD, parent)
#         )


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


# рефакторинг Relationships
class Relationships(RelationshipBrowser):  # low-level module
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# class Research:
#     def __init__(self, relationships):
#         relations = relationships.relations
#         for r in relations:
#             if r[0].name == 'John' and r[1] == Relationship.PARENT:
#                 print(f'John has a child {r[2].name}.')


# рефакторинг Research
class Research:  # hight-level module
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child {p}.')


# добавим три персоны (родителя и двоих детей)
parent = Prerson('John')
child1 = Prerson('Chris')
child2 = Prerson('Matt')

# установим отношения персон (добавим родственные связи)
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

# До рефакторинга есть зависимость от хранилища. Research сработает, если
# relations будет списком. Если его изменить на словарь, то Research уже не
# сработает. После рефакторинга Research не зависит от хранилища.
Research(relationships)

# low-level module имеет дело с хранением. Вместо списка может быть DataBase.
# hight-level module не зависит от типа хранилища данных.

# Цель 'DIP' - избегать зависимости от внутренней механики хранения данных.
# Классы должны зависеть от абстракций, а не от конкретных деталей.
