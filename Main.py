import pdfplumber
import pandas as pd
import tkinter as tk

def extract_table_from_pdf(pdf_path, page_number):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Get the specified page
        page = pdf.pages[page_number]

        # Extract tables
        tables = page.extract_tables()

        # Process and print each table
        for table in tables:
            df = pd.DataFrame(table)  # Convert to a DataFrame for better formatting
            print(df.to_string(index=False))  # Print the table


# Path to your PDF file and page number (0-indexed)
pdf_path = "test2.pdf"
extract_table_from_pdf(pdf_path, page_number=0)  # Example: Extract table from the first page
