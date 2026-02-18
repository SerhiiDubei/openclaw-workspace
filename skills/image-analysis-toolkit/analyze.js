#!/usr/bin/env node
/**
 * Image Analysis via OpenAI Vision API
 * Usage: node analyze.js <image_path> [mode]
 */

const fs = require('fs');
const https = require('https');

const API_KEY = process.env.OPENAI_API_KEY;
if (!API_KEY) {
  console.error('Error: OPENAI_API_KEY not set');
  process.exit(1);
}

const imagePath = process.argv[2];
const mode = process.argv[3] || 'full';

if (!imagePath) {
  console.log('Usage: node analyze.js <image_path> [describe|prompt|ocr|full]');
  process.exit(1);
}

if (!fs.existsSync(imagePath)) {
  console.error('Error: File not found:', imagePath);
  process.exit(1);
}

const base64Image = fs.readFileSync(imagePath, 'base64');

const prompts = {
  describe: 'Describe this image in detail. Include: main subjects, colors, composition, lighting, mood, style, and any notable elements.',
  prompt: 'Create a detailed prompt for AI image generation that would recreate this image. Include style, subject, composition, lighting, colors, and technical details.',
  ocr: 'Extract all text visible in this image. Preserve formatting and layout as much as possible.',
  full: 'Provide comprehensive analysis:\n1) Detailed description of content\n2) Suggested AI generation prompt\n3) Any text visible (OCR)\n4) Style and artistic elements\n5) Technical composition details'
};

const requestData = JSON.stringify({
  model: 'gpt-4o',
  messages: [
    {
      role: 'user',
      content: [
        { type: 'text', text: prompts[mode] || prompts.full },
        {
          type: 'image_url',
          image_url: {
            url: `data:image/jpeg;base64,${base64Image}`
          }
        }
      ]
    }
  ],
  max_tokens: 2000
});

const options = {
  hostname: 'api.openai.com',
  path: '/v1/chat/completions',
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${API_KEY}`,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(requestData)
  }
};

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    try {
      const response = JSON.parse(data);
      if (response.choices && response.choices[0]) {
        console.log(response.choices[0].message.content);
      } else {
        console.error('Error:', response.error || 'Unknown error');
      }
    } catch (e) {
      console.error('Parse error:', e.message);
      console.log('Raw:', data.substring(0, 500));
    }
  });
});

req.on('error', (e) => {
  console.error('Request error:', e.message);
});

req.write(requestData);
req.end();
