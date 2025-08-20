def calculate_interest(principal, rate, time):
    return principal * rate * time / 100


def format_currency(amount, symbol="$"):
    return f"{symbol}{amount:,.2f}"


def is_valid_account(account_number):
    return str(account_number).isdigit() and len(str(account_number)) == 10


def mask_sensitive_info(data, visible_chars=4):
    return "*" * (len(data) - visible_chars) + data[-visible_chars:]


def transfer_funds(sender_balance, receiver_balance, amount):
    if amount > sender_balance:
        raise ValueError("Insufficient funds.")
    return sender_balance - amount, receiver_balance + amount
