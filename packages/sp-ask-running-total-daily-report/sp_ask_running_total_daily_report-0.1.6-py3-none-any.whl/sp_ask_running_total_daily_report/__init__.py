__version__ = '0.1.6'

import json
import os
import datetime
from pprint import pprint as print
import calendar
import datetime

import lh3.api as lh3


client = lh3.Client()
chats = client.chats()

#chats_this_day = chats.list_day(2019,8,29)


#print(len(chats_this_day))
#print(chats_this_day[0])

import csv
import xlrd
import pandas as pd
import numpy as np


def create_excel_file_no_column_adjusted(filename, data):
    df = pd.DataFrame(data)
    df.index = np.arange(1, len(df)+1)
    df.to_excel(filename + '.xlsx')
    print(filename + '.xlsx')

def create_excel_file(filename, data):
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter(filename+".xlsx", engine='xlsxwriter')
    df.to_excel(writer)  # send df to writer
    worksheet = writer.sheets['Sheet1']  # pull worksheet object
    for idx, col in enumerate(df):  # loop through all columns
        series = df[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            )) + 1  # adding a little extra space
        worksheet.set_column(idx, idx, max_len)  # set column width
    writer.save()
    print(filename+".xlsx")


FRENCH_QUEUES = ['algoma-fr', 'clavardez', 'laurentian-fr', 'ottawa-fr',
        'saintpaul-fr', 'western-fr', 'york-glendon-fr']
SMS_QUEUES = ['carleton-txt', 'clavardez-txt', 'guelph-humber-txt',
            'mcmaster-txt', 'ottawa-fr-txt', 'ottawa-txt',
            'scholars-portal-txt', 'western-txt', 'york-txt']
PRACTICE_QUEUES = ['practice-webinars', 'practice-webinars-fr', 'practice-webinars-txt']

def french_queues(chats):
    french = list()
    for chat in chats:
        if chat.get('queue') in FRENCH_QUEUES:
            french.append(chat)
    return french

def sms_queues(chats):
    sms = list()
    for chat in chats:
        if chat.get('queue') in SMS_QUEUES:
            sms.append(chat)
    return sms

def remove_practice_queues(chats_this_day):
    res = [chat for chat in chats_this_day if not "practice" in chat.get("queue")]
    return res


def create_report(year=2019, month=2):
    given_date = datetime.datetime(year, month, 1)
    month = given_date.month
    month_name = given_date.strftime("%B")
    filename = str(month) + "-" + month_name

    first_day, last_day = calendar.monthrange(year, month)

    total_answered_chats = []
    days = []
    data = []
    for day in range(1,last_day+1):
        all_chats = chats.list_day(year,month,day)
        chats_this_day = remove_practice_queues(all_chats)
        chat_not_none = [chat for chat in chats_this_day if chat.get("accepted") != None]
        unanswered_chats = [chat for chat in chats_this_day if chat.get("accepted") is None]
        answered_chats_nbr = len(chats_this_day)- len(unanswered_chats)
        french_chats = french_queues(chat_not_none)
        sms_chats = sms_queues(chat_not_none)
        print(str(day)+": "+ str(answered_chats_nbr))

        total_answered_chats.append(answered_chats_nbr)
        days.append(day)
        data.append({
            'Date': str(year)+'-'+str(month)+'-'+str(day),
            'Total chats': len(all_chats),
            'Total Answered Chats': answered_chats_nbr,
            'Total UnAnswered Chats': len(unanswered_chats),
            'Total French Answered': len(french_chats),
            'Total SMS Answered': len(sms_chats)
            })

    create_excel_file(filename, data)



if __name__ == '__main__':
    create_report(2019, 11)

    for month_number in range(1, 13):
        pass
        #create_report(2019, month_number)
