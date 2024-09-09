package StretegicDesignPattern.WithoutStretegicDesignPattern;

public class SportsVehicle extends Vehicle{
    @Override
    public void drive() {
        // Duplicate Code
        System.out.println("Special Drive");
    }
}