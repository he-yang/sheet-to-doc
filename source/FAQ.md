# FAQ

[中文](https://sheet-to-doc.wtsolutions.cn/zh-cn/latest/FAQ.html)


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

## Activation Issues

1. I entered the activation code, why does it say activation failed?
- Activation codes come in two types: online and offline desktop. The online activation code is the email address used during Stripe payment; the offline desktop activation code is the characters received via email after purchase.
- Offline and online activation codes are different and cannot be used interchangeably.
- The offline activation code is bound to the device. Each device has a fixed device code, and the activation code must match this device code; it cannot be used on other devices.
- When copying the offline activation code from your email, make sure there are no leading or trailing spaces or line breaks.

## File Download Issues
1. I generated multiple files, but only one or a few were downloaded?
- Different generation modes produce different files, for example:
  - Mode 2 generates a single file containing all content.
  - Mode 1 generates multiple files, each containing part of the content.
- Please check which generation mode you are using.
- When downloading multiple files, the browser usually asks for permission to download multiple files; you need to allow it.

## Data Related Issues
1. I pasted data, but it says there is an error, what should I do?
- Please check if the pasted data meets the requirements, for example:
  - Does the data contain a header row?
  - Does the data contain empty rows?
  - Does the data contain special characters?
- If the data meets the requirements, it may be a problem with the data content. Please check the specific rows where the error occurs and try to remove that row to see if the error is resolved.
- In addition to manual checking, we highly recommend using Excel's built-in error checking feature to verify the data. In Excel's formula bar, there is an error check button.