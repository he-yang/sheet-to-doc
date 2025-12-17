# Getting Started

Sheet to Doc is a powerful tool that automatically converts Excel sheets to professional documents. This guide will walk you through the basic usage steps, limitations, and provide some examples.


## Use Cases

### Example 1: Generate a Sales Report

1. **Prepare Excel Sheet**: Create a sheet with columns: Product Name, Quantity, Price, Total.
2. **Select Template**: Choose the "Sales Report" template.
3. **Generate**: Click "Generate" to create the sales report.
4. **Result**: A professional sales report with a table of products, quantities, prices, and totals.

### Example 2: Generate Invoices

1. **Prepare Excel Sheet**: Create a sheet with columns: Invoice Number, Customer Name, Date, Item, Quantity, Price, Total.
2. **Select Template**: Choose the "Invoice" template.
3. **Generate**: Click "Generate" to create invoices for each row.
4. **Result**: Multiple invoices, each with its own invoice number, customer name, date, and item details.

### Example 3: Generate Letters

1. **Prepare Excel Sheet**: Create a sheet with columns: Recipient Name, Address, Date, Subject, Body.
2. **Select Template**: Choose the "Business Letter" template.
3. **Generate**: Click "Generate" to create personalized letters.
4. **Result**: Personalized business letters with the recipient's name, address, and customized content.

## Basic Usage Steps

### 1. Prepare Your Excel Data

First, you need to prepare your Excel sheet with the data you want to convert to a document. The sheet should have a clear structure, with:
- headers in the first row, and
- data in subsequent rows.

Example:

Download sample Excel file: [sample1-sheet.xlsx](_static/sample1-sheet.xlsx)

| Name   | Date of Birth | Gender |
|--------|--------------|--------|
| Zhang San  | 1990-05-12   | M     |


### 2. Prepare your Word (.docx) Template

Next, you need to prepare a Word document template that will be used to generate the final document. The template should contain placeholders for the data from the Excel sheet.

Example:

- Create a new Word document.
- Insert placeholders using the `{placeholder}` syntax. For example, `{Name}` will be replaced with the data from the "Name" column, and `{Date of Birth}` will be replaced with the data from the "Date of Birth" column.
- Add any other text or formatting as needed.
- Save the template as a DOCX file.

Example 2:

Download sample Word template file: [sample1-doc.docx](_static/sample1-doc.docx)


```text
Subject: Visit Notification: One Colleague Visiting Tomorrow

Dear Davidson,

We are writing to inform you that one of our colleagues will be visiting your office tomorrow. His/Her details, as shown on the employee ID, are as follows:

Full Name: {Name}
Date of Birth: {Date of Birth}
Gender: {Gender}

Please kindly assist with his/her entry and coordination upon arrival. Should you need further information, feel free to contact me.
Thank you for your support.
Best regards,
WTSolutions
```

### 3. Access the Tool

You can use Sheet to Doc:

-  Visit [https://s.wtsolutions.cn/sheet-to-doc.html](https://s.wtsolutions.cn/sheet-to-doc.html) using one of your modern browsers (e.g., Chrome, Firefox, Safari).


### 4. Fill in the Data

- Copy the data directly from your Excel sheet.
- Paste it into the "Data" field in the Sheet to Doc web app.
- You can see a preview of the data in the web app.

### 5. Upload the Template

- Upload the Word template file you prepared in step 2.


### 4. Generate the Document

Click the "Generate" button. The tool will populate the template with the data from the Excel sheet and generate a professional document based on your chosen template.

Example:

Download sample generated document: [sample1-report.docx](_static/sample1-report.docx)

```text
Subject: Visit Notification: One Colleague Visiting Tomorrow

Dear Davidson,

We are writing to inform you that one of our colleagues will be visiting your office tomorrow. His/Her details, as shown on the employee ID, are as follows:
Full Name: Zhang San
Date of Birth: 1990/5/12
Gender: M
Please kindly assist with his/her entry and coordination upon arrival. Should you need further information, feel free to contact me.
Thank you for your support.
Best regards,
WTSolutions

```


## Need Help?

If you encounter any issues or have questions, please email he.yang@wtsolutions.cn.