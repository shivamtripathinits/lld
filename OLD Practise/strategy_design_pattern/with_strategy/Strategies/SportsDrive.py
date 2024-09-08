from lld.strategy_design_pattern.with_strategy.Strategies.DriveStrategy import DriveStrategy


class SportsDrive(DriveStrategy):
    def drive(self):
        print("sport")

