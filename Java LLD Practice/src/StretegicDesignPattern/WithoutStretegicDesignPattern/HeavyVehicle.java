package StretegicDesignPattern.WithoutStretegicDesignPattern;

public class HeavyVehicle extends Vehicle{
    @Override
    public void drive() {
        // Duplicate Code
        System.out.println("Special Drive");
    }
}
