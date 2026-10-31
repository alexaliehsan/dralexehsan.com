import fs from 'node:fs';

const htmlPath = 'dist/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');

const existing = new Set(
  [...html.matchAll(/\['([^']+)'\s*,\s*'[^']+'\s*,\s*'[^']*'\s*,\s*'[^']+'\]/g)]
    .map(match => match[1].toLowerCase())
);

const groups = {
  'Internal Medicine': [
    'Acne','Rosacea','Atopic dermatitis','Contact dermatitis','Psoriasis','Hidradenitis suppurativa','Urticaria','Alopecia areata','Vitiligo','Cellulitis','Impetigo','Shingles','Fungal skin infections','Nail fungus','Scabies','Bedbug bites','Skin abscess','Pressure injuries','Venous stasis dermatitis','Diabetic foot ulcers','Migraine','Tension headache','Cluster headache','Medication overuse headache','Trigeminal neuralgia','Bell palsy','Epilepsy','Febrile seizures','Multiple sclerosis','Parkinson disease','Amyotrophic lateral sclerosis','Huntington disease','Normal pressure hydrocephalus','Idiopathic intracranial hypertension','Concussion','Traumatic brain injury','Carpal tunnel syndrome','Sciatica','Cervical radiculopathy','Lumbar spinal stenosis','Major depressive disorder','Generalized anxiety disorder','Panic disorder','Post-traumatic stress disorder','Obsessive compulsive disorder','Bipolar disorder','Schizophrenia','Attention deficit hyperactivity disorder','Autism spectrum disorder','Eating disorders','Alcohol use disorder','Opioid use disorder','Tobacco dependence','Insomnia treatment','Sleep apnea treatment','Narcolepsy','Circadian rhythm disorders','Grief and bereavement','Caregiver stress','Delirium','Falls in older adults'
  ],
  'Tests & Treatment': [
    'Blood pressure monitoring at home','Continuous glucose monitoring','Ambulatory heart monitoring','Coronary calcium scan','CT angiography','Cardiac catheterization','Upper endoscopy','Colonoscopy preparation','Capsule endoscopy','Liver elastography','Kidney biopsy','Skin biopsy','Patch testing for allergies','Food allergy testing','Spirometry','Bronchoscopy','Thoracentesis','Paracentesis','Joint aspiration','Arthroscopy','Mammography','Breast ultrasound','Breast MRI','Pelvic ultrasound','Hysteroscopy','Colposcopy','Prenatal genetic screening','Newborn screening','Hearing tests','Vision screening','Sleep hygiene','Cognitive behavioral therapy','Physical therapy','Occupational therapy','Speech therapy','Cardiac rehabilitation','Pulmonary rehabilitation','Dialysis','Kidney transplantation','Organ donation','Antibiotic stewardship','Medication reconciliation','Polypharmacy in older adults','Shared decision making','Understanding absolute risk','Understanding relative risk','Reading a clinical study','Understanding confidence intervals','False positive test results','False negative test results'
  ],
  'Cancer': [
    'Cancer survivorship care','Late effects of cancer treatment','Second primary cancers','Cancer screening after treatment','Cardio-oncology','Oncofertility','Geriatric oncology assessment','Adolescent and young adult oncology','Cancer pain management','Cancer-related insomnia','Cancer-related anxiety','Cancer-related depression','Sexual health after cancer','Menopause after cancer treatment','Bone health after cancer treatment','Cognitive changes after chemotherapy','Return to exercise after cancer','Return to work after cancer treatment','Travel during cancer treatment','Vaccines after stem cell transplant','Nutrition after stem cell transplant','Graft-versus-host disease of the skin','Graft-versus-host disease of the gut','Graft-versus-host disease of the liver','Cytokine release syndrome','Immune effector cell neurotoxicity syndrome','CAR T-cell therapy preparation','Bispecific antibody monitoring','Tumor lysis prevention','Febrile neutropenia prevention','Central line infection prevention','Oral mucositis prevention','Hand-foot syndrome','Radiation dermatitis','Cancer-related itching','Malignant spinal cord compression','Brain metastasis symptoms','Leptomeningeal disease symptoms','Neutropenic diet myths','Complementary medicine during cancer care'
  ],
  'Blood': [
    'Iron deficiency without anemia','Anemia in pregnancy','Anemia in older adults','Drug-induced hemolytic anemia','Paroxysmal nocturnal hemoglobinuria','Aplastic anemia','Pure red cell aplasia','Diamond-Blackfan anemia','Fanconi anemia','Shwachman-Diamond syndrome','Congenital dyserythropoietic anemia','Methemoglobinemia','Sickle cell pain crisis','Acute chest syndrome','Sickle cell kidney disease','Sickle cell stroke prevention','Thalassemia transfusion care','Iron chelation therapy','Platelet transfusion refractoriness','Neonatal alloimmune thrombocytopenia','Gestational thrombocytopenia','Thrombocytopenia in liver disease','Thrombocytopenia in infection','Neutropenia after chemotherapy','Febrile neutropenia','Secondary polycythemia','Reactive thrombocytosis','Clonal hematopoiesis','Monoclonal B-cell lymphocytosis','Smoldering multiple myeloma'
  ],
  'Prevention': [
    'Adult vaccination schedule','Childhood vaccination schedule','Influenza prevention','COVID-19 prevention','RSV prevention','Pneumococcal vaccination','HPV vaccination','Hepatitis A vaccination','Hepatitis B vaccination','Meningococcal vaccination','Tetanus vaccination','Travel vaccines','Sun protection','Skin cancer self-examination','Breast cancer screening','Cervical cancer screening','Colorectal cancer screening','Lung cancer screening','Prostate cancer screening decisions','Osteoporosis screening','Abdominal aortic aneurysm screening','Depression screening','Diabetes screening','Cholesterol screening','Blood pressure screening','Healthy sleep duration','Physical activity recommendations','Strength training for health','Healthy eating patterns','Reducing alcohol-related risk','Quitting tobacco','Fall prevention at home','Firearm injury prevention','Food safety','Heat illness prevention','Cold weather safety','Preventing medication errors','Advance directives','Health care proxy','Preparing for a medical visit'
  ]
};

const descriptions = {
  'Cancer': title => `${title} explained in plain language, including who may be affected, common symptoms or concerns, evaluation, treatment and supportive-care principles, monitoring, and questions to discuss with an oncology team.`,
  'Blood': title => `${title} explained through blood counts, likely causes, confirmatory testing, complications, treatment principles, follow-up, and when hematology evaluation may be important.`,
  'Internal Medicine': title => `${title} explained through common symptoms, risk factors, evaluation, treatment principles, prevention, follow-up, and warning signs that require prompt medical attention.`,
  'Tests & Treatment': title => `${title} explained in plain language, including why it is used, what to expect, benefits, limitations, possible risks, and how results or response can guide next steps.`,
  'Prevention': title => `${title} explained with practical, evidence-based steps, who may benefit, common limitations, and questions to discuss with a qualified healthcare professional.`
};

const candidates = Object.entries(groups).flatMap(([category, titles]) =>
  titles.map(title => [title, category === 'Prevention' ? 'Internal Medicine' : category, descriptions[category](title), 'English'])
);
const additions = candidates.filter(row => !existing.has(row[0].toLowerCase())).slice(0, 200);
if (additions.length !== 200) throw new Error(`Expected 200 unique guide additions, found ${additions.length}`);

const escapeValue = value => value.replaceAll('\\', '\\\\').replaceAll("'", "\\'");
const rows = additions.map(row => `      ['${escapeValue(row[0])}','${escapeValue(row[1])}','${escapeValue(row[2])}','${row[3]}']`).join(',\n');
const marker = '    guides.push(...oncologyExpansion,...medicalExpansion,...prioritySearchExpansion,...fiveHundredExpansion);';
if (!html.includes(marker)) throw new Error('Guide insertion marker not found');
html = html.replace(marker, `    const sevenHundredExpansion=[\n${rows}\n    ];\n    guides.push(...oncologyExpansion,...medicalExpansion,...prioritySearchExpansion,...fiveHundredExpansion,...sevenHundredExpansion);`);

html = html.replaceAll('Search 500 medical guides', 'Search 700 medical guides');
html = html.replaceAll('500 medical guides', '700 medical guides');
fs.writeFileSync(htmlPath, html);
console.log(`Added ${additions.length} guides for a total of ${existing.size + additions.length}.`);

