import json

from datetime import datetime

def load_transactions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    executed_transactions = [trans for trans in data if trans.get('state') == 'EXECUTED']
    return executed_transactions


def sort_transactions(transactions):
    transactions.sort(key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return transactions[:5]

def mask_card_number(card_number):
    if len(card_number) >= 10:
        return card_number[:6] + "******" + card_number[-4:]
    else:
        return card_number

def mask_account_number(account_number):
    if len(account_number) >= 4:
        return "****" + account_number[-4:]
    else:
        return account_number



def format_and_print_transactions(transactions):
    for t in transactions:
        date = datetime.strptime(t['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
        description = t['description']
        amount = t['operationAmount']['amount']
        currency = t['operationAmount']['currency']['name']


        from_acc = t.get('from', 'N/A')
        if 'Счет' in from_acc:
            from_acc = "Счет " + from_acc.split()[-1][-4:]
        else:
            from_acc = mask_card_number(from_acc.replace(' ', ''))

        to_acc = t.get('to', 'N/A')
        if 'Счет' in to_acc:
            to_acc = "Счет " + to_acc.split()[-1][-4:]
        else:
            to_acc = mask_card_number(to_acc.replace(' ', ''))

        print(f"{date} {description}")
        print(f"{from_acc} -> {to_acc}")
        print(f"{amount} {currency}\n")
