from utils import format_and_print_transactions, sort_transactions, load_transactions,

def main():
    file_path = 'transactions.json'
    transactions = load_transactions(file_path)
    sorted_transactions = sort_transactions(transactions)
    format_and_print_transactions(sorted_transactions)

if __name__ == "__main__":
    main()
