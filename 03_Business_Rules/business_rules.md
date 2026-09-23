# Business Rules

The automated Purchase-to-Pay control process will apply the following rules.

## BR-01: Valid Supplier

Every invoice must belong to a valid and active supplier.

## BR-02: Purchase Order Required

Where a purchase order is expected, the invoice must contain a valid PO reference.

## BR-03: PO and Invoice Amount Match

The invoice amount should match the approved purchase-order amount.

Any difference should be flagged for review.

## BR-04: Invoice Approval Required

An invoice must be approved before payment is made.

## BR-05: Duplicate Invoice Detection

The system should flag possible duplicate invoices where the same supplier, purchase order and invoice amount appear more than once.

## BR-06: Payment Amount Validation

The payment amount should match the approved invoice amount.

## BR-07: Currency Consistency

The currency used on the purchase order, invoice and payment should be consistent.

## BR-08: Exception Reporting

Any transaction that fails one or more controls should be added to a Finance Exceptions Report for investigation.

## BR-09: Auditability

Each exception should clearly show:

* Invoice ID
* Supplier ID
* Purchase Order ID
* Control that failed
* Reason for the exception
* Recommended next action
