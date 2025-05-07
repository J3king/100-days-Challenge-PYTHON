def currency_converter():
    rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'INR': 83.0,
        'GBP': 0.75,
        'JPY': 110.0
    }

    print("Available currencies: ", ', '.join(rates.keys()))
    
    from_currency = input("Convert from (e.g. USD): ").upper()
    to_currency = input("Convert to (e.g. EUR): ").upper()

    if from_currency not in rates or to_currency not in rates:
        print("Unsupported currency.")
        return

    amount = float(input(f"Enter amount in {from_currency}: "))

    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]

    print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")

if __name__ == "__main__":
    currency_converter()
