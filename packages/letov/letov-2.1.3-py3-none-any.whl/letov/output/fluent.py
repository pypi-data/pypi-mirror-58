import os

from io import BytesIO

import msgpack

from fluent.sender import FluentSender


class Fluent:
    def __init__(self, host=None, port=None):
        self.sender = FluentSender(
            'letov',
            host=host or os.environ['FLUENTBIT_HOST'],
            port=port or int(os.environ['FLUENTBIT_PORT']),
            buffer_overflow_handler=self.overflow_handler
        )

    @staticmethod
    def overflow_handler(pending):
        unpacker = msgpack.Unpacker(BytesIO(pending), raw=False)
        for tag, ts, record in unpacker:
            # last resort - try to send logs through docker engine (stdout)
            print(record['log'])

    def send(self, message):
        return self.sender.emit('applogs', {
            'log': message,
            'source': 'letov',
        })

    def close(self):
        self.sender.close()
