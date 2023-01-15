#!/usr/bin/env python3

import time
import string

class Sendable:

  _history = {}
  _created_at = time.time()
  _updated_at = time.time()
  _sent_at = None

  def __init__(self, _body: str, _subject: str, _from: str, _to: str):
      self._body = _body
      self._subject = _subject
      self._from = _from
      self._to = _to


  def send(self):
        if self._sent_at:
            raise Exception("DataAlreadySent")
        else:
            self._sent_at = time.time()
            if self._from not in Sendable.history:
                Sendable.history[self._from] = {}
            if self._to not in Sendable.history[self._from]:
                Sendable.history[self._from][self._to] = []
            Sendable.history[self._from][self._to].append(self._sent_at)

  def history(cls):
        return cls.history

  def encrypt(self, rotate=13):
        self._body = "".join([chr((ord(c) + rotate) % 126) for c in self._body])
        return self._body

# --------------------------reverse--------------------------
  def decrypt(self, rotate=13):
        self._body = "".join([chr((ord(c) - rotate) % 126) for c in self._body])
        return self._body

# def encrypt(self, rotate=13):
#     alphabet = string.ascii_lowercase
#     rotated_alphabet = alphabet[rotate:] + alphabet[:rotate]
#     table = string.maketrans(alphabet, rotated_alphabet)
#     return self._body.translate(table)

# def decrypt(self, rotate=13):
#     alphabet = string.ascii_lowercase
#     rotated_alphabet = alphabet[-rotate:] + alphabet[:-rotate]
#     table = string.maketrans(alphabet, rotated_alphabet)
#     return self._body.translate(table)



# sendable= Sendable("je ne t'aime pas Marvin body", "hater subject", "casu3475@gmail.com", "speranzalucie@gmail.com")
# print(sendable._body)

# sendable = Sendable()
# sendable._body = "hello world"

# encrypted_text = sendable.encrypt()
# print(encrypted_text)  

# decrypted_text = sendable.decrypt(encrypted_text)
# print(decrypted_text)  




