#!/usr/bin/env python3

import time
from sendable import Sendable

class Email(Sendable):
    def __init__(self, _body: str, _subject: str, _from: str, _to: str):
        super().__init__(_body, _subject, _from, _to)


# email= Email("je ne t'aime pas Marvin body", "hater subject", "casu3475@gmail.com", "speranzalucie@gmail.com")

# print(email._body)
# print(email._from)
# print(email._to)
# print(email._created_at)
# print(email._updated_at)
# print(email._sent_at)