import csv

def main():
    with open(r'C:/Users/gamer/Downloads/MarketDataTest.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
main()