# AS-IS Purchase-to-Pay Process

## Overview

The current Purchase-to-Pay process contains several manual activities across Procurement, Finance and business teams.

Invoices are reviewed manually against purchase orders, approval information and payment records. Exceptions are often identified only after Finance has already spent time investigating the transaction.

## Current Process Flow

1. Business user requests goods or services.
2. Purchase Order is created and approved.
3. Supplier provides goods or services.
4. Supplier sends invoice.
5. Finance receives the invoice.
6. Finance manually checks the invoice against the Purchase Order.
7. Finance checks whether the invoice has been approved.
8. Finance investigates differences or missing information.
9. Approved invoices are sent for payment.
10. Payment is processed.
11. Finance prepares reports and follows up on outstanding exceptions.

## Main Pain Points

The current process creates several challenges:

* Manual comparison of invoice and Purchase Order data.
* Manual identification of duplicate invoices.
* Missing or incorrect Purchase Order references.
* Delays caused by incomplete approvals.
* Limited visibility of exceptions.
* Repetitive reconciliation work.
* Increased risk of incorrect or duplicate payments.
* Finance employees spend time reviewing transactions that may not require manual intervention.

## Current Control Weaknesses

The process relies heavily on manual review.

Potential issues include:

* Duplicate invoices may not be identified early.
* Invoice amounts may differ from approved Purchase Orders.
* Invoices may be received without valid PO references.
* Payment information may not match approved invoice amounts.
* Exceptions are not consolidated into a single structured report.
* Manual controls become harder to manage as transaction volumes increase.

## AS-IS Process Summary

```text
Business Need
      ↓
Purchase Order
      ↓
Supplier
      ↓
Invoice Received
      ↓
Manual Finance Review
      ↓
Manual PO / Invoice Comparison
      ↓
Manual Approval Check
      ↓
Exception Investigation
      ↓
Payment
      ↓
Manual Reporting
```

## Transformation Need

The current process is functional but highly dependent on manual checks.

The transformation opportunity is to automate repetitive controls, identify exceptions earlier and allow Finance teams to focus only on transactions that require investigation.

