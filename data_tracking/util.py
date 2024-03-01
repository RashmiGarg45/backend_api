import json

from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import gspread
from datetime import datetime,timedelta
from operator import itemgetter

def get_credential(host=''):
    return {
    "type": "service_account",
    "project_id": "team2-404311",
    "private_key_id": "235080bbb2da916163961e5443ff78b3fb8e781f",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC0X9G08OGMfDUn\n83m0do4sbMQhtUg3dAyioRqOSusQmYBbf6NIDAtFRAh7kGa/q2YRaO0aW67s4IBg\nc+xOf/R+LkcFaaE3u2dMD48eZ0mkDMbv668+XZInidWPb27Ga6ZzK5XRWyt2m6Tm\nOw0XzS1h0jxQclwiFz/btxopWKkfLA1+QTNPjYbScZZHdFDYSrCens1JDFqqRr8P\n9mttjIg7fkX+eBo3RS62XWNNjvbK1e5KBYuv43x/TvaBOL14lpBrjRX7Wg9tK7Iq\n3Ho3E8WVxqKH1ohu+mtgz/6tfsmnC6WtZNTAxSfJeiZNST2odybgaxAudKEKmIRT\nftqeXWXFAgMBAAECggEAJAdBqY012CxVJ8o7xJ6rrlb5ZCxEJQNypKdeWQ7A3jtz\nBpO7px/0vlyk/x1sUJupUw/s0EeA7MK5EcsF5/Yp/Ww79mpPcAToUKqI8U87R9/f\nervOcLwa/ffLpw9ghpSpFjceAUffKh1TtkMUTe1HQ9NNBdqZ6ZtQP5BW0uxpN5bs\nrsQKkb54Z3h96yCUyQuN4MbKmDOwgtzlx767pqCYMSt99Ak6CvkyDst10y37g165\nLKJIYL2PrdqCr68aR/0YllCFz502K3QEcJ3vjb2mOHhr1A5oSA4lYSb2sfxNnQFo\nKb1PYxmPC1anEuJGjnmHO5Owu6cbbQGAvsHgMDCGjwKBgQDZ08HrEaBjr0iQzkYy\ncwm/8ly3B6KwsY3LYOF/NOprbFKdX2dnJTySFzSyZbwjguAPm6PMtubI2NZuHXim\nN2F3QJPcM93Yzsk4iuyAruB0d2tuHm8DChFTjowjPmqMMmZPf4tyRnv0ERpgpQBP\nrLZCuEz2C3NxscNYVBSjDwewZwKBgQDT+9Yxag3VD30f9bk+Nf/UUdtA29edRNE6\nYu4EjUR9rPGTD2Rv/Scb6bnsLXUANtqbkTRxoyWB3KhCQecbJ4XVn2Ol3Q4iy5hJ\nNfmIzAvudxRvVbxtZkVmQVtgXjE9a5dIQJMgbbFdeYHIMG2WvQuDdY0+VpjP6SOY\n0pv/kb7s8wKBgFsoFQTskXRmDDYdPJ8sKS5cnJQz68+J3k74MiXr3RYrdL9LB5jQ\nqnJwp6rojD1ILcAaYAfxms7+f24Bg1X74xvmuHn0cqiikO7KpIKNrHzQ5PJmZgqd\nkfanttmg6zHUfaBTPeYKvSC8b492PZUaMAPn4L0uuZcgzyENvr0mMw+NAoGBAJLb\n5sFnItwXlez9VG+IA4u5hfdCFvdKhNU5UoJuyCN1HAtw33lCXcTVwMuhlmwmlH6w\nMzADAeocz6jPdWd3kx2zBdsT8UYj3IXj0dN24VE8yDh1okv8TVoRL1ftCZnunukc\na5FMzVLf6gyhmFqU75QMbWTho45uiw3F4vNEqowHAoGAAUL4kZ5HpXWSy3oEh/J1\nfJtqbOtQzEUzL1+EotwpSFNbrlre0Yr2eBkBvwF0KyBtHIrwEWBfTwW36hpzoU6J\nwFg0eNKrWwKgTlfcd889pYo0zWhQAt4DJWqBl/T+Se7dzbhKEb8BMB7k6O0g5BnQ\n/VZu8DbqBvoZmKIptSRrqgg=\n-----END PRIVATE KEY-----\n",
    "client_email": "team2-bot@team2-404311.iam.gserviceaccount.com",
    "client_id": "111403532864044151953",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/team2-bot%40team2-404311.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}


def googleChatBot_send_message(space_name, message="",host=''):
    # Specify required scopes.
    SCOPES = ['https://www.googleapis.com/auth/chat.bot']

    json_credential = get_credential(host)
    # Specify service account details.
    CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_dict(
        json_credential, SCOPES)

    # Build the URI and authenticate with the service account.
    chat = build('chat', 'v1', http=CREDENTIALS.authorize(Http()))

    # Create a Chat message.
    result = chat.spaces().messages().create(
        parent='spaces/{}'.format(space_name),
        body=message
    ).execute()
    return result


def get_list_data_from_raw(data):
    sheet_url = data.get('teamBTSheetURL','https://docs.google.com/spreadsheets/d/1CIcoZDETrXnRt4HXmjd_23ri6y5jz5il2j2RKiCMqYY')
    if not sheet_url or sheet_url=='None':
        message = 'Seems like you do not have updated sheet url in .env file'
        print('[-] Error:{}'.format(message))

    subsheet_name = data.get('subsheet_name','Business Team [ALLOTTED] NEW')
    if not sheet_url or sheet_url=='None':
        message = 'Seems like you do not have provided subsheet name in request.'
        print('[-] Error:{}'.format(message))

    credentials = get_credential()
  
    Sheet_credential = gspread.service_account_from_dict(credentials)
    spreadsheet = Sheet_credential.open_by_url(sheet_url)
    print('[+] Subsheet Access: {}'.format(subsheet_name))
    worksheet = spreadsheet.worksheet(subsheet_name)
    list_of_lists = worksheet.get_all_values()
    print('[+] Accessed Sheet! Now will start reading things.')    

    header_row = []
    print('[+] Searching For Header Row.')    
    header_row_index = -1
    for row_index in range(len(list_of_lists)):
        row = list_of_lists[row_index]
        any_col_empty = False
        header_row_index += 1
        for col_value in row:
            if col_value == '':
                any_col_empty = True
                break
        if not any_col_empty:
            header_row = row
            break
    
    print('[+] Header Row Found : {}'.format(header_row))    

    work_data_map = []
    for row in list_of_lists[header_row_index+1:]:
        subheader_row = []
        for col in row:
            if col!= '':
                subheader_row.append(col)
        
        if len(subheader_row)>1:
            header_index = 0
            dict__ = {}
            for header_item in header_row:
                dict__[header_item] = row[header_index]
                header_index +=1
            work_data_map.append(dict__)
    return work_data_map
