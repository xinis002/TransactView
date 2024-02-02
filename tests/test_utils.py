import unittest
from unittest.mock import mock_open, patch
import json



from utils import load_transactions, sort_transactions, mask_card_number, mask_account_number, format_and_print_transactions

class TestTransactions(unittest.TestCase):
    def test_load_transactions(self):
        mock_data = json.dumps([
            {"state": "EXECUTED", "date": "2023-01-01T12:00:00.000", "description": "Transaction 1"},
            {"state": "PENDING", "date": "2023-01-02T12:00:00.000", "description": "Transaction 2"},
            {"state": "EXECUTED", "date": "2023-01-03T12:00:00.000", "description": "Transaction 3"}
        ])
        with patch('builtins.open', mock_open(read_data=mock_data)):
            transactions = load_transactions('dummy_path')
            self.assertEqual(len(transactions), 2)
            self.assertEqual(transactions[0]['description'], 'Transaction 1')
            self.assertEqual(transactions[1]['description'], 'Transaction 3')

    def test_sort_transactions(self):
        transactions = [
            {"date": "2023-01-03T12:00:00.000"},
            {"date": "2023-01-01T12:00:00.000"},
            {"date": "2023-01-05T12:00:00.000"},
            {"date": "2023-01-02T12:00:00.000"},
            {"date": "2023-01-04T12:00:00.000"},
            {"date": "2023-01-06T12:00:00.000"}
        ]
        sorted_transactions = sort_transactions(transactions)
        self.assertEqual(len(sorted_transactions), 5)
        self.assertEqual(sorted_transactions[0]['date'], '2023-01-06T12:00:00.000')

    def test_mask_card_number(self):
        self.assertEqual(mask_card_number('1234567890123456'), '123456******3456')
        self.assertEqual(mask_card_number('12345'), '12345')

    def test_mask_account_number(self):
        self.assertEqual(mask_account_number('12345678'), '****5678')
        self.assertEqual(mask_account_number('123'), '123')

    @patch('builtins.print')
    def test_format_and_print_transactions(self, mock_print):
        transactions = [{
            "date": "2023-01-01T12:00:00.000",
            "description": "Test Transaction",
            "operationAmount": {"amount": 100, "currency": {"name": "USD"}},
            "from": "1234567890123456",
            "to": "Account 12345678"
        }]
        format_and_print_transactions(transactions)
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()
