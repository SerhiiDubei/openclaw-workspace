#!/usr/bin/env node
/**
 * Gemini Vision API Image Analysis
 * Usage: node gemini-vision.js <image_path> [prompt]
 */

const fs = require('fs');
const https = require('https');

const API_KEY = process.env.GEMINI_API_KEY;
if (!API_KEY) {
  console.error('Error: GEMINI_API_KEY not set');
  process.exit(1);
}

const imagePath = process.argv[2];
const prompt = process.argv[3] || 'Describe this image in detail';

if (!imagePath) {
  console.log('Usage: node gemini-vision.js <image_path> [prompt]');
  process.exit(1);
}

const base64Image = fs.readFileSync(imagePath, 'base64');

const requestData = JSON.stringify({
  contents: [{
    parts: [
      { text: prompt },
      {
        inline_data: {
          mime_type: 'image/jpeg',
          data: base64Image
        }
      }
    ]
  }]
});

const options = {
  hostname: 'generativelanguage.googleapis.com',
  path: `/v1beta/models/gemini-2.0-flash:generateContent?key=${API_KEY}`,
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  }
};

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    try {
      const response = JSON.parse(data);
      if (response.candidates?.[0]?.content?.parts?.[0]?.text) {
        console.log(response.candidates[0].content.parts[0].text);
      } else {
        console.error('Error:', response.error?.message || 'Unknown error');
      }
    } catch (e) {
      console.error('Parse error:', e.message);
    }
  });
});

req.on('error', (e) => console.error('Request error:', e.message));
req.write(requestData);
req.end();
