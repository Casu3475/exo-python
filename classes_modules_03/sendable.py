#!/usr/bin/env python3

import time
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
    # Sendable._history.append(sent_at)

# s1 = Sendable("body1", "subject1", "from1", "to1")
# s1.send()
# s2 = Sendable("body2", "subject2", "from1", "to1")
# s2.send()
# print(Sendable.history(cls=Sendable))


