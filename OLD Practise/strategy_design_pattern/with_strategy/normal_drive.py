# from vehicle import Vehicle
from lld.strategy_design_pattern.with_strategy.vehicle import Vehicle
from lld.strategy_design_pattern.with_strategy.Strategies.normal_drive_strategy import NormalDriveStrategy


class NormalVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())
