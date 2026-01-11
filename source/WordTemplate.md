# Word Template Preparation

[中文](https://sheet-to-doc.wtsolutions.cn/zh-cn/latest/WordTemplate.html)


```{include} _snippet/intro.md
```

## Preparing Your Word Template

:::{hint}
We recommend using Microsoft Word to prepare your template files. If you don't have Word, you can use other editors (such as LibreOffice Writer) to prepare template files.
It is recommended to set the formatting when preparing the template, as Sheet to Doc only fills in data and will not change the formatting you have already set.
:::

- Create a new Word document, must be in .docx format.
- Insert placeholders using the `{placeholder}` syntax. For detailed usage of placeholders, see the "Placeholders" section below.
- Add any other text, images, tables, etc., as needed, and set formatting.
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

Placeholders are special markers used in Word templates for inserting data. Each placeholder is enclosed by **English characters** `{` and `}` , such as `{Name}`, `{@image | _inline_image}` , etc.

### Data Placeholders

| Supported? | Mode 1 (Multiple Docs) | Mode 2 (Single Doc) |
| :--- | :---: | :---: |
| Data Placeholder | Y | Y |

Data placeholders are special markers used in Word templates for inserting data, such as `{Name}`, `{Date_of_Birth}`, etc.

> You can refer to the invitation examples in [Usage Examples](Examples.md).

:::{warning}
The name of the placeholder must exactly match the column header in the Excel spreadsheet, otherwise the data will not be filled correctly.
:::

Suppose your Excel spreadsheet contains the following columns: Name, Age, Gender.
```
    Name    Age    Gender
    Zhang San    25    Male
```

In the Word template, you can insert the following placeholders:

---
<div class="word-document">

{Name},{Age},{Gender}.

</div>

---

When the tool runs, it will fill these placeholders with data from the Excel spreadsheet.

---
<div class="word-document">

Zhang San,25,Male.

</div>

---



### Loop Placeholders

| Supported? | Mode 1 (Multiple Docs) | Mode 2 (Single Doc) |
| :--- | :---: | :---: |
| Loop Placeholder 1 | N | Y |
| Loop Placeholder 2 | Y | Y |

If your Excel spreadsheet contains multiple rows of data, and you want to:
- Repeat filling content in the template within a single Word document, or
- Generate multiple Word documents with each row of data occupying one page.

Then you can use Loop Placeholder 1 or Loop Placeholder 2 to achieve this.

#### Loop Placeholder 1

Loop Placeholder 1 is suitable for repeatedly writing each row of data from the Excel spreadsheet into a single Word document, resulting in one file.

The format of Loop Placeholder 1 is `{#data}...{/data}`.

- Loop Placeholder 1 is fixed as `{#data}` and `{/data}`, and cannot be changed.
- When you use Loop Placeholder 1, you must select Generation Mode 2.

:::{tip}
If you want each row of data to occupy a separate page in Word, you need to add a page break after the template, and then add `{/data}` at the beginning of the second page. You can refer to the invitation examples in the usage cases.
:::

Within `{#data}...{/data}`, you can use data placeholders and other placeholders, such as `{#data}{Name}{/data}` to reference specific data. Note that `{}` must use **English characters**.

> You can refer to the invitation and award notice examples in [Usage Examples](Examples.md).

Suppose your Excel spreadsheet contains the following columns: Name, Age, Gender.

```
    Name    Age    Gender
    Zhang San    25    Male
    Li Si    30    Female
```

In the Word template, you can insert the following placeholders:

---
<div class="word-document">

{#data}

{Name},{Age},{Gender}.

{/data}
</div>

---

When using Generation Mode 2, it will loop through the data in the Excel spreadsheet and fill these placeholders row by row.

---
<div class="word-document">

Zhang San,25,Male.

Li Si,30,Female.

</div>

---

#### Loop Placeholder 2

> (Since version 2.4.0)

Loop Placeholder 2 is a more general version compared to Loop Placeholder 1.
- The format of Loop Placeholder 2 is `{#loop1}...{/loop1}`.
- The `loop1` in Loop Placeholder 2 can be replaced with other names, such as `{#person}...{/person}`, `{#info}...{/info}`, etc., but it cannot be `{#data}` or `{/data}`.
- Loop Placeholder 2 can take effect in both Generation Mode 1 and 2.

:::{warning}
Loop Placeholder 2 is relatively more complex to use. If not necessary, it is recommended to use Loop Placeholder 1.
If you use Loop Placeholder 2, you need to make some considerations in Excel data preparation and Word template preparation, otherwise it will lead to data filling errors. This is explained through the following example.
:::

We use the same example as Loop Placeholder 1, assuming your Excel spreadsheet contains the following columns: Name, Age, Gender.
```
    Name    Age    Gender
    Zhang San    25    Male
    Li Si    30    Female
    Wang Wu    35    Male
```
If you use Loop Placeholder 2, you need to make some considerations in Excel data preparation and Word template preparation.

Excel data needs to be adjusted as follows:

```
    info.Name    info.Age    info.Gender
    Zhang San        25          Male
    Li Si        30          Female
    Wang Wu        35          Male
```
- We added `info.` before the headers `Name`, `Age`, and `Gender`. This is to correctly reference the columns in Excel data when using Loop Placeholder 2 in the Word template.

The following explains Generation Mode 1 and Generation Mode 2 separately.

- In Generation Mode 1, you need to use `{#info}` and `{/info}` as Loop Placeholder 2 in the Word template, wrapping the content of the data placeholders `{Name}`, `{Age}`, and `{Gender}`.
- In Generation Mode 2, you can use `{#info}` and `{/info}` as Loop Placeholder 2 in the Word template, wrapping the content of the data placeholders `{Name}`, `{Age}`, and `{Gender}`. At the same time, you also need to use `{#data}` and `{/data}` on the outermost layer, because this is a required placeholder for using Generation Mode 2.

In the Word template prepared for Generation Mode 1, you can insert the following placeholders:

---
<div class="word-document">

{#info}

{Name},{Age},{Gender}.

{/info}

</div>

---

When Generation Mode 1 is selected, it will loop through the data in the Excel spreadsheet and generate 3 files.

---
<div class="word-document">

Zhang San,25,Male.

</div>

---

<div class="word-document">

Li Si,30,Female.

</div>

---

<div class="word-document">

Wang Wu,35,Male.

</div>

---


In the Word template prepared for Generation Mode 2, you can insert the following placeholders:

---
<div class="word-document">

{#data}

{#info}

{Name},{Age},{Gender}.

{/info}

{/data}




</div>

---

When using Generation Mode 2, it will loop through the data in the Excel spreadsheet and fill these placeholders row by row. Finally, one file is generated.

---
<div class="word-document">

Zhang San,25,Male.

Li Si,30,Female.

Wang Wu,35,Male.

</div>

---

### Conditional Placeholders

| Supported? | Mode 1 (Multiple Docs) | Mode 2 (Single Doc) |
| :--- | :---: | :---: |
| Conditional Placeholder 1 | Y | Y |
| Conditional Placeholder 2 | Y | Y |
| Conditional Placeholder 3 | Y | Y |

If your Excel spreadsheet contains conditional data, you can use conditional placeholders to fill content in the template based on conditions. For example, fill content in the template only when a certain data reaches a certain value, otherwise do not fill.

#### Conditional Placeholder 1 - true false

The format of Conditional Placeholder 1 is `{#aCondition}...{/aCondition}`. Note that `{}` must use **English characters**.

- aCondition: The `aCondition` in Conditional Placeholder 1 can be any column in the Excel data, such as `Name`, `Age`, `Gender`, `Awarded`, etc.
- Condition: The `Condition` in Conditional Placeholder 1 must be `true` or `false`.

Suppose your Excel spreadsheet contains the following columns: Name, Age, Gender, Awarded (whether they won an award). We use whether they won an award as a condition to fill content in the template.

```
    Name    Age    Gender    Awarded
    Zhang San    25    Male    true
    Li Si    30    Female    false
    Wang Wu    35    Male    true
```

In the Word template, you can insert the conditional placeholder `{#Awarded}...{/Awarded}`:

---
<div class="word-document">

Winners of this competition:

{#data}

{#Awarded}

{Name},{Age},{Gender}.

{/Awarded}

{/data}

</div>

---

When the tool runs, it will loop through the data in the Excel spreadsheet, check if the person is an award winner (based on whether the value in the `Awarded` column is `true`), and if so, fill the placeholders; if not, it will not fill them.

---
<div class="word-document">

Winners of this competition:

Zhang San,25,Male.

Wang Wu,35,Male.

</div>

---

#### Conditional Placeholder 2 - equal to or not equal to specified value

The format of conditional placeholders is `{#aCondition == "specifiedValue"}...{/}` or `{#aCondition != "specifiedValue"}...{/}`.
Note that symbols like `{}`, `#`, etc. must use **English characters**.

Example:

Suppose your Excel spreadsheet contains the following columns: Name, Prize.

```
    Name    Prize
    Zhang San    Watch
    Li Si    BatteryBank
    Wang Wu    Watch
```

---
<div class="word-document">

{#data}

{Name} won a {Prize}, as shown below:

{#Prize == "Watch"}

![Watch](_static/watch.png)

{/}

{#Prize == "BatteryBank"}

![BatteryBank](_static/batterybank.png)

{/}

{/data}

</div>

---
:::{warning}
- The double quotes around "Watch" and "BatteryBank" in the examples must be English double quotes.
- If the condition value is a number, you do not need to enclose it in double quotes. Just write the number directly.
:::


When the tool runs, it will loop through the data in the Excel spreadsheet and check if the person won a watch or battery bank, and if so, fill the placeholder; if not, it will not fill it.

---
<div class="word-document">

Zhang San won a Watch, as shown below:

![Watch](_static/watch.png)

Li Si won a BatteryBank, as shown below:

![BatteryBank](_static/batterybank.png)

Wang Wu won a Watch, as shown below:

![Watch](_static/watch.png)

</div>

---

#### Conditional Placeholder 3 - Comparison

> (Since version 2.4.0)

The format of Conditional Placeholder 3 is `{#aCondition operator "specifiedValue"}...{/}`.
- Operators include `>`, `>=`, `<`, `<=`.
- Note that symbols like `{}`, `#` etc. must use **English characters**.

Example:

Suppose your Excel spreadsheet contains the following columns:
```
    Name    Age
    Zhang San    25
    Li Si    30
    Wang Wu    35
```

---

<div class="word-document">

{#data}

{#Age >= 30}

{Name} is 30 years old or above.

{/}

{/data}

</div>

---
:::{warning}
- If the condition specified value is a number, no double quotes are needed, just write the number directly.
- This example should run in Generation Mode 2 where all data is repeated in one Word document.
:::

When the tool runs, it will loop through the data in the Excel spreadsheet and check the set condition. If it is true, it will fill the placeholder; if not, it will not fill it.

---

<div class="word-document">

Li Si is 30 years old or above.

Wang Wu is 30 years old or above.

</div>

---


### Image Placeholders

| Supported? | Mode 1 (Multiple Docs) | Mode 2 (Single Doc) |
| :--- | :---: | :---: |
| Image Placeholders | Y | Y |

> (Since version 2.2.0)

Sheet to Doc provides two methods for inserting images:
- The first method is described in the "Conditional Placeholder 2" section above (pre-inserting all possible images into the Word template and using conditions to control display).
- The other method is the image placeholder method covered in this chapter, which dynamically inserts images by inserting special placeholders in the Word template. Images need to be uploaded to the tool in advance.

Image placeholders are special markers used in Word templates for inserting images. Each image placeholder is enclosed by **English characters** `{` and `}` , such as `{@image | _inline_image} `, `{@image | _block_image:width:height} `, etc.

- `_inline_image` represents an inline image, which will insert the image into the text, closely integrated with the text.
- `_block_image` represents a block-level image (top and bottom wrapping), which will insert the image into a paragraph, independent of the paragraph.
- `width` and `height` are optional parameters, used to specify the width and height of the image. If not specified, the image will be displayed at 5cm x 5cm. If specified, the unit must be in **centimeters**. For example, `{@image | _inline_image:10:10}` means to insert the image into the text, with a width of 10cm and a height of 10cm.
- Symbols like `@`, `|`, `_` must use **English characters**, for example, in `{@image | _inline_image}`, `@`, `|`, `_` must all use **English characters**.

> You can refer to the award notice examples in [Usage Examples](Examples.md).

Note:
- Image placeholders must start with `@` , for example `{@image | _inline_image}`
- Image placeholders must include the image type ( `| _inline_image` or `| _block_image` ), otherwise the tool cannot recognize them. Note that `|` and `_` must use **English characters**.
- Image placeholders must appear as a separate line in the Word template and cannot be on the same line as other text. Otherwise, they will not display properly.
- Image placeholders must include an image filename variable, otherwise the tool cannot recognize the image filename. For example, in `{@image | _inline_image}` , `image` is the image filename variable.
- The image filename must match the uploaded image filename (case-sensitive, must include extension), otherwise the tool cannot find the corresponding image file (e.g., watch.png ). The image name can contain Chinese characters, but errors may occur if it contains special characters.

Example:

Suppose the Excel data lists Image Name and Image Chinese Name.

For example:

```
    Image_Chinese_Name  Image_Filename
    Watch    watch.png
    Power_Bank    batterybank.png
```
At the same time, we need to upload the two images watch.png and batterybank.png.

The Word template uses the following format:

---
<div class = "word-document">

{#data}

{@Image_Filename | _inline_image}

{/data}
</div>

---

In Generation Mode 2, this will generate the following document:

---
<div class="word-document">

![watch](_static/watch.png)

![batterybank](_static/batterybank.png)


</div>

---
 

### Filters

You can use filters to transform data in your templates. Filters are applied to placeholders using the pipe (`|`) syntax: `{placeholder | filterName}` or `{placeholder | filterName:parameter}`. Note that `{}`,`|` and `:` must use **English characters**. If the filter requires a parameter, and if this parameter is not a number, then the parameter must be enclosed in **English double quotes**.

> You can refer to the receipt examples in [Usage Examples](Examples.md).

#### String Filters

| Filter Name | Description | Example | Output |
|-------------|-------------|---------|--------|
| `toUpperCase` | Converts English strings to uppercase | `{Name \| toUpperCase}` | `Zhang San` → `ZHANG SAN` |
| `toLowerCase` | Converts English strings to lowercase | `{Name \| toLowerCase}` | `Zhang San` → `zhang san` |
| `capitalize` | Capitalizes the first character of an English string | `{Name \| capitalize}` | `Zhang San` → `Zhang san` |

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
| `currency` | Formats a number as currency | `{Price \| currency:"$":2}` when Price is 1234.56 | `$1,234.56` |
| `accounting` | Formats a number in accounting format (uses parentheses for negative numbers) | `{Price \| accounting:"$":2}` when Price is -1234.56 | `$(1,234.56)` | 
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


### Placeholder Appearances

Placeholder can appear in any position in the Word template, including but not limited to:
- Paragraphs
- Tables
- Lists
- Headers
- Footers
- Text boxes
- And more...

## Notes


- Placeholders must be enclosed in curly braces `{}`.
- The name of the placeholder must exactly match the column header in the Excel spreadsheet, including case.
- Placeholders can be used anywhere in the template, including paragraphs, tables, lists, etc.
