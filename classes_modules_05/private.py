#!/usr/bin/env python3

import time
from sendable import Sendable

class Private(Sendable):
    def send(self):
        if self._sent_at:
            raise Exception("DataAlreadySent")
        else:
            self._sent_at = time.time()
            

# p1 = Private("body", "subject", "from2", "to2")
# p1.send()
# print(Sendable.history())
