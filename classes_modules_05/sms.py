#!/usr/bin/env python3

import time
from sendable import Sendable

class Sms(Sendable):
    def __init__(self, _body: str, _from: str, _to: str):
        super().__init__(_body, _from, _to)

# sms= Sms("je ne t'aime pas Marvin body", "from casu3475@gmail.com", "to alucie@gmail.com")

# print(sms._body)
# print(sms._from)
# print(sms._to)
# print(sms._created_at)
# print(sms._updated_at)
# print(sms._sent_at)