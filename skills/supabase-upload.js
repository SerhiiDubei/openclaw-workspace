#!/usr/bin/env node
/**
 * Supabase Storage Upload
 * Usage: node supabase-upload.js <file_path> <bucket_name>
 */

const fs = require('fs');
const https = require('https');

const SUPABASE_URL = process.env.SUPABASE_URL || 'https://your-project.supabase.co';
const SUPABASE_KEY = process.env.SUPABASE_KEY;

if (!SUPABASE_KEY) {
  console.error('Error: SUPABASE_KEY not set');
  process.exit(1);
}

const filePath = process.argv[2];
const bucketName = process.argv[3] || 'music';
const fileName = process.argv[4] || filePath.split('/').pop();

if (!filePath) {
  console.log('Usage: node supabase-upload.js <file_path> [bucket_name] [file_name]');
  process.exit(1);
}

const fileData = fs.readFileSync(filePath);
const contentType = 'audio/mpeg';

const options = {
  hostname: SUPABASE_URL.replace('https://', ''),
  path: `/storage/v1/object/${bucketName}/${fileName}`,
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${SUPABASE_KEY}`,
    'Content-Type': contentType,
    'Content-Length': fileData.length,
    'x-upsert': 'true'
  }
};

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    try {
      const response = JSON.parse(data);
      if (response.Key) {
        const publicUrl = `${SUPABASE_URL}/storage/v1/object/public/${response.Key}`;
        console.log('Upload successful!');
        console.log('Public URL:', publicUrl);
      } else {
        console.error('Error:', response);
      }
    } catch (e) {
      console.error('Parse error:', e.message);
      console.log('Raw:', data);
    }
  });
});

req.on('error', (e) => console.error('Request error:', e.message));
req.write(fileData);
req.end();
