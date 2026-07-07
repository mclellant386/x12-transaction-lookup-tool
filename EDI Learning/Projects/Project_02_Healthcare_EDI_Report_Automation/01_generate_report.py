import csv
import random
from datetime import datetime
from pathlib import Path

rows = []

status_options = [
    {
        "status": "Accepted",
        "status_code": "A001",
        "status_message": "Transaction accepted"
    },
    {
        "status": "Rejected",
        "status_code": "R101",
        "status_message": "Invalid member ID"
    },
    {
        "status": "Rejected",
        "status_code": "R202",
        "status_message": "Missing required segment"
    }
]

transaction_number = 1

for batch_number in range(1, 6):
    batch_id = f"BATCH{batch_number:03}"
    file_name = f"837_CENTENE_{batch_id}.edi"

    for claim_number in range(1, 21):
        status_result = random.choices(
    status_options,
    weights=[90, 6, 4],
    k=1
)[0]
        transaction = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "transaction_id": f"TXN{transaction_number:06}",
            "batch_id": batch_id,
            "trading_partner": "Centene",
            "payer_id": "11315",
            "receiver_id": "CENTENE",
            "transaction_type": "837",
            "mode": "batch",
            "status": status_result["status"],
            "status_code": status_result["status_code"],
            "status_message": status_result["status_message"],
            "claim_count": 1,
            "file_name": file_name,
            "processing_time_seconds": 12.4
        }

        rows.append(transaction)
        transaction_number += 1

project_folder = Path(__file__).parent
output_file = project_folder / "edi_transaction_report.csv"

with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Report generated: {output_file}")