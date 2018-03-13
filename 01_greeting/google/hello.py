#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import json
import sys

input = json.load(sys.stdin)

print("Content-type: application/json\n\n")

output = {
  "speech": u"こんにちは"
}

json.dump(output, sys.stdout)