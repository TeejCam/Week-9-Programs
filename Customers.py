import csv

def menu():
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")

def promptUser(customers):
    while True:
        menu()
        option = input("Please type your choice as a number: ").strip().lower()

        if option == "1":
            sortedByCompany = sortedCustomers(customers, 'CompanyName')
            displaySortedCustomers(sortedByCompany, 'company')

        elif option == "2":
            sortedByContact = sortedCustomers(customers, 'ContactName')
            displaySortedCustomers(sortedByContact, 'contact')

        elif option == "3":
            searchKey = input("Enter a company name or part of a name you'd like to find: ").strip()
            searchCustomers(customers, searchKey, 'CompanyName')

        elif option == "4":
            searchKey = input("Enter a contact name or part of a name you'd like to find: ").strip()
            searchCustomers(customers, searchKey, 'ContactName')

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")

def readCSV(file):
    customers = []
    try:
        with open(file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(row)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
    return customers

def sortedCustomers(customers, keyName):
    return sorted(customers, key=lambda customer: customer[keyName].lower())

def displaySortedCustomers(sortedData, displayFormat):
    for customer in sortedData:
        if displayFormat == 'contact':
            print(f"Contact Name: {customer['ContactName']}, Company Name: {customer['CompanyName']}, Phone: {customer['Phone']}")
        elif displayFormat == 'company':
            print(f"Company Name: {customer['CompanyName']}, Contact Name: {customer['ContactName']}, Phone: {customer['Phone']}")

def searchCustomers(customers, searchKey, fieldName):
    searchKey = searchKey.lower()
    matchingCustomers = [customer for customer in customers if searchKey in customer[fieldName].lower()]

    if not matchingCustomers:
        print(f"No matching customers found with {fieldName} !")
        return
    for customer in matchingCustomers:
        print(f"Company Name: {customer['CompanyName']}, Contact Name: {customer['ContactName']}, Phone: {customer['Phone']}")

if __name__ == "__main__":
    customers = readCSV('northwind.csv')

    sortedByCompany = sortedCustomers(customers, 'CompanyName')
    sortedByContact = sortedCustomers(customers, 'ContactName')

    promptUser(customers)

