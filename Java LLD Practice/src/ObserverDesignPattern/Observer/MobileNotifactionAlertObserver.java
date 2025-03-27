package ObserverDesignPattern.Observer;

public class MobileNotifactionAlertObserver implements NotifactionAlertObserver{
    String iDD;

    public MobileNotifactionAlertObserver(String iDD){
        this.iDD = iDD;
    }
    @Override
    public void notifySubs() {
        System.out.println("SMS Sent to " + iDD);
    }
}
