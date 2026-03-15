#!/usr/bin/env node
/**
 * Main CLI for SunoAPI skill
 * Usage: node music-api-ai.js "create a jazz song about rain"
 * Updated for sunoapi.org provider
 */

import { generatePrompt, parseRequest } from './prompt-generator.js';
import { createTask, pollUntilComplete, downloadAudio } from './client.js';
import { writeFile, mkdir } from 'fs/promises';
import { existsSync } from 'fs';
import path from 'path';

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_KEY = process.env.SUPABASE_SERVICE_KEY;

async function saveToSupabase(data) {
  // Save track metadata to Supabase music_tracks table
  const response = await fetch(`${SUPABASE_URL}/rest/v1/music_tracks`, {
    method: 'POST',
    headers: {
      'apikey': SUPABASE_SERVICE_KEY,
      'Authorization': `Bearer ${SUPABASE_SERVICE_KEY}`,
      'Content-Type': 'application/json',
      'Prefer': 'return=representation'
    },
    body: JSON.stringify(data)
  });
  return response.json();
}

async function generateMusic(userInput, userId, username) {
  console.log('🎵 Parsing request...');
  const parsed = parseRequest(userInput);
  console.log('Detected:', parsed);
  
  console.log('🎵 Generating production prompt...');
  const promptData = generatePrompt(parsed.request, parsed);
  
  console.log('Prompt template ready:', promptData.user.substring(0, 200) + '...');
  
  return {
    parsed,
    promptTemplate: promptData,
    userId,
    username
  };
}

async function submitToAPI(fullParams, userId, username) {
  console.log('🎵 Creating music task...');
  const createResult = await createTask(fullParams);
  
  // Check if API call was successful
  if (createResult.code !== 200) {
    throw new Error(`Failed to create task: ${createResult.msg}`);
  }
  
  const taskId = createResult.data?.taskId;
  if (!taskId) {
    throw new Error(`No task_id in response: ${JSON.stringify(createResult)}`);
  }
  
  console.log(`✓ Task created: ${taskId}`);
  
  console.log('⏳ Waiting for generation (this may take 1-3 minutes)...');
  const finalResult = await pollUntilComplete(taskId, (status) => {
    process.stderr.write(`\rStatus: ${status.status}                    `);
  });
  
  console.log('\n✓ Generation complete!');
  return finalResult;
}

async function downloadAndSave(audioUrl, title, variant) {
  const safeTitle = title.replace(/[^a-z0-9]/gi, '_').toLowerCase();
  const outputPath = `./output/${safeTitle}_v${variant}.mp3`;
  
  if (!existsSync('./output')) {
    await mkdir('./output', { recursive: true });
  }
  
  console.log(`📥 Downloading to ${outputPath}...`);
  await downloadAudio(audioUrl, outputPath);
  
  return outputPath;
}

// Main execution
async function main() {
  const input = process.argv.slice(2).join(' ');
  const userId = process.env.USER_ID || 'unknown';
  const username = process.env.USERNAME || 'Unknown';
  
  if (!input) {
    console.log('Usage: node music-api-ai.js "create a jazz song about rain"');
    process.exit(1);
  }
  
  try {
    // Step 1: Parse and prepare
    const { parsed, promptTemplate } = await generateMusic(input, userId, username);
    
    // Step 2: The agent should generate full lyrics using promptTemplate
    console.log('\n--- Ready for LLM generation ---');
    console.log('Use this prompt with your LLM to generate full lyrics:');
    console.log(JSON.stringify(promptTemplate, null, 2));
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  }
}

export { generateMusic, submitToAPI, downloadAndSave, saveToSupabase };

// Run if called directly
if (import.meta.url === `file://${process.argv[1]}`) {
  main();
}