import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '397853694:AAHhPvnkGoFFYeI_jRlzPzAjab90gUM7S-c'
WEBHOOK_URL = 'https://930490b0.ngrok.io/show-fsm'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        '92',
        '95',
		'98',
		'full',
		'amo',
		'cash',
		'credit'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': '92',
            'conditions': 'is_going_to_92'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': '95',
            'conditions': 'is_going_to_95'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': '98',
            'conditions': 'is_going_to_98'
        },
        {
            'trigger': 'advance',
            'source': ['92','95','98'],
            'dest': 'amo',
            'conditions': 'is_going_to_amo'
        },
        {
            'trigger': 'advance',
            'source': ['92','95','98'],
            'dest': 'full',
            'conditions': 'is_going_to_full'
        },
        {
            'trigger': 'advance',
            'source': ['amo','full'],
            'dest': 'credit',
            'conditions': 'is_going_to_credit'
        },
        {
            'trigger': 'advance',
            'source': ['amo','full'],
            'dest': 'cash',
            'conditions': 'is_going_to_cash'
        },
        {
            'trigger': 'go_back',
            'source': [
#                'state1',
#                'state2',
				'cash',
				'credit'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')

if __name__ == "__main__":
    _set_webhook()
    app.run()
