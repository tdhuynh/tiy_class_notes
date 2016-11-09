from twilio.rest import TwilioRestClient


class Messenger:

    account_sid = "AC506a9ce0cf7a2bf87b0a2411425c651a"
    auth_token  = "beace99085bddf6d9f00af951567c4cc"

    def __init__(self):
        self.client = TwilioRestClient(self.account_sid, self.auth_token)

    def send(self, message):
        return self.client.messages.create(body=message, to="+18642660709", from_="+18643107035")
