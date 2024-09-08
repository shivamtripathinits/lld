# from vehicle import Vehicle
from lld.strategy_design_pattern.with_strategy.vehicle import Vehicle
from lld.strategy_design_pattern.with_strategy.Strategies.SportsDrive import SportsDrive

class SportVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportsDrive())
