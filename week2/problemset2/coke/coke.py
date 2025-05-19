def main():
    amount_due = 50


    while True:
        print(f"Amount Due: {amount_due}")
        insert_coin = int(input("Insert Coin: ").strip())

        if insert_coin in (25, 10, 5):
                amount_due -= insert_coin
        else:
            continue

        if amount_due <= 0:
            print(f"Change Owed: {abs(amount_due)}")
            break


main()


