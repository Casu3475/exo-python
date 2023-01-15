#!/usr/bin/env python3

import time
from sendable import Sendable

class Private(Sendable):
    def send(self):
        # super().send(self)
        if self._sent_at:
            raise Exception("DataAlreadySent")
        else:
            self._sent_at = time.time()


# p1 = Private("body3", "subject3", "from2", "to2")
# p1.send()
# print(Sendable.history(cls=Private))
