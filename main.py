from lld.strategy_design_pattern.with_strategy.sports_vehicle import SportVehicle
from lld.strategy_design_pattern.with_strategy.normal_drive import NormalVehicle


def run_sport__vehicle():
    # curr_strategy = SportsDrive()
    vehicle = SportVehicle()
    vehicle.drive()


def run_normal_vehicle():
    # curr_strategy = SportsDrive()
    vehicle = NormalVehicle()
    vehicle.drive()


run_sport__vehicle()
run_normal_vehicle()

