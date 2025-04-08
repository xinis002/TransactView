# 💳 TransactView: Customer Transaction Widget
TransactView is a lightweight Python backend utility that filters and displays a customer's most recent successful banking transactions.
It’s ideal for integrating into dashboards or frontend account widgets.

## 🚀 Features
> - Filters only successful transactions
>
> - Sorts by date to show the most recent
>
> - Returns the last N transactions
>
> - Includes unit tests for logic validation

## 📁 Project Structure
```bash
TransactView/
├── main.py              → Main script 
├── utils.py             → Core functions: filtering, sorting
├── transactions.json    → Sample transaction dataset
├── tests/
│   └── test_utils.py    → Unit tests
└── README.md            → Project overview 
```

## 📥 Installation
### 💻 Local Development

#### Clone the Repository:
```bash
git clone https://github.com/xinis002/TransactView.git
```

#### Create and Activate a Virtual Environment:
##### Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
##### Windows
```bash
python3 -m venv venv
venv\Scripts\activate
```

#### Run the app
```bash
python main.py
```

## 🧮 Sample Data Format
```bash
[
  {
    "transaction_id": "TX123456",
    "status": "SUCCESS",
    "amount": 250.00,
    "currency": "USD",
    "timestamp": "2024-04-08T10:30:00"
  }
]
```

## 🤝 Contributing
> Contributions are welcome! 
> Please fork the repository and submit a pull request with your changes.
> 1. Fork the repository
> 2. Create a new branch ```git checkout -b feature-name```
> 3. Commit your changes
> 4. Push to your fork
> 5. Open a pull request

## 📝 License
This project is open-source and available under the MIT License.


