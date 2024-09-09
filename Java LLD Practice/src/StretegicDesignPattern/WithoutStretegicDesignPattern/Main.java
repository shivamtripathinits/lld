package StretegicDesignPattern.WithoutStretegicDesignPattern;

public class Main {
    public static void main(String[] args) {

        System.out.println("Hello world!");

        driveVehicle(new HeavyVehicle());
        driveVehicle(new SportsVehicle());
        driveVehicle(new TravelVehicle());
    }

    public static void driveVehicle(Vehicle vehicle){
        vehicle.drive();
    }
}