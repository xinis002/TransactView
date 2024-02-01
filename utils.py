import json

from datetime import datetime

def load_transactions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    executed_transactions = [trans for trans in data if trans.get('state') == 'EXECUTED']
    return executed_transactions


def sort_transactions(transactions):
    transactions.sort(key=lambda x: datetime.strftime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return transactions[:5]

def mask_card_number(card_number):
    return card_number[:6] + "******" + card_number[-4:]


def mask_account_number(account_number):
    return "****" + account_number[-4:]


def format_and_print_transactions(transactions):
    for trans in transactions:
        date = datetime.strptime(trans['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
        amount = trans['operationAmount']['amount']
        currency = trans['operationAmount']['currency']['name']
        description = trans['description']
        from_account = trans.get('from', '')
        to_account = trans.get('to', '')

        if from_account.startswith('Счет'):
            from_account = mask_account_number(from_account.split()[-1])
        else:
            from_account = mask_card_number(from_account.split()[-1])

        if to_account.startswith('Счет'):
            to_account = mask_account_number(to_account.split()[-1])
        else:
            to_account = mask_card_number(to_account.split()[-1])

        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount} {currency}\n")