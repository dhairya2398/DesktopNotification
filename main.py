import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Created by Dhairya Patel.",
            timeout = 3
        )
        time.sleep(5)