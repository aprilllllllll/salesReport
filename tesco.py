import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os 
# import tkinter as tk
def run():
    df = pd.read_csv('YUKI - INVOICE BY DATE RANGE.csv')
    # removed Sale Mode = NaN 
    df = df[df['Sale Mode'].notna()]
    # covert $ to the number eg: $1.0 -> 1
    df['Sold Price'] = df['Sold Price'].replace(
        '[\$,]', '', regex=True).astype(float).round(2)
    # drop rows where sold price == 0
    df = df[df['Sold Price']!=0]

    df['Total Sale'] =round( df['Qty Sold'] * df['Sold Price'],2)
    
    invoice_counts = df.groupby('Invoice Date')[
        'Invoice ID'].nunique().reset_index()

    invoice_counts.rename(
        columns={'Invoice ID': 'Invoice Count'}, inplace=True)

    # Sum total sales per invoice date
    total_sales_per_date = df.groupby('Invoice Date')[
        'Total Sale'].sum().reset_index()
    # Merge the total sales and invoice count dataframes
    summary = total_sales_per_date.merge(invoice_counts, on='Invoice Date')

    # Calculate the average total sale per invoice
    summary['Avg per Invoice'] = round(summary['Total Sale'] / summary['Invoice Count'],2)

    #barChat(summary)

    reportDate = df['Invoice Date'].min()
    reportDate = pd.to_datetime(reportDate)
    reportDate = reportDate.strftime('%Y-%m')
   
    fileName = f"{reportDate}-report.csv"
    filePath = os.path.join("./",fileName)
    lineChart(summary,reportDate)
    if os.path.exists(filePath):
        os.remove(filePath)
    summary.to_csv(fileName)


def barChat(data):
    plt.figure(figsize=(20, 5))
    bars = plt.bar(data['Invoice Date'],
                   data['Avg per Invoice'], color='b')

    for bar in bars:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{bar.get_height():.2f}",ha='center', va='bottom', fontsize=10, color='black')

    plt.xlabel('Invoice Date')
    plt.ylabel('Avg per Invoice')
    plt.title('Average Total Sale per Invoice by Date')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def lineChart(data,date):
    plt.figure(figsize=(20, 5))
    plt.plot(data['Invoice Date'], data['Avg per Invoice'], marker='o', linestyle='-', color='b')

    # 計算數據標籤偏移量，防止重疊
    y_values = data['Avg per Invoice']
    offsets = np.linspace(0.01, 0.01, len(y_values)) * max(y_values)

    for i, txt in enumerate(y_values):
        plt.text(i, txt + offsets[i], f"{txt:.2f}", ha='center', va='bottom', fontsize=10, color='black')

    # 計算總平均值
    overall_avg = data['Avg per Invoice'].mean()

    # 顯示總平均值在圖的右上角
    plt.text(len(data) - 1, max(y_values), f"Monthly Avg: {overall_avg:.2f}", 
             ha='right', va='bottom', fontsize=12, color='darkred', fontweight='bold')

    # 設定標題和標籤
    plt.xlabel('Invoice Date')
    plt.ylabel('Avg Total Sale per Invoice')
    plt.title('Average Total Sale per Invoice by Date')

    # 調整X軸標籤方向
    plt.xticks(rotation=45)

    # 顯示網格
    plt.grid(True)

    plt.savefig('./avg_invoice_chart.png', bbox_inches='tight', dpi=300)
    plt.show()

    
run()
