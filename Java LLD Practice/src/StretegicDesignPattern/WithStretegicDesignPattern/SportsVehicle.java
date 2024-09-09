package StretegicDesignPattern.WithStretegicDesignPattern;

import StretegicDesignPattern.WithStretegicDesignPattern.DriveStrategy.SpecialDriveStrategy;

public class SportsVehicle extends Vehicle {
    SportsVehicle(){
        super(new SpecialDriveStrategy());

    }
}