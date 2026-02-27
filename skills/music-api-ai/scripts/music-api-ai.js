#!/usr/bin/env node
/**
 * Main CLI for MusicAPI.ai skill
 * Usage: node music-api-ai.js "create a jazz song about rain"
 */

import { generatePrompt, parseRequest } from './prompt-generator.js';
import { createTask, pollUntilComplete, downloadAudio } from './client.js';
import { writeFile, appendFile, mkdir } from 'fs/promises';
import { existsSync } from 'fs';
import path from 'path';

const LOG_FILE = './memory/music-log.jsonl';

async function logGeneration(data) {
  if (!existsSync('./memory')) {
    await mkdir('./memory', { recursive: true });
  }
  await appendFile(LOG_FILE, JSON.stringify({
    timestamp: new Date().toISOString(),
    ...data
  }) + '\n');
}

async function generateMusic(userInput) {
  console.log('🎵 Parsing request...');
  const parsed = parseRequest(userInput);
  console.log('Detected:', parsed);
  
  console.log('🎵 Generating production prompt...');
  const promptData = generatePrompt(parsed.request, parsed);
  
  // For now, use OpenAI/Claude to generate the full lyrics
  // This would be done by the main agent using the promptData
  console.log('Prompt template ready:', promptData.user.substring(0, 200) + '...');
  
  return {
    parsed,
    promptTemplate: promptData
  };
}

async function submitToAPI(fullParams) {
  console.log('🎵 Creating music task...');
  const createResult = await createTask(fullParams);
  
  if (!createResult.task_id && !createResult.body?.task_id) {
    throw new Error(`Failed to create task: ${JSON.stringify(createResult)}`);
  }
  
  const taskId = createResult.task_id || createResult.body.task_id;
  console.log(`✓ Task created: ${taskId}`);
  
  console.log('⏳ Waiting for generation (this may take 1-3 minutes)...');
  const finalResult = await pollUntilComplete(taskId, (status) => {
    process.stderr.write(`\rStatus: ${status.status} ${status.progress ? `(${status.progress}%)` : ''}  `);
  });
  
  console.log('\n✓ Generation complete!');
  return finalResult;
}

async function downloadAndSave(audioUrl, title) {
  const safeTitle = title.replace(/[^a-z0-9]/gi, '_').toLowerCase();
  const outputPath = `./output/${safeTitle}_${Date.now()}.mp3`;
  
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
  
  if (!input) {
    console.log('Usage: node music-api-ai.js "create a jazz song about rain"');
    process.exit(1);
  }
  
  try {
    // Step 1: Parse and prepare
    const { parsed, promptTemplate } = await generateMusic(input);
    
    // Step 2: The agent should generate full lyrics using promptTemplate
    // For CLI demo, we'd need the full params from user or LLM
    console.log('\n--- Ready for LLM generation ---');
    console.log('Use this prompt with your LLM to generate full lyrics:');
    console.log(JSON.stringify(promptTemplate, null, 2));
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  }
}

export { generateMusic, submitToAPI, downloadAndSave, logGeneration };

// Run if called directly
if (import.meta.url === `file://${process.argv[1]}`) {
  main();
}
