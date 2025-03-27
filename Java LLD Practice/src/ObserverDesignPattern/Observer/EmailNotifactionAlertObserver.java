package ObserverDesignPattern.Observer;

public class EmailNotifactionAlertObserver implements NotifactionAlertObserver{
    String iDD;

    public EmailNotifactionAlertObserver(String iDD){
        this.iDD = iDD;
    }
    @Override
    public void notifySubs() {
        System.out.println("Email Sent to " + iDD);
    }
}
