def send_alert(log):
    print(f"ALERT: [{log['severity']}] {log['service']} - {log['message']}")
    # Add email or SMS integration (Twilio, SendGrid, etc.)
