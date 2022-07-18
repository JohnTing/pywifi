#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from __future__ import annotations


"""Define WiFi Profile."""

from typing import List
from pywifi.const import *


class Profile():

    def __init__(self, auth=AUTH_ALG_OPEN, akm=[AKM_TYPE_NONE], 
    cipher=CIPHER_TYPE_NONE, ssid: str=None, bssid: str=None, 
    key: str=None):
    
        self.id = 0
        self.auth:int = auth
        self.akm: List[int] = akm
        self.cipher: int = cipher
        self.ssid: str = ssid
        self.bssid: str = bssid
        self.key: str = key
        self.signal: int = None
        self.freq: int = None


    def process_akm(self):

        if len(self.akm) > 1:
            self.akm = self.akm[-1:]

    def __eq__(self, profile: Profile):

        if profile.ssid:
            if profile.ssid != self.ssid:
                return False

        if profile.bssid:
            if profile.bssid != self.bssid:
                return False

        if profile.auth:
            if profile.auth!= self.auth:
                return False

        if profile.cipher:
            if profile.cipher != self.cipher:
                return False

        if profile.akm:
            if set(profile.akm).isdisjoint(set(self.akm)):
                return False

        return True
