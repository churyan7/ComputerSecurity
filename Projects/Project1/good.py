#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = '''
           "�A��C����(z%4����j��.�
�#���q�<�/cc��@b����}&Jp��jS��e&�j"X&-Ұ#On�Q�5:&"�@����]2�F�;se��/ |�
���P@�r��U^T��'''
import urllib
attack= urllib.quote(blob)
if len(attack)==224:
    print "I come in peace."
else:
    print "Prepare to be destroyed!"
