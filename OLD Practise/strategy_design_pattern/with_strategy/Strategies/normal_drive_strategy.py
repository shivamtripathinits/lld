from lld.strategy_design_pattern.with_strategy.Strategies.DriveStrategy import DriveStrategy


class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print("Normal drive")