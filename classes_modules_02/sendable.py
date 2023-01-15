#!/usr/bin/env python3

import time
class Sendable:
  _created_at = time.time()
  _updated_at = time.time()
  _sent_at = None

  def __init__(self, body: str, subject: str, from_: str, to: str):
      self._body = body
      self._subject = subject
      self._from = from_
      self._to = to


  def send(self):
        if self._sent_at:
            raise Exception("DataAlreadySent")
        else:
            self._sent_at = time.time()



# sendable= Sendable("je ne t'aime pas Marvin body", "hater subject", "casu3475@gmail.com", "speranzalucie@gmail.com")

# print(sendable._body)
# print(sendable._subject)
# print(sendable._from)
# print(sendable._to)
# print(sendable._created_at)
# print(sendable._updated_at)
# print(sendable._sent_at)