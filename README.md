# Script Programming Labs — 663380578-6

ทุก Lab จะพิมพ์ `รหัสนักศึกษา: 663380578-6` ตอนรัน เพื่อให้เห็นในภาพแคปหน้าจอ

| Week | โฟลเดอร์ | หัวข้อ |
|---|---|---|
| 7 | `Week7/web-scraping-intro` | Web Scraping (requests + BeautifulSoup) |
| 8 | `Week8/data-processor` | อ่าน/เขียน CSV และ JSON |
| 8 | `Week8/my-oop-task-manager` | OOP Task Manager |
| 10 | `Week10/spreadsheet-automator` | Automating Spreadsheets (openpyxl) |
| 11 | `Week11/enhanced-task-manager-design` | Enhanced Task Manager |
| 11 | `Week11/agentic-document-automator` | Word / PDF Automation |
| 12 | `Week12/email-sms-automator` | ส่ง Email / SMS อัตโนมัติ |

---

## ขั้นตอนที่ทำครั้งเดียว (Windows)

เปิด PowerShell แบบ **Run as Administrator** แล้วรัน (ตอบ `Y`):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## ขั้นตอนรันแต่ละ Lab (ทำซ้ำทุก Lab)

```powershell
cd <โฟลเดอร์ของ Lab นั้น>
python -m venv venv
venv\Scripts\Activate.ps1
pip install <แพ็กเกจของ Lab นั้น ดูตารางด้านล่าง>
python main.py
```

macOS: ใช้ `python3 -m venv venv` และ `source venv/bin/activate`

| Lab | ติดตั้ง | รัน | หมายเหตุ |
|---|---|---|---|
| Week7 web-scraping-intro | `pip install -r requirements.txt` | `python main.py` | ต้องต่ออินเทอร์เน็ต |
| Week8 data-processor | ไม่ต้องติดตั้ง | `python main.py` | ได้ไฟล์ `data/output_*.csv/json` |
| Week8 my-oop-task-manager | ไม่ต้องติดตั้ง | `python main.py` | เมนูโต้ตอบ: ลองกด 1 เพิ่มงาน, 2 ดูรายการ, 3, 4, 5 ออก. เทสต์: `python -m unittest discover -s tests` |
| Week10 spreadsheet-automator | `pip install openpyxl` | `python main.py` | ได้ไฟล์ `data/output_sales_report.xlsx` เปิดใน Excel แล้วแคปด้วย |
| Week11 enhanced-task-manager-design | ไม่ต้องติดตั้ง | `python main.py` | เมนูภาษาไทย 0–9. เทสต์: `python -m unittest discover -s tests` |
| Week11 agentic-document-automator | `pip install -r requirements.txt` | `python create_sample_files.py` แล้ว `python main.py` | ได้ไฟล์ใน `documents/` เปิด `generated_report.docx`, `merged_docs.pdf`, `watermarked_document.pdf` แล้วแคป |
| Week12 email-sms-automator | `pip install -r requirements.txt` | `copy .env.example .env` → แก้ `.env` → `python main.py` | ต้องใช้ Gmail App Password (ดู README ในโฟลเดอร์). เทสต์ไม่ต้องใช้รหัส: `python -m unittest discover -s tests` |

## สิ่งที่ต้องแคป

- หน้าต่าง terminal ให้เห็น `(venv)`, คำสั่งที่รัน และผลลัพธ์ที่มี `รหัสนักศึกษา: 663380578-6`
- Lab ที่สร้างไฟล์ (Week8, Week10, Week11 document) แคปไฟล์ผลลัพธ์ที่เปิดดูแล้วด้วย
- Week12 แคปอีเมลที่ได้รับใน Gmail (ในเนื้อหาจะมีชื่อ + รหัส)
- เก็บรูปไว้ในโฟลเดอร์ `screenshots/` ของแต่ละ Lab แล้ว commit + push

> ห้าม commit ไฟล์ `.env` และโฟลเดอร์ `venv/` (ใส่ไว้ใน `.gitignore` แล้ว)
