import csv


def lookup():
    while True:
        # Request user input - Name of company
        search = input("What company do you need the symbol for? :").title()

        # Load list from csv and create Dictionary
        with open('symbols_list.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

        # For each row check "name" against search criteria if match found print symbol
        # added printing of company name as some have similar results e.g. apple = AAPL & APLE
            for row in csv_reader:
                if search in row["Name"]:
                    print(row["Symbol"], "|", row["Name"])
                else:
                    continue

        continue
