import pywhatkit as kit
import time

def sendmessage(phones):

    for phone in phones:
        try:
            message = input(f"what you wanna exactly send to the number {phone} ??")
            kit.sendwhatmsg_instantly(
                phone,
                message,
                wait_time=15,     # seconds to wait for WhatsApp Web to load
            )
            print(f"Message prepared to send for {phone}")
            time.sleep(5)       # short pause between numbers

        except Exception as e:
            print(f"Failed to send message to {phone}: {e}")
