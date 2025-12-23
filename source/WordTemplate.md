# Word Template Preparation

[中文](https://sheet-to-doc.wtsolutions.cn/zh/latest/WordTemplate.html)


## Preparing Your Word Template

> We recommend using Microsoft Word to prepare your template files. If you don't have Word, you can use other editors (such as WPS) to prepare template files.


- Create a new Word document, must be in .docx format.
- Insert placeholders using the `{placeholder}` syntax. For detailed usage of placeholders, see the "Placeholders" section below.
- Add any other text or formatting as needed.
- Save the template as a .docx file.

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

## Placeholders

### Data Placeholders

Placeholders are special markers used in Word templates to insert data. Each placeholder is enclosed in `{` and `}`, for example `{Name}`, `{Date of Birth}`, etc.

The name of the placeholder must exactly match the column header in the Excel spreadsheet, otherwise the data will not be filled correctly.

Suppose your Excel spreadsheet contains the following columns: Name, Age, Gender.
```
    Name    Age    Gender
    Zhang San    25    Male
```

In the Word template, you can insert the following placeholders:

<div class="word-document">

{Name},{Age},{Gender}.

</div>

When the tool runs, it will fill these placeholders with data from the Excel spreadsheet.
<div class="word-document">

Zhang San,25,Male.

</div>

### Loop Placeholders

> Loop placeholders only work in Generation Mode 2 (generate one Word document for all data items).

If your Excel spreadsheet contains multiple rows of data, you can use loop placeholders to repeatedly fill content in the template.

> The format of loop placeholders is `{#data}...{/data}`. Within `{#data}...{/data}`, you can use data placeholders such as `{Name}` to reference specific data.

Suppose your Excel spreadsheet contains the following columns: Name, Age, Gender.
```
    Name    Age    Gender
    Zhang San    25    Male
    Li Si    30    Female
```

In the Word template, you can insert the following placeholders:

<div class="word-document">

{#data}

{Name},{Age},{Gender}.

{/data}
</div>

When the tool runs, it will loop through the data in the Excel spreadsheet and fill these placeholders row by row.

<div class="word-document">

Zhang San,25,Male.

Li Si,30,Female.

</div>


### Conditional Placeholders

If your Excel spreadsheet contains conditional data, you can use conditional placeholders to fill content in the template based on conditions.

> The format of conditional placeholders is `{#aCondition}...{/aCondition}`.

Suppose your Excel spreadsheet contains the following columns: Name, Age, Gender, Awarded.
```
    Name    Age    Gender    Awarded
    Zhang San    25    Male    true
    Li Si    30    Female    false
    Wang Wu    35    Male    true
```

In the Word template, you can insert the conditional placeholder `{#Awarded}...{/Awarded}`:

<div class="word-document">

Winners of this competition:

{#data}

{#Awarded}

{Name},{Age},{Gender}.

{/Awarded}

{/data}

</div>

When the tool runs, it will loop through the data in the Excel spreadsheet, check if the person is an award winner, and if so, fill the placeholders; if not, it will not fill them.

<div class="word-document">

Winners of this competition:

Zhang San,25,Male.

Wang Wu,35,Male.

</div>


### Notes

- Placeholders must be enclosed in curly braces `{}`.
- The name of the placeholder must exactly match the column header in the Excel spreadsheet, including case.
- Placeholders can be used anywhere in the template, including paragraphs, tables, lists, etc.

