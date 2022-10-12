# SOLID

# Принципы дизайна, представленные Робертом Мартином.

# ISP - Interface Segrigation Principle (принцип разделения интерфейса).

from abc import abstractmethod


class Machine:
    def print_doc(self, document):
        raise NotImplementedError

    def fax_doc(self, document):
        raise NotImplementedError

    def scan_doc(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print_doc(self, document):
        pass

    def fax_doc(self, document):
        pass

    def scan_doc(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print_doc(self, document):
        pass  # OK

    def fax_doc(self, document):
        pass  # NOK

    def scan_doc(self, document):
        """Method not supported!"""
        raise NotImplementedError("Printer can't scan!")


class Printer:
    @abstractmethod
    def print_doc(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan_doc(self, document):
        pass


class MyPrinter(Printer):
    def print_doc(self, document):
        print(document)


class MyPhotocopier(Printer, Scanner):
    def print_doc(self, document):
        pass

    def scan_doc(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print_doc(self, document):
        pass

    @abstractmethod
    def scan_doc(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print_doc(self, document):
        self.printer.print_doc(document)

    def scan_doc(self, document):
        self.scanner.scan_doc(document)

# Создание интерфейсов, содержащих слишком много програмных членов - не лучшая
# идея, т.е. класса Machine включает методы (принтер, факс и сканер), которые
# могут не понадобиться.
# Согласно принципу 'ISP' программист должен разделять интерфейс на самые узкие
# интерфейсы, которые можно создать, чтобы клиенту не приходилось реализовывать
# больше, чем нужно.
