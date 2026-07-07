import csv
from pathlib import Path

project_folder = Path(__file__).parent
input_file = project_folder / "edi_transaction_report.csv"

total_transactions = 0
accepted_count = 0
rejected_count = 0

file_status = {}

file_rejection_counts = {}

rejection_summary = {}
rejection_detail_by_file = {}

with open(input_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_transactions += 1
        file_name = row["file_name"]

        if file_name not in file_status:
            file_status[file_name] = True

        if row["status"] == "Accepted":
            accepted_count += 1

        elif row["status"] == "Rejected":
            rejected_count += 1
            file_status[file_name] = False

            file_rejection_counts[file_name] = (
                file_rejection_counts.get(file_name, 0) + 1
            )

            rejection_key = f'{row["status_code"]} - {row["status_message"]}'

            rejection_summary[rejection_key] = (
                rejection_summary.get(rejection_key, 0) + 1
            )

            if file_name not in rejection_detail_by_file:
                rejection_detail_by_file[file_name] = {}

            rejection_detail_by_file[file_name][rejection_key] = (
                rejection_detail_by_file[file_name].get(rejection_key, 0) + 1
            )

print("EDI Daily Processing Summary")
print("============================")
print(f"Total Transactions: {total_transactions}")
print(f"Accepted: {accepted_count}")
print(f"Rejected: {rejected_count}")

fully_accepted_files = []
files_with_rejections = []

for file_name, is_fully_accepted in file_status.items():
    if is_fully_accepted:
        fully_accepted_files.append(file_name)
    else:
        files_with_rejections.append(file_name)

print()
print("Fully Accepted Files")
print("--------------------")

for file in sorted(fully_accepted_files):
    print(file)

print()
print("Files with Rejections")
print("---------------------")

for file in sorted(files_with_rejections):
    print(f"{file} - {file_rejection_counts[file]} rejections")

print()
print("Rejection Summary")
print("-----------------")

for rejection, count in sorted(rejection_summary.items()):
    print(f"{rejection}: {count}")

print()
print("Rejection Detail by File")
print("------------------------")

for file_name in sorted(rejection_detail_by_file):
    print(file_name)

    for rejection, count in sorted(rejection_detail_by_file[file_name].items()):
        print(f"    {rejection}: {count}")