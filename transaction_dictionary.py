transactions = {
"270": "Eligibility Inquiry",
"271": "Eligibility Response",
"276": "Claim Status Request",
"277": "Claim Status Response",
"277CA": "Claim Acknowledgment",
"278": "Prior Authorization",
"820": "Premium Payment",
"834": "Benefit Enrollment",
"835": "Electronic Remittance Advice",
"837": "Healthcare Claim",
"999": "Implementation Acknowledgment"
}

print("Healthcare X12 Lookup Tool")
print("--------------------------")

print("Search by:")
print("1 - Transaction Code")
print("2 - Description")

choice = input("Choice: ")

if choice == "1":
    code = input("Enter a transaction code: ")

    if code in transactions:
        print(f"{code}: {transactions[code]}")
    else:
        print(f"{code}: Transaction code not found.")

elif choice == "2":
    keyword = input("Enter a keyword: ")

    print(f"\nResults for: {keyword}")

    for code, description in transactions.items():
        if keyword.lower() in description.lower():
            print(f"{code}: {description}")

else:
    print("Invalid choice.")