#!/usr/bin/env node
/**
 * Airtable File Upload
 * Usage: node airtable-upload.js <file_path> <base_id> <table_name>
 */

const fs = require('fs');
const https = require('https');

const AIRTABLE_TOKEN = process.env.AIRTABLE_TOKEN;
if (!AIRTABLE_TOKEN) {
  console.error('Error: AIRTABLE_TOKEN not set');
  process.exit(1);
}

const filePath = process.argv[2];
const baseId = process.argv[3];
const tableName = process.argv[4] || 'Table 1';

if (!filePath || !baseId) {
  console.log('Usage: node airtable-upload.js <file_path> <base_id> [table_name]');
  process.exit(1);
}

// First, upload file to get URL
const fileName = filePath.split('/').pop();
const fileData = fs.readFileSync(filePath);

// Create record with attachment
const recordData = JSON.stringify({
  fields: {
    'Name': fileName,
    'File': [
      {
        url: 'data:audio/mpeg;base64,' + fileData.toString('base64')
      }
    ]
  }
});

const options = {
  hostname: 'api.airtable.com',
  path: `/v0/${baseId}/${encodeURIComponent(tableName)}`,
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${AIRTABLE_TOKEN}`,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(recordData)
  }
};

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    try {
      const response = JSON.parse(data);
      if (response.id) {
        console.log('Upload successful!');
        console.log('Record ID:', response.id);
        if (response.fields?.File?.[0]?.url) {
          console.log('File URL:', response.fields.File[0].url);
        }
      } else {
        console.error('Error:', response);
      }
    } catch (e) {
      console.error('Parse error:', e.message);
      console.log('Raw:', data.substring(0, 500));
    }
  });
});

req.on('error', (e) => console.error('Request error:', e.message));
req.write(recordData);
req.end();
