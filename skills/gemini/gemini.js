#!/usr/bin/env node
/**
 * Gemini API Client з підтримкою зображень
 * Usage: 
 *   node gemini.js [prompt]                    - текстовий запит
 *   node gemini.js image [image-path] [prompt] - аналіз зображення
 */

const API_KEY = process.env.GEMINI_API_KEY || 'AIzaSyDjHTizhAG4haSUMRJ5qHvnFcOL15arsGQ';
const https = require('https');
const fs = require('fs');

// Функція для кодування зображення в base64
function encodeImage(filePath) {
  const data = fs.readFileSync(filePath);
  return data.toString('base64');
}

// Функція для визначення MIME-типу
function getMimeType(filePath) {
  const ext = filePath.split('.').pop().toLowerCase();
  const mimeTypes = {
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'webp': 'image/webp'
  };
  return mimeTypes[ext] || 'image/jpeg';
}

// Текстовий запит
function textPrompt(prompt) {
  return {
    contents: [{
      parts: [{
        text: prompt
      }]
    }]
  };
}

// Запит з зображенням
function imagePrompt(imagePath, prompt) {
  const base64Image = encodeImage(imagePath);
  const mimeType = getMimeType(imagePath);
  
  return {
    contents: [{
      parts: [
        {
          text: prompt
        },
        {
          inline_data: {
            mime_type: mimeType,
            data: base64Image
          }
        }
      ]
    }]
  };
}

// Відправка запиту
function sendRequest(requestData) {
  const options = {
    hostname: 'generativelanguage.googleapis.com',
    path: `/v1beta/models/gemini-2.0-flash:generateContent?key=${API_KEY}`,
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  };

  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const result = JSON.parse(data);
          if (result.error) {
            reject(new Error(result.error.message));
          } else {
            const text = result.candidates?.[0]?.content?.parts?.[0]?.text;
            resolve(text || 'No response text found');
          }
        } catch (e) {
          reject(new Error(`Parse error: ${e.message}`));
        }
      });
    });

    req.on('error', (e) => reject(e));
    req.write(JSON.stringify(requestData));
    req.end();
  });
}

// Головна функція
async function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.log('Usage:');
    console.log('  node gemini.js [prompt]                    - текстовий запит');
    console.log('  node gemini.js image [image-path] [prompt] - аналіз зображення');
    console.log('');
    console.log('Examples:');
    console.log('  node gemini.js "Яка погода сьогодні?"');
    console.log('  node gemini.js image /path/to/photo.jpg "Опиши це зображення"');
    process.exit(1);
  }

  try {
    let requestData;
    
    if (args[0] === 'image') {
      // Режим зображення
      if (args.length < 3) {
        console.error('Error: Для режиму image потрібно: image [path] [prompt]');
        process.exit(1);
      }
      const imagePath = args[1];
      const prompt = args.slice(2).join(' ');
      
      if (!fs.existsSync(imagePath)) {
        console.error(`Error: Файл не знайдено: ${imagePath}`);
        process.exit(1);
      }
      
      console.log(`Аналізую зображення: ${imagePath}\n`);
      requestData = imagePrompt(imagePath, prompt);
    } else {
      // Текстовий режим
      const prompt = args.join(' ');
      requestData = textPrompt(prompt);
    }
    
    const response = await sendRequest(requestData);
    console.log(response);
    
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

main();
