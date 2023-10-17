#import os

from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

account_sid = "AC2b97531dddf280102034f5f7dffa4deb" #os.getenv('TWILIO_SID')
#AC2b97531dddf280102034f5f7dffa4deb
auth_token = "b3f2189dea01d6c9d6096741c28a6548" #os.getenv('TWILIO_TOKEN')
#b3f2189dea01d6c9d6096741c28a6548
client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> None:
    '''
    Send message to a Telegram user.
    Parameters:
        - to(str): sender whatsapp number in this whatsapp:+919558515995 form
        - message(str): text message to send
    Returns:
        - None
    '''

    _ = client.messages.create(
        from_='whatsapp:+14155238886', #+14155238886
        body=message,
        to=to
    )