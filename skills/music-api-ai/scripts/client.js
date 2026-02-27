#!/usr/bin/env node
/**
 * MusicAPI.ai Client
 * Create music generation task and poll for completion
 */

const API_BASE = 'https://api.musicapi.ai/api/v1/sonic';
const API_KEY = process.env.MUSICAPI_KEY || '0f8dc17272d612483647231c6aef1705';

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
  const response = await makeRequest(`${API_BASE}/create`, {
    method: 'POST',
    body: JSON.stringify(params)
  });
  return response;
}

async function checkStatus(taskId) {
  const response = await makeRequest(`${API_BASE}/task/${taskId}`);
  return response;
}

async function pollUntilComplete(taskId, onStatus = () => {}) {
  const maxAttempts = 60; // 10 minutes max (10s intervals)
  
  for (let i = 0; i < maxAttempts; i++) {
    const status = await checkStatus(taskId);
    onStatus(status);
    
    if (status.status === 'complete' || status.status === 'success') {
      return status;
    }
    
    if (status.status === 'failed' || status.status === 'error') {
      throw new Error(`Task failed: ${status.error || 'Unknown error'}`);
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

// CLI usage
if (import.meta.url === `file://${process.argv[1]}`) {
  const command = process.argv[2];
  
  if (command === 'create') {
    const params = JSON.parse(process.argv[3]);
    const result = await createTask(params);
    console.log(JSON.stringify(result, null, 2));
  }
  
  if (command === 'status') {
    const taskId = process.argv[3];
    const result = await checkStatus(taskId);
    console.log(JSON.stringify(result, null, 2));
  }
  
  if (command === 'poll') {
    const taskId = process.argv[3];
    const result = await pollUntilComplete(taskId, (s) => {
      console.error(`Status: ${s.status}`);
    });
    console.log(JSON.stringify(result, null, 2));
  }
}

export { createTask, checkStatus, pollUntilComplete, downloadAudio };
