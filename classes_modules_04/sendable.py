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

            if self._from not in Sendable._history:
                Sendable._history[self._from] = {}
            if self._to not in Sendable._history[self._from]:
                Sendable._history[self._from][self._to] = []
            Sendable._history[self._from][self._to].append(self._sent_at)


  def history(cls):
        return cls.history


# La méthode encrypt prend un argument entier rotate et l'utilise pour chiffrer la chaîne de caractères stockée dans l'attribut _body de l'instance de la classe. 
# ord(c) retourne la valeur ASCII du caractère c, rotate est ajouté à cette valeur, et le résultat est pris modulo 126. la valeur est convertie avec la fonction "chr".

  def encrypt(self, rotate=13):
        self._body = "".join([chr((ord(c) + rotate) % 126) for c in self._body])
        return self._body

# --------------------------reverse--------------------------
  def decrypt(self, rotate=13):
        self._body = "".join([chr((ord(c) - rotate) % 126) for c in self._body])
        return self._body


