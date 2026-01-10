# Generation Settings

[中文](https://sheet-to-doc.wtsolutions.cn/zh-cn/latest/Settings.html)

```{include} _snippet/intro.md
```

## Generation Modes 

### Mode 1: Generate Separate Word Documents for Each Row (Recommended for New Users)

- Each data row will generate a separate Word document.
- This mode may generate multiple files
   - If you use web version, the browser will pop up a reminder to download multiple files, which requires your permission.
   - If you use desktop version, it is recommended to set the file download directory in advance by right-clicking on the page to avoid download errors.
- This mode is recommended for all new users.

### Mode 2: Generate One Word Document for All Data

- All Excel data will be written into the Word template in a loop, inside the Word document, the data will be repeatedly generated according to the placeholder design of the template, and finally a single Word document will be generated.
- In this mode, you must use the loop placeholder 1 `{#data}..{/data}` in the template, otherwise it will cause an error. Learn how to use loop placeholder 1 in [Template Preparation](WordTemplate.md).

## Filename Settings

Sheet to Doc provides flexible filename customization functionality, allowing you to set the filenames of the generated documents according to your needs.

### Filename Generation Methods

You can choose from two filename generation methods:

1. **Default Filename**: The system automatically generates filenames in the following format:
   - Mode 1: sheet_to_doc_R_{row_number}_{timestamp+random_number}.docx
   - Mode 2: sheet_to_doc_All_{timestamp+random_number}.docx

2. **Custom Filename**: You can customize the filename format according to your needs, including prefix, middle content (from titles in Excel data), and suffix.

### Custom Filename Settings

When selecting the custom filename method, you can set the following options:

- **Prefix**: The beginning part of the filename, which can be any text or empty.
- **Middle (from Excel data titles)**: Select a column from the Excel data as the middle part of the filename.
- **Suffix**: The ending part of the filename, which can be any text or empty.

The final filename format is: `[Prefix][Middle][Suffix].docx`

### Filename Preview

The system will use the first row of data to generate a real-time filename preview, helping you confirm whether the filename format meets your expectations. The preview format is: `[Prefix][Value from corresponding column in first row data][Suffix].docx`

### Custom Filename Examples

Here are several actual examples of custom filenames to help you better understand how to use this feature:

#### Example 1: Using Name as Filename

- Prefix: `Employee_`
- Middle (from data): Select the column containing employee names (e.g., the value in the "Name" column is "Zhang San")
- Suffix: `_Profile`
- Generated filename: `Employee_Zhang San_Profile.docx`

#### Example 2: Using ID as Filename

- Prefix: `Contract_`
- Middle (from data): Select the column containing contract IDs (e.g., the value in the "Contract ID" column is "CON2024001")
- Suffix: Empty
- Generated filename: `Contract_CON2024001.docx`

#### Example 3: Using Date and Name Combination

- Prefix: `Report_`
- Middle (from data): Select the column containing report dates (e.g., the value in the "Date" column is "2024-05-20")
- Suffix: `_Zhang San`
- Generated filename: `Report_2024-05-20_Zhang San.docx`

#### Example 4: Using Product Name and Version Number

- Prefix: Empty
- Middle (from data): Select the column containing product names (e.g., the value in the "Product Name" column is "SheetToDoc")
- Suffix: `_v1.2.0`
- Generated filename: `SheetToDoc_v1.2.0.docx`


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

