from flask import Flask
from twilio.html.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("We are all homos. Homo sapiens.", voice='alice')
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
