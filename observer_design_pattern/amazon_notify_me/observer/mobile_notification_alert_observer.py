from lld.observer_design_pattern.amazon_notify_me.observer.notification_alert_observer \
    import NotificationAlertObserver


class MobileNotificationAlertObserver(NotificationAlertObserver):
    def __init__(self, observable, mobile_no):
        self.observable = observable
        self.mobile_no = mobile_no

    def update(self):
        self.send_mail()

    def send_mail(self):
        print("msg sent to {} with count {}".format(self.mobile_no, self.observable.stock_count))
