# importing library
import random

# Medical knowledge base
medical_db = {
    "headache": {
        "description": "A headache is pain in the head or face.",
        "causes": ["Stress", "Tension", "Migraine", "Dehydration", "Eye strain"],
        "remedies": ["Rest in a quiet room", "Apply cold compress", "Take OTC pain relievers", "Stay hydrated"]
    },
"osteomyelitis": {
  "description": "Osteomyelitis is an infection of the bone.",
  "causes": ["Bacterial infection", "Open fractures"],
  "remedies": ["Antibiotics", "Surgical drainage"]
},

"sepsis": {
  "description": "Sepsis is a life-threatening response to infection.",
  "causes": ["Severe bacterial infection"],
  "remedies": ["IV antibiotics", "Emergency hospital care"]
},

"septic_arthritis": {
  "description": "Septic arthritis is infection in a joint.",
  "causes": ["Bacterial infection"],
  "remedies": ["Antibiotics", "Joint drainage"]
},

"temporal_arteritis": {
  "description": "Temporal arteritis is inflammation of arteries in the head.",
  "causes": ["Autoimmune response"],
  "remedies": ["Corticosteroids"]
},

"vasculitis": {
  "description": "Vasculitis is inflammation of blood vessels.",
  "causes": ["Autoimmune disorders"],
  "remedies": ["Immunosuppressants"]
},

"wilson_disease": {
  "description": "Wilson disease is genetic disorder causing copper buildup.",
  "causes": ["Inherited mutation"],
  "remedies": ["Chelation therapy"]
},

"hemochromatosis": {
  "description": "Hemochromatosis causes excess iron accumulation.",
  "causes": ["Genetic mutation"],
  "remedies": ["Blood removal therapy"]
},

"cushing_syndrome": {
  "description": "Cushing syndrome is excess cortisol production.",
  "causes": ["Steroid overuse", "Adrenal tumor"],
  "remedies": ["Medication", "Surgery"]
},

"addison_disease": {
  "description": "Addison disease is adrenal hormone deficiency.",
  "causes": ["Autoimmune destruction"],
  "remedies": ["Hormone replacement therapy"]
},

"pheochromocytoma": {
  "description": "Pheochromocytoma is rare adrenal gland tumor.",
  "causes": ["Genetic mutation"],
  "remedies": ["Surgical removal"]
},

"acromegaly": {
  "description": "Acromegaly is excessive growth hormone in adults.",
  "causes": ["Pituitary tumor"],
  "remedies": ["Surgery", "Medication"]
},

"gigantism": {
  "description": "Gigantism is excessive growth hormone in children.",
  "causes": ["Pituitary tumor"],
  "remedies": ["Surgery"]
},

"pituitary_adenoma": {
  "description": "Pituitary adenoma is benign tumor of pituitary gland.",
  "causes": ["Abnormal cell growth"],
  "remedies": ["Surgery", "Medication"]
},

"retinal_detachment": {
  "description": "Retinal detachment is separation of retina from eye.",
  "causes": ["Eye injury", "Aging"],
  "remedies": ["Surgical repair"]
},

"macular_degeneration": {
  "description": "Macular degeneration causes central vision loss.",
  "causes": ["Aging"],
  "remedies": ["Eye injections", "Lifestyle changes"]
},

"keratitis": {
  "description": "Keratitis is inflammation of the cornea.",
  "causes": ["Infection", "Contact lens misuse"],
  "remedies": ["Antibiotic or antifungal drops"]
},

"uveitis": {
  "description": "Uveitis is inflammation of middle eye layer.",
  "causes": ["Autoimmune disease", "Infection"],
  "remedies": ["Steroid eye drops"]
},

"retinopathy": {
  "description": "Retinopathy is damage to retina blood vessels.",
  "causes": ["Diabetes", "High blood pressure"],
  "remedies": ["Laser therapy", "Blood sugar control"]
},

"hyperopia": {
  "description": "Hyperopia is farsightedness vision problem.",
  "causes": ["Eye shape abnormality"],
  "remedies": ["Corrective lenses"]
},

"myopia": {
  "description": "Myopia is nearsightedness vision problem.",
  "causes": ["Eye elongation"],
  "remedies": ["Glasses", "Contact lenses"]
},

"astigmatism": {
  "description": "Astigmatism causes blurred vision due to irregular cornea.",
  "causes": ["Corneal irregularity"],
  "remedies": ["Corrective lenses"]
},

"amblyopia": {
  "description": "Amblyopia is reduced vision in one eye.",
  "causes": ["Childhood eye misalignment"],
  "remedies": ["Eye patch therapy"]
},

"strabismus": {
  "description": "Strabismus is misalignment of eyes.",
  "causes": ["Muscle imbalance"],
  "remedies": ["Glasses", "Surgery"]
},

"otitis_externa": {
  "description": "Otitis externa is outer ear infection.",
  "causes": ["Water exposure"],
  "remedies": ["Antibiotic ear drops"]
},

"meniere_disease": {
  "description": "Meniere disease affects inner ear causing vertigo.",
  "causes": ["Fluid buildup"],
  "remedies": ["Low salt diet", "Medication"]
},

"tinnitus": {
  "description": "Tinnitus is ringing sound in ears.",
  "causes": ["Noise exposure"],
  "remedies": ["Sound therapy"]
},

"labyrinthitis": {
  "description": "Labyrinthitis is inner ear inflammation.",
  "causes": ["Viral infection"],
  "remedies": ["Medication", "Rest"]
},

"adenoiditis": {
  "description": "Adenoiditis is inflammation of adenoids.",
  "causes": ["Bacterial infection"],
  "remedies": ["Antibiotics"]
},

"nasal_polyps": {
  "description": "Nasal polyps are soft growths in nasal passages.",
  "causes": ["Chronic inflammation"],
  "remedies": ["Steroid sprays", "Surgery"]
},

"epistaxis": {
  "description": "Epistaxis is medical term for nosebleed.",
  "causes": ["Dry air", "Injury"],
  "remedies": ["Pinch nose", "Medical care if severe"]
},

"sleepwalking": {
  "description": "Sleepwalking is performing activities while asleep.",
  "causes": ["Sleep disorders"],
  "remedies": ["Safety measures", "Medical advice"]
},

"night_terrors": {
  "description": "Night terrors are episodes of screaming during sleep.",
  "causes": ["Stress", "Sleep deprivation"],
  "remedies": ["Stress management"]
},

"bruxism": {
  "description": "Bruxism is teeth grinding during sleep.",
  "causes": ["Stress"],
  "remedies": ["Mouth guard"]
},

"obsessive_compulsive_disorder": {
  "description": "OCD is mental health disorder with repetitive thoughts.",
  "causes": ["Brain chemistry imbalance"],
  "remedies": ["Therapy", "Medication"]
},

"bipolar_disorder": {
  "description": "Bipolar disorder causes mood swings.",
  "causes": ["Genetic factors"],
  "remedies": ["Mood stabilizers", "Therapy"]
},

"schizophrenia": {
  "description": "Schizophrenia is serious mental disorder affecting thinking.",
  "causes": ["Genetics", "Brain chemistry"],
  "remedies": ["Antipsychotic medication"]
},

"post_traumatic_stress_disorder": {
  "description": "PTSD develops after traumatic event.",
  "causes": ["Severe trauma"],
  "remedies": ["Therapy", "Medication"]
},

"anorexia_nervosa": {
  "description": "Anorexia is eating disorder causing weight loss.",
  "causes": ["Psychological factors"],
  "remedies": ["Therapy", "Nutritional support"]
},

"bulimia_nervosa": {
  "description": "Bulimia is eating disorder with binge and purge cycles.",
  "causes": ["Psychological stress"],
  "remedies": ["Therapy"]
},

"alcohol_use_disorder": {
  "description": "Alcohol use disorder is inability to control alcohol use.",
  "causes": ["Addiction"],
  "remedies": ["Rehabilitation", "Counseling"]
},

"drug_addiction": {
  "description": "Drug addiction is compulsive substance use.",
  "causes": ["Substance dependence"],
  "remedies": ["Rehabilitation", "Therapy"]
},

"g6pd_deficiency": {
  "description": "G6PD deficiency is genetic disorder affecting red blood cells.",
  "causes": ["Inherited mutation"],
  "remedies": ["Avoid trigger drugs"]
},

"sickle_cell_disease": {
  "description": "Sickle cell disease is inherited blood disorder.",
  "causes": ["Genetic mutation"],
  "remedies": ["Pain management", "Transfusions"]
},

"thalidomide_embryopathy": {
  "description": "Birth defects caused by thalidomide exposure.",
  "causes": ["Drug exposure during pregnancy"],
  "remedies": ["Supportive care"]
}
"trigeminal_neuralgia": {
  "description": "Trigeminal neuralgia is a chronic pain condition affecting the facial nerve.",
  "causes": ["Nerve compression", "Multiple sclerosis"],
  "remedies": ["Anticonvulsant medication", "Surgery"]
},

"guillain_barre_syndrome": {
  "description": "Guillain-Barré syndrome is an autoimmune disorder causing muscle weakness.",
  "causes": ["Immune response after infection"],
  "remedies": ["Immunotherapy", "Supportive care"]
},

"tourettes_syndrome": {
  "description": "Tourette syndrome is a neurological disorder causing repetitive movements or sounds.",
  "causes": ["Genetic factors"],
  "remedies": ["Behavior therapy", "Medication"]
},

"narcolepsy": {
  "description": "Narcolepsy is a sleep disorder causing excessive daytime sleepiness.",
  "causes": ["Brain chemical imbalance"],
  "remedies": ["Stimulant medication", "Scheduled naps"]
},

"restless_leg_syndrome": {
  "description": "Restless leg syndrome causes urge to move legs during rest.",
  "causes": ["Iron deficiency", "Nerve disorders"],
  "remedies": ["Iron supplements", "Medication"]
},

"cluster_headache": {
  "description": "Cluster headache causes severe one-sided head pain.",
  "causes": ["Unknown neurological factors"],
  "remedies": ["Oxygen therapy", "Medication"]
},

"tension_headache": {
  "description": "Tension headache is mild to moderate head pain.",
  "causes": ["Stress", "Muscle strain"],
  "remedies": ["Pain relievers", "Relaxation"]
},

"subarachnoid_hemorrhage": {
  "description": "Subarachnoid hemorrhage is bleeding in the space around the brain.",
  "causes": ["Ruptured aneurysm"],
  "remedies": ["Emergency surgery"]
},

"brain_tumor": {
  "description": "Brain tumor is abnormal growth of cells in the brain.",
  "causes": ["Genetic mutations"],
  "remedies": ["Surgery", "Radiation therapy"]
},

"concussion": {
  "description": "Concussion is a mild traumatic brain injury.",
  "causes": ["Head injury"],
  "remedies": ["Rest", "Medical monitoring"]
},

"heat_cramps": {
  "description": "Heat cramps are painful muscle spasms due to heat exposure.",
  "causes": ["Dehydration", "Electrolyte imbalance"],
  "remedies": ["Hydration", "Electrolyte drinks"]
},

"water_intoxication": {
  "description": "Water intoxication is overhydration leading to low sodium levels.",
  "causes": ["Excess water intake"],
  "remedies": ["Electrolyte correction", "Medical care"]
},

"carbon_monoxide_poisoning": {
  "description": "Carbon monoxide poisoning occurs from inhaling CO gas.",
  "causes": ["Faulty heaters", "Car exhaust"],
  "remedies": ["Oxygen therapy", "Emergency care"]
},

"lead_poisoning": {
  "description": "Lead poisoning results from lead accumulation in body.",
  "causes": ["Contaminated water", "Lead paint"],
  "remedies": ["Chelation therapy"]
},

"mercury_poisoning": {
  "description": "Mercury poisoning affects nervous system.",
  "causes": ["Contaminated seafood"],
  "remedies": ["Chelation therapy"]
},

"arsenic_poisoning": {
  "description": "Arsenic poisoning occurs from contaminated water or food.",
  "causes": ["Industrial exposure"],
  "remedies": ["Chelation therapy"]
},

"silicosis": {
  "description": "Silicosis is lung disease from silica dust inhalation.",
  "causes": ["Occupational exposure"],
  "remedies": ["Supportive care"]
},

"asbestosis": {
  "description": "Asbestosis is lung scarring from asbestos exposure.",
  "causes": ["Inhalation of asbestos fibers"],
  "remedies": ["Oxygen therapy"]
},

"black_lung_disease": {
  "description": "Black lung disease affects coal miners.",
  "causes": ["Coal dust inhalation"],
  "remedies": ["Supportive care"]
},

"mesothelioma": {
  "description": "Mesothelioma is cancer linked to asbestos exposure.",
  "causes": ["Asbestos exposure"],
  "remedies": ["Chemotherapy", "Surgery"]
},

"whooping_cough": {
  "description": "Whooping cough is a contagious bacterial respiratory infection.",
  "causes": ["Bordetella pertussis bacteria"],
  "remedies": ["Antibiotics", "Vaccination"]
},

"mononucleosis": {
  "description": "Mononucleosis is viral infection causing fatigue and sore throat.",
  "causes": ["Epstein-Barr virus"],
  "remedies": ["Rest", "Hydration"]
},

"hand_tremor": {
  "description": "Hand tremor is involuntary shaking of hands.",
  "causes": ["Neurological disorders", "Stress"],
  "remedies": ["Medication", "Therapy"]
},

"kyphosis": {
  "description": "Kyphosis is excessive curvature of upper spine.",
  "causes": ["Poor posture", "Osteoporosis"],
  "remedies": ["Physical therapy", "Bracing"]
},

"scoliosis": {
  "description": "Scoliosis is sideways curvature of spine.",
  "causes": ["Congenital factors"],
  "remedies": ["Bracing", "Surgery"]
},

"lordosis": {
  "description": "Lordosis is excessive inward spinal curvature.",
  "causes": ["Obesity", "Muscle imbalance"],
  "remedies": ["Exercise therapy"]
},

"frozen_shoulder": {
  "description": "Frozen shoulder causes stiffness and pain in shoulder joint.",
  "causes": ["Immobility", "Diabetes"],
  "remedies": ["Physiotherapy", "Pain relief"]
},

"rotator_cuff_injury": {
  "description": "Rotator cuff injury affects shoulder tendons.",
  "causes": ["Overuse", "Trauma"],
  "remedies": ["Rest", "Surgery if severe"]
},

"plantar_fasciitis": {
  "description": "Plantar fasciitis causes heel pain.",
  "causes": ["Overuse", "Flat feet"],
  "remedies": ["Stretching", "Orthotics"]
},

"bursitis": {
  "description": "Bursitis is inflammation of fluid-filled sacs near joints.",
  "causes": ["Repetitive motion"],
  "remedies": ["Rest", "Anti-inflammatory medication"]
},

"tendinitis": {
  "description": "Tendinitis is inflammation of a tendon.",
  "causes": ["Overuse injury"],
  "remedies": ["Rest", "Ice therapy"]
},

"shingles": {
  "description": "Shingles is viral infection causing painful rash.",
  "causes": ["Reactivation of varicella virus"],
  "remedies": ["Antiviral medication"]
},

"herpes_simplex": {
  "description": "Herpes simplex is viral infection causing sores.",
  "causes": ["HSV infection"],
  "remedies": ["Antiviral drugs"]
},

"genital_warts": {
  "description": "Genital warts are caused by HPV infection.",
  "causes": ["Human papillomavirus"],
  "remedies": ["Topical treatment", "Cryotherapy"]
},

"syphilis": {
  "description": "Syphilis is bacterial sexually transmitted infection.",
  "causes": ["Treponema pallidum"],
  "remedies": ["Antibiotics"]
},

"gonorrhea": {
  "description": "Gonorrhea is sexually transmitted bacterial infection.",
  "causes": ["Neisseria gonorrhoeae"],
  "remedies": ["Antibiotics"]
},

"chlamydia": {
  "description": "Chlamydia is common sexually transmitted infection.",
  "causes": ["Chlamydia trachomatis"],
  "remedies": ["Antibiotics"]
},

"hiv_aids": {
  "description": "HIV/AIDS is viral infection damaging immune system.",
  "causes": ["Human immunodeficiency virus"],
  "remedies": ["Antiretroviral therapy"]
},

"hepatitis_a": {
  "description": "Hepatitis A is viral liver infection.",
  "causes": ["Contaminated food or water"],
  "remedies": ["Rest", "Vaccination prevention"]
},

"hepatitis_b": {
  "description": "Hepatitis B is viral liver infection.",
  "causes": ["Blood or body fluids"],
  "remedies": ["Antiviral medication", "Vaccination prevention"]
},

"hepatitis_c": {
  "description": "Hepatitis C is viral infection causing liver inflammation.",
  "causes": ["Blood exposure"],
  "remedies": ["Antiviral medication"]
}
"sarcoidosis": {
  "description": "Sarcoidosis is an inflammatory disease that forms granulomas in organs.",
  "causes": ["Immune system overreaction", "Unknown triggers"],
  "remedies": ["Corticosteroids", "Immunosuppressants"]
},

"scleroderma": {
  "description": "Scleroderma is an autoimmune disease causing skin thickening.",
  "causes": ["Immune dysfunction"],
  "remedies": ["Immunotherapy", "Symptom management"]
},

"lupus": {
  "description": "Lupus is an autoimmune disease affecting multiple organs.",
  "causes": ["Genetics", "Environmental triggers"],
  "remedies": ["Immunosuppressants", "Anti-inflammatory drugs"]
},

"rheumatic_fever": {
  "description": "Rheumatic fever is an inflammatory disease following strep infection.",
  "causes": ["Untreated streptococcal infection"],
  "remedies": ["Antibiotics", "Anti-inflammatory medication"]
},

"ankylosing_spondylitis": {
  "description": "Ankylosing spondylitis is arthritis affecting the spine.",
  "causes": ["Genetic factors"],
  "remedies": ["Exercise", "Medication"]
},

"fibromyalgia": {
  "description": "Fibromyalgia causes widespread muscle pain and fatigue.",
  "causes": ["Unknown", "Stress triggers"],
  "remedies": ["Pain management", "Exercise"]
},

"chronic_fatigue_syndrome": {
  "description": "Chronic fatigue syndrome causes extreme fatigue.",
  "causes": ["Unknown", "Viral triggers"],
  "remedies": ["Energy management", "Therapy"]
},

"raynaud_disease": {
  "description": "Raynaud disease reduces blood flow to fingers and toes.",
  "causes": ["Cold exposure", "Stress"],
  "remedies": ["Keep warm", "Medication"]
},

"crohn_disease": {
  "description": "Crohn disease is inflammatory bowel disease.",
  "causes": ["Immune response", "Genetics"],
  "remedies": ["Medication", "Diet control"]
},

"ulcerative_colitis": {
  "description": "Ulcerative colitis causes inflammation in colon.",
  "causes": ["Autoimmune factors"],
  "remedies": ["Medication", "Surgery"]
},

"diverticulitis": {
  "description": "Diverticulitis is inflammation of colon pouches.",
  "causes": ["Infection"],
  "remedies": ["Antibiotics", "Diet changes"]
},

"barrett_esophagus": {
  "description": "Barrett esophagus is damage to esophageal lining from acid reflux.",
  "causes": ["Chronic GERD"],
  "remedies": ["Acid reducers", "Monitoring"]
},

"achalasia": {
  "description": "Achalasia is difficulty swallowing due to esophageal dysfunction.",
  "causes": ["Nerve damage"],
  "remedies": ["Surgery", "Medication"]
},

"hiatal_hernia": {
  "description": "Hiatal hernia occurs when stomach pushes into chest cavity.",
  "causes": ["Weak diaphragm"],
  "remedies": ["Medication", "Surgery"]
},

"inguinal_hernia": {
  "description": "Inguinal hernia is protrusion in groin area.",
  "causes": ["Muscle weakness"],
  "remedies": ["Surgical repair"]
},

"umbilical_hernia": {
  "description": "Umbilical hernia is swelling near navel.",
  "causes": ["Weak abdominal wall"],
  "remedies": ["Surgery if needed"]
},

"hydrocele": {
  "description": "Hydrocele is fluid buildup in scrotum.",
  "causes": ["Injury", "Infection"],
  "remedies": ["Surgery"]
},

"varicocele": {
  "description": "Varicocele is enlarged veins in scrotum.",
  "causes": ["Poor vein valves"],
  "remedies": ["Surgery"]
},

"interstitial_cystitis": {
  "description": "Interstitial cystitis causes chronic bladder pain.",
  "causes": ["Unknown"],
  "remedies": ["Medication", "Bladder training"]
},

"nephritis": {
  "description": "Nephritis is inflammation of kidneys.",
  "causes": ["Infection", "Autoimmune disease"],
  "remedies": ["Medication", "Diet control"]
},

"glomerulonephritis": {
  "description": "Glomerulonephritis damages kidney filtering units.",
  "causes": ["Infection", "Immune disorders"],
  "remedies": ["Medication", "Dialysis"]
},

"cystitis": {
  "description": "Cystitis is bladder inflammation.",
  "causes": ["Bacterial infection"],
  "remedies": ["Antibiotics", "Hydration"]
},

"urethritis": {
  "description": "Urethritis is inflammation of urethra.",
  "causes": ["Bacterial infection", "STIs"],
  "remedies": ["Antibiotics"]
},

"pelvic_inflammatory_disease": {
  "description": "PID is infection of female reproductive organs.",
  "causes": ["Sexually transmitted infections"],
  "remedies": ["Antibiotics"]
},

"uterine_fibroids": {
  "description": "Uterine fibroids are noncancerous growths in uterus.",
  "causes": ["Hormonal imbalance"],
  "remedies": ["Medication", "Surgery"]
},

"adenomyosis": {
  "description": "Adenomyosis is uterine lining growth into muscle wall.",
  "causes": ["Hormonal factors"],
  "remedies": ["Pain management", "Surgery"]
},

"preeclampsia": {
  "description": "Preeclampsia is high blood pressure during pregnancy.",
  "causes": ["Pregnancy complications"],
  "remedies": ["Monitoring", "Early delivery if severe"]
},

"gestational_diabetes": {
  "description": "Gestational diabetes occurs during pregnancy.",
  "causes": ["Hormonal changes"],
  "remedies": ["Diet control", "Insulin"]
},

"miscarriage": {
  "description": "Miscarriage is pregnancy loss before 20 weeks.",
  "causes": ["Chromosomal abnormalities"],
  "remedies": ["Medical care"]
},

"ectopic_pregnancy": {
  "description": "Ectopic pregnancy occurs outside uterus.",
  "causes": ["Blocked fallopian tube"],
  "remedies": ["Emergency treatment"]
},

"infertility": {
  "description": "Infertility is inability to conceive after one year.",
  "causes": ["Hormonal imbalance", "Low sperm count"],
  "remedies": ["Fertility treatment"]
},

"andropause": {
  "description": "Andropause is age-related testosterone decline in men.",
  "causes": ["Aging"],
  "remedies": ["Hormone therapy"]
},

"metabolic_syndrome": {
  "description": "Metabolic syndrome is cluster of conditions increasing heart risk.",
  "causes": ["Obesity", "Insulin resistance"],
  "remedies": ["Lifestyle changes"]
},

"hyperlipidemia": {
  "description": "Hyperlipidemia is high levels of fats in blood.",
  "causes": ["Poor diet", "Genetics"],
  "remedies": ["Diet control", "Medication"]
},

"hypoglycemia": {
  "description": "Hypoglycemia is low blood sugar.",
  "causes": ["Excess insulin", "Skipping meals"],
  "remedies": ["Glucose intake"]
},

"hypercalcemia": {
  "description": "Hypercalcemia is high calcium levels in blood.",
  "causes": ["Parathyroid disorders"],
  "remedies": ["Hydration", "Medication"]
},

"hypocalcemia": {
  "description": "Hypocalcemia is low calcium levels.",
  "causes": ["Vitamin D deficiency"],
  "remedies": ["Calcium supplements"]
},

"rickets": {
  "description": "Rickets is bone weakness in children.",
  "causes": ["Vitamin D deficiency"],
  "remedies": ["Vitamin D supplements"]
},

"scurvy": {
  "description": "Scurvy is vitamin C deficiency disease.",
  "causes": ["Poor diet"],
  "remedies": ["Vitamin C intake"]
},

"beriberi": {
  "description": "Beriberi is vitamin B1 deficiency disease.",
  "causes": ["Malnutrition"],
  "remedies": ["Thiamine supplements"]
},

"pellagra": {
  "description": "Pellagra is niacin deficiency disease.",
  "causes": ["Poor nutrition"],
  "remedies": ["Niacin supplements"]
},

"kwashiorkor": {
  "description": "Kwashiorkor is severe protein malnutrition.",
  "causes": ["Protein deficiency"],
  "remedies": ["Nutritional therapy"]
},

"marasmus": {
  "description": "Marasmus is severe calorie deficiency malnutrition.",
  "causes": ["Starvation"],
  "remedies": ["Gradual nutritional rehabilitation"]
}
"meningitis": {
  "description": "Meningitis is inflammation of the protective membranes covering the brain and spinal cord.",
  "causes": ["Bacterial infection", "Viral infection", "Fungal infection"],
  "remedies": ["Antibiotics if bacterial", "Hospital care", "Vaccination prevention"]
},

"encephalitis": {
  "description": "Encephalitis is inflammation of the brain tissue.",
  "causes": ["Viral infections", "Autoimmune response"],
  "remedies": ["Antiviral drugs", "Supportive hospital care"]
},

"multiple_sclerosis": {
  "description": "Multiple sclerosis is an autoimmune disease affecting the central nervous system.",
  "causes": ["Immune system attack on nerves", "Genetics"],
  "remedies": ["Disease-modifying therapy", "Physiotherapy"]
},

"parkinson_disease": {
  "description": "Parkinson disease is a progressive nervous system disorder affecting movement.",
  "causes": ["Loss of dopamine-producing neurons", "Genetics"],
  "remedies": ["Medications", "Physical therapy"]
},

"alzheimer_disease": {
  "description": "Alzheimer disease is a progressive brain disorder causing memory loss.",
  "causes": ["Age-related changes", "Genetics"],
  "remedies": ["Medications", "Cognitive therapy"]
},

"huntington_disease": {
  "description": "Huntington disease is an inherited disorder causing nerve cell breakdown.",
  "causes": ["Genetic mutation"],
  "remedies": ["Supportive therapy", "Medications"]
},

"amyotrophic_lateral_sclerosis": {
  "description": "ALS is a progressive disease affecting nerve cells controlling muscles.",
  "causes": ["Genetics", "Unknown factors"],
  "remedies": ["Supportive care", "Medications"]
},

"cerebral_palsy": {
  "description": "Cerebral palsy affects movement and posture due to brain damage.",
  "causes": ["Birth injury", "Premature birth"],
  "remedies": ["Physical therapy", "Assistive devices"]
},

"bell_palsy": {
  "description": "Bell palsy causes sudden weakness in facial muscles.",
  "causes": ["Viral infection"],
  "remedies": ["Steroids", "Eye care"]
},

"myasthenia_gravis": {
  "description": "Myasthenia gravis is an autoimmune disorder causing muscle weakness.",
  "causes": ["Immune system attack on nerve-muscle junction"],
  "remedies": ["Medications", "Thymus surgery"]
},

"lyme_disease": {
  "description": "Lyme disease is a bacterial infection transmitted by ticks.",
  "causes": ["Tick bite"],
  "remedies": ["Antibiotics"]
},

"zika": {
  "description": "Zika is a viral infection spread by mosquitoes.",
  "causes": ["Aedes mosquito bite"],
  "remedies": ["Rest", "Hydration"]
},

"yellow_fever": {
  "description": "Yellow fever is a viral hemorrhagic disease spread by mosquitoes.",
  "causes": ["Mosquito bite"],
  "remedies": ["Supportive care", "Vaccination"]
},

"ebola": {
  "description": "Ebola is a severe viral disease causing hemorrhagic fever.",
  "causes": ["Contact with infected bodily fluids"],
  "remedies": ["Supportive hospital care"]
},

"marburg_virus": {
  "description": "Marburg virus disease is a severe hemorrhagic fever.",
  "causes": ["Contact with infected fluids"],
  "remedies": ["Supportive care"]
},

"cholera": {
  "description": "Cholera is a bacterial infection causing severe diarrhea.",
  "causes": ["Contaminated water"],
  "remedies": ["ORS", "Antibiotics"]
},

"plague": {
  "description": "Plague is a serious bacterial infection spread by fleas.",
  "causes": ["Flea bites", "Contact with infected animals"],
  "remedies": ["Antibiotics"]
},

"leprosy": {
  "description": "Leprosy is a chronic bacterial infection affecting skin and nerves.",
  "causes": ["Mycobacterium leprae"],
  "remedies": ["Long-term antibiotics"]
},

"polio": {
  "description": "Polio is a viral disease that can cause paralysis.",
  "causes": ["Poliovirus"],
  "remedies": ["Supportive care", "Vaccination prevention"]
},

"smallpox": {
  "description": "Smallpox was a contagious viral disease eradicated globally.",
  "causes": ["Variola virus"],
  "remedies": ["Vaccination prevention"]
},

"bronchiolitis": {
  "description": "Bronchiolitis is inflammation of small airways in children.",
  "causes": ["Respiratory syncytial virus"],
  "remedies": ["Oxygen therapy", "Fluids"]
},

"emphysema": {
  "description": "Emphysema is a lung condition causing shortness of breath.",
  "causes": ["Smoking"],
  "remedies": ["Inhalers", "Quit smoking"]
},

"pulmonary_fibrosis": {
  "description": "Pulmonary fibrosis causes lung tissue scarring.",
  "causes": ["Environmental exposure", "Autoimmune diseases"],
  "remedies": ["Oxygen therapy", "Medication"]
},

"pleurisy": {
  "description": "Pleurisy is inflammation of lung lining causing chest pain.",
  "causes": ["Infection", "Autoimmune disease"],
  "remedies": ["Pain relief", "Treat underlying cause"]
},

"arrhythmia": {
  "description": "Arrhythmia is irregular heartbeat.",
  "causes": ["Heart disease", "Electrolyte imbalance"],
  "remedies": ["Medication", "Pacemaker"]
},

"angina": {
  "description": "Angina is chest pain due to reduced blood flow to heart.",
  "causes": ["Coronary artery disease"],
  "remedies": ["Medication", "Lifestyle changes"]
},

"heart_failure": {
  "description": "Heart failure occurs when heart cannot pump effectively.",
  "causes": ["High blood pressure", "Heart attack"],
  "remedies": ["Medication", "Diet control"]
},

"cardiomyopathy": {
  "description": "Cardiomyopathy affects heart muscle function.",
  "causes": ["Genetics", "Alcohol abuse"],
  "remedies": ["Medication", "Implantable devices"]
},

"atherosclerosis": {
  "description": "Atherosclerosis is narrowing of arteries due to plaque buildup.",
  "causes": ["High cholesterol", "Smoking"],
  "remedies": ["Healthy diet", "Medication"]
},

"deep_vein_thrombosis": {
  "description": "DVT is a blood clot in deep veins.",
  "causes": ["Prolonged immobility"],
  "remedies": ["Blood thinners"]
},

"varicose_veins": {
  "description": "Varicose veins are enlarged twisted veins.",
  "causes": ["Weak vein valves"],
  "remedies": ["Compression stockings"]
},

"thalassemia": {
  "description": "Thalassemia is inherited blood disorder affecting hemoglobin.",
  "causes": ["Genetic mutation"],
  "remedies": ["Blood transfusion"]
},

"hemophilia": {
  "description": "Hemophilia is a bleeding disorder due to clotting factor deficiency.",
  "causes": ["Genetic mutation"],
  "remedies": ["Clotting factor replacement"]
},

"leukemia": {
  "description": "Leukemia is cancer of blood-forming tissues.",
  "causes": ["Genetic mutations", "Radiation exposure"],
  "remedies": ["Chemotherapy", "Bone marrow transplant"]
},

"lymphoma": {
  "description": "Lymphoma is cancer of lymphatic system.",
  "causes": ["Immune dysfunction"],
  "remedies": ["Chemotherapy", "Radiation"]
},

"melanoma": {
  "description": "Melanoma is a serious skin cancer.",
  "causes": ["UV exposure"],
  "remedies": ["Surgery", "Immunotherapy"]
},

"breast_cancer": {
  "description": "Breast cancer is cancer that forms in breast cells.",
  "causes": ["Genetics", "Hormonal factors"],
  "remedies": ["Surgery", "Chemotherapy"]
},

"lung_cancer": {
  "description": "Lung cancer begins in lung tissues.",
  "causes": ["Smoking", "Air pollution"],
  "remedies": ["Surgery", "Radiation"]
},

"prostate_cancer": {
  "description": "Prostate cancer affects prostate gland.",
  "causes": ["Age", "Genetics"],
  "remedies": ["Surgery", "Hormone therapy"]
},

"ovarian_cancer": {
  "description": "Ovarian cancer affects ovaries.",
  "causes": ["Genetics"],
  "remedies": ["Surgery", "Chemotherapy"]
},

"colon_cancer": {
  "description": "Colon cancer begins in large intestine.",
  "causes": ["Diet", "Genetics"],
  "remedies": ["Surgery", "Chemotherapy"]
},

"stomach_cancer": {
  "description": "Stomach cancer develops in stomach lining.",
  "causes": ["H. pylori infection"],
  "remedies": ["Surgery", "Chemotherapy"]
},

"skin_cancer": {
  "description": "Skin cancer is abnormal growth of skin cells.",
  "causes": ["UV exposure"],
  "remedies": ["Surgery"]
}
"motion_sickness": {
  "description": "Motion sickness is nausea and dizziness triggered by movement during travel.",
  "causes": ["Travel by car/boat/air", "Inner ear sensitivity"],
  "remedies": ["Look at horizon", "Ginger", "Motion sickness tablets"]
},

"heatstroke": {
  "description": "Heatstroke is a severe heat-related illness with very high body temperature.",
  "causes": ["Prolonged heat exposure", "Dehydration"],
  "remedies": ["Cool the body", "Fluids", "Emergency medical care"]
},

"hypothermia": {
  "description": "Hypothermia occurs when body temperature drops dangerously low.",
  "causes": ["Cold exposure", "Wet clothing"],
  "remedies": ["Warm blankets", "Warm drinks", "Medical help"]
},

"sunburn": {
  "description": "Sunburn is skin damage caused by excessive UV exposure.",
  "causes": ["Prolonged sun exposure"],
  "remedies": ["Aloe vera", "Cool bath", "Hydration"]
},

"ringworm": {
  "description": "Ringworm is a fungal skin infection causing circular rash.",
  "causes": ["Fungal infection", "Contact with infected surfaces"],
  "remedies": ["Antifungal creams", "Keep area dry"]
},

"scabies": {
  "description": "Scabies is a skin infestation by mites causing itching.",
  "causes": ["Mite infestation", "Close contact"],
  "remedies": ["Medicated lotions", "Wash clothes in hot water"]
},

"lice_infestation": {
  "description": "Lice infestation affects scalp causing itching.",
  "causes": ["Head-to-head contact"],
  "remedies": ["Medicated shampoo", "Fine combing"]
},

"impetigo": {
  "description": "Impetigo is a contagious bacterial skin infection.",
  "causes": ["Bacteria", "Skin cuts"],
  "remedies": ["Antibiotic ointment", "Hygiene"]
},

"cellulitis": {
  "description": "Cellulitis is a bacterial skin infection causing redness and swelling.",
  "causes": ["Skin injury", "Bacteria"],
  "remedies": ["Antibiotics", "Rest"]
},

"abscess": {
  "description": "Abscess is a collection of pus due to infection.",
  "causes": ["Bacterial infection"],
  "remedies": ["Drainage", "Antibiotics"]
},

"boils": {
  "description": "Boils are painful pus-filled lumps under the skin.",
  "causes": ["Bacterial infection"],
  "remedies": ["Warm compress", "Medical drainage"]
},

"warts": {
  "description": "Warts are small skin growths caused by HPV virus.",
  "causes": ["HPV infection"],
  "remedies": ["Salicylic acid", "Cryotherapy"]
},

"corns": {
  "description": "Corns are thickened skin areas due to friction.",
  "causes": ["Tight footwear"],
  "remedies": ["Proper shoes", "Foot care"]
},

"calluses": {
  "description": "Calluses are hardened skin areas due to pressure.",
  "causes": ["Repeated friction"],
  "remedies": ["Moisturizers", "Reduce pressure"]
},

"frostbite": {
  "description": "Frostbite is skin and tissue injury from freezing.",
  "causes": ["Extreme cold"],
  "remedies": ["Warm gradually", "Medical care"]
},

"heat_rash": {
  "description": "Heat rash is skin irritation from blocked sweat ducts.",
  "causes": ["Hot humid weather"],
  "remedies": ["Cool skin", "Loose clothing"]
},

"dehydration": {
  "description": "Dehydration occurs when body loses more fluids than taken in.",
  "causes": ["Vomiting", "Heat", "Low water intake"],
  "remedies": ["ORS", "Water", "Electrolytes"]
},

"electrolyte_imbalance": {
  "description": "Electrolyte imbalance affects body functions due to mineral level changes.",
  "causes": ["Vomiting", "Kidney issues"],
  "remedies": ["Fluids", "Medical correction"]
},

"food_allergy": {
  "description": "Food allergy is immune reaction to certain foods.",
  "causes": ["Peanuts", "Milk", "Shellfish"],
  "remedies": ["Avoid allergen", "Antihistamines"]
},

"lactose_intolerance": {
  "description": "Lactose intolerance causes digestive issues after dairy intake.",
  "causes": ["Lactase deficiency"],
  "remedies": ["Lactose-free foods", "Enzyme supplements"]
},

"celiac_disease": {
  "description": "Celiac disease is an autoimmune reaction to gluten.",
  "causes": ["Genetic", "Gluten intake"],
  "remedies": ["Gluten-free diet"]
},

"gerd": {
  "description": "GERD is acid reflux causing heartburn.",
  "causes": ["Obesity", "Spicy food"],
  "remedies": ["Antacids", "Diet control"]
},

"hiccups": {
  "description": "Hiccups are involuntary diaphragm contractions.",
  "causes": ["Eating fast", "Carbonated drinks"],
  "remedies": ["Hold breath", "Sip water"]
},

"nosebleed": {
  "description": "Nosebleed is bleeding from nasal passages.",
  "causes": ["Dry air", "Injury"],
  "remedies": ["Pinch nose", "Lean forward"]
},

"earwax_blockage": {
  "description": "Earwax blockage occurs when wax accumulates in ear canal.",
  "causes": ["Excess wax"],
  "remedies": ["Ear drops", "Medical removal"]
},

"tooth_decay": {
  "description": "Tooth decay is damage to teeth due to bacteria.",
  "causes": ["Sugary foods", "Poor hygiene"],
  "remedies": ["Brushing", "Dental treatment"]
},

"gingivitis": {
  "description": "Gingivitis is gum inflammation.",
  "causes": ["Plaque buildup"],
  "remedies": ["Oral hygiene", "Dental cleaning"]
},

"periodontitis": {
  "description": "Periodontitis is severe gum infection.",
  "causes": ["Untreated gingivitis"],
  "remedies": ["Dental treatment"]
},

"tooth_sensitivity": {
  "description": "Tooth sensitivity causes pain to hot or cold.",
  "causes": ["Enamel erosion"],
  "remedies": ["Desensitizing toothpaste"]
},

"mouth_ulcer": {
  "description": "Mouth ulcers are painful sores in the mouth.",
  "causes": ["Stress", "Injury"],
  "remedies": ["Salt rinse", "Topical gels"]
},

"cold_sore": {
  "description": "Cold sores are blisters caused by herpes virus.",
  "causes": ["HSV infection"],
  "remedies": ["Antiviral creams"]
},

"hand_foot_mouth_disease": {
  "description": "Viral illness causing sores in mouth and rash.",
  "causes": ["Enterovirus"],
  "remedies": ["Rest", "Fluids"]
},

"pink_eye": {
  "description": "Pink eye is inflammation of conjunctiva.",
  "causes": ["Virus", "Bacteria"],
  "remedies": ["Eye drops", "Hygiene"]
},

"stye": {
  "description": "Stye is a painful eyelid lump.",
  "causes": ["Bacterial infection"],
  "remedies": ["Warm compress"]
},

"dry_eye": {
  "description": "Dry eye occurs when tears are insufficient.",
  "causes": ["Screen use", "Aging"],
  "remedies": ["Artificial tears"]
},

"color_blindness": {
  "description": "Color blindness affects color perception.",
  "causes": ["Genetics"],
  "remedies": ["Corrective lenses"]
},

"carpal_tunnel_syndrome": {
  "description": "Nerve compression in wrist causing pain.",
  "causes": ["Repetitive motion"],
  "remedies": ["Wrist splint", "Rest"]
},

"tennis_elbow": {
  "description": "Tennis elbow is tendon inflammation in elbow.",
  "causes": ["Overuse"],
  "remedies": ["Rest", "Ice"]
},

"sprain": {
  "description": "Sprain is ligament injury.",
  "causes": ["Twisting injury"],
  "remedies": ["Rest", "Ice", "Compression"]
},

"strain": {
  "description": "Strain is muscle or tendon injury.",
  "causes": ["Overstretching"],
  "remedies": ["Rest", "Pain relief"]
},

"fracture": {
  "description": "Fracture is a broken bone.",
  "causes": ["Trauma"],
  "remedies": ["Immobilization", "Medical care"]
},

"dislocation": {
  "description": "Dislocation is bone displacement from joint.",
  "causes": ["Injury"],
  "remedies": ["Medical reposition"]
},

"burn": {
  "description": "Burn is skin damage from heat or chemicals.",
  "causes": ["Fire", "Hot liquids"],
  "remedies": ["Cool water", "Burn cream"]
},

"electric_shock": {
  "description": "Electric shock injury from current exposure.",
  "causes": ["Electrical contact"],
  "remedies": ["Emergency care"]
},

"poisoning": {
  "description": "Poisoning occurs from harmful substance intake.",
  "causes": ["Chemicals", "Drugs"],
  "remedies": ["Medical help"]
},

"snake_bite": {
  "description": "Snake bite injects venom.",
  "causes": ["Venomous snake"],
  "remedies": ["Antivenom", "Hospital care"]
},

"insect_sting_allergy": {
  "description": "Allergic reaction to insect sting.",
  "causes": ["Bee/wasp sting"],
  "remedies": ["Antihistamines", "Epinephrine"]
},

"altitude_sickness": {
  "description": "Altitude sickness from low oxygen at high altitudes.",
  "causes": ["Rapid ascent"],
  "remedies": ["Descend", "Oxygen"]
},

"panic_attack": {
  "description": "Sudden intense fear with physical symptoms.",
  "causes": ["Stress", "Anxiety disorder"],
  "remedies": ["Breathing exercises", "Therapy"]
},

"adhd": {
  "description": "ADHD affects attention and impulse control.",
  "causes": ["Genetics", "Brain development"],
  "remedies": ["Behavior therapy", "Medication"]
},

"autism": {
  "description": "Autism is a developmental condition affecting communication.",
  "causes": ["Genetic factors"],
  "remedies": ["Therapy", "Support programs"]
},

"dyslexia": {
  "description": "Dyslexia affects reading ability.",
  "causes": ["Neurological factors"],
  "remedies": ["Special education"]
},

"stuttering": {
  "description": "Speech disorder with repetition of sounds.",
  "causes": ["Developmental factors"],
  "remedies": ["Speech therapy"]
}
"corns": {
"description": "Corns are thickened skin areas due to
friction.",
"causes": ["Tight footwear"], "remedies": ["Proper shoes", "Foot care"]},

"warts": {
"description": "Warts are small skin growths caused by HPV virus.",
"causes": ["HPV infection"],

"remedies": ["Salicylic acid", "Cryotherapy"]},
"boils": {
"description": "Boils are painful pus-filled lumps under the skin.",

"causes": ["Bacterial infection"],

"remedies": ["Warm compress", "Medical drainage"]},
"abscess": {

"description": "Abscess is a collection of pus due to  infection.",

},

"causes": ["Bacterial infection"],

"remedies": ["Drainage", "Antibiotics"]},
cellulitis": {

