from lld.observer_design_pattern.amazon_notify_me.observable.stocks_observable import StocksObservable


class IphoneObservable(StocksObservable):
    def __init__(self):
        self.observer_list = []
        self.stock_count = 0

    def add(self, observer):
        self.observer_list.append(observer)

    def remove(self, observer):
        self.observer_list.remove(observer)

    def notify_subscribers(self):
        for observer in self.observer_list:
            observer.update()

    def set_stock_count(self, new_count):
        self.stock_count = new_count
        self.notify_subscribers()

    def get_stock_count(self):
        return self.stock_count
