#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = '''
           "�A��C����(z%�����j��.�
�#���q�<�/cc�Ab����}&Jp���S��e&�j"X&-Ұ#On�Q�5:�"�@����]2�F�;se��/ �{�
���P@�r���^T��'''
import urllib
attack= urllib.quote(blob)
if len(attack)==224:
    print "I come in peace."
else:
    print "Prepare to be destroyed!"
