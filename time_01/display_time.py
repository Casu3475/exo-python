#!/usr/bin/env python3

import time

def display_time(epoch_format):
  go_time = time.strftime("%T, %A, %w* day of the %W* week of %Y, %B", time.gmtime(epoch_format))
  print(go_time)


display_time(730540800)


