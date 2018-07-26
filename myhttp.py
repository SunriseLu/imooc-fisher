"""
-*- coding: utf-8 -*-
@Time    : 2018/7/23 22:44
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : myhttp.py
"""
import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
