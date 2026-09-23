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
# Control 5: Find payment amount mismatches

payment_mismatch = invoice_payment[
    (invoice_payment["Payment_Status"] == "Paid") &
    (invoice_payment["Payment_Amount"] != invoice_payment["Invoice_Amount"])
]

print("\nPayments with amount mismatch:")
print(payment_mismatch)
# Create Finance Exceptions Report

exceptions = []

# Missing PO exceptions
for _, row in missing_po.iterrows():
    exceptions.append({
        "Invoice_ID": row["Invoice_ID"],
        "Supplier_ID": row["Supplier_ID"],
        "PO_ID": row["PO_ID"],
        "Control": "Missing Purchase Order",
        "Reason": "Invoice does not contain a valid PO reference",
        "Recommended_Action": "Verify whether a PO is required and investigate with Procurement"
    })

# PO amount mismatch exceptions
for _, row in amount_mismatch.iterrows():
    exceptions.append({
        "Invoice_ID": row["Invoice_ID"],
        "Supplier_ID": row["Supplier_ID"],
        "PO_ID": row["PO_ID"],
        "Control": "PO Amount Mismatch",
        "Reason": f"Invoice amount {row['Invoice_Amount']} does not match PO amount {row['PO_Amount']}",
        "Recommended_Action": "Review invoice and purchase order before payment"
    })

# Duplicate invoice exceptions
for _, row in duplicate_invoices.iterrows():
    exceptions.append({
        "Invoice_ID": row["Invoice_ID"],
        "Supplier_ID": row["Supplier_ID"],
        "PO_ID": row["PO_ID"],
        "Control": "Possible Duplicate Invoice",
        "Reason": "Same supplier, PO and invoice amount appears more than once",
        "Recommended_Action": "Review invoices and block duplicate payment if confirmed"
    })

# Convert the exception list into a table
exceptions_report = pd.DataFrame(exceptions)

print("\nFinance Exceptions Report:")
print(exceptions_report)
# Save Finance Exceptions Report

exceptions_report.to_csv(
    "02_Data/finance_exceptions_report.csv",
    index=False
)

print("\nFinance Exceptions Report saved successfully.")
