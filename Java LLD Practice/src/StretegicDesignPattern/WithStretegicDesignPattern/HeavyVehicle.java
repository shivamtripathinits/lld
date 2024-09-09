package StretegicDesignPattern.WithStretegicDesignPattern;

import StretegicDesignPattern.WithStretegicDesignPattern.DriveStrategy.DriveStrategy;
import StretegicDesignPattern.WithStretegicDesignPattern.DriveStrategy.SpecialDriveStrategy;

public class HeavyVehicle extends Vehicle {
    HeavyVehicle(){
        super(new SpecialDriveStrategy());
    }
}
