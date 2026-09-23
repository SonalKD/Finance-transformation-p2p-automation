import pandas as pd

# Load the finance data
suppliers = pd.read_csv("02_Data/suppliers.csv")
purchase_orders = pd.read_csv("02_Data/purchase_orders.csv")
invoices = pd.read_csv("02_Data/invoices.csv")
payments = pd.read_csv("02_Data/payments.csv")

print("Finance data loaded successfully.")

print("Suppliers:", len(suppliers))
print("Purchase Orders:", len(purchase_orders))
print("Invoices:", len(invoices))
print("Payments:", len(payments))
# Control 1: Find invoices with missing Purchase Order

missing_po = invoices[invoices["PO_ID"].isna()]

print("\nInvoices with missing Purchase Order:")
print(missing_po)
