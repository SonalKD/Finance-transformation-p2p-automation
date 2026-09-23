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
# Control 2: Find PO and invoice amount mismatches

invoice_po = invoices.merge(
    purchase_orders[["PO_ID", "PO_Amount"]],
    on="PO_ID",
    how="left"
)

amount_mismatch = invoice_po[
    (invoice_po["PO_ID"].notna()) &
    (invoice_po["PO_Amount"].notna()) &
    (invoice_po["Invoice_Amount"] != invoice_po["PO_Amount"])
]

print("\nInvoices with PO amount mismatch:")
print(amount_mismatch)
# Control 3: Find possible duplicate invoices

duplicate_invoices = invoices[
    invoices.duplicated(
        subset=["Supplier_ID", "PO_ID", "Invoice_Amount"],
        keep=False
    )
]

print("\nPossible duplicate invoices:")
print(duplicate_invoices)
# Control 4: Find invoices paid without approval

invoice_payment = invoices.merge(
    payments[["Invoice_ID", "Payment_Amount", "Payment_Status"]],
    on="Invoice_ID",
    how="left"
)

paid_without_approval = invoice_payment[
    (invoice_payment["Payment_Status"] == "Paid") &
    (invoice_payment["Approval_Status"] != "Approved")
]

print("\nInvoices paid without approval:")
print(paid_without_approval)
