#!/usr/bin/env python3

import time
class Email:
  _created_at = time.time()
  _updated_at = time.time()
  _sent_at = None

  def __init__(self, _body: str, _subject: str, _from: str, _to: str):
      self._body = _body
      self._subject = _subject
      self._from = _from
      self._to = _to


# email = Email("je ne t'aime pas Marvin", "hater", "casu3475@gmail.com", "lucie@gmail.com")

# print(email._body)
# print(email._subject)
# print(email._from)
# print(email._to)
# print(email._created_at)
# print(email._updated_at)
# print(email._sent_at)