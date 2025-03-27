CSV request：
---------------------------

SV -> report generate -> Transaction History -> Transaction History -> YUKI- INVOICE BY DATE RANGE

-> filter ->Invoice Date (select the date range) -> export CSV

RUN:
-
move YUKI-INVOICE BY DATE RAGANE to the folder (name must be the same)
**make sure DO NOT have other .csv and .png**

click run.sh

after run the program you will have YYYY-MM-report.csv  and avg_invoice_chart.png



Sales Calculation Guidelines
-------------------------------
Layaway Sales
Only include completed layaway transactions in the total sales.

Note: If a product has not been picked up, it should not be included in the sales total.

Account Payments
Do not count account payments as part of the sales total for the current invoice.

Tax Exclusion
The total sales amount should be calculated before tax. Tax amounts should not be included.

Returns
All returns must be deducted from the total sales.


might cause issues:

return - sale = 0 which count as one invoice

layaway 
