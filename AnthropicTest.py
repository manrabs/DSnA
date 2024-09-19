from datetime import datetime, timedelta
from collections import defaultdict, deque

# Constants
MILLISECONDS_IN_1_DAY = 86400000

class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.transaction_values = defaultdict(int)  # Default value of 0 for new keys
        self.transfers = {}
        self.transfer_counter = 0

    def create_account(self, timestamp, account_id):
        if account_id in self.accounts:
            return "false"
        else:
            self.accounts[account_id] = 0
            return "true"

    def deposit(self, timestamp, account_id, amount):
        if account_id not in self.accounts:
            return ""
        else:
            self.accounts[account_id] += amount
            self.transaction_values[account_id] += amount
            return str(self.accounts[account_id])

    def pay(self, timestamp, account_id, amount):
        if account_id not in self.accounts or self.accounts[account_id] < amount:
            return ""
        else:
            self.accounts[account_id] -= amount
            self.transaction_values[account_id] += amount
            return str(self.accounts[account_id])

    def transfer(self, timestamp, source_account_id, target_account_id, amount):
        if source_account_id == target_account_id:
            return ""
        if source_account_id not in self.accounts or target_account_id not in self.accounts:
            return ""
        if self.accounts[source_account_id] < amount:
            return ""

        # Withhold the amount from the source account
        self.accounts[source_account_id] -= amount
        transfer_id = f"transfer{self.transfer_counter + 1}"
        self.transfer_counter += 1

        expiration_time = timestamp + timedelta(milliseconds=86400000)
        self.transfers[transfer_id] = {
            "source": source_account_id,
            "target": target_account_id,
            "amount": amount,
            "expiration_time": expiration_time,
            "accepted": False
        }
        return transfer_id

    def accept_transfer(self, timestamp, account_id, transfer_id):
        if transfer_id not in self.transfers:
            return "false"

        transfer = self.transfers[transfer_id]
        if transfer["accepted"]:
            return "false"
        if transfer["target"] != account_id:
            return "false"
        if timestamp > transfer["expiration_time"]:
            # Expire the transfer and refund the amount to the source account
            self.accounts[transfer["source"]] += transfer["amount"]
            del self.transfers[transfer_id]
            return "false"

        # Accept the transfer
        self.accounts[transfer["target"]] += transfer["amount"]
        self.transaction_values[transfer["source"]] += transfer["amount"]
        self.transaction_values[transfer["target"]] += transfer["amount"]
        transfer["accepted"] = True
        return "true"

    def top_activity(self, timestamp, n):
        # Include all accounts in the transaction values
        for account_id in self.accounts:
            if account_id not in self.transaction_values:
                self.transaction_values[account_id] = 0
        
        # Sort accounts based on total transaction values, and then alphabetically by account_id
        sorted_accounts = sorted(self.transaction_values.items(), key=lambda x: (-x[1], x[0]))
        top_n_accounts = sorted_accounts[:n]

        result = ", ".join([f"{account_id}({value})" for account_id, value in top_n_accounts])
        return result

# Helper function to parse and process commands
def process_commands(commands):
    banking_system = BankingSystem()
    results = []

    for command in commands:
        operation = command[0]
        timestamp = datetime.fromtimestamp(int(command[1]))
        if operation == "CREATE_ACCOUNT":
            account_id = command[2]
            result = banking_system.create_account(timestamp, account_id)
        elif operation == "DEPOSIT":
            account_id = command[2]
            amount = int(command[3])
            result = banking_system.deposit(timestamp, account_id, amount)
        elif operation == "PAY":
            account_id = command[2]
            amount = int(command[3])
            result = banking_system.pay(timestamp, account_id, amount)
        elif operation == "TRANSFER":
            source_account_id = command[2]
            target_account_id = command[3]
            amount = int(command[4])
            result = banking_system.transfer(timestamp, source_account_id, target_account_id, amount)
        elif operation == "ACCEPT_TRANSFER":
            account_id = command[2]
            transfer_id = command[3]
            result = banking_system.accept_transfer(timestamp, account_id, transfer_id)
        elif operation == "TOP_ACTIVITY":
            n = int(command[2])
            result = banking_system.top_activity(timestamp, n)
        else:
            result = "Invalid command"

        results.append(result)
    
    return results

# Example usage
queries = [
    ["CREATE_ACCOUNT", "1", "account1"],
    ["CREATE_ACCOUNT", "2", "account2"],
    ["DEPOSIT", "3", "account1", "2000"],
    ["DEPOSIT", "4", "account2", "3000"],
    ["TRANSFER", "5", "account1", "account2", "5000"],
    ["TRANSFER", "16", "account1", "account2", "1000"],
    ["ACCEPT_TRANSFER", "20", "account1", "transfer1"],
    ["ACCEPT_TRANSFER", "21", "non-existing", "transfer1"],
    ["ACCEPT_TRANSFER", "22", "account1", "transfer2"],
    ["ACCEPT_TRANSFER", "25", "account2", "transfer1"],
    ["ACCEPT_TRANSFER", "30", "account2", "transfer1"],
    ["TRANSFER", "40", "account1", "account2", "1000"],
    ["ACCEPT_TRANSFER", str(45 + MILLISECONDS_IN_1_DAY), "account2", "transfer2"],
    ["TRANSFER", str(50 + MILLISECONDS_IN_1_DAY), "account1", "account1", "1000"]
]

results = process_commands(queries)
for result in results:
    print(result)
