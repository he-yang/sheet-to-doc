# Data and Placeholders Comparison

[中文](https://sheet-to-doc.wtsolutions.cn/zh-cn/latest/Comparison.html)

```{include} _snippet/intro.md
```



:::{hint}
Step 2.1 Data Comparison is optional and can be skipped.
:::

> (Since version 2.1.0.0)

Step 2.1 Data Comparison is optional and can be skipped.

Step 2.1 compares the data and images provided in Step 1 with the content of the Word template uploaded in Step 2, helping users identify errors in the template and offering suggestions for correction.

After the comparison, recommendations for subsequent steps are given; however, regardless of the comparison results, you may skip Step 2.1 and proceed directly to the “Generate Document” button in Step 3.

## Comparison Process

- Data placeholders and data comparison
   - Find the data placeholders in the Word template uploaded in Step 2, such as `{Name}`, `{Date_of_Birth}`, etc.
   - Compare the data items provided in Step 1 with the data placeholders in the Word template from Step 2
   - If the template contains a placeholder `{Name}` but Step 1 only supplies `Age` without `Name`, it is marked as a mismatch
   - A Tick mark indicates a match; A Cross Mark indicates a mismatch
   - At the same time, based on the template, recommend whether to use Generation Mode 1 or Generation Mode 2

- Filters comparison
   - Detect any filters in the Word template uploaded in Step 2
   - If Sheet-to-Doc can process these filters, they are marked A Tick mark
   - If Sheet-to-Doc cannot process them, they are marked A Cross Mark
   - Refer to [Word Template](WordTemplate.md) for supported filters
   - If the template contains no filters, you can ignore this step

- Image placeholders and image comparison
   - First detect whether the Word template uploaded in Step 2 uses image placeholders
   - If placeholders exist, check whether the image data column names supplied in Step 1 match them
      - Match → A Tick mark
      - Mismatch → A Cross Mark
   - Verify that the image type is acceptable (jpg, png, jpeg, gif, bmp)
      - Acceptable → A Tick mark
      - Unacceptable → A Cross Mark
   - Confirm whether the image was uploaded in Step 1
      - Uploaded → A Tick mark
      - Not uploaded → A Cross Mark
   - If the template contains no image placeholders, you can ignore this step


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

## Modification

- According to the comparison results, users can manually modify the template.
- Alternatively, users can manually adjust the data according to the suggestions.
- Repeat until both match, then proceed to the next steps.


:::{hint}
- This step is optional and can be skipped.
- If users choose to skip this step, they need to manually confirm the match between data and template in the subsequent steps.
- A successful comparison does not guarantee a successful document generation. Users should still review the final output.
:::