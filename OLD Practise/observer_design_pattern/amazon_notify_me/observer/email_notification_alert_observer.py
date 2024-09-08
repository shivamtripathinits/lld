from lld.observer_design_pattern.amazon_notify_me.observer.notification_alert_observer\
    import NotificationAlertObserver


class EmailNotificationAlertObserver(NotificationAlertObserver):
    def __init__(self, observable, email):
        self.observable = observable
        self.email = email

    def update(self):
        self.send_mail()

    def send_mail(self):
        print("mail sent to {} with count {} ".format(self.email, self.observable.stock_count))
