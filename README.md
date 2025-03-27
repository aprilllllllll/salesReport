# Avg Invoice by date range Report Generator

This script processes transaction history exported from SV's **"YUKI - INVOICE BY DATE RANGE"** feature to generate a monthly sales report and a visual chart.

---

## 📝 CSV Export Instructions

1. In SV, navigate to:

   ```
   Report Generate -> Transaction History -> Transaction History -> YUKI - INVOICE BY DATE RANGE
   ```

2. Apply filter:
   - `Invoice Date` → Select your desired date range

3. Export the CSV file.

---

## 🚀 How to Run

1. Move the exported CSV file into the project folder.
   - **The file name must be exactly:** `YUKI-INVOICE BY DATE RANGE.csv`
   - ✅ **Make sure there are NO other `.csv` or `.png` files in the folder. If it is, please delete it.**

2. Run the script:
   ```bash
   ./run.sh
   ```

3. After execution, then close it, you will get:
   - A monthly sales report: `YYYY-MM-report.csv`
   - A chart: `avg_invoice_chart.png`

---

## 📊 Sales Calculation Guidelines

- **Layaway Sales**
  - Only include **completed layaway** transactions in the total.
  - If a product hasn't been picked up, **do not include** it.

- **Account Payments**
  - **Do not count** account payments as part of the sales total.

- **Tax Exclusion**
  - Sales are calculated **before tax**. Tax is **excluded**.

- **Returns**
  - All returns must be **deducted** from total sales.

---

## ⚠️ Known Issues / Notes

- If a **return cancels out a sale** (e.g., return - sale = 0), it still counts as **one invoice**
- Layaway logic may require manual validation in edge cases

---

## 📁 Output Example

```
📄 2025-03-report.csv
📊 avg_invoice_chart.png
```

---

Let me know if you'd like to add a contributors section or license info!

