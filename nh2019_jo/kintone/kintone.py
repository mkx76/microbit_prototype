#!/usr/bin/python
# _*_ coding: utf-8 _*_

import os, sys, time, requests
from datetime import datetime, timedelta, timezone
import random

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_TOKEN= os.environ.get("API_TOKEN")

URL = "https://mkx.cybozu.com/k/v1/record.json"
PARAMS = {
  "app": 7,
  "record": {
    "range": {
      "value": 0
    },
    "str_datetime": {
      "value": 0
    }
  }
}
API_TOKEN = "sf3xELObnBqK2Pm92Il4kcCKUOoXbt7GsxkWz6U0"

JST = timezone(timedelta(hours=+9), 'JST')

def post_kintone(url, api_token, value):
  """kintoneにレコードを1件登録する関数"""
  headers = {"X-Cybozu-API-Token": api_token, "Content-Type" : "application/json"}
  PARAMS["record"]["range"]["value"] = value
  nowtime = datetime.now(JST)
  PARAMS["record"]["str_datetime"]["value"] = nowtime.strftime("%Y-%m-%d %H:%M:%S")
  resp = requests.post(url, json=PARAMS, headers=headers)

  return resp

if __name__ == "__main__":
  for i in range(10):
    value = random.randint(1, 40)
    RESP = post_kintone(URL, API_TOKEN, value)
    # print(RESP.text)
    time.sleep(1)