"description": "Cellulitis is a bacterial skin infection causing redness and swelling.",

"causes": ["Skin injury",

"remedies": ["Antibiotics", "Rest"]},
"sunburn": {

"description": "Sunburn is skin damage caused by excessive UV exposure.",

},
"impetigo": {

"description": "Impetigo is a contagious bacterial skin infection.",

"causes": ["Bacteria", "Skin cuts"],

"remedies": ["Antibiotic ointment", "Hygiene"]},
"lice_infestation": {

"description": "Lice infestation affects scalp causing itching.

"causes": ["Head-to-head contact"],

"remedies": ["Medicated shampoo", "Fine combing"]},
"scabies": {

"description": "Scabies is a skin infestation by mites causing itching.",

'causes": ["Mite infestation", "Close contact"], "remedies": ["Medicated lotions", "Wash clothes in

hot water]},
"ringworm": {

"description": "Ringworm is a fungal skin infection causing circular rash.",

"causes": ["Fungal infection", "Contact with infected surfaces"],

"remedies": ["Antifungal creams", "Keep area dry"]},
"scabies": {

"description": "Scabies is a skin infestation by mites causing itching.",

"causes": ["Mite infestation", "Close contact"],

"remedies": ["Medicated lotions", "Wash clothes in

hot water"]},

"causes": ["Prolonged sun exposure"],

"remedies": ["Aloe vera", "Cool bath", "Hydration"]},
hypothermia": {

"description": "Hypothermia occurs when body temperature drops dangerously low.",

"causes": ["Cold exposure", "Wet clothing"],

"remedies": ["Warm blankets", "Warm drinks", "Medical

help"]},
"heatstroke": {

"description": "Heatstroke is a severe heat-related illness with very high body temperature.",

"causes": ["Prolonged heat exposure", "Dehydration"],

"remedies": ["Cool the body", "Fluids", "Emergency medical care"]
    "motion_sickness": {
         "description": "Motion sickness is nausea and dizziness triggered by movement during travel.",
   "causes": ["Travel by car/boat/air", "Inner ear sensitivity"],
    "remedies": ["Look at horizon", "Ginger", "Motion sickness tablets"]},
    
    "vitiligo": {
        "description": "Vitiligo causes loss of skin pigmentation.",
        "causes": ["Autoimmune condition"],
        "remedies": ["Skin therapy", "Medical treatment"]
    },
    
    "psoriasis": {
        "description": "Psoriasis is a chronic skin disease causing red patches.",
        "causes": ["Immune disorder", "Genetics"],
        "remedies": ["Topical creams", "Medication"]
    },
    
    "epilepsy": {
        "description": "Epilepsy is a neurological disorder causing seizures.",
        "causes": ["Brain injury", "Genetics"],
        "remedies": ["Antiepileptic drugs", "Medical care"]
    },
    
    "sleep_apnea": {
        "description": "Sleep apnea causes breathing interruptions during sleep.",
        "causes": ["Obesity", "Airway blockage"],
        "remedies": ["CPAP therapy", "Weight loss"]
    },
    
    "allergic_rhinitis": {
        "description": "Allergic rhinitis causes sneezing and nasal congestion.",
        "causes": ["Dust", "Pollen"],
        "remedies": ["Antihistamines", "Avoid allergens"]
    },
    
    "influenza": {
        "description": "Influenza is a viral respiratory illness.",
        "causes": ["Influenza virus"],
        "remedies": ["Antivirals", "Rest", "Fluids"]
    },
    
    "rubella": {
        "description": "Rubella is a viral infection with rash and fever.",
        "causes": ["Rubella virus"],
        "remedies": ["Rest", "Vaccination"]
    },
    
    "mumps": {
        "description": "Mumps is a viral infection causing swollen salivary glands.",
        "causes": ["Mumps virus"],
        "remedies": ["Rest", "Pain relievers"]
    },
    
    "diphtheria": {
        "description": "Diphtheria affects the throat and airways.",
        "causes": ["Bacterial infection"],
        "remedies": ["Antibiotics", "Vaccination"]
    },
    
    "whooping_cough": {
        "description": "Whooping cough is a contagious respiratory disease.",
        "causes": ["Bacterial infection"],
        "remedies": ["Antibiotics", "Vaccination"]
    },
    
    "tetanus": {
        "description": "Tetanus causes muscle stiffness and spasms.",
        "causes": ["Bacterial infection through wounds"],
        "remedies": ["Vaccination", "Medical treatment"]
    },
    
    "rabies": {
        "description": "Rabies is a fatal viral disease affecting the nervous system.",
        "causes": ["Animal bites"],
        "remedies": ["Immediate vaccination", "Medical care"]
    },
    
    "chikungunya": {
        "description": "Chikungunya is a viral disease causing joint pain and fever.",
        "causes": ["Mosquito bite"],
        "remedies": ["Pain relievers", "Rest", "Hydration"]
    },
    
    "dengue": {
        "description": "Dengue is a mosquito-borne viral infection.",
        "causes": ["Aedes mosquito bite"],
        "remedies": ["Fluids", "Rest", "Medical monitoring"]
    },
    
    "prostatitis": {
        "description": "Prostatitis is inflammation of the prostate gland.",
        "causes": ["Bacterial infection"],
        "remedies": ["Antibiotics", "Pain relief"]
    },
    
    "erectile_dysfunction": {
        "description": "ED is difficulty achieving or maintaining an erection.",
        "causes": ["Stress", "Diabetes", "Heart disease"],
        "remedies": ["Lifestyle changes", "Medication"]
    },
    
    "endometriosis": {
        "description": "Endometriosis occurs when tissue grows outside the uterus.",
        "causes": ["Hormonal imbalance", "Genetics"],
        "remedies": ["Pain medication", "Hormone therapy"]
    },
    
    "polycystic_ovary_syndrome": {
        "description": "PCOS is a hormonal disorder affecting women.",
        "causes": ["Hormonal imbalance", "Genetics"],
        "remedies": ["Lifestyle changes", "Medication"]
    },
    
    "hyperthyroidism": {
        "description": "Hyperthyroidism is excess thyroid hormone production.",
        "causes": ["Graves' disease", "Thyroid nodules"],
        "remedies": ["Medication", "Radioactive iodine", "Surgery"]
    },
    
    "hypothyroidism": {
        "description": "Hypothyroidism is underactive thyroid hormone production.",
        "causes": ["Autoimmune disease", "Iodine deficiency"],
        "remedies": ["Thyroid medication", "Regular monitoring"]
    },
    
    "pancreatitis": {
        "description": "Pancreatitis is inflammation of the pancreas.",
        "causes": ["Alcohol abuse", "Gallstones"],
        "remedies": ["Hospital care", "Fluids", "Pain control"]
    },
    
    "gallstones": {
        "description": "Gallstones are hardened digestive fluid deposits in the gallbladder.",
        "causes": ["High cholesterol", "Obesity"],
        "remedies": ["Surgery", "Diet control"]
    },
    
    "fatty_liver": {
        "description": "Fatty liver is excess fat accumulation in the liver.",
        "causes": ["Obesity", "Alcohol consumption"],
        "remedies": ["Weight loss", "Healthy diet", "Avoid alcohol"]
    },
    
    "chronic_kidney_disease": {
        "description": "CKD is gradual loss of kidney function.",
        "causes": ["Diabetes", "High blood pressure"],
        "remedies": ["Diet control", "Medication", "Dialysis"]
    },
    
    "kidney_stones": {
        "description": "Kidney stones are hard mineral deposits (stones) in the kidneys.",
        "causes": ["Dehydration", "High mineral intake"],
        "remedies": ["Drink more water", "Pain medication", "Medical procedures"]
    },
    
    "hemorrhoids": {
        "description": "Hemorrhoids are swollen veins in the rectal area.",
        "causes": ["Straining", "Chronic constipation"],
        "remedies": ["High-fiber diet", "Creams", "Warm baths"]
    },
    
    "constipation": {
        "description": "Constipation is difficulty in passing stools.",
        "causes": ["Low fiber intake", "Dehydration"],
        "remedies": ["Fiber-rich diet", "Water intake", "Exercise"]
    },
    
    "irritable_bowel_syndrome": {
        "description": "IBS affects the large intestine causing cramps and bloating.",
        "causes": ["Stress", "Digestive sensitivity"],
        "remedies": ["Diet control", "Stress management", "Medication"]
    },
    
    "peptic_ulcer": {
        "description": "Peptic ulcer is an open sore in the stomach lining.",
        "causes": ["H. pylori infection", "Painkillers"],
        "remedies": ["Antacids", "Antibiotics", "Avoid spicy food"]
    },
    
    "sciatica": {
        "description": "Sciatica is pain along the sciatic nerve path.",
        "causes": ["Herniated disc", "Spinal issues"],
        "remedies": ["Physiotherapy", "Pain medication", "Exercise"]
    },
    
    "gout": {
        "description": "Gout is a form of arthritis causing sudden joint pain.",
        "causes": ["High uric acid levels", "Diet"],
        "remedies": ["Medication", "Low-purine diet", "Hydration"]
    },
    
    "osteoporosis": {
        "description": "Osteoporosis weakens bones making them fragile.",
        "causes": ["Calcium deficiency", "Aging", "Hormonal changes"],
        "remedies": ["Calcium supplements", "Exercise", "Medication"]
    },
    
    "cataract": {
        "description": "Cataract is clouding of the eye lens leading to vision loss.",
        "causes": ["Aging", "Diabetes", "UV exposure"],
        "remedies": ["Surgery", "Protective eyewear"]
    },
    
    "glaucoma": {
        "description": "Glaucoma damages the optic nerve due to high eye pressure.",
        "causes": ["Increased eye pressure", "Genetics"],
        "remedies": ["Eye drops", "Surgery", "Regular eye check-ups"]
    },
    
    "otitis_media": {
        "description": "Otitis media is a middle ear infection.",
        "causes": ["Bacterial infection", "Viral infection"],
        "remedies": ["Antibiotics", "Pain relievers", "Warm compress"]
    },
    
    "laryngitis": {
        "description": "Laryngitis is inflammation of the voice box causing hoarseness.",
        "causes": ["Voice overuse", "Infection"],
        "remedies": ["Voice rest", "Steam inhalation", "Fluids"]
    },
    
    "pharyngitis": {
        "description": "Pharyngitis is inflammation of the throat.",
        "causes": ["Viral infection", "Bacteria"],
        "remedies": ["Saltwater gargle", "Hydration", "Pain relievers"]
    },
    
    "tonsillitis": {
        "description": "Tonsillitis is inflammation of the tonsils causing sore throat.",
        "causes": ["Viral infection", "Bacterial infection"],
        "remedies": ["Warm fluids", "Antibiotics if bacterial", "Rest"]
    },
    
    "vertigo": {
        "description": "Vertigo is a sensation of spinning or dizziness.",
        "causes": ["Inner ear problems", "Head injury"],
        "remedies": ["Balance exercises", "Medication", "Rest"]
    },
    
    "insomnia": {
        "description": "Insomnia is difficulty falling or staying asleep.",
        "causes": ["Stress", "Poor sleep habits", "Medical conditions"],
        "remedies": ["Maintain sleep schedule", "Relaxation", "Avoid caffeine"]
    },
    
    "depression": {
        "description": "Depression is a mood disorder causing persistent sadness and loss of interest.",
        "causes": ["Stress", "Trauma", "Chemical imbalance"],
        "remedies": ["Counseling", "Medication", "Lifestyle changes"]
    },
    
    "anxiety": {
        "description": "Anxiety is a mental health condition characterized by excessive worry or fear.",
        "causes": ["Stress", "Genetics", "Brain chemistry imbalance"],
        "remedies": ["Therapy", "Relaxation techniques", "Medication"]
    },
    
    "alopecia": {
        "description": "Alopecia is a condition that causes hair loss from the scalp or body.",
        "causes": ["Genetics", "Autoimmune disorder", "Stress"],
        "remedies": ["Medicated treatments", "Healthy diet", "Medical consultation"]
    },
    
    "bronchitis": {
        "description": "Bronchitis is inflammation of the bronchial tubes causing cough and mucus.",
        "causes": ["Viral infections", "Smoking", "Polluted air"],
        "remedies": ["Cough suppressants", "Warm fluids", "Avoid smoking"]
    },
    
    "hepatitis": {
        "description": "Hepatitis is inflammation of the liver caused by viral infections or toxins.",
        "causes": ["Hepatitis A, B, C viruses", "Alcohol", "Contaminated food/water"],
        "remedies": ["Antiviral medications", "Rest", "Avoid alcohol"]
    },
    
    "conjunctivitis": {
        "description": "Conjunctivitis is inflammation of the eye's outer membrane, causing redness and irritation.",
        "causes": ["Virus", "Bacteria", "Allergens"],
        "remedies": ["Eye drops", "Cold compress", "Maintain eye hygiene"]
    },
    
    "gastritis": {
        "description": "Gastritis is inflammation of the stomach lining.",
        "causes": ["Spicy food", "Alcohol", "H. pylori infection"],
        "remedies": ["Antacids", "Avoid spicy food", "Medications for H. pylori"]
    },
    
    "obesity": {
        "description": "Obesity is a condition involving excessive body fat.",
        "causes": ["Overeating", "Lack of exercise", "Genetics"],
        "remedies": ["Healthy diet", "Regular physical activity", "Lifestyle changes"]
    },
    
    "eczema": {
        "description": "Eczema is a skin condition causing dryness, itching, and inflammation.",
        "causes": ["Allergic reaction", "Genetics", "Stress"],
        "remedies": ["Moisturizers", "Steroid creams", "Avoid triggers"]
    },
    
    "covid19": {
        "description": "COVID-19 is a contagious respiratory disease caused by SARS-CoV-2.",
        "causes": ["Coronavirus infection", "Close exposure to infected individuals"],
        "remedies": ["Rest", "Isolation", "Antiviral drugs", "Hydration"]
    },
    
    "stroke": {
        "description": "Stroke occurs when blood supply to the brain is reduced or blocked.",
        "causes": ["Blood clot", "Burst blood vessel", "High blood pressure"],
        "remedies": ["Immediate medical care", "Rehabilitation", "Medications"]
    },
    
    "food_poisoning": {
        "description": "Food poisoning occurs due to consuming contaminated food.",
        "causes": ["Bacteria", "Viruses", "Toxins in food"],
        "remedies": ["ORS", "Rest", "Avoid heavy meals", "Medical care if severe"]
    },
    
    "appendicitis": {
        "description": "Appendicitis is inflammation of the appendix causing severe abdominal pain.",
        "causes": ["Blockage of the appendix", "Infection"],
        "remedies": ["Surgery", "Pain relief", "Antibiotics"]
    },
    
    "urinary_tract_infection": {
        "description": "UTI is an infection in the urinary system causing pain and frequent urination.",
        "causes": ["Bacterial infection", "Poor hygiene"],
        "remedies": ["Antibiotics", "Drink plenty of water", "Maintain hygiene"]
    },
    
    "pneumonia": {
        "description": "Pneumonia is an infection that inflames the lungs' air sacs.",
        "causes": ["Bacteria", "Viruses", "Fungi"],
        "remedies": ["Antibiotics", "Rest", "Fluids", "Hospitalization in severe cases"]
    },
    
    "jaundice": {
        "description": "Jaundice is yellowing of the skin and eyes due to high bilirubin levels.",
        "causes": ["Liver infection", "Hepatitis", "Alcoholic liver disease"],
        "remedies": ["Treat underlying liver issue", "Hydration", "Healthy diet"]
    },
    
    "sinusitis": {
        "description": "Sinusitis is inflammation of the sinuses causing congestion and facial pain.",
        "causes": ["Viral infections", "Allergies", "Nasal polyps"],
        "remedies": ["Steam inhalation", "Nasal sprays", "Hydration"]
    },
    
    "migraine": {
        "description": "Migraine is a neurological condition with severe headache and sensitivity to light.",
        "causes": ["Stress", "Hormonal changes", "Sleep disturbances"],
        "remedies": ["Migraine medication", "Rest in dark room", "Cold compress"]
    },
    
    "arthritis": {
        "description": "Arthritis is inflammation of the joints causing pain and stiffness.",
        "causes": ["Aging", "Autoimmune disorders", "Injury"],
        "remedies": ["Pain relievers", "Physiotherapy", "Regular exercise"]
    },
    
    "anemia": {
        "description": "Anemia is a condition where the body lacks enough healthy red blood cells.",
        "causes": ["Iron deficiency", "Vitamin B12 deficiency", "Chronic diseases"],
        "remedies": ["Iron supplements", "Eat leafy greens", "Vitamin B12 injections"]
    },
    
    "tuberculosis": {
        "description": "Tuberculosis is a bacterial infection that primarily affects the lungs.",
        "causes": ["Mycobacterium tuberculosis", "Airborne transmission"],
        "remedies": ["Long-term antibiotics", "Good nutrition", "Regular doctor check-ups"]
    },
    
    "measles": {
        "description": "Measles is a highly contagious viral infection that causes fever, rash, and cough.",
        "causes": ["Measles virus", "Exposure to infected droplets"],
        "remedies": ["Vitamin A supplements", "Hydration", "Fever reducers"]
    },
    
    "chickenpox": {
        "description": "Chickenpox is a viral infection causing an itchy rash with small, fluid-filled blisters.",
        "causes": ["Varicella-zoster virus", "Close contact with infected person"],
        "remedies": ["Calamine lotion", "Oatmeal bath", "Rest", "Antiviral medicine in severe cases"]
    },
    
    "skin_allergy": {
        "description": "Skin allergy is a reaction causing itching, redness, or swelling of the skin.",
        "causes": ["Dust", "Detergents", "Food allergens", "Insect bites"],
        "remedies": ["Use antihistamines", "Apply soothing creams", "Avoid allergens", "Keep skin clean"]
    },
    
    "diabetes": {
        "description": "Diabetes is a chronic condition where the body cannot regulate blood sugar properly.",
        "causes": ["Genetics", "Obesity", "Poor lifestyle habits", "Insulin resistance"],
        "remedies": ["Healthy diet", "Regular exercise", "Medications or insulin", "Monitor blood sugar"]
    },
    
    "hypertension": {
        "description": "Hypertension is a condition where blood pressure is persistently higher than normal.",
        "causes": ["Stress", "Obesity", "High salt intake", "Genetics"],
        "remedies": ["Reduce salt intake", "Exercise regularly", "Take prescribed medication", "Manage stress"]
    },
    
    "fever": {
        "description": "Fever is a temporary increase in body temperature, often due to illness.",
        "causes": ["Infection (viral or bacterial)", "Heat exhaustion", "Certain medications"],
        "remedies": ["Rest and drink fluids", "Take fever reducers like acetaminophen", "Cool compress", "Monitor temperature"]
    },
    
    "typhoid": {
        "description": "Typhoid is a bacterial infection that spreads through contaminated food and water.",
        "causes": ["Salmonella typhi bacteria", "Contaminated food", "Contaminated water"],
        "remedies": ["Antibiotics", "Drink clean water", "Proper hygiene", "Rest and fluids"]
    },
    
    "malaria": {
        "description": "Malaria is a mosquito-borne infectious disease caused by Plasmodium parasites.",
        "causes": ["Bite of infected Anopheles mosquito", "Travel to malaria-prone areas"],
        "remedies": ["Antimalarial medications", "Use mosquito nets", "Stay hydrated", "Seek medical care"]
    },
    
    "asthma": {
        "description": "Asthma is a chronic condition where airways become inflamed and narrow, causing breathing difficulty.",
        "causes": ["Allergens", "Air pollution", "Exercise", "Respiratory infections"],
        "remedies": ["Use inhalers", "Avoid triggers", "Breathing exercises", "Take prescribed medications"]
    },
    
    "diarrhea": {
        "description": "Diarrhea is frequent loose or watery bowel movements.",
        "causes": ["Food poisoning", "Viral or bacterial infection", "Food intolerance", "Medications"],
        "remedies": ["Drink ORS", "Avoid spicy foods", "Eat bananas, rice, toast", "Consult a doctor if severe"]
    },
    
    "cough": {
        "description": "A cough is a reflex action to clear your airways.",
        "causes": ["Common cold", "Flu", "Allergies", "Asthma", "COVID-19"],
        "remedies": ["Stay hydrated", "Use cough drops", "Try honey (for adults)", "Use a humidifier"]
    }
}

# Common greetings and responses
greetings = ["hello", "hi", "hey", "greetings"]
farewells = ["bye", "goodbye", "see you", "exit"]
thanks = ["thanks", "thank you", "appreciate it"]

def get_response(user_input):
    user_input = user_input.lower()
    
    # Check for greetings
    if any(word in user_input for word in greetings):
        return random.choice([
            "Hello! I'm MediBot. How can I help you today?",
            "Hi there! What health concerns do you have?",
            "Greetings! I'm here to provide general health information."
        ])
    
    # Check for farewells
    if any(word in user_input for word in farewells):
        return random.choice([
            "Take care and stay healthy!",
            "Goodbye! Remember to consult a doctor for serious symptoms.",
            "See you later! Wishing you good health."
        ])
    
    # Check for thanks
    if any(word in user_input for word in thanks):
        return random.choice([
            "You're welcome!",
            "Happy to help!",
            "No problem! Stay healthy."
        ])
    
    # Check for symptoms in the database
    for symptom, info in medical_db.items():
        if symptom in user_input:
            response = f"About {symptom}:\n"
            response += f"Description: {info['description']}\n"
            response += f"Possible causes: {', '.join(info['causes'])}\n"
            response += f"Suggested remedies: {', '.join(info['remedies'])}\n"
            response += "Note: If symptoms persist or worsen, please consult a doctor."
            return response
    
    # Default response if no matches found
    return "I'm sorry, I can only provide information about common symptoms like headache, fever, and cough. For other concerns, please consult a healthcare professional."


def main():
    print("MediBot: Hello! I'm a simple medical chatbot. I can provide general information about common symptoms.")
    print("Type 'bye' to exit at any time\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in farewells:
            print("MediBot:", get_response(user_input))
            break
        response = get_response(user_input)
        print("MediBot:", response)
        print()

if __name__ == "__main__":
    main()
