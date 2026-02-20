"""
CSV export utilities for tasks.
Converts task data to CSV format.
"""
import csv
import io
from typing import List, Dict


def tasks_to_csv_bytes(tasks: List[Dict[str, any]]) -> bytes:
    """
    Convert a list of task dictionaries to CSV bytes.
    
    Args:
        tasks: List of task dictionaries with keys: id, text, user, created_at
    
    Returns:
        UTF-8 encoded bytes of the CSV content
    """
    # Create StringIO buffer for CSV writing
    output = io.StringIO()
    
    # Define CSV header
    fieldnames = ["id", "text", "user", "created_at"]
    
    # Write CSV data
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    
    for task in tasks:
        writer.writerow({
            "id": task["id"],
            "text": task["text"],
            "user": task["user"],
            "created_at": task["created_at"]
        })
    
    # Get string content and encode to UTF-8 bytes
    csv_string = output.getvalue()
    output.close()
    
    return csv_string.encode("utf-8")
