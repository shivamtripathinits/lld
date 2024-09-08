from abc import ABC, abstractmethod


class DriveStrategy:
    @abstractmethod
    def drive(self):
        pass
