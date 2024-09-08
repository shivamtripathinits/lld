from lld.strategy_design_pattern.with_strategy.Strategies.DriveStrategy import DriveStrategy

class Vehicle:
    def __init__(self, strategy):
        self.strategy = strategy

    def drive(self):
        self.strategy.drive()

