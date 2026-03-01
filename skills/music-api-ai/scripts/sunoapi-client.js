#!/usr/bin/env node
/**
 * SunoAPI.org Client - Standalone
 * Usage: node sunoapi-client.js "create a jazz song about rain"
 */

const API_BASE = 'https://api.sunoapi.org/api/v1';
const API_KEY = process.env.SUNOAPI_KEY || '9d1c695345ed3583c3c56b26c45d0b50';

async function makeRequest(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
      ...options.headers
    }
  });
  return response.json();
}

async function createTask(params) {
  const response = await makeRequest(`${API_BASE}/generate`, {
    method: 'POST',
    body: JSON.stringify(params)
  });
  return response;
}

async function checkStatus(taskId) {
  const response = await makeRequest(`${API_BASE}/generate/record-info?taskId=${taskId}`);
  return response;
}

async function pollUntilComplete(taskId, onStatus = () => {}) {
  const maxAttempts = 60; // 10 minutes max (10s intervals)
  
  for (let i = 0; i < maxAttempts; i++) {
    const result = await checkStatus(taskId);
    
    if (result.code !== 200) {
      onStatus({ status: 'error', error: result.msg });
      throw new Error(`API error: ${result.msg}`);
    }
    
    const status = result.data?.status || 'UNKNOWN';
    onStatus({ status, data: result.data });
    
    if (status === 'SUCCESS') {
      return result.data;
    }
    
    if (status === 'FAILED' || status === 'ERROR') {
      throw new Error(`Task failed: ${result.data?.errorMessage || 'Unknown error'}`);
    }
    
    // Wait 10 seconds before next poll
    await new Promise(r => setTimeout(r, 10000));
  }
  
  throw new Error('Polling timeout - task took too long');
}

async function downloadAudio(url, outputPath) {
  const response = await fetch(url);
  const buffer = await response.arrayBuffer();
  const fs = await import('fs');
  fs.writeFileSync(outputPath, Buffer.from(buffer));
  return outputPath;
}

// Main execution
async function main() {
  const input = process.argv.slice(2).join(' ');
  
  if (!input) {
    console.log('Usage: node sunoapi-client.js "create a jazz song about rain"');
    process.exit(1);
  }
  
  console.log('🎵 Creating music task...');
  console.log('Prompt:', input);
  
  try {
    const createResult = await createTask({
      prompt: input,
      customMode: true,
      instrumental: true,
      style: 'Jazz',
      title: 'AI Generated Track',
      model: 'V4_5',
      callBackUrl: 'https://httpbin.org/post'
    });
    
    if (createResult.code !== 200) {
      throw new Error(`Failed to create task: ${createResult.msg}`);
    }
    
    const taskId = createResult.data?.taskId;
    console.log(`✓ Task created: ${taskId}`);
    
    console.log('⏳ Waiting for generation (~2-3 minutes)...');
    const finalResult = await pollUntilComplete(taskId, (status) => {
      process.stdout.write(`\rStatus: ${status.status}                    `);
    });
    
    console.log('\n✓ Generation complete!');
    
    // Display results
    if (finalResult.response?.sunoData) {
      finalResult.response.sunoData.forEach((track, index) => {
        console.log(`\nTrack ${index + 1}:`);
        console.log(`  Title: ${track.title}`);
        console.log(`  Audio: ${track.audioUrl}`);
        console.log(`  Duration: ${track.duration}s`);
      });
    }
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  }
}

// Run if called directly
if (import.meta.url === `file://${process.argv[1]}`) {
  main();
}

export { createTask, checkStatus, pollUntilComplete, downloadAudio };