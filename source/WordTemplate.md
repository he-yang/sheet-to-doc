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

#### Conditional Placeholder 1 - true false

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

#### Conditional Placeholder 2 - equal to

> The format of conditional placeholders is `{#aCondition == "value"}...{/}`.

Suppose your Excel spreadsheet contains the following columns: Name, Prize.

```
    Name    Prize
    Zhang San    Watch
    Li Si    BatteryBank
    Wang Wu    Watch
```

In the Word template, you can insert the conditional placeholder `{#Prize == "Watch"}...{/}`:

<div class="word-document">


{#data}

{Name} won a {Prize}.

{#Prize == "Watch"}

![Watch](_static/watch.png)

{/}

{#Prize == "BatteryBank"}

![BatteryBank](_static/batterybank.png)

{/}

{/data}

</div>

> Note: 
> If the condition value is a number, you do not need to enclose it in double quotes.


When the tool runs, it will loop through the data in the Excel spreadsheet, check if the person won a watch or battery bank, and if so, fill the placeholder; if not, it will not fill it.

<div class="word-document">



Zhang San won a Watch.

![Watch](_static/watch.png)

Li Si won a BatteryBank.

![BatteryBank](_static/batterybank.png)

Wang Wu won a Watch.

![Watch](_static/watch.png)

</div>

### Filters

You can use filters to transform data in your templates. Filters are applied to placeholders using the pipe (`|`) syntax: `{placeholder | filterName}` or `{placeholder | filterName:parameter}`.

#### String Filters

| Filter Name | Description | Example | Output |
|-------------|-------------|---------|--------|
| `toUpperCase` | Converts the string to uppercase | `{Name \| toUpperCase}` | `ZHANG SAN` |
| `toLowerCase` | Converts the string to lowercase | `{Name \| toLowerCase}` | `zhang san` |
| `capitalize` | Capitalizes the first character of the string | `{Name \| capitalize}` | `Zhang san` |

#### Number Filters

##### Basic Number Formatting

| Filter Name | Description | Example | Output |
|-------------|-------------|---------|--------|
| `fixed` | Formats a number with a fixed number of decimal places | `{Price \| fixed:2}` when Price is 123.456 | `123.46` |
| `round` | Rounds a number to the nearest integer | `{Price \| round}` when Price is 123.6 | `124` |
| `ceil` | Rounds a number up to the nearest integer | `{Price \| ceil}` when Price is 123.1 | `124` |
| `floor` | Rounds a number down to the nearest integer | `{Price \| floor}` when Price is 123.9 | `123` |

##### Currency and Financial Formatting

| Filter Name | Description | Example | Output |
|-------------|-------------|---------|--------|
| `currency` | Formats a number as currency | `{Price \| currency:$:2}` when Price is 1234.56 | `$1,234.56` |
| `accounting` | Formats a number in accounting format (uses parentheses for negative numbers) | `{Price \| accounting:$:2}` when Price is -1234.56 | `$(1,234.56)` |
| `thousandSeparator` | Formats a number with thousand separators | `{Price \| thousandSeparator:2}` when Price is 1234567.89 | `1,234,567.89` |

##### Percentage and Scientific Notation

| Filter Name | Description | Example | Output |
|-------------|-------------|---------|--------|
| `percentage` | Formats a number as a percentage | `{Rate \| percentage:2}` when Rate is 0.1234 | `12.34%` |
| `scientific` | Formats a number in scientific notation | `{Value \| scientific:2}` when Value is 123456 | `1.23e+05` |

##### Number Abbreviation

| Filter Name | Description | Example | Output |
|-------------|-------------|---------|--------|
| `shortNumber` | Formats a number in short form (K, M, B) | `{Amount \| shortNumber}` when Amount is 1234567 | `1.23M` |

### Notes

- Placeholders must be enclosed in curly braces `{}`.
- The name of the placeholder must exactly match the column header in the Excel spreadsheet, including case.
- Placeholders can be used anywhere in the template, including paragraphs, tables, lists, etc.

## Placeholder Appearances

Placeholder can appear in any position in the Word template, including but not limited to:
- Paragraphs
- Tables
- Lists
- Headers
- Footers
- Text boxes
- And more...