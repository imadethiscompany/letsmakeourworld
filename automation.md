# Automation Artifact: Simple Email Capture

This is a minimal automation artifact for **"Is 0-1 the easiest part of building a business?"**.

It includes a simple email capture form that posts to a dummy endpoint (you can replace with your own webhook).

```html
<form action="https://example.com/webhook" method="POST">
  <label for="email">Enter your email to get the free playbook:</label><br>
  <input type="email" id="email" name="email" required placeholder="you@example.com" style="margin-top:8px;padding:8px;width:250px;"/>
  <button type="submit" style="margin-left:8px;padding:8px;">Submit</button>
</form>
```

Feel free to integrate this form with your automation pipeline.
