#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers

appid = '1252480325'
secret_id = 'AKIDiLQQGy9p253zpJOIIDiHj2Nh9cChmGWe'
secret_key = 'hEdqurOmz5lJfrrfRJyWt56vqdLvLadU'
bucket = 'imagetest'

client = Client(appid, secret_id, secret_key, bucket)
client.use_http()
client.set_timeout(30)

#单个或多个图片file
result = client.idcard_detect(CIFiles(['idcard.jpg']), 0)