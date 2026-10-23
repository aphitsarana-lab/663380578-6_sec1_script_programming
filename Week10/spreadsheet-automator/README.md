# Week 10: Automating Spreadsheets (Excel & Google Sheets)

This project uses Python's `openpyxl` library to read, process, and write Microsoft Excel `.xlsx` files. It reads sales data from a spreadsheet, calculates the total for each item and the grand total, and saves a formatted report to a new Excel file.

## Key Concepts Demonstrated

* **`openpyxl` Library**: reading, writing, and modifying `.xlsx` files.
* **Workbook & Worksheet Management**: loading, creating, and saving workbooks; accessing and creating sheets.
* **Cell Manipulation**: reading and writing cell values with `sheet.cell(row, column)`.
* **Data Processing**: iterating rows with `iter_rows()`, skipping empty rows, and calculating totals.
* **Basic Formatting**: fonts, fills, borders, alignment, number formats, and merged cells.
* **Column Width Adjustment**: setting column widths from the content length.

## Setup & How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kittynakaa/spreadsheet-automator.git
   cd spreadsheet-automator
   ```

2. **Install dependencies** (a virtual environment is recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   # source venv/bin/activate   # macOS / Linux
   pip install openpyxl
   ```

3. **Prepare input data:** `data/input_sales.xlsx` is already included. Its first sheet has headers in A1–C1 and data from row 2:

   | Product Name | Quantity | Unit Price |
   | :----------- | :------- | :--------- |
   | Laptop       | 2        | 1200.50    |
   | Mouse        | 5        | 25.00      |
   | Keyboard     | 3        | 75.99      |
   | Monitor      | 1        | 300.00     |
   | *(empty row)* |         |            |
   | Printer      | 1        | 150.00     |

   The empty row checks that the script skips blank rows correctly.

4. **Run the script:**
   ```bash
   python main.py
   ```

   Expected output:
   ```
   Starting sales data processing from '...\data\input_sales.xlsx'...
   Workbook '...\data\input_sales.xlsx' loaded successfully.
   New workbook 'new_workbook.xlsx' created.
   Workbook saved to '...\data\output_sales_report.xlsx'.
   Sales report successfully generated and saved to '...\data\output_sales_report.xlsx'.
   ```

## Result

`data/output_sales_report.xlsx` (sheet **Sales Report**):

| Product Name | Quantity | Unit Price | Total Price |
| :----------- | -------: | ---------: | ----------: |
| Laptop       | 2        | 1,200.50   | 2,401.00    |
| Mouse        | 5        | 25.00      | 125.00      |
| Keyboard     | 3        | 75.99      | 227.97      |
| Monitor      | 1        | 300.00     | 300.00      |
| Printer      | 1        | 150.00     | 150.00      |
| **Grand Total:** |      |            | **3,203.97** |

* Header row: bold white text on a green background.
* Grand Total row: bold text on a yellow background, label cells merged (A–C).
* All cells have thin borders; prices use the `#,##0.00` format.

## Project Structure

```
spreadsheet-automator/
├── src/
│   ├── __init__.py            # Python package marker
│   ├── excel_processor.py     # Core logic for Excel manipulation
│   └── data_models.py         # SaleItem dataclass for structured sales data
├── data/
│   ├── input_sales.xlsx        # Sample input Excel file
│   └── output_sales_report.xlsx # Generated output Excel file
├── main.py                    # Application entry point
├── .gitignore
└── README.md
```

## Debugging Spreadsheet Automation

* **`FileNotFoundError`**: make sure `input_sales.xlsx` is in the `data` folder and the name matches exactly.
* **`InvalidFileException`**: the file is corrupted or is an old `.xls` file. `openpyxl` only supports `.xlsx`.
* **`ValueError` / `TypeError`**: a cell has text where a number is expected. The script prints a warning and skips that row.
* **`PermissionError` when saving**: `output_sales_report.xlsx` is open in Excel. Close it and run again.
* **Data mismatches**: the script expects the column order Product Name, Quantity, Unit Price.

## Google Sheets (Conceptual Overview)

Google Sheets can be automated with the Google Sheets API, for example through the `gspread` library. Unlike local Excel files, it needs authentication with a Google Cloud service account or OAuth 2.0, and the credentials file must be kept secret (never commit it to GitHub). Reading and writing cells is similar in idea (`worksheet.cell(row, col).value`, `worksheet.update(...)`), but every call goes over the network and is subject to API rate limits.

## Ethical Notes

* Spreadsheets often contain personal or business-sensitive data. Only process files you are allowed to use.
* Keep API keys and credential files out of the repository (use `.gitignore` / `.env`).
* Always keep a copy of the original file; write results to a new file instead of overwriting the source.

## Extension Ideas

* Google Sheets integration with `gspread`
* Input data validation (missing values, negative numbers)
* Charts with `openpyxl.chart`
* Conditional formatting (e.g., highlight high sales)
* A simple GUI with Tkinter for choosing input/output files

## References

1. https://automatetheboringstuff.com/2e/chapter13/
2. https://openpyxl.readthedocs.io/
3. https://github.com/sapphanyu/Week10_LabX-BASIC_-Automating
