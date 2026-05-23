# Command A+ Automation

This minimal automation artifact demonstrates a simple API endpoint that returns a greeting.

```javascript
// pages/api/command-a-plus.js
export default function handler(req, res) {
  res.status(200).json({ message: "Command A+ is live!" });
}
```

Deploy this to Vercel to get a live endpoint.
