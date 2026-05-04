<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>FireAlert Early Fire Detection</title>
<style>
  body {font-family: Arial, sans-serif; margin:0; padding:0; background:#f5f5f5;}
  .hero {background:#ff5722; color:#fff; padding:40px 20px; text-align:center;}
  .container {max-width:800px; margin:20px auto; background:#fff; padding:20px; border-radius:8px;}
  .form-group {margin-bottom:15px;}
  label {display:block; margin-bottom:5px;}
  input, button {padding:10px; width:100%; box-sizing:border-box;}
  button {background:#ff5722; color:#fff; border:none; cursor:pointer;}
  button:hover {opacity:0.9;}
</style>
</head>
<body>
<div class="hero">
<h1>FireAlert Early Fire Detection</h1>
<p>Realtime AI‑driven hotspot alerts for your business or municipality.</p>
<a href="https://buy.stripe.com/test_4gMfZ9ahRgbq22Lgzoc7z16" target="_blank"><button>Subscribe for $9/month</button></a>
</div>
<div class="container">
<h2>Set Up Your Alert</h2>
<div class="form-group">
<label for="lat">Latitude</label>
<input type="number" step="any" id="lat" placeholder="e.g., 34.05">
</div>
<div class="form-group">
<label for="lon">Longitude</label>
<input type="number" step="any" id="lon" placeholder="e.g., -118.25">
</div>
<div class="form-group">
<label for="email">Email for alerts</label>
<input type="email" id="email" placeholder="you@example.com">
</div>
<button id="setupBtn">Create Alert</button>
<p id="status"></p>
</div>
<script>
document.getElementById('setupBtn').addEventListener('click', async () => {
  const lat = document.getElementById('lat').value;
  const lon = document.getElementById('lon').value;
  const email = document.getElementById('email').value;
  const statusEl = document.getElementById('status');
  if(!lat || !lon || !email){statusEl.textContent='Please fill all fields.'; return;}
  statusEl.textContent='Setting up alert...';
  try {
    const resp = await fetch('https://api.wildfire.ai/alert', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({latitude: lat, longitude: lon, email: email})
    });
    const data = await resp.json();
    if(resp.ok){
      statusEl.textContent='Alert created! You will receive notifications when hotspots are detected.';
    } else {
      statusEl.textContent='Error: ' + (data.error || resp.status);
    }
  } catch(e){
    statusEl.textContent='Network error: ' + e.message;
  }
});
</script>
</body>
</html>