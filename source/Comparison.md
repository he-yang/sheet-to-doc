# Data and Placeholder Comparison

[中文](https://sheet-to-doc.wtsolutions.cn/zh-cn/latest/Comparison.html)

(Since version 2.1.0.0)

Step 2.1 Data Comparison is optional and can be skipped.

Step 2.1 compares the data and images provided in Step 1 with the content of the Word template uploaded in Step 2, helping users identify errors in the template and offering suggestions for correction.

After the comparison, recommendations for subsequent steps are given; however, regardless of the comparison results, you may skip Step 2.1 and proceed directly to the “Generate Document” button in Step 3.

## Comparison Process

- Data placeholders vs. data
   - Compare the data items provided in Step 1 with the data placeholders in the Word template uploaded in Step 2
   - If the template contains a placeholder `{Name}` but Step 1 only supplies `Age` without `Name`, it is marked as a mismatch
   - ✅ indicates a match; ❌ indicates a mismatch
   - Based on the template, recommend whether to use Generation Mode 1 or Generation Mode 2

- Filters comparison
   - Detect any filters in the Word template uploaded in Step 2
   - If Sheet to Doc can process these filters, they are marked ✅
   - If Sheet to Doc cannot process them, they are marked ❌
   - Refer to [Word Template](https://sheet-to-doc.wtsolutions.cn/en/latest/WordTemplate.html) for supported filters
   - If the template contains no filters, you can ignore this step

- Image placeholders vs. images
   - First detect whether the Word template uploaded in Step 2 uses image placeholders
   - If placeholders exist, check whether the images data supplied in Step 1 match them
      - Match → ✅
      - Mismatch → ❌
   - Verify that the image type is acceptable (jpg, png, jpeg, gif, bmp)
      - Acceptable → ✅
      - Unacceptable → ❌
   - Confirm whether the image was uploaded in Step 1
      - Uploaded → ✅
      - Not uploaded → ❌
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

## Modification Methods

- Users can manually modify the template based on the comparison results.
- Alternatively, users can manually adjust the data according to the suggestions.
- Repeat until both match, then proceed to the next steps.

## Additional Notes

- This step is optional and can be skipped.
- If users choose to skip this step, they need to manually confirm the match between data and template in the subsequent steps.
- A successful comparison does not guarantee a successful document generation. Users should still review the final output.