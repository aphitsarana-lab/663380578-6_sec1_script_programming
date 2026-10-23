# รหัสนักศึกษา: 663380578-6
# spreadsheet-automator/main.py
import os

from src.excel_processor import ExcelProcessor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


STUDENT_ID = "663380578-6"


def main():
    """
    Main entry point for the spreadsheet automation application.
    """
    print(f"รหัสนักศึกษา: {STUDENT_ID}")
    data_dir = os.path.join(BASE_DIR, 'data')
    input_file = os.path.join(data_dir, 'input_sales.xlsx')
    output_file = os.path.join(data_dir, 'output_sales_report.xlsx')

    # Ensure the 'data' directory exists
    os.makedirs(data_dir, exist_ok=True)

    # Check if the input file exists as it's required for the prototype
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        print("Please create 'input_sales.xlsx' in the 'data' folder with sample sales data "
              "(Product Name, Quantity, Unit Price).")
        print("Refer to the README.md for example content.")
        return

    processor = ExcelProcessor()
    print(f"Starting sales data processing from '{input_file}'...")
    success = processor.process_sales_data(input_file, output_file)

    if success:
        print(f"Sales report successfully generated and saved to '{output_file}'.")
    else:
        print("Failed to generate sales report.")


if __name__ == "__main__":
    main()
