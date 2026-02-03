# Pricing

[中文](https://sheet-to-doc.wtsolutions.cn/zh-cn/latest/Pricing.html)



<script src="https://cdn.paddle.com/paddle/v2/paddle.js"></script>
<script type="text/javascript">
  Paddle.Initialize({ 
    token: "live_1c12997e01d459f8b047201cd55"
  });
  function checkoutnow(priceId){
    Paddle.Checkout.open({
        items: [{priceId: priceId,quantity: 1}]
    });  
  }
  function checkoutnowwithcustomdata(priceId, customData){
    if (!customData) {
      alert("Please enter your Device ID, which can be obtained from the topright corner of the offline installed version of Sheet-to-Doc.");
      return;
    }
    Paddle.Checkout.open({
        items: [{priceId: priceId,quantity: 1}],
        customData : {
          machine_id: customData
        }
    });  
  }
</script>

[中文](https://sheet-to-doc.wtsolutions.cn/zh-cn/latest/Pricing.html)


## Software Versions


| Feature Limits | Free Version | Pro Version |
| :--------: | :--------: | :--------: |
| Data Length | 10 rows per time | Unlimited |
| Image Quantity (including QR Codes) | 10 images per time | Unlimited |



:::{include} _snippet/version.md
:::

## Pricing Models

:::{note}
Different Pricing Models for Web Version, PWA Version, Addin Version, and Offline Desktop Version Installations
- Subscription Model for Web Version, PWA Version, and Addin Version
- One-time-purchase Model for Offline Desktop Version
:::


### Subscribe though Paddle for Web, PWA Pro, and Addin Pro Version

The subscription is managed through our trusted partner [Paddle](https://paddle.com/). 

#### Payment Methods
- Paypal
- Credit Card/Debit Card with Visa, Mastercard, American Express, Maestro, Cartes Bancaires, Dankort, UnionPay, Mada, JCB, Diners Club, and Discover.
- Google Pay (Chrome or Android device required)
- Apple Pay (Apple Device required)
- BanContact in BE


#### Subscription links

<button onclick='checkoutnow("pri_01ke8y2d2emyfgq1xnjwtk88eb")'>Start 7 Day Free Trial Now, then USD $2.66 / month (excluding tax)</button>

<button onclick='checkoutnow("pri_01ke8y6dzhk312g4g11rwdt54r")'>Start 7 Day Free Trial Now, then USD $4.29 / 3 months (excluding tax)</button>

<button onclick='checkoutnow("pri_01ke8y8kezwcp0a9k6aqv7z0sy")'>Start 7 Day Free Trial Now, then USD $5.59 / 6 months (excluding tax)</button>

<button onclick='checkoutnow("pri_01ke8yc08j2afhpvjhz1jm63ej")'>Start 7 Day Free Trial Now, then USD $6.99 / year (excluding tax)</button>

:::{note}
1. When subscribing, please enter an accessible email address, which will be your Pro Code.
2. 7-day free trial available, you can cancel for free before the trial ends, and the system will automatically deduct payment after the trial ends.
3. After subscribing, the Pro Code can be used on up to 3 devices.
4. Tax is not included in the subscription price, depending on your local tax rules.
:::

#### Cancel or Manage Subcription (Paddle)

You can cancel your subscription at any time. After the current billing cycle ends, you will no longer have access to the pro features. Management of subscription can be performed through paddle customer portal.

[https://customer-portal.paddle.com/cpl_01jxkve1dh6g9v8j172pybc4nf](https://customer-portal.paddle.com/cpl_01jxkve1dh6g9v8j172pybc4nf)


### Purchase Offline Desktop Version Pro Code

The transaction is managed through our trusted partner [Paddle](https://paddle.com/). 

#### Payment Methods
- Paypal
- Credit Card/Debit Card with Visa, Mastercard, American Express, Maestro, Cartes Bancaires, Dankort, UnionPay, Mada, JCB, Diners Club, and Discover.
- Google Pay (Chrome or Android device required)
- Apple Pay (Apple Device required)
- BanContact in BE

Offline desktop version Pro Code:

Price $14.99 with Discount Code: `WAHS8W4L0J` -> $6.99

Discount Code valid until 28, Feb 2026.

:::{note}
1. When purchasing, please enter an accessible email address, which will be used to receive the Pro Code.
2. When purchasing, please enter your Device ID, which can be obtained from the topright corner of the offline installed version of Sheet-to-Doc.
3. No free trial available for Offline Desktop Version, if you'd like to try the Pro Version, please try with the Web version 7-day-free-trial.
4. The Pro Code is binded to the Device ID, and only valid on the very same device.
5. The Pro Code is valid for lifetime, and can be used on future updated Offline Desktop Version.
6. This is a one-time purchase.
:::

## Purchase Link

Enter your Device ID (from the top right corner of the offline desktop version of Sheet-to-Doc.):

<input id="customdata" type="text" placeholder="Enter your Device ID">
<button onclick='checkoutnowwithcustomdata("pri_01kem3y7zgnwa7471qv9hws3qg", document.getElementById("customdata").value)'>Purchase Now</button>


Once the transaction is completed, you will receive the Pro Code via email within serveral minutes. If not, please contact us by email he.yang@wtsolutions.cn

When activating the Pro Code, please enter the Pro Code in the activation area of the offline desktop version of Sheet-to-Doc. If fails, please try to copy the Pro Code from the email, and make sure to copy the entire Pro Code, without any extra characters. If the problem persists, please contact us by email he.yang@wtsolutions.cn
