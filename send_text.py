from twilio.rest import Client
import keys

def send_sms(price):
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(
        body = f"Current Uber price: {price}",
        from_ = keys.twilio_number,
        to = keys.target_number
    )

    # print(message.body)