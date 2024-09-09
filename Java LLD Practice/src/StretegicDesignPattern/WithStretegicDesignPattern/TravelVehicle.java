package StretegicDesignPattern.WithStretegicDesignPattern;

import StretegicDesignPattern.WithStretegicDesignPattern.DriveStrategy.NormalDriveStrategy;

public class TravelVehicle extends Vehicle {
    TravelVehicle(){
        super(new NormalDriveStrategy());

    }
}