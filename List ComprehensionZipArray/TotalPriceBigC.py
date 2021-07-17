transactions = [10000,20000,30000,40000,50000]
TAX_RATE = 0.08
SERVICE_CHARGE = 0.07

def get_price_tax_service(bill):
    return bill*(1+TAX_RATE+SERVICE_CHARGE)

def main():
    final_prices = [get_price_tax_service(transaction) for transaction in transactions]
    print(final_prices)

if __name__ == '__main__':
    main()