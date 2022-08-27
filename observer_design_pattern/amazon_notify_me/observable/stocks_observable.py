from abc import ABC, abstractmethod


class StocksObservable:
    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass

    @abstractmethod
    def set_stock_count(self, new_count):
        pass

    @abstractmethod
    def get_stock_count(self):
        pass
