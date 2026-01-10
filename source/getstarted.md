# Getting Started

[中文](https://sheet-to-doc.wtsolutions.cn/zh-cn/latest/getstarted.html)

Sheet to Doc is a powerful tool that automatically writes Excel, CSV, JSON, JSONL data into docx format Word templates, converting them into Word documents in batches.

Building on the basis of mail merge, this tool has developed more features, such as custom file names, custom file paths, embedding images, and so on.

:::{attention}
This getting started guide (this page) will walk you through the basic usage steps to help you quickly get started with Sheet to Doc. Once you're familiar with it, you are advised to read the detailed [Usage Instructions](Usage.md) for more features.
:::

## Use Cases

### Example 1: Generate Sales Reports

1. **Prepare Excel Spreadsheet**: Create a spreadsheet with the following columns: Product Name, Quantity, Price, Total.
2. **Select Template**: Choose the "Sales Report" template.
3. **Generate**: Click the "Generate" button to create sales reports.
4. **Result**: A professional sales report containing a table with products, quantities, prices, and totals.

### Example 2: Generate Invoices

1. **Prepare Excel Spreadsheet**: Create a spreadsheet with the following columns: Invoice Number, Customer Name, Date, Item, Quantity, Price, Total.
2. **Select Template**: Choose the "Invoice" template.
3. **Generate**: Click the "Generate" button to create invoices for each row.
4. **Result**: Multiple invoices, each with its own invoice number, customer name, date, and item details.

### Example 3: Generate Letters

1. **Prepare Excel Spreadsheet**: Create a spreadsheet with the following columns: Recipient Name, Address, Date, Subject, Body.
2. **Select Template**: Choose the "Business Letter" template.
3. **Generate**: Click the "Generate" button to create personalized letters.
4. **Result**: Personalized business letters with recipient names, addresses, and customized content.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8772217510669640"
     crossorigin="anonymous"></script>
   <ins class="adsbygoogle"
      style="display:block; text-align:center;"
      data-ad-layout="in-article"
      data-ad-format="fluid"
      data-ad-client="ca-pub-8772217510669640"
      data-ad-slot="2653271427"></ins>
   <script>
      (adsbygoogle = window.adsbygoogle || []).push({});
   </script>

## Basic Usage Steps

### Prepare Your Excel Data

First, you need to prepare an Excel spreadsheet containing the data to be converted into documents. The spreadsheet should have a clear structure:
- The first row is the header row,
- Subsequent rows are data rows.

Example:

Download sample Excel file: [sample1-sheet.xlsx](_static/sample1-sheet.xlsx)

| Name  | Date_of_Birth | Gender |
|-------|---------------|--------|
| Zhang San | 1990-05-12   | M     |


### Prepare Your Word (.docx) Template

Next, you need to prepare a Word document template for generating the final documents. The template should contain placeholders from the Excel spreadsheet data.

Example:

- Create a new Word document.
- Insert placeholders using the `{placeholder}` syntax. For example, `{Name}` will be replaced with data from the "Name" column, and `{Date_of_Birth}` will be replaced with data from the "Date of Birth" column.
- Add any other text or formatting as needed.
- Save the template as a DOCX file.

Example 2:

Download sample Word template file: [sample1-doc.docx](_static/sample1-doc.docx)

---

<div class="word-document">

Subject: Visit Notification: A Colleague Will Visit Tomorrow

Dear Davidson:

We hereby inform you that one of our colleagues will visit your office tomorrow. The details as shown on their employee ID are as follows:

Name: {Name}

Date of Birth: {Date_of_Birth}

Gender: {Gender}

Please assist with entry procedures and coordination upon their arrival. If you need any further information, please feel free to contact me.

Thank you for your support.

Sincerely,

Best regards,

WTSolutions

</div>

---



### Open Sheet to Doc

You can access Sheet to Doc in the following ways:

1. Use a modern browser (such as Chrome, Firefox, Edge, Safari) to visit [https://s.wtsolutions.cn/sheet-to-doc.html](https://s.wtsolutions.cn/sheet-to-doc.html).
2. Download the software as a desktop application for offline use. [Download](Download.md)

### Fill in Data

- Copy data directly from your Excel spreadsheet.
- Paste it into the "Data" field in the Sheet to Doc web application.
- You can view a data preview in the web application.

### Upload Template

- Upload the Word template file you prepared.


### Generate Documents

When selecting the generation mode, choose mode 1: Generate separate Word documents for each row of data.

Click the "Generate" button. The tool will populate the template with data from the Excel spreadsheet and generate professional documents based on the template you selected.

Example:

Download sample generated document: [sample1-report.docx](_static/sample1-report.docx)

---

<div class="word-document">

Subject: Visit Notification: A Colleague Will Visit Tomorrow

Dear Davidson:

We hereby inform you that one of our colleagues will visit your office tomorrow. The details as shown on their employee ID are as follows:

Name: Zhang San

Date of Birth: 1990/5/12

Gender: M

Please assist with entry procedures and coordination upon their arrival. If you need any further information, please feel free to contact me.

Thank you for your support.

Sincerely,

Best regards,

WTSolutions

</div>

---

:::{note}
The above is a simple quick start tutorial, and now you can start using Sheet to Doc to automatically generate professional documents.
If you want to learn more features, please refer to [Usage Tutorial](Usage.md).
:::