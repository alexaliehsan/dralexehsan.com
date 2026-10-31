import fs from 'node:fs';

const htmlPath = 'dist/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');
const rows = [
  ['Pediatric fever','Internal Medicine','Pediatric fever explained through age-specific temperature thresholds, common causes, hydration, evaluation, treatment principles, and warning signs that require prompt medical attention.','English'],
  ['Childhood asthma','Internal Medicine','Childhood asthma explained through symptoms, triggers, inhaler use, monitoring, prevention, school planning, and warning signs that require urgent medical attention.','English'],
  ['Developmental milestones','Internal Medicine','Developmental milestones explained in plain language, including typical patterns, screening, normal variation, early warning signs, and when pediatric evaluation may be helpful.','English'],
  ['Sports physicals','Internal Medicine','Sports physicals explained through health history, examination, safe participation, injury prevention, cardiac warning signs, and questions to discuss with a qualified clinician.','English']
];
const serialized = rows.map(row => `      ['${row.join("','")}']`).join(',\n');
const marker = '    guides.push(...oncologyExpansion,...medicalExpansion,...prioritySearchExpansion,...fiveHundredExpansion,...sevenHundredExpansion);';
if (!html.includes(marker)) throw new Error('Guide insertion marker not found');
html = html.replace(marker, `    const finalSevenHundredGuides=[\n${serialized}\n    ];\n    guides.push(...oncologyExpansion,...medicalExpansion,...prioritySearchExpansion,...fiveHundredExpansion,...sevenHundredExpansion,...finalSevenHundredGuides);`);
fs.writeFileSync(htmlPath, html);
console.log('Added final 4 guides for a total of 700.');
