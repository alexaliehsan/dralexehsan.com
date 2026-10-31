import fs from 'node:fs';
import path from 'node:path';

const htmlPath = 'dist/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');
const topics = [
  'Acne','Rosacea','Atopic dermatitis','Psoriasis','Hidradenitis suppurativa','Urticaria','Alopecia areata','Vitiligo','Cellulitis','Shingles','Migraine','Cluster headache','Trigeminal neuralgia','Bell palsy','Epilepsy','Multiple sclerosis','Parkinson disease','Amyotrophic lateral sclerosis','Concussion','Carpal tunnel syndrome','Sciatica','Major depressive disorder','Generalized anxiety disorder','Panic disorder','Post-traumatic stress disorder','Obsessive compulsive disorder','Bipolar disorder','Schizophrenia','Attention deficit hyperactivity disorder','Autism spectrum disorder','Sleep apnea treatment','Narcolepsy','Grief and bereavement','Delirium','Blood pressure monitoring at home','Continuous glucose monitoring','Ambulatory heart monitoring','Coronary calcium scan','Cardiac catheterization','Upper endoscopy','Colonoscopy preparation','Capsule endoscopy','Liver elastography','Kidney biopsy','Skin biopsy','Spirometry','Bronchoscopy','Thoracentesis','Paracentesis','Mammography','Breast ultrasound','Breast MRI','Pelvic ultrasound','Prenatal genetic screening','Newborn screening','Physical therapy','Cardiac rehabilitation','Pulmonary rehabilitation','Dialysis','Kidney transplantation','Cancer survivorship care','Cardio-oncology','Cancer pain management','Cancer-related insomnia','Bone health after cancer treatment','Cognitive changes after chemotherapy','Graft-versus-host disease of the skin','Cytokine release syndrome','CAR T-cell therapy preparation','Bispecific antibody monitoring','Tumor lysis prevention','Febrile neutropenia prevention','Oral mucositis prevention','Hand-foot syndrome','Radiation dermatitis','Malignant spinal cord compression','Brain metastasis symptoms','Iron deficiency without anemia','Aplastic anemia','Paroxysmal nocturnal hemoglobinuria','Sickle cell pain crisis','Acute chest syndrome','Iron chelation therapy','Febrile neutropenia','Clonal hematopoiesis','Smoldering multiple myeloma','Adult vaccination schedule','HPV vaccination','Sun protection','Breast cancer screening','Cervical cancer screening','Colorectal cancer screening','Lung cancer screening','Osteoporosis screening','Healthy sleep duration','Strength training for health','Quitting tobacco','Fall prevention at home','Food safety','Advance directives'
];

if (topics.length !== 100) throw new Error(`Expected 100 topics, found ${topics.length}`);
const slugify = value => value.toLowerCase().normalize('NFKD').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const escapeHtml = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const palette = [
  ['#083b66','#0f7fa8','#d9f2f7'],['#54204f','#a04783','#f6ddea'],['#284b36','#4d9365','#def2e5'],['#5a3515','#c7772b','#f9e4ce']
];

const cards = [];
topics.forEach((topic, index) => {
  const slug = slugify(topic);
  const [dark, mid, light] = palette[index % palette.length];
  const words = topic.split(' ');
  const midpoint = Math.ceil(words.length / 2);
  const line1 = escapeHtml(words.slice(0, midpoint).join(' '));
  const line2 = escapeHtml(words.slice(midpoint).join(' '));
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="640" height="640" viewBox="0 0 640 640" role="img" aria-labelledby="title desc"><title id="title">${escapeHtml(topic)}</title><desc id="desc">Patient education visual for ${escapeHtml(topic)}</desc><rect width="640" height="640" rx="48" fill="${light}"/><circle cx="320" cy="250" r="154" fill="white" opacity=".93"/><path d="M320 138v224M208 250h224" stroke="${mid}" stroke-width="58" stroke-linecap="round"/><circle cx="320" cy="250" r="176" fill="none" stroke="${dark}" stroke-width="12" opacity=".18"/><text x="320" y="492" text-anchor="middle" font-family="Arial,sans-serif" font-size="34" font-weight="700" fill="${dark}">${line1}</text>${line2 ? `<text x="320" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="34" font-weight="700" fill="${dark}">${line2}</text>` : ''}<text x="320" y="592" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" fill="${dark}" opacity=".75">Medical education</text></svg>`;
  fs.writeFileSync(path.join('dist', 'illustrations', `${slug}.svg`), svg);
  cards.push(`<a class="illustration-card" href="#library" data-topic="${escapeHtml(topic)}"><img src="illustrations/${slug}.svg" alt="${escapeHtml(topic)} medical education visual" loading="lazy" width="640" height="640"><span>${escapeHtml(topic)}</span><small>Open guide</small></a>`);
});

const insertionPoint = '</div><div class="illustration-empty" id="illustration-empty">';
if (!html.includes(insertionPoint)) throw new Error('Illustration insertion marker not found');
html = html.replace(insertionPoint, `${cards.join('')}</div><div class="illustration-empty" id="illustration-empty">`);
html = html.replaceAll('400 medical illustrations', '500 medical illustrations');
html = html.replaceAll('Showing 400 illustrations', 'Showing 500 illustrations');
html = html.replaceAll('of 400 illustrations', 'of 500 illustrations');
fs.writeFileSync(htmlPath, html);
console.log('Added 100 medical education visuals for a total of 500.');
