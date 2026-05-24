# BTC Price Tracker Automation

This minimal automation artifact fetches the current Bitcoin price and displays it.

```html
<div id="btc-price">Loading...</div>
<script>
async function fetchPrice() {
  const res = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd');
  const data = await res.json();
  document.getElementById('btc-price').innerText = `BTC: $${data.bitcoin.usd}`;
}
fetchPrice();
setInterval(fetchPrice, 60000); // refresh every minute
</script>
```

*Deploy this page to quickly monitor the price of Bitcoin.*