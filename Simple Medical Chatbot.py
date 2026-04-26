import random

medical_db = {
    "headache": {
        "description": "A headache is pain in the head or face.",
        "causes": ["Stress", "Tension", "Migraine", "Dehydration", "Eye strain"],
        "remedies": ["Rest in a quiet room", "Apply cold compress", "Take OTC pain relievers", "Stay hydrated"]
   },
"progeria": {
  "type": "Genetic (Rare)",
  "description": "Progeria is an extremely rare genetic disorder that causes rapid aging in children.",
  "causes": ["Mutation in LMNA gene"],
  "remedies": ["No cure available", "Supportive care", "Medications to manage symptoms"]
},
"fatal_familial_insomnia": {
  "type": "Genetic (Rare)",
  "description": "Fatal familial insomnia is an extremely rare inherited brain disorder that causes progressively worsening insomnia leading to severe neurological decline.",
  "causes": ["Mutation in PRNP gene affecting prion proteins"],
  "remedies": ["No cure available", "Supportive care", "Symptom management"]
},
"fibrodysplasia_ossificans_progressiva": {
  "type": "Genetic (Rare)",
  "description": "Fibrodysplasia ossificans progressiva (FOP) is an extremely rare disorder where soft tissues like muscles and ligaments gradually turn into bone.",
  "causes": ["Mutation in ACVR1 gene"],
  "remedies": ["No cure available", "Symptom management", "Avoid injury to prevent progression"]
},
"zoster_fever": {
  "description": "Zoster fever is a mild fever associated with shingles infection.",
  "causes": ["Varicella-zoster virus reactivation"],
  "remedies": ["Rest", "Fluids", "Antiviral medication"]
},
"zinc_deficiency_skin": {
  "description": "Zinc deficiency skin condition causes dryness, rashes, and delayed wound healing.",
  "causes": ["Low zinc intake", "Malabsorption"],
  "remedies": ["Zinc supplements", "Balanced diet"]
},
"zoster_eye_infection": {
  "description": "Zoster eye infection is an eye condition caused by varicella-zoster virus affecting ocular tissues.",
  "causes": ["Varicella-zoster virus reactivation"],
  "remedies": ["Antiviral medication", "Eye care"]
},
"zoster_rash": {
  "description": "Zoster rash is a painful skin rash caused by reactivation of the varicella-zoster virus.",
  "causes": ["Varicella-zoster virus reactivation"],
  "remedies": ["Antiviral medications", "Pain relief"]
},
"zinc_deficiency_anemia": {
  "description": "Zinc deficiency anemia is a condition where low zinc levels contribute to reduced red blood cell production.",
  "causes": ["Low dietary zinc", "Malabsorption"],
  "remedies": ["Zinc supplements", "Improved diet"]
},
"zollinger_ellison": {
  "description": "Zollinger-Ellison is a condition where tumors cause excess stomach acid.",
  "causes": ["Gastrin-secreting tumors"],
  "remedies": ["Proton pump inhibitors", "Surgery"]
},
"zinc_deficiency": {
  "description": "Zinc deficiency is a condition where the body lacks enough zinc for normal function.",
  "causes": ["Poor diet", "Malabsorption"],
  "remedies": ["Zinc supplements", "Balanced diet"]
},
"zika_fever": {
  "description": "Zika fever is a mild viral illness transmitted by mosquitoes.",
  "causes": ["Zika virus infection", "Mosquito bites"],
  "remedies": ["Rest", "Fluids", "Pain relief"]
},
"zoster_neuralgia": {
  "description": "Zoster neuralgia is persistent nerve pain following a shingles infection.",
  "causes": ["Nerve damage from varicella-zoster virus"],
  "remedies": ["Pain medications", "Antiviral therapy"]
},
"zinc_overdose": {
  "description": "Zinc overdose is a condition caused by excessive intake of zinc, leading to digestive and systemic symptoms.",
  "causes": ["Excessive zinc supplements", "Accidental ingestion"],
  "remedies": ["Stop zinc intake", "Supportive care"]
},
"zoster": {
  "description": "Zoster is a viral infection causing a painful rash, also known as shingles.",
  "causes": ["Reactivation of varicella-zoster virus"],
  "remedies": ["Antiviral medications", "Pain relief"]
},
"zollinger_syndrome": {
  "description": "Zollinger syndrome is a condition causing excessive stomach acid leading to ulcers.",
  "causes": ["Gastrin-secreting tumors"],
  "remedies": ["Proton pump inhibitors", "Surgery"]
},
"zoster_peripheral_neuropathy": {
  "description": "Zoster peripheral neuropathy is nerve damage caused by reactivation of the varicella-zoster virus, leading to persistent pain and sensory disturbances even after the rash resolves.",
  "symptoms": [
    "Burning or stabbing pain",
    "Numbness or tingling",
    "Increased sensitivity to touch",
    "Muscle weakness",
    "Persistent nerve pain (postherpetic neuralgia)"
  ],
  "causes": [
    "Reactivation of varicella-zoster virus",
    "Damage to peripheral nerves during infection"
  ],
  "risk_factors": [
    "Older age",
    "Weakened immune system",
    "Severe shingles episode"
  ],
  "diagnosis": [
    "Clinical neurological examination",
    "History of shingles infection",
    "Nerve conduction studies"
  ],
  "remedies": [
    "Antiviral medications (early stage)",
    "Pain management (e.g., gabapentin, pregabalin)",
    "Physical therapy"
  ],
  "prevention": [
    "Shingles vaccination",
    "Early antiviral treatment of shingles",
    "Managing immune health"
  ]
},
"zoster_ganglionitis": {
  "description": "Zoster ganglionitis is an inflammation of nerve ganglia caused by reactivation of the varicella-zoster virus, leading to localized nerve pain and possible skin manifestations.",
  "symptoms": [
    "Localized burning or sharp nerve pain",
    "Tingling or numbness",
    "Sensitivity to touch",
    "Possible rash in affected area",
    "Fatigue"
  ],
  "causes": [
    "Reactivation of varicella-zoster virus",
    "Infection of sensory nerve ganglia"
  ],
  "risk_factors": [
    "Older age",
    "Weakened immune system",
    "History of chickenpox"
  ],
  "diagnosis": [
    "Clinical examination",
    "PCR testing for varicella-zoster virus",
    "Neurological assessment"
  ],
  "remedies": [
    "Antiviral medications",
    "Pain management therapy",
    "Rest and supportive care"
  ],
  "prevention": [
    "Shingles vaccination",
    "Early treatment of shingles"
  ]
},
"zygomycosis_cutaneous": {
  "description": "Cutaneous zygomycosis is a fungal infection of the skin caused by Mucorales species, often entering through wounds and potentially spreading rapidly.",
  "symptoms": [
    "Red or swollen skin area",
    "Pain at infection site",
    "Blisters or ulcers",
    "Blackened or necrotic tissue",
    "Fever in severe cases"
  ],
  "causes": [
    "Fungal spores entering through cuts or wounds",
    "Contaminated soil or organic matter exposure",
    "Weakened immune system"
  ],
  "risk_factors": [
    "Open wounds or burns",
    "Uncontrolled diabetes",
    "Immunocompromised conditions",
    "Traumatic injuries"
  ],
  "diagnosis": [
    "Skin biopsy",
    "Fungal culture",
    "Microscopic examination"
  ],
  "remedies": [
    "Prompt antifungal therapy (e.g., amphotericin B)",
    "Surgical removal of infected tissue",
    "Management of underlying conditions"
  ],
  "prevention": [
    "Proper wound care",
    "Avoid exposure of open wounds to contaminated environments",
    "Control of diabetes and immune conditions"
  ]
},
"zika_congenital_microcephaly": {
  "description": "Zika congenital microcephaly is a severe birth defect in which babies are born with abnormally small heads and brain development issues due to Zika virus infection during pregnancy.",
  "symptoms": [
    "Abnormally small head size",
    "Developmental delays",
    "Seizures",
    "Feeding difficulties",
    "Vision and hearing problems"
  ],
  "causes": [
    "Zika virus infection during pregnancy",
    "Transmission from mother to fetus"
  ],
  "risk_factors": [
    "Pregnancy in Zika-endemic regions",
    "Exposure to infected mosquitoes",
    "Lack of protective measures against mosquito bites"
  ],
  "diagnosis": [
    "Prenatal ultrasound",
    "PCR testing for Zika virus",
    "Physical examination after birth"
  ],
  "remedies": [
    "Supportive medical care",
    "Physical and developmental therapy",
    "Management of complications"
  ],
  "prevention": [
    "Avoid mosquito bites during pregnancy",
    "Use repellents and protective clothing",
    "Avoid travel to high-risk areas during outbreaks"
  ]
},
"zinc_deficiency_immunodeficiency": {
  "description": "Zinc deficiency immunodeficiency is a condition where low zinc levels impair immune system function, increasing susceptibility to infections.",
  "symptoms": [
    "Frequent infections",
    "Delayed wound healing",
    "Fatigue",
    "Hair loss",
    "Skin rashes"
  ],
  "causes": [
    "Inadequate dietary zinc intake",
    "Malabsorption disorders",
    "Chronic illnesses",
    "Excessive loss of zinc"
  ],
  "risk_factors": [
    "Malnutrition",
    "Chronic gastrointestinal diseases",
    "Elderly individuals",
    "Alcohol dependence"
  ],
  "diagnosis": [
    "Blood zinc level test",
    "Immune function tests",
    "Clinical evaluation"
  ],
  "remedies": [
    "Zinc supplementation",
    "Balanced diet rich in zinc",
    "Treatment of underlying conditions"
  ],
  "prevention": [
    "Maintain adequate zinc intake",
    "Regular health check-ups",
    "Early treatment of deficiency symptoms"
  ]
},
"zenker_related_esophageal_cancer": {
  "description": "Zenker-related esophageal cancer is a rare malignancy that can develop in the upper esophagus, often associated with long-standing Zenker diverticulum and chronic irritation.",
  "symptoms": [
    "Progressive difficulty swallowing (dysphagia)",
    "Unintentional weight loss",
    "Persistent cough",
    "Hoarseness",
    "Regurgitation of food",
    "Neck discomfort"
  ],
  "causes": [
    "Chronic irritation from retained food in Zenker diverticulum",
    "Long-standing inflammation of esophageal lining",
    "Cellular mutations leading to cancer"
  ],
  "risk_factors": [
    "Untreated Zenker diverticulum",
    "Older age",
    "Chronic esophageal irritation",
    "Smoking and alcohol use"
  ],
  "diagnosis": [
    "Endoscopy with biopsy",
    "Barium swallow study",
    "CT scan or MRI for staging"
  ],
  "remedies": [
    "Surgical removal of tumor",
    "Radiation therapy",
    "Chemotherapy depending on stage",
    "Nutritional support"
  ],
  "prevention": [
    "Early treatment of Zenker diverticulum",
    "Avoid smoking and excessive alcohol",
    "Regular screening for persistent swallowing issues"
  ]
},
"zollinger_ellison_related_diarrhea": {
  "description": "Zollinger-Ellison related diarrhea is a condition where excessive stomach acid from gastrin-secreting tumors leads to chronic diarrhea and digestive disturbances.",
  "symptoms": [
    "Chronic watery diarrhea",
    "Abdominal pain",
    "Bloating",
    "Weight loss",
    "Frequent ulcers"
  ],
  "causes": [
    "Excess gastrin production from gastrinomas",
    "High stomach acid interfering with digestion",
    "Association with Zollinger-Ellison syndrome"
  ],
  "risk_factors": [
    "Presence of gastrin-secreting tumors",
    "MEN1 genetic syndrome",
    "Chronic acid-related disorders"
  ],
  "diagnosis": [
    "Blood gastrin level test",
    "Stool analysis",
    "Endoscopy",
    "Imaging (CT/MRI)"
  ],
  "remedies": [
    "Proton pump inhibitors",
    "Antidiarrheal medications",
    "Surgical removal of tumors",
    "Nutritional support"
  ],
  "prevention": [
    "Early diagnosis of gastrinomas",
    "Regular monitoring in high-risk individuals",
    "Proper management of acid-related conditions"
  ]
},
"zinc_deficiency_hypogeusia": {
  "description": "Zinc deficiency hypogeusia is a condition where reduced zinc levels lead to a decreased sense of taste.",
  "symptoms": [
    "Reduced ability to taste",
    "Altered taste perception",
    "Loss of appetite",
    "Weight loss",
    "Nutritional deficiencies"
  ],
  "causes": [
    "Low dietary zinc intake",
    "Malabsorption disorders",
    "Chronic illnesses",
    "Excessive zinc loss from the body"
  ],
  "risk_factors": [
    "Poor nutrition",
    "Gastrointestinal disorders",
    "Elderly individuals",
    "Chronic disease conditions"
  ],
  "diagnosis": [
    "Blood zinc level test",
    "Taste function tests",
    "Dietary assessment"
  ],
  "remedies": [
    "Zinc supplementation",
    "Improved dietary intake",
    "Treatment of underlying conditions"
  ],
  "prevention": [
    "Balanced diet with adequate zinc",
    "Regular nutritional monitoring",
    "Early treatment of deficiency symptoms"
  ]
},
"zoster_keratitis": {
  "description": "Zoster keratitis is an eye condition caused by reactivation of the varicella-zoster virus, leading to inflammation of the cornea.",
  "symptoms": [
    "Eye pain",
    "Redness in the eye",
    "Blurred vision",
    "Sensitivity to light",
    "Excess tearing"
  ],
  "causes": [
    "Reactivation of varicella-zoster virus",
    "Spread of infection to the cornea"
  ],
  "risk_factors": [
    "Older age",
    "Weakened immune system",
    "History of shingles"
  ],
  "diagnosis": [
    "Eye examination with slit lamp",
    "Fluorescein staining",
    "PCR testing for varicella-zoster virus"
  ],
  "remedies": [
    "Antiviral eye drops or oral antivirals",
    "Pain management",
    "Lubricating eye drops"
  ],
  "prevention": [
    "Shingles vaccination",
    "Early treatment of shingles"
  ]
},
"zinc_deficiency_growth_retardation": {
  "description": "Zinc deficiency growth retardation is a condition where inadequate zinc levels impair normal growth and development, especially in children.",
  "symptoms": [
    "Stunted growth",
    "Delayed puberty",
    "Frequent infections",
    "Poor appetite",
    "Delayed wound healing"
  ],
  "causes": [
    "Insufficient dietary zinc intake",
    "Malabsorption disorders",
    "Chronic illnesses"
  ],
  "risk_factors": [
    "Malnutrition",
    "Poverty or limited food access",
    "Digestive disorders",
    "Children in developing regions"
  ],
  "diagnosis": [
    "Blood zinc level test",
    "Growth assessment",
    "Dietary evaluation"
  ],
  "remedies": [
    "Zinc supplementation",
    "Balanced diet rich in zinc",
    "Treatment of underlying conditions"
  ],
  "prevention": [
    "Ensure adequate nutrition",
    "Regular growth monitoring in children",
    "Nutritional supplementation when needed"
  ]
},
"zoster_radiculitis": {
  "description": "Zoster radiculitis is a nerve root inflammation caused by reactivation of the varicella-zoster virus, leading to sharp pain along the affected nerve pathway.",
  "symptoms": [
    "Sharp or burning nerve pain",
    "Tingling or numbness",
    "Muscle weakness in affected area",
    "Sensitivity to touch",
    "Possible skin rash in the same region"
  ],
  "causes": [
    "Reactivation of varicella-zoster virus",
    "Spread of the virus to spinal nerve roots"
  ],
  "risk_factors": [
    "Older age",
    "Weakened immune system",
    "History of chickenpox"
  ],
  "diagnosis": [
    "Clinical examination",
    "MRI of spine",
    "PCR testing for varicella-zoster virus"
  ],
  "remedies": [
    "Antiviral medications",
    "Pain management therapy",
    "Physical therapy if needed"
  ],
  "prevention": [
    "Shingles vaccination",
    "Early antiviral treatment of shingles"
  ]
},
"yellow_nail_syndrome_variant": {
  "description": "Yellow nail syndrome variant is a rare condition characterized by slow-growing yellow nails along with respiratory issues and mild lymphatic dysfunction.",
  "symptoms": [
    "Thickened yellow nails",
    "Slow nail growth",
    "Chronic cough",
    "Shortness of breath",
    "Mild swelling in limbs"
  ],
  "causes": [
    "Lymphatic system abnormalities",
    "Chronic respiratory disease",
    "Unknown underlying factors"
  ],
  "risk_factors": [
    "Chronic lung disease",
    "Lymphatic disorders",
    "Older age"
  ],
  "diagnosis": [
    "Clinical examination of nails",
    "Chest imaging (X-ray or CT)",
    "Lymphatic function assessment"
  ],
  "remedies": [
    "Treat underlying respiratory conditions",
    "Vitamin supplementation",
    "Supportive care for symptoms"
  ],
  "prevention": [
    "Manage respiratory health",
    "Regular medical check-ups",
    "Early treatment of symptoms"
  ]
},
"yersinia_pestis_infection": {
  "description": "Yersinia pestis infection is a serious bacterial disease known as plague, which can affect the lymph nodes, lungs, or bloodstream.",
  "symptoms": [
    "Fever and chills",
    "Swollen and painful lymph nodes (buboes)",
    "Weakness",
    "Cough with bloody sputum (in pneumonic form)",
    "Sepsis in severe cases"
  ],
  "causes": [
    "Infection with Yersinia pestis bacteria",
    "Bites from infected fleas",
    "Contact with infected animals"
  ],
  "risk_factors": [
    "Living in areas with rodent infestations",
    "Exposure to infected animals",
    "Poor sanitation conditions"
  ],
  "diagnosis": [
    "Blood tests",
    "Culture of bacteria",
    "PCR testing"
  ],
  "remedies": [
    "Antibiotic treatment (e.g., streptomycin, doxycycline)",
    "Supportive care",
    "Isolation in pneumonic cases"
  ],
  "prevention": [
    "Control rodent populations",
    "Avoid flea bites",
    "Use protective measures when handling animals"
  ]
},
"yaws_early_stage": {
  "description": "Early-stage yaws is an infectious bacterial disease affecting the skin, primarily in tropical regions, characterized by painless skin lesions that can spread if untreated.",
  "symptoms": [
    "Painless skin sores or ulcers",
    "Papules or nodules on skin",
    "Mild itching",
    "Swollen lymph nodes"
  ],
  "causes": [
    "Treponema pallidum pertenue bacteria",
    "Direct skin-to-skin contact with infected person"
  ],
  "risk_factors": [
    "Living in tropical or rural areas",
    "Poor hygiene conditions",
    "Close contact with infected individuals"
  ],
  "diagnosis": [
    "Clinical examination of lesions",
    "Blood tests for treponemal infection",
    "PCR testing in some cases"
  ],
  "remedies": [
    "Single-dose antibiotic treatment (e.g., azithromycin)",
    "Wound care and hygiene",
    "Follow-up treatment if needed"
  ],
  "prevention": [
    "Maintain personal hygiene",
    "Avoid direct contact with infected lesions",
    "Community-wide antibiotic programs in endemic areas"
  ]
},
"yolk_sac_tumor": {
  "description": "Yolk sac tumor is a rare and aggressive type of germ cell tumor that typically occurs in the ovaries or testes, most commonly in children and young adults.",
  "symptoms": [
    "Abdominal or pelvic pain",
    "Swelling or mass in abdomen",
    "Unexplained weight loss",
    "Fatigue",
    "Testicular swelling (in males)"
  ],
  "causes": [
    "Abnormal development of germ cells",
    "Genetic mutations affecting cell growth"
  ],
  "risk_factors": [
    "Young age (children and adolescents)",
    "History of germ cell tumors",
    "Certain genetic conditions"
  ],
  "diagnosis": [
    "Blood test for alpha-fetoprotein (AFP)",
    "Ultrasound or CT scan",
    "Biopsy of the tumor"
  ],
  "remedies": [
    "Surgical removal of the tumor",
    "Chemotherapy",
    "Regular follow-up monitoring"
  ],
  "prevention": [
    "No known prevention",
    "Early detection through medical evaluation of symptoms"
  ]
},
"zinc_induced_copper_deficiency": {
  "description": "Zinc-induced copper deficiency is a condition where excessive zinc intake interferes with copper absorption, leading to low copper levels and related health issues.",
  "symptoms": [
    "Fatigue",
    "Anemia",
    "Neurological problems such as numbness or weakness",
    "Pale skin",
    "Impaired immune function"
  ],
  "causes": [
    "Excessive zinc supplementation",
    "Long-term use of zinc-containing medications",
    "Imbalance in dietary mineral intake"
  ],
  "risk_factors": [
    "High-dose zinc supplements",
    "Chronic use of denture creams containing zinc",
    "Poor nutritional balance"
  ],
  "diagnosis": [
    "Blood tests showing low copper and high zinc levels",
    "Complete blood count",
    "Neurological evaluation"
  ],
  "remedies": [
    "Reduce or stop excess zinc intake",
    "Copper supplementation",
    "Dietary adjustment to restore mineral balance"
  ],
  "prevention": [
    "Avoid unnecessary high-dose zinc supplements",
    "Maintain balanced micronutrient intake",
    "Regular monitoring when on long-term supplements"
  ]
},
"zinc_induced_copper_deficiency": {
  "description": "Zinc-induced copper deficiency is a condition where excessive zinc intake interferes with copper absorption, leading to low copper levels and related health issues.",
  "symptoms": [
    "Fatigue",
    "Anemia",
    "Neurological problems such as numbness or weakness",
    "Pale skin",
    "Impaired immune function"
  ],
  "causes": [
    "Excessive zinc supplementation",
    "Long-term use of zinc-containing medications",
    "Imbalance in dietary mineral intake"
  ],
  "risk_factors": [
    "High-dose zinc supplements",
    "Chronic use of denture creams containing zinc",
    "Poor nutritional balance"
  ],
  "diagnosis": [
    "Blood tests showing low copper and high zinc levels",
    "Complete blood count",
    "Neurological evaluation"
  ],
  "remedies": [
    "Reduce or stop excess zinc intake",
    "Copper supplementation",
    "Dietary adjustment to restore mineral balance"
  ],
  "prevention": [
    "Avoid unnecessary high-dose zinc supplements",
    "Maintain balanced micronutrient intake",
    "Regular monitoring when on long-term supplements"
  ]
},
"zika_neurological_syndrome": {
  "description": "Zika neurological syndrome refers to neurological complications associated with Zika virus infection, including conditions like Guillain-Barré syndrome and nerve inflammation.",
  "symptoms": [
    "Muscle weakness",
    "Numbness or tingling",
    "Difficulty walking",
    "Facial paralysis",
    "Fatigue"
  ],
  "causes": [
    "Zika virus infection",
    "Immune-mediated nerve damage triggered by the virus"
  ],
  "risk_factors": [
    "Recent Zika virus infection",
    "Living in endemic areas",
    "Weakened immune response"
  ],
  "diagnosis": [
    "Neurological examination",
    "PCR or serological tests for Zika virus",
    "Nerve conduction studies"
  ],
  "remedies": [
    "Supportive care",
    "Physical therapy",
    "Immunotherapy in severe cases"
  ],
  "prevention": [
    "Avoid mosquito bites",
    "Use protective clothing and repellents",
    "Control mosquito breeding sites"
  ]
},
"zenker_diverticulitis": {
  "description": "Zenker diverticulitis is an inflammation or infection of a Zenker diverticulum in the upper esophagus, often due to retained food and bacterial growth.",
  "symptoms": [
    "Pain while swallowing",
    "Fever",
    "Bad breath",
    "Regurgitation of food",
    "Neck discomfort or swelling"
  ],
  "causes": [
    "Food retention in Zenker diverticulum",
    "Bacterial infection",
    "Poor esophageal motility"
  ],
  "risk_factors": [
    "Older age",
    "Existing Zenker diverticulum",
    "Chronic swallowing difficulties"
  ],
  "diagnosis": [
    "Barium swallow study",
    "Endoscopy",
    "Clinical examination"
  ],
  "remedies": [
    "Antibiotics for infection",
    "Diet modification",
    "Surgical or endoscopic treatment"
  ],
  "prevention": [
    "Early management of Zenker diverticulum",
    "Proper chewing and eating habits",
    "Regular follow-up for swallowing issues"
  ]
},
"zollinger_like_syndrome": {
  "description": "Zollinger-like syndrome is a condition resembling Zollinger-Ellison syndrome, characterized by excessive gastric acid production without identifiable gastrin-secreting tumors.",
  "symptoms": [
    "Persistent abdominal pain",
    "Frequent peptic ulcers",
    "Chronic diarrhea",
    "Acid reflux",
    "Nausea"
  ],
  "causes": [
    "Unknown mechanisms leading to increased acid secretion",
    "Possible hormonal imbalances",
    "Gastric hyperactivity"
  ],
  "risk_factors": [
    "History of chronic gastric disorders",
    "Long-term acid-related conditions",
    "Genetic predisposition"
  ],
  "diagnosis": [
    "Endoscopy",
    "Gastrin level tests",
    "Imaging to rule out tumors"
  ],
  "remedies": [
    "Proton pump inhibitors",
    "Dietary modifications",
    "Regular medical monitoring"
  ],
  "prevention": [
    "Manage gastric health",
    "Avoid excessive use of irritant foods",
    "Routine check-ups for chronic symptoms"
  ]
},
"zoster_encephalitis": {
  "description": "Zoster encephalitis is a rare but serious complication of varicella-zoster virus reactivation, leading to inflammation of the brain.",
  "symptoms": [
    "Confusion or altered mental state",
    "Severe headache",
    "Fever",
    "Seizures",
    "Weakness or neurological deficits",
    "Difficulty speaking"
  ],
  "causes": [
    "Reactivation of varicella-zoster virus",
    "Spread of the virus to brain tissue"
  ],
  "risk_factors": [
    "Weakened immune system",
    "Older age",
    "History of shingles"
  ],
  "diagnosis": [
    "MRI or CT scan of the brain",
    "Lumbar puncture (CSF analysis)",
    "PCR testing for varicella-zoster virus"
  ],
  "remedies": [
    "Intravenous antiviral therapy (e.g., acyclovir)",
    "Supportive hospital care",
    "Management of seizures and complications"
  ],
  "prevention": [
    "Shingles vaccination",
    "Early treatment of shingles infections"
  ]
},
"zoster_otitis": {
  "description": "Zoster otitis, also known as Ramsay Hunt syndrome, is a condition where the varicella-zoster virus affects the facial nerve near the ear, causing ear pain and facial paralysis.",
  "symptoms": [
    "Severe ear pain",
    "Facial weakness or paralysis",
    "Rash or blisters around the ear",
    "Hearing loss",
    "Dizziness or vertigo",
    "Loss of taste"
  ],
  "causes": [
    "Reactivation of varicella-zoster virus",
    "Infection of the facial nerve near the ear"
  ],
  "risk_factors": [
    "Older age",
    "Weakened immune system",
    "History of chickenpox"
  ],
  "diagnosis": [
    "Clinical examination",
    "PCR test for varicella-zoster virus",
    "Hearing tests"
  ],
  "remedies": [
    "Antiviral medications (e.g., acyclovir)",
    "Corticosteroids",
    "Pain management",
    "Physical therapy for facial muscles"
  ],
  "prevention": [
    "Shingles vaccination",
    "Early treatment of shingles symptoms"
  ]
},
"zygomycosis_pulmonary": {
  "description": "Pulmonary zygomycosis is a serious fungal infection of the lungs caused by organisms in the Mucorales group, often affecting immunocompromised individuals.",
  "symptoms": [
    "Fever",
    "Cough",
    "Chest pain",
    "Shortness of breath",
    "Coughing up blood (hemoptysis)"
  ],
  "causes": [
    "Inhalation of fungal spores",
    "Weakened immune system",
    "Spread from sinus infection"
  ],
  "risk_factors": [
    "Uncontrolled diabetes",
    "Cancer or chemotherapy",
    "Organ transplant recipients",
    "Use of corticosteroids"
  ],
  "diagnosis": [
    "Chest CT scan",
    "Bronchoscopy with biopsy",
    "Fungal culture and microscopy"
  ],
  "remedies": [
    "Intravenous antifungal therapy (e.g., amphotericin B)",
    "Surgical removal of infected lung tissue if necessary",
    "Management of underlying conditions"
  ],
  "prevention": [
    "Control blood sugar levels",
    "Avoid exposure to contaminated environments",
    "Proper management of immune-compromising conditions"
  ]
},

"zinc_deficiency_dermatitis": {
  "description": "Zinc deficiency dermatitis is a skin condition caused by inadequate zinc levels, leading to inflammation and impaired skin healing.",
  "symptoms": [
    "Red, inflamed skin patches",
    "Dry or scaly skin",
    "Cracks around mouth and eyes",
    "Hair thinning or loss",
    "Delayed wound healing"
  ],
  "causes": [
    "Low dietary zinc intake",
    "Malabsorption disorders",
    "Chronic illnesses affecting nutrient absorption"
  ],
  "risk_factors": [
    "Malnutrition",
    "Digestive disorders",
    "Infants and elderly individuals",
    "Strict vegetarian or restrictive diets"
  ],
  "diagnosis": [
    "Blood zinc level test",
    "Clinical examination of skin",
    "Dietary assessment"
  ],
  "remedies": [
    "Zinc supplementation",
    "Diet rich in zinc (meat, nuts, seeds)",
    "Treat underlying digestive issues"
  ],
  "prevention": [
    "Maintain balanced nutrition",
    "Monitor zinc intake in high-risk groups",
    "Early treatment of symptoms"
  ]
},
"zygomycosis_rhino_orbital": {
  "description": "Rhino-orbital zygomycosis is a severe fungal infection affecting the nasal passages, sinuses, and eye orbit, often seen in immunocompromised individuals.",
  "symptoms": [
    "Facial pain or swelling",
    "Nasal congestion or black discharge",
    "Eye swelling or vision problems",
    "Fever",
    "Headache"
  ],
  "causes": [
    "Inhalation of fungal spores (Mucor species)",
    "Spread of infection from sinuses to orbit"
  ],
  "risk_factors": [
    "Uncontrolled diabetes",
    "Weakened immune system",
    "Use of immunosuppressive drugs"
  ],
  "diagnosis": [
    "CT scan or MRI of sinuses and orbit",
    "Biopsy and fungal culture",
    "Clinical examination"
  ],
  "remedies": [
    "Urgent antifungal therapy (e.g., amphotericin B)",
    "Surgical removal of infected tissue",
    "Control of underlying conditions like diabetes"
  ],
  "prevention": [
    "Manage blood sugar levels",
    "Avoid exposure to contaminated environments",
    "Early treatment of sinus infections"
  ]
},
"zenker_carcinoma": {
  "description": "Zenker carcinoma is a rare condition where cancer develops within a Zenker diverticulum in the upper esophagus.",
  "symptoms": [
    "Difficulty swallowing (dysphagia)",
    "Unexplained weight loss",
    "Regurgitation of food",
    "Persistent cough",
    "Bad breath",
    "Hoarseness"
  ],
  "causes": [
    "Chronic irritation within Zenker diverticulum",
    "Long-standing food retention in esophageal pouch",
    "Cellular changes due to inflammation"
  ],
  "risk_factors": [
    "Older age",
    "Untreated Zenker diverticulum",
    "Chronic esophageal irritation"
  ],
  "diagnosis": [
    "Endoscopy with biopsy",
    "Barium swallow study",
    "CT scan for staging"
  ],
  "remedies": [
    "Surgical removal of tumor and diverticulum",
    "Radiation therapy",
    "Chemotherapy depending on stage"
  ],
  "prevention": [
    "Early treatment of Zenker diverticulum",
    "Regular monitoring of chronic swallowing issues",
    "Avoid prolonged esophageal irritation"
  ]
},
"zoster_myelitis": {
  "description": "Zoster myelitis is a rare neurological complication of shingles where the varicella-zoster virus causes inflammation of the spinal cord.",
  "symptoms": [
    "Back pain",
    "Weakness in limbs",
    "Numbness or tingling",
    "Difficulty walking",
    
  ],
  "causes": [
    "Reactivation of varicella-zoster virus",
    "Spread of the virus to the spinal cord"
  ],
  "risk_factors": [
    "Older age",
    "Weakened immune system",
    "History of chickenpox or shingles"
  ],
  "diagnosis": [
    "MRI scan of the spinal cord",
    "Lumbar puncture (spinal fluid test)"
  ],
  "remedies": [
    "Antiviral medications such as acyclovir",
    "Corticosteroids to reduce inflammation",
    "Physical therapy for recovery"
  ],
  "prevention": [
    "Shingles vaccination",
    "Early antiviral treatment for shingles"
  ]
},
"zinc_responsive_dermatosis": {
  "description": "Zinc responsive dermatosis is a skin disorder in which skin lesions improve after zinc supplementation, often associated with zinc deficiency or impaired zinc absorption.",
  "symptoms": [
    "Red or crusty skin lesions",
    "Hair loss",
    "Scaling around mouth, eyes, or paws (in some cases in animals or rare human forms)",
    "Skin inflammation",
    "Delayed wound healing"
  ],
  "causes": [
    "Zinc deficiency",
    "Impaired absorption of zinc",
    "Genetic metabolic disorders affecting zinc utilization"
  ],
  "risk_factors": [
    "Poor nutrition",
    "Malabsorption disorders",
    "Certain genetic conditions"
  ],
  "diagnosis": [
    "Blood zinc level test",
    "Clinical examination of skin lesions",
    "Response to zinc supplementation"
  ],
  "remedies": [
    "Zinc supplementation",
    "Balanced diet with zinc-rich foods",
    "Treatment of underlying absorption disorders"
  ],
  "prevention": [
    "Maintain adequate dietary zinc intake",
    "Monitor nutritional status",
    "Early treatment of skin symptoms"
  ]
},
"zieve_syndrome": {
  "description": "Zieve syndrome is a rare condition associated with chronic alcohol use that involves a combination of hemolytic anemia, jaundice, and high levels of fats in the blood.",
  "symptoms": [
    "Jaundice (yellowing of skin and eyes)",
    "Fatigue",
    "Abdominal pain",
    "Nausea and vomiting",
    "Weakness",
    "Dark urine"
  ],
  "causes": [
    "Chronic alcohol consumption",
    "Liver dysfunction leading to abnormal fat metabolism",
    "Destruction of red blood cells (hemolysis)"
  ],
  "risk_factors": [
    "Long-term heavy alcohol use",
    "Liver disease",
    "Poor nutrition"
  ],
  "diagnosis": [
    "Blood tests showing anemia and high lipid levels",
    "Liver function tests",
    "Medical history of alcohol use"
  ],
  "remedies": [
    "Complete abstinence from alcohol",
    "Nutritional support",
    "Treatment of anemia and liver complications"
  ],
  "prevention": [
    "Avoid excessive alcohol consumption",
    "Maintain a balanced diet",
    "Regular medical monitoring for liver health"
  ]
},
"zoster_ophthalmicus": {
  "description": "Zoster ophthalmicus is a form of shingles that affects the eye and surrounding areas due to reactivation of the varicella-zoster virus in the ophthalmic branch of the trigeminal nerve.",
  "symptoms": [
    "Pain or burning sensation around the eye",
    "Red rash or blisters on the forehead or eyelid",
    "Eye redness",
    "Blurred vision",
    "Sensitivity to light",
    "Headache"
  ],
  "causes": [
    "Reactivation of varicella-zoster virus",
    "Previous infection with chickenpox"
  ],
  "risk_factors": [
    "Older age",
    "Weakened immune system",
    "Stress or illness"
  ],
  "diagnosis": [
    "Physical examination of rash and eye symptoms",
    "PCR test for varicella-zoster virus",
    "Eye examination by ophthalmologist"
  ],
  "remedies": [
    "Antiviral medications such as acyclovir or valacyclovir",
    "Pain management",
    "Steroid eye drops in some cases"
  ],
  "prevention": [
    "Shingles vaccination",
    "Early antiviral treatment if shingles symptoms appear"
  ]
},
"zollinger_ellison_variant": {
  "description": "Zollinger-Ellison variant is a rare digestive condition similar to Zollinger-Ellison syndrome where excess gastrin hormone leads to extremely high stomach acid and recurrent ulcers.",
  "symptoms": [
    "Burning stomach pain",
    "Frequent or severe ulcers",
    "Chronic diarrhea",
    "Acid reflux",
    "Nausea and vomiting"
  ],
  "causes": [
    "Gastrin-secreting tumors in pancreas or duodenum",
    "Genetic conditions such as MEN1"
  ],
  "risk_factors": [
    "Family history of endocrine tumors",
    "Genetic mutation linked to MEN1",
    "Middle-aged adults"
  ],
  "diagnosis": [
    "Blood gastrin level test",
    "Endoscopy",
    "CT scan or MRI",
    "Secretin stimulation test"
  ],
  "remedies": [
    "Proton pump inhibitors",
    "Surgical removal of gastrinomas",
    "Targeted therapy or chemotherapy in advanced cases"
  ],
  "prevention": [
    "Genetic screening for MEN1",
    "Regular monitoring in high-risk individuals"
  ]
},
"zoster_meningitis": {
  "description": "Zoster meningitis is an inflammation of the protective membranes of the brain and spinal cord caused by the reactivation of the varicella-zoster virus.",
  "symptoms": [
    "Severe headache",
    "Neck stiffness",
    "Fever",
    "Sensitivity to light",
    "Nausea and vomiting",
    "Confusion or difficulty concentrating"
  ],
  "causes": [
    "Reactivation of varicella-zoster virus (the virus that causes chickenpox)",
    "Spread of the virus to the central nervous system"
  ],
  "risk_factors": [
    "Weakened immune system",
    "Older age",
    "History of chickenpox or shingles"
  ],
  "diagnosis": [
    "Lumbar puncture (spinal fluid test)",
    "PCR test for varicella-zoster virus",
    "Brain imaging such as MRI"
  ],
  "remedies": [
    "Antiviral medications such as acyclovir",
    "Pain management",
    "Hospital monitoring for severe cases"
  ],
  "prevention": [
    "Shingles vaccination",
    "Maintaining strong immune health",
    "Early treatment of shingles infections"
  ]
},
"zoster_sine_herpete": {
  "description": "Zoster sine herpete is a form of shingles where nerve pain occurs without the typical skin rash.",
  "symptoms": [
    "Burning or stabbing nerve pain",
    "Tingling or numbness",
    "Sensitivity to touch",
    "Headache",
    "Fatigue"
  ],
"zollinger_ellison_syndrome": {
  "description": "Zollinger-Ellison syndrome is a rare digestive disorder in which tumors called gastrinomas form in the pancreas or duodenum and produce excessive amounts of the hormone gastrin, leading to very high stomach acid levels.",
  "symptoms": [
    "Severe stomach pain",
    "Frequent peptic ulcers",
    "Diarrhea",
    "Acid reflux",
    "Nausea and vomiting",
    "Unexplained weight loss"
  ],
  "causes": [
    "Gastrin-secreting tumors (gastrinomas)",
    "Genetic condition such as Multiple Endocrine Neoplasia type 1 (MEN1)"
  ],
  "risk_factors": [
    "Family history of MEN1 syndrome",
    "Presence of endocrine tumors",
    "Middle adulthood"
  ],
  "diagnosis": [
    "Blood test for gastrin levels",
    "Endoscopy",
    "CT scan or MRI imaging",
    "Secretin stimulation test"
  ],
  "remedies": [
    "Proton pump inhibitors to reduce stomach acid",
    "Surgical removal of tumors",
    "Targeted therapy or chemotherapy in advanced cases"
  ],
  "prevention": [
    "Genetic counseling for MEN1 families",
    "Regular medical monitoring for high-risk individuals"
  ]
},
  "causes": [
    "Reactivation of the varicella-zoster virus",
    "Weak immune system",
    "Previous chickenpox infection"
  ],
  "risk_factors": [
    "Older age",
    "Immunocompromised conditions",
    "Stress or illness"
  ],
  "diagnosis": [
    "Clinical evaluation of nerve pain",
    "PCR test for varicella-zoster virus",
    "Blood antibody tests"
  ],
  "remedies": [
    "Antiviral medications",
    "Pain management medications",
    "Rest and supportive care"
  ],
  "prevention": [
    "Shingles vaccination",
    "Maintaining strong immune health",
    "Early treatment of symptoms"
  ]
},
"zinc_toxicity": {
  "description": "Zinc toxicity occurs when there is an excessive amount of zinc in the body, usually due to overuse of supplements or exposure to industrial sources.",
  "symptoms": [
    "Nausea",
    "Vomiting",
    "Stomach cramps",
    "Headache",
    "Loss of appetite",
    "Diarrhea"
  ],
  "causes": [
    "Excessive zinc supplement intake",
    "Exposure to zinc fumes in industrial environments",
    "Accidental ingestion of zinc-containing products"
  ],
  "risk_factors": [
    "High-dose zinc supplementation",
    "Occupational exposure to metal fumes",
    "Improper use of nutritional supplements"
  ],
  "diagnosis": [
    "Blood zinc level test",
    "Clinical symptom evaluation",
    "Medical history review"
  ],
  "remedies": [
    "Stop zinc supplements",
    "Hydration and supportive treatment",
    "Medical monitoring for severe cases"
  ],
  "prevention": [
    "Follow recommended dietary allowances for zinc",
    "Avoid unnecessary high-dose supplements",
    "Use protective equipment in industrial workplaces"
  ]
},
    "waldenstrom_macroglobulinemia": {
  "description": "Waldenstrom macroglobulinemia is a rare type of blood cancer affecting white blood cells.",
  "causes": ["Genetic mutations in bone marrow cells"],
  "remedies": ["Chemotherapy", "Targeted therapy", "Plasmapheresis"]
},
"zinc_deficiency": {
  "description": "Zinc deficiency is a nutritional condition where the body lacks sufficient zinc, an essential mineral required for immune function, wound healing, and cell growth.",
  "symptoms": [
    "Frequent infections",
    "Slow wound healing",
    "Hair loss",
    "Loss of appetite",
    "Reduced sense of taste or smell",
    "Skin rashes"
  ],
  "causes": [
    "Poor dietary intake of zinc",
    "Malabsorption disorders",
    "Chronic illnesses",
    "Vegetarian or restrictive diets without proper supplementation"
  ],
  "risk_factors": [
    "Malnutrition",
    "Digestive disorders such as Crohn’s disease",
    "Pregnancy",
    "Chronic alcohol use"
  ],
  "diagnosis": [
    "Blood zinc level test",
    "Dietary assessment",
    "Clinical symptom evaluation"
  ],
  "remedies": [
    "Zinc supplements",
    "Increase intake of zinc-rich foods such as meat, nuts, seeds, and whole grains",
    "Treat underlying digestive disorders"
  ],
  "prevention": [
    "Maintain a balanced diet",
    "Regular nutritional monitoring in high-risk individuals",
    "Proper supplementation when needed"
  ]
},
"zika_virus_disease": {
  "description": "Zika virus disease is a mosquito-borne viral infection that can cause mild symptoms in most people but may lead to serious birth defects if a pregnant woman becomes infected.",
  "symptoms": ["Fever", "Skin rash", "Joint pain", "Red eyes (conjunctivitis)", "Headache", "Muscle pain"],
  "causes": ["Zika virus infection", "Bite from infected Aedes mosquitoes", "Transmission from mother to fetus", "Rarely through blood transfusion or sexual contact"],
  "risk_factors": ["Living in or traveling to tropical regions", "Exposure to mosquito bites", "Pregnancy during infection"],
  "diagnosis": ["Blood test", "Urine test", "PCR testing for viral RNA"],
  "remedies": ["Rest", "Drink plenty of fluids", "Pain relievers such as acetaminophen", "Medical monitoring especially during pregnancy"],
  "prevention": ["Use mosquito repellents", "Wear protective clothing", "Remove standing water around homes", "Practice safe sex when traveling to affected areas"]
},
"zenker_diverticulum": {
  "description": "Zenker diverticulum is a condition in which a pouch (diverticulum) forms in the upper part of the esophagus due to weakness in the muscle wall. Food can collect in the pouch, leading to swallowing difficulties and regurgitation.",
  "symptoms": ["Difficulty swallowing (dysphagia)", "Regurgitation of undigested food", "Bad breath (halitosis)", "Coughing while eating", "Sensation of lump in the throat"],
  "causes": ["Weakness in the upper esophageal muscle wall", "Increased pressure during swallowing", "Aging-related muscle changes"],
  "risk_factors": ["Older age", "Esophageal motility disorders", "Chronic swallowing problems"],
  "diagnosis": ["Barium swallow X-ray", "Endoscopy", "Esophageal manometry"],
  "remedies": ["Diet modification and eating slowly", "Endoscopic diverticulotomy", "Surgical removal of the pouch"],
  "prevention": ["Early treatment of swallowing disorders", "Regular medical checkups for persistent swallowing difficulty"]
},

"wandering_spleen": {
  "description": "Wandering spleen is a rare condition where the spleen moves from its normal position.",
  "causes": ["Weak or absent spleen ligaments"],
  "remedies": ["Surgical fixation", "Splenectomy if severe"]
},

"weaver_syndrome": {
  "description": "Weaver syndrome is a rare genetic disorder characterized by rapid growth and developmental delay.",
  "causes": ["Genetic mutation"],
  "remedies": ["Supportive therapy", "Developmental support"]
},

"wegener_granulomatosis": {
  "description": "Wegener granulomatosis is an autoimmune disease causing inflammation of blood vessels.",
  "causes": ["Autoimmune reaction"],
  "remedies": ["Immunosuppressive medications"]
},

"weill_marchesani_syndrome": {
  "description": "Weill-Marchesani syndrome is a genetic disorder affecting connective tissue and eye structure.",
  "causes": ["Genetic mutation"],
  "remedies": ["Eye treatment", "Supportive care"]
},

"werner_syndrome": {
  "description": "Werner syndrome is a genetic disorder causing premature aging.",
  "causes": ["Genetic mutation"],
  "remedies": ["Symptomatic treatment"]
},

"west_syndrome": {
  "description": "West syndrome is a severe form of epilepsy in infants.",
  "causes": ["Brain abnormalities", "Genetic factors"],
  "remedies": ["Antiepileptic medication", "Hormone therapy"]
},

"white_coat_hypertension": {
  "description": "White coat hypertension is high blood pressure observed in clinical settings due to anxiety.",
  "causes": ["Stress during medical visits"],
  "remedies": ["Lifestyle management", "Regular monitoring"]
},

"whipple_procedure_complication": {
  "description": "Complications occurring after pancreatic surgery known as the Whipple procedure.",
  "causes": ["Surgical complications"],
  "remedies": ["Medical management", "Post-surgical care"]
},

"wiskott_aldrich_syndrome": {
  "description": "Wiskott-Aldrich syndrome is a rare immune deficiency disorder.",
  "causes": ["Genetic mutation affecting immune system"],
  "remedies": ["Bone marrow transplant", "Supportive care"]
},

"wolman_disease": {
  "description": "Wolman disease is a rare genetic disorder affecting fat metabolism.",
  "causes": ["Enzyme deficiency"],
  "remedies": ["Enzyme replacement therapy"]
},

"xerophthalmia": {
  "description": "Xerophthalmia is severe dryness of the eye due to vitamin A deficiency.",
  "causes": ["Vitamin A deficiency"],
  "remedies": ["Vitamin A supplementation"]
},

"xanthoma": {
  "description": "Xanthoma is a condition where fatty deposits accumulate under the skin.",
  "causes": ["High cholesterol levels"],
  "remedies": ["Cholesterol-lowering medications"]
},

"xanthopsia": {
  "description": "Xanthopsia is a visual disorder where objects appear yellow.",
  "causes": ["Medication side effects", "Jaundice"],
  "remedies": ["Treat underlying cause"]
},

"x_linked_agammaglobulinemia": {
  "description": "X-linked agammaglobulinemia is a genetic immune disorder causing low antibody levels.",
  "causes": ["Genetic mutation"],
  "remedies": ["Immunoglobulin therapy"]
},

"x_linked_hypophosphatemia": {
  "description": "X-linked hypophosphatemia causes weak bones due to low phosphate levels.",
  "causes": ["Genetic mutation"],
  "remedies": ["Phosphate supplements", "Vitamin D therapy"]
},

"x_linked_sideroblastic_anemia": {
  "description": "X-linked sideroblastic anemia is a blood disorder affecting red blood cell formation.",
  "causes": ["Genetic mutation"],
  "remedies": ["Vitamin B6 therapy"]
},

"yaws_late_stage": {
  "description": "Late stage yaws causes bone and skin deformities.",
  "causes": ["Untreated bacterial infection"],
  "remedies": ["Antibiotic treatment"]
},

"yellow_fever_severe": {
  "description": "Severe yellow fever causes liver damage and bleeding.",
  "causes": ["Yellow fever virus infection"],
  "remedies": ["Supportive care", "Vaccination prevention"]
},

"yersiniosis": {
  "description": "Yersiniosis is a bacterial infection affecting the intestines.",
  "causes": ["Contaminated food or water"],
  "remedies": ["Antibiotics in severe cases"]
},

"yolk_sac_tumor": {
  "description": "Yolk sac tumor is a rare cancer usually affecting the ovaries or testes.",
  "causes": ["Abnormal germ cells"],
  "remedies": ["Chemotherapy", "Surgery"]
},

"young_syndrome": {
  "description": "Young syndrome causes respiratory infections and infertility in males.",
  "causes": ["Unknown factors"],
  "remedies": ["Respiratory treatment"]
},

"zika_congenital_syndrome": {
  "description": "Congenital syndrome caused by Zika virus infection during pregnancy.",
  "causes": ["Zika virus"],
  "remedies": ["Supportive care"]
},

"zoster": {
  "description": "Zoster, also known as shingles, causes painful skin rash.",
  "causes": ["Varicella-zoster virus reactivation"],
  "remedies": ["Antiviral medication"]
},

"zygomycosis": {
  "description": "Zygomycosis is a rare fungal infection affecting sinuses or lungs.",
  "causes": ["Fungal spores"],
  "remedies": ["Antifungal medication", "Surgery"]
},

"zollinger_syndrome_variant": {
  "description": "A variant of Zollinger syndrome causing excessive stomach acid production.",
  "causes": ["Gastrin-secreting tumors"],
  "remedies": ["Proton pump inhibitors"]
},

"zoster_opthalmicus": {
  "description": "Zoster ophthalmicus is shingles affecting the eye region.",
  "causes": ["Varicella-zoster virus"],
  "remedies": ["Antiviral therapy"]
},

"zoster_neuralgia": {
  "description": "Postherpetic neuralgia is nerve pain after shingles infection.",
  "causes": ["Nerve damage from shingles"],
  "remedies": ["Pain medications"]
},

"zygote_implantation_disorder": {
  "description": "A rare reproductive condition affecting embryo implantation.",
  "causes": ["Hormonal imbalance", "Uterine abnormalities"],
  "remedies": ["Fertility treatments"]
},
    "urticarial_vasculitis": {
        "description": "Urticarial vasculitis is a condition where blood vessels become inflamed and cause hives-like skin lesions.",
        "causes": ["Autoimmune disorders", "Infections", "Medication reactions"],
        "remedies": ["Antihistamines", "Anti-inflammatory medications", "Treat underlying condition"]
    },
    "urticaria_pigmentosa": {
        "description": "Urticaria pigmentosa is a skin condition caused by an abnormal buildup of mast cells in the skin.",
        "causes": ["Mast cell accumulation in skin", "Genetic or unknown factors"],
        "remedies": ["Antihistamines", "Avoid triggers such as heat or friction", "Medical monitoring"]
    },
    "uremia": {
        "description": "Uremia is a serious condition that occurs when waste products build up in the blood due to severe kidney dysfunction.",
        "causes": ["Chronic kidney disease", "Acute kidney failure", "Severe dehydration"],
        "remedies": ["Dialysis", "Kidney transplant", "Treatment of underlying kidney disease"]
    },
    "uveitis": {
        "description": "Uveitis is inflammation of the uvea, the middle layer of the eye, which can cause redness, pain, and blurred vision.",
        "causes": ["Autoimmune diseases", "Eye infections", "Eye injury"],
        "remedies": ["Corticosteroid eye drops", "Immunosuppressive medications", "Treat underlying infection"]
    },
    "vasovagal_syncope": {
        "description": "Vasovagal syncope is a common cause of fainting triggered by a sudden drop in heart rate and blood pressure.",
        "causes": ["Emotional stress", "Standing for long periods", "Pain or dehydration"],
        "remedies": ["Lie down and elevate legs", "Stay hydrated", "Avoid known triggers", "Medical evaluation if recurrent"]
    },
    "vitiligo": {
        "description": "Vitiligo is a skin condition where patches of skin lose their pigment.",
        "causes": ["Autoimmune response", "Genetic factors", "Environmental triggers"],
        "remedies": ["Topical corticosteroids", "Phototherapy", "Skin camouflage therapy"]
    },
    "waterborne_disease": {
        "description": "Waterborne diseases are illnesses caused by microorganisms in contaminated water.",
        "causes": ["Contaminated drinking water", "Poor sanitation", "Pathogens like bacteria or viruses"],
        "remedies": ["Drink clean treated water", "Oral rehydration therapy", "Antibiotics depending on infection"]
    },
    "west_nile_fever": {
        "description": "West Nile fever is a viral infection transmitted primarily through mosquito bites.",
        "causes": ["West Nile virus", "Bite from infected mosquito"],
        "remedies": ["Supportive care", "Rest and fluids", "Hospital care in severe cases"]
    },
    "wilms_tumor": {
        "description": "Wilms tumor is a rare kidney cancer that primarily affects young children.",
        "causes": ["Genetic mutations", "Congenital abnormalities"],
        "remedies": ["Surgical removal of tumor", "Chemotherapy", "Radiation therapy if required"]
    },
    "wernicke_encephalopathy": {
        "description": "Wernicke encephalopathy is a neurological disorder caused by severe thiamine (vitamin B1) deficiency.",
        "causes": ["Chronic alcohol misuse", "Malnutrition", "Prolonged vomiting"],
        "remedies": ["Immediate thiamine supplementation", "Nutritional support", "Treat underlying cause"]
    },
    "wolff_parkinson_white_syndrome": {
        "description": "Wolff-Parkinson-White syndrome is a heart condition with an extra electrical pathway causing rapid heartbeats.",
        "causes": ["Congenital extra electrical pathway in the heart"],
        "remedies": ["Medications to control heart rhythm", "Catheter ablation procedure", "Regular cardiac monitoring"]
    },
    "von_willebrand_disease": {
        "description": "Von Willebrand disease is a genetic bleeding disorder caused by a deficiency of von Willebrand factor.",
        "causes": ["Inherited genetic mutation affecting clotting protein"],
        "remedies": ["Desmopressin (DDAVP)", "Clotting factor replacement therapy", "Avoid blood-thinning medications"]
    },
    "zollinger_ellison_syndrome": {
        "description": "Zollinger-Ellison syndrome is a rare condition where tumors cause the stomach to produce excessive acid.",
        "causes": ["Gastrin-secreting tumors (gastrinomas)", "Genetic factors such as MEN1 syndrome"],
        "remedies": ["Proton pump inhibitors", "Surgical removal of tumors", "Regular monitoring"]
    },
    "whipple_disease": {
        "description": "Whipple disease is a rare bacterial infection that affects the small intestine.",
        "causes": ["Tropheryma whipplei bacteria"],
        "remedies": ["Long-term antibiotic therapy", "Regular medical monitoring"]
    },
    "yellow_nail_syndrome": {
        "description": "Yellow nail syndrome is characterized by yellow, thickened nails and respiratory or lymphatic problems.",
        "causes": ["Lymphatic dysfunction", "Chronic respiratory disease", "Unknown factors"],
        "remedies": ["Treat underlying respiratory issues", "Vitamin E supplementation", "Symptomatic management"]
    },
    "xeroderma_pigmentosum": {
        "description": "Xeroderma pigmentosum is a rare genetic disorder making the skin extremely sensitive to UV light.",
        "causes": ["Inherited DNA repair defect", "Genetic mutation"],
        "remedies": ["Strict sun protection", "Regular skin examinations", "Protective clothing and sunscreen"]
    },
    "yaws": {
        "description": "Yaws is a chronic bacterial infection affecting the skin, bones, and joints, mainly in tropical regions.",
        "causes": ["Treponema pallidum pertenue bacteria", "Direct skin contact with an infected person"],
        "remedies": ["Single-dose antibiotic treatment", "Maintain personal hygiene", "Early medical care"]
    },
    "zoonotic_infection": {
        "description": "Zoonotic infection is a disease transmitted from animals to humans.",
        "causes": ["Contact with infected animals", "Animal bites", "Contaminated animal products"],
        "remedies": ["Proper hygiene", "Vaccination when available", "Antibiotics or antivirals depending on cause"]
    },
    "xerostomia": {
        "description": "Xerostomia is a condition characterized by dry mouth due to reduced saliva production.",
        "causes": ["Dehydration", "Medication side effects", "Salivary gland disorders"],
        "remedies": ["Stay hydrated", "Sugar-free lozenges", "Saliva substitutes", "Treat underlying cause"]
    },
    "borderline_personality_disorder": {
        "description": "Borderline personality disorder is a mental health condition affecting mood and relationships.",
        "causes": ["Genetic factors", "Childhood trauma"],
        "remedies": ["Psychotherapy", "Medication"]
    },
    "narcissistic_personality_disorder": {
        "description": "Narcissistic personality disorder involves inflated self-importance.",
        "causes": ["Environmental and genetic factors"],
        "remedies": ["Psychotherapy"]
    },
    "antisocial_personality_disorder": {
        "description": "Antisocial personality disorder involves disregard for others.",
        "causes": ["Genetic predisposition", "Childhood environment"],
        "remedies": ["Therapy"]
    },
    "paranoid_personality_disorder": {
        "description": "Paranoid personality disorder causes distrust of others.",
        "causes": ["Genetic and environmental factors"],
        "remedies": ["Psychotherapy"]
    },
    "schizoid_personality_disorder": {
        "description": "Schizoid personality disorder involves detachment from social relationships.",
        "causes": ["Genetic factors"],
        "remedies": ["Therapy"]
    },
    "avoidant_personality_disorder": {
        "description": "Avoidant personality disorder involves social inhibition.",
        "causes": ["Low self-esteem", "Genetics"],
        "remedies": ["Cognitive behavioral therapy"]
    },
    "dependent_personality_disorder": {
        "description": "Dependent personality disorder involves excessive need for care.",
        "causes": ["Childhood experiences"],
        "remedies": ["Psychotherapy"]
    },
    "histrionic_personality_disorder": {
        "description": "Histrionic personality disorder involves excessive emotionality.",
        "causes": ["Environmental factors"],
        "remedies": ["Therapy"]
    },
    "dissociative_identity_disorder": {
        "description": "Dissociative identity disorder involves multiple personality states.",
        "causes": ["Severe trauma"],
        "remedies": ["Long-term psychotherapy"]
    },
    "dissociative_amnesia": {
        "description": "Dissociative amnesia involves memory loss due to stress.",
        "causes": ["Psychological trauma"],
        "remedies": ["Psychotherapy"]
    },
    "conversion_disorder": {
        "description": "Conversion disorder presents neurological symptoms without medical cause.",
        "causes": ["Psychological stress"],
        "remedies": ["Therapy"]
    },
    "somatic_symptom_disorder": {
        "description": "Somatic symptom disorder causes excessive focus on physical symptoms.",
        "causes": ["Psychological factors"],
        "remedies": ["Cognitive therapy"]
    },
    "illness_anxiety_disorder": {
        "description": "Illness anxiety disorder involves fear of serious illness.",
        "causes": ["Anxiety disorders"],
        "remedies": ["Therapy"]
    },
    "hoarding_disorder": {
        "description": "Hoarding disorder involves difficulty discarding possessions.",
        "causes": ["Anxiety-related factors"],
        "remedies": ["Behavioral therapy"]
    },
    "trichotillomania": {
        "description": "Trichotillomania involves compulsive hair pulling.",
        "causes": ["Stress", "Genetic predisposition"],
        "remedies": ["Behavior therapy"]
    },
    "kleptomania": {
        "description": "Kleptomania is an impulse control disorder causing stealing.",
        "causes": ["Impulse regulation issues"],
        "remedies": ["Therapy"]
    },
    "pyromania": {
        "description": "Pyromania involves compulsive fire setting.",
        "causes": ["Impulse control disorder"],
        "remedies": ["Psychotherapy"]
    },
    "oppositional_defiant_disorder": {
        "description": "ODD involves defiant and hostile behavior in children.",
        "causes": ["Genetic and environmental factors"],
        "remedies": ["Behavior therapy"]
    },
    "conduct_disorder": {
        "description": "Conduct disorder involves serious behavioral issues in youth.",
        "causes": ["Environmental and genetic factors"],
        "remedies": ["Therapy"]
    },
    "intermittent_explosive_disorder": {
        "description": "Intermittent explosive disorder causes sudden anger outbursts.",
        "causes": ["Impulse control issues"],
        "remedies": ["Therapy", "Medication"]
    },
    "delirium": {
        "description": "Delirium is sudden confusion due to illness or medication.",
        "causes": ["Infection", "Drug effects"],
        "remedies": ["Treat underlying cause"]
    },
    "mild_cognitive_impairment": {
        "description": "Mild cognitive impairment is slight but noticeable decline in cognition.",
        "causes": ["Aging", "Early dementia"],
        "remedies": ["Cognitive exercises"]
    },
    "frontotemporal_dementia": {
        "description": "Frontotemporal dementia affects personality and behavior.",
        "causes": ["Neurodegeneration"],
        "remedies": ["Supportive care"]
    },
    "vascular_dementia": {
        "description": "Vascular dementia is cognitive decline from reduced brain blood flow.",
        "causes": ["Stroke", "Vascular disease"],
        "remedies": ["Manage risk factors"]
    },
    "lewy_body_dementia": {
        "description": "Lewy body dementia involves abnormal brain protein deposits.",
        "causes": ["Neurodegeneration"],
        "remedies": ["Medication"]
    },
    "heat_exhaustion": {
        "description": "Heat exhaustion is heat-related illness causing weakness.",
        "causes": ["Prolonged heat exposure"],
        "remedies": ["Cooling", "Hydration"]
    },
    "altitude_pulmonary_edema": {
        "description": "Altitude pulmonary edema causes fluid in lungs at high altitude.",
        "causes": ["High altitude exposure"],
        "remedies": ["Descend altitude", "Oxygen therapy"]
    },
    "altitude_cerebral_edema": {
        "description": "Altitude cerebral edema causes brain swelling at high altitude.",
        "causes": ["Rapid ascent"],
        "remedies": ["Immediate descent", "Medical care"]
    },
    "motion_induced_vertigo": {
        "description": "Motion-induced vertigo causes dizziness during movement.",
        "causes": ["Inner ear imbalance"],
        "remedies": ["Medication", "Vestibular therapy"]
    },
    "benign_paroxysmal_positional_vertigo": {
        "description": "BPPV causes brief episodes of dizziness.",
        "causes": ["Inner ear crystals displacement"],
        "remedies": ["Epley maneuver"]
    },
    "labral_tear": {
        "description": "Labral tear is injury to shoulder or hip cartilage.",
        "causes": ["Trauma", "Overuse"],
        "remedies": ["Physical therapy", "Surgery"]
    },
    "shin_splints": {
        "description": "Shin splints cause pain along shin bone.",
        "causes": ["Overuse"],
        "remedies": ["Rest", "Ice"]
    },
    "stress_fracture": {
        "description": "Stress fracture is small crack in bone from overuse.",
        "causes": ["Repetitive stress"],
        "remedies": ["Rest"]
    },
    "compartment_syndrome": {
        "description": "Compartment syndrome is increased pressure in muscle compartments.",
        "causes": ["Trauma"],
        "remedies": ["Emergency surgery"]
    },
    "rhabdomyolysis": {
        "description": "Rhabdomyolysis is muscle breakdown releasing toxins into blood.",
        "causes": ["Severe injury", "Overexertion"],
        "remedies": ["IV fluids"]
    },
    "anaphylaxis": {
        "description": "Anaphylaxis is severe allergic reaction.",
        "causes": ["Food allergy", "Insect sting"],
        "remedies": ["Epinephrine injection"]
    },
    "urticaria": {
        "description": "Urticaria is hives causing itchy skin welts.",
        "causes": ["Allergic reaction"],
        "remedies": ["Antihistamines"]
    },
    "angioedema": {
        "description": "Angioedema is swelling beneath skin surface.",
        "causes": ["Allergic reaction"],
        "remedies": ["Antihistamines", "Epinephrine"]
    },
    "neurofibromatosis": {
        "description": "Neurofibromatosis is a genetic disorder causing tumors on nerve tissue.",
        "causes": ["Inherited genetic mutation"],
        "remedies": ["Monitoring", "Surgical removal if needed"]
    },
    "myocardial_infarction": {
        "description": "Myocardial infarction (heart attack) occurs when blood flow to the heart is blocked.",
        "causes": ["Coronary artery blockage", "Blood clot"],
        "remedies": ["Emergency medical care", "Medications", "Surgery"]
    },
    "hypertrophic_cardiomyopathy": {
        "description": "Hypertrophic cardiomyopathy is thickening of the heart muscle.",
        "causes": ["Genetic mutation"],
        "remedies": ["Medications", "Surgical procedures"]
    },
    "dilated_cardiomyopathy": {
        "description": "Dilated cardiomyopathy causes enlargement of the heart chambers.",
        "causes": ["Genetics", "Alcohol abuse"],
        "remedies": ["Medications", "Heart transplant in severe cases"]
    },
    "restrictive_cardiomyopathy": {
        "description": "Restrictive cardiomyopathy reduces heart flexibility.",
        "causes": ["Amyloidosis", "Scar tissue"],
        "remedies": ["Medications", "Treat underlying cause"]
    },
    "thoracic_aneurysm": {
        "description": "Thoracic aneurysm is abnormal bulging in chest aorta.",
        "causes": ["High blood pressure", "Atherosclerosis"],
        "remedies": ["Surgical repair"]
    },
    "abdominal_aortic_aneurysm": {
        "description": "Abdominal aortic aneurysm is enlargement of lower aorta.",
        "causes": ["Smoking", "High blood pressure"],
        "remedies": ["Surgery"]
    },
    "mitral_valve_prolapse": {
        "description": "Mitral valve prolapse occurs when valve bulges backward.",
        "causes": ["Connective tissue disorder"],
        "remedies": ["Monitoring", "Surgery if severe"]
    },
    "aortic_stenosis": {
        "description": "Aortic stenosis is narrowing of aortic valve.",
        "causes": ["Aging", "Congenital defect"],
        "remedies": ["Valve replacement"]
    },
    "mitral_regurgitation": {
        "description": "Mitral regurgitation is leakage of blood backward in heart.",
        "causes": ["Valve damage"],
        "remedies": ["Surgery"]
    },
    "rheumatoid_arthritis": {
        "description": "Rheumatoid arthritis is autoimmune joint inflammation.",
        "causes": ["Immune system attack"],
        "remedies": ["Immunosuppressants", "Physical therapy"]
    },
    "juvenile_arthritis": {
        "description": "Juvenile arthritis affects children's joints.",
        "causes": ["Autoimmune factors"],
        "remedies": ["Medication", "Therapy"]
    },
    "ankle_sprain": {
        "description": "Ankle sprain is ligament injury in ankle.",
        "causes": ["Twisting injury"],
        "remedies": ["Rest", "Ice", "Compression"]
    },
    "patellar_tendinitis": {
        "description": "Patellar tendinitis causes knee pain.",
        "causes": ["Overuse injury"],
        "remedies": ["Rest", "Physiotherapy"]
    },
    "meniscus_tear": {
        "description": "Meniscus tear is knee cartilage injury.",
        "causes": ["Sudden twisting"],
        "remedies": ["Rest", "Surgery if severe"]
    },
    "degenerative_disc_disease": {
        "description": "Degenerative disc disease affects spinal discs.",
        "causes": ["Aging"],
        "remedies": ["Physical therapy", "Pain relief"]
    },
    "herniated_disc": {
        "description": "Herniated disc occurs when spinal disc bulges.",
        "causes": ["Spinal strain"],
        "remedies": ["Physiotherapy", "Surgery if severe"]
    },
    "spinal_stenosis": {
        "description": "Spinal stenosis is narrowing of spinal canal.",
        "causes": ["Arthritis"],
        "remedies": ["Medication", "Surgery"]
    },
    "osteogenesis_imperfecta": {
        "description": "Osteogenesis imperfecta causes brittle bones.",
        "causes": ["Genetic mutation"],
        "remedies": ["Supportive care"]
    },
    "paget_disease_of_bone": {
        "description": "Paget disease disrupts bone remodeling.",
        "causes": ["Genetic factors"],
        "remedies": ["Medication"]
    },
    "costochondritis": {
        "description": "Costochondritis is inflammation of chest cartilage.",
        "causes": ["Injury", "Infection"],
        "remedies": ["Pain relievers"]
    },
    "thalassemia_minor": {
        "description": "Thalassemia minor is mild inherited blood disorder.",
        "causes": ["Genetic mutation"],
        "remedies": ["Monitoring"]
    },
    "iron_deficiency_anemia": {
        "description": "Iron deficiency anemia results from low iron levels.",
        "causes": ["Poor diet", "Blood loss"],
        "remedies": ["Iron supplements"]
    },
    "pernicious_anemia": {
        "description": "Pernicious anemia is vitamin B12 deficiency anemia.",
        "causes": ["Autoimmune disorder"],
        "remedies": ["Vitamin B12 injections"]
    },
    "hemolytic_anemia": {
        "description": "Hemolytic anemia is destruction of red blood cells.",
        "causes": ["Autoimmune disease"],
        "remedies": ["Medication"]
    },
    "thrombocytopenia": {
        "description": "Thrombocytopenia is low platelet count.",
        "causes": ["Bone marrow disorders"],
        "remedies": ["Treat underlying cause"]
    },
    "hyperparathyroidism": {
        "description": "Hyperparathyroidism causes excess parathyroid hormone.",
        "causes": ["Parathyroid tumor"],
        "remedies": ["Surgery"]
    },
    "hypoparathyroidism": {
        "description": "Hypoparathyroidism is low parathyroid hormone.",
        "causes": ["Surgical removal"],
        "remedies": ["Calcium supplements"]
    },
    "diabetic_neuropathy": {
        "description": "Diabetic neuropathy damages nerves due to diabetes.",
        "causes": ["High blood sugar"],
        "remedies": ["Blood sugar control"]
    },
    "diabetic_retinopathy": {
        "description": "Diabetic retinopathy damages retinal blood vessels.",
        "causes": ["Uncontrolled diabetes"],
        "remedies": ["Laser therapy"]
    },
    "diabetic_nephropathy": {
        "description": "Diabetic nephropathy damages kidneys.",
        "causes": ["Chronic high blood sugar"],
        "remedies": ["Blood sugar control"]
    },
    "methemoglobinemia": {
        "description": "Methemoglobinemia reduces oxygen delivery in blood.",
        "causes": ["Genetic defect", "Drug exposure"],
        "remedies": ["Methylene blue treatment"]
    },
    "gouty_arthritis": {
        "description": "Gouty arthritis causes joint inflammation from uric acid.",
        "causes": ["High uric acid"],
        "remedies": ["Medication", "Diet control"]
    },
    "complex_regional_pain_syndrome": {
        "description": "CRPS causes chronic pain after injury.",
        "causes": ["Nerve dysfunction"],
        "remedies": ["Physical therapy", "Medication"]
    },
    "narcolepsy_type_1": {
        "description": "Narcolepsy type 1 includes sudden muscle weakness.",
        "causes": ["Hypocretin deficiency"],
        "remedies": ["Stimulants"]
    },
    "sleep_paralysis": {
        "description": "Sleep paralysis is temporary inability to move during sleep.",
        "causes": ["Sleep cycle disruption"],
        "remedies": ["Improve sleep hygiene"]
    },
    "jet_lag": {
        "description": "Jet lag is temporary sleep disturbance from travel.",
        "causes": ["Time zone changes"],
        "remedies": ["Gradual schedule adjustment"]
    },
    "seasonal_affective_disorder": {
        "description": "SAD is depression related to seasonal changes.",
        "causes": ["Reduced sunlight"],
        "remedies": ["Light therapy"]
    },
    "claustrophobia": {
        "description": "Claustrophobia is fear of confined spaces.",
        "causes": ["Anxiety disorder"],
        "remedies": ["Therapy"]
    },
    "agoraphobia": {
        "description": "Agoraphobia is fear of open or crowded spaces.",
        "causes": ["Anxiety disorder"],
        "remedies": ["Cognitive behavioral therapy"]
    },
    "social_anxiety_disorder": {
        "description": "Social anxiety disorder causes intense fear of social situations.",
        "causes": ["Psychological factors"],
        "remedies": ["Therapy", "Medication"]
    },
    "tuberous_sclerosis": {
        "description": "Tuberous sclerosis is a genetic disorder causing benign tumors in organs.",
        "causes": ["Genetic mutation"],
        "remedies": ["Medication", "Surgery"]
    },
    "fragile_x_syndrome": {
        "description": "Fragile X syndrome is a genetic condition causing intellectual disability.",
        "causes": ["FMR1 gene mutation"],
        "remedies": ["Supportive therapy"]
    },
    "down_syndrome": {
        "description": "Down syndrome is a genetic disorder caused by extra chromosome 21.",
        "causes": ["Chromosomal abnormality"],
        "remedies": ["Supportive care", "Therapies"]
    },
    "turner_syndrome": {
        "description": "Turner syndrome affects females due to missing X chromosome.",
        "causes": ["Chromosomal abnormality"],
        "remedies": ["Hormone therapy"]
    },
    "klinefelter_syndrome": {
        "description": "Klinefelter syndrome affects males with extra X chromosome.",
        "causes": ["Chromosomal abnormality"],
        "remedies": ["Testosterone therapy"]
    },
    "marfan_syndrome": {
        "description": "Marfan syndrome is a connective tissue disorder.",
        "causes": ["Genetic mutation"],
        "remedies": ["Monitoring", "Surgery if needed"]
    },
    "ehlers_danlos_syndrome": {
        "description": "Ehlers-Danlos syndrome affects connective tissues causing hypermobility.",
        "causes": ["Genetic mutation"],
        "remedies": ["Physical therapy"]
    },
    "phenylketonuria": {
        "description": "Phenylketonuria is a metabolic disorder affecting amino acid breakdown.",
        "causes": ["Inherited enzyme deficiency"],
        "remedies": ["Special diet"]
    },
    "galactosemia": {
        "description": "Galactosemia is inability to process galactose sugar.",
        "causes": ["Genetic enzyme deficiency"],
        "remedies": ["Avoid dairy products"]
    },
    "tay_sachs_disease": {
        "description": "Tay-Sachs is genetic disorder destroying nerve cells.",
        "causes": ["Inherited mutation"],
        "remedies": ["Supportive care"]
    },
    "gaucher_disease": {
        "description": "Gaucher disease is inherited disorder affecting fat metabolism.",
        "causes": ["Genetic mutation"],
        "remedies": ["Enzyme replacement therapy"]
    },
    "pompe_disease": {
        "description": "Pompe disease is genetic disorder affecting muscle function.",
        "causes": ["Enzyme deficiency"],
        "remedies": ["Enzyme replacement therapy"]
    },
    "cystic_fibrosis": {
        "description": "Cystic fibrosis affects lungs and digestive system.",
        "causes": ["Inherited gene mutation"],
        "remedies": ["Respiratory therapy", "Medication"]
    },
    "primary_ciliary_dyskinesia": {
        "description": "Primary ciliary dyskinesia affects respiratory tract clearance.",
        "causes": ["Genetic mutation"],
        "remedies": ["Airway clearance therapy"]
    },
    "alpha_1_antitrypsin_deficiency": {
        "description": "Genetic disorder affecting lungs and liver.",
        "causes": ["Inherited mutation"],
        "remedies": ["Augmentation therapy"]
    },
    "goodpasture_syndrome": {
        "description": "Autoimmune disorder affecting lungs and kidneys.",
        "causes": ["Immune system attack"],
        "remedies": ["Immunosuppressants"]
    },
    "sjogren_syndrome": {
        "description": "Autoimmune disease causing dry eyes and mouth.",
        "causes": ["Immune dysfunction"],
        "remedies": ["Artificial tears", "Medication"]
    },
    "hashimoto_thyroiditis": {
        "description": "Autoimmune disease causing hypothyroidism.",
        "causes": ["Immune system attack on thyroid"],
        "remedies": ["Thyroid hormone replacement"]
    },
    "graves_disease": {
        "description": "Autoimmune disease causing hyperthyroidism.",
        "causes": ["Immune system stimulation of thyroid"],
        "remedies": ["Medication", "Radioactive iodine"]
    },
    "idiopathic_thrombocytopenic_purpura": {
        "description": "ITP is immune disorder lowering platelet count.",
        "causes": ["Autoimmune destruction of platelets"],
        "remedies": ["Steroids", "Immunotherapy"]
    },
    "aplastic_anemia": {
        "description": "Aplastic anemia is bone marrow failure.",
        "causes": ["Autoimmune factors", "Radiation"],
        "remedies": ["Transfusions", "Bone marrow transplant"]
    },
    "polycythemia_vera": {
        "description": "Polycythemia vera causes excess red blood cell production.",
        "causes": ["Bone marrow disorder"],
        "remedies": ["Phlebotomy", "Medication"]
    },
    "essential_thrombocythemia": {
        "description": "Essential thrombocythemia increases platelet production.",
        "causes": ["Bone marrow mutation"],
        "remedies": ["Medication"]
    },
    "myelofibrosis": {
        "description": "Myelofibrosis is bone marrow scarring disorder.",
        "causes": ["Genetic mutation"],
        "remedies": ["Medication", "Transplant"]
    },
    "amyloidosis": {
        "description": "Amyloidosis is buildup of abnormal protein in organs.",
        "causes": ["Protein misfolding"],
        "remedies": ["Chemotherapy", "Supportive care"]
    },
    "churg_strauss_syndrome": {
        "description": "Autoimmune disorder causing blood vessel inflammation.",
        "causes": ["Immune dysfunction"],
        "remedies": ["Steroids"]
    },
    "wegener_granulomatosis": {
        "description": "Autoimmune vasculitis affecting respiratory tract.",
        "causes": ["Immune system attack"],
        "remedies": ["Immunosuppressants"]
    },
    "takayasu_arteritis": {
        "description": "Inflammation of large arteries.",
        "causes": ["Autoimmune disorder"],
        "remedies": ["Steroids"]
    },
    "bechets_disease": {
        "description": "Behcet disease causes blood vessel inflammation.",
        "causes": ["Immune system dysfunction"],
        "remedies": ["Immunosuppressants"]
    },
    "dermatomyositis": {
        "description": "Dermatomyositis causes muscle weakness and skin rash.",
        "causes": ["Autoimmune disorder"],
        "remedies": ["Steroids", "Immunotherapy"]
    },
    "polymyositis": {
        "description": "Polymyositis is inflammatory muscle disease.",
        "causes": ["Autoimmune response"],
        "remedies": ["Steroids"]
    },
    "myocarditis": {
        "description": "Myocarditis is inflammation of heart muscle.",
        "causes": ["Viral infection"],
        "remedies": ["Medication", "Rest"]
    },
    "pericarditis": {
        "description": "Pericarditis is inflammation of heart lining.",
        "causes": ["Viral infection"],
        "remedies": ["Anti-inflammatory drugs"]
    },
    "endocarditis": {
        "description": "Endocarditis is infection of heart valves.",
        "causes": ["Bacterial infection"],
        "remedies": ["IV antibiotics"]
    },
    "pulmonary_embolism": {
        "description": "Pulmonary embolism is blockage in lung artery.",
        "causes": ["Blood clot"],
        "remedies": ["Blood thinners"]
    },
    "coarctation_of_aorta": {
        "description": "Congenital narrowing of the aorta.",
        "causes": ["Birth defect"],
        "remedies": ["Surgery"]
    },
    "tetralogy_of_fallot": {
        "description": "Congenital heart defect with four abnormalities.",
        "causes": ["Developmental defect"],
        "remedies": ["Surgery"]
    },
    "ventricular_septal_defect": {
        "description": "Hole in heart's ventricular wall.",
        "causes": ["Congenital defect"],
        "remedies": ["Surgery if severe"]
    },
    "atrial_septal_defect": {
        "description": "Hole in heart's atrial wall.",
        "causes": ["Congenital defect"],
        "remedies": ["Surgical repair"]
    },
    "actinomycosis": {
        "description": "Actinomycosis is a rare bacterial infection causing abscess formation.",
        "causes": ["Actinomyces bacteria"],
        "remedies": ["Long-term antibiotics"]
    },
    "brucellosis": {
        "description": "Brucellosis is a bacterial infection transmitted from animals.",
        "causes": ["Unpasteurized dairy", "Animal contact"],
        "remedies": ["Antibiotics"]
    },
    "campylobacteriosis": {
        "description": "Campylobacteriosis is intestinal infection causing diarrhea.",
        "causes": ["Contaminated poultry"],
        "remedies": ["Hydration", "Antibiotics if severe"]
    },
    "cryptosporidiosis": {
        "description": "Cryptosporidiosis is parasitic infection causing diarrhea.",
        "causes": ["Contaminated water"],
        "remedies": ["Hydration"]
    },
    "giardiasis": {
        "description": "Giardiasis is intestinal infection by Giardia parasite.",
        "causes": ["Contaminated water"],
        "remedies": ["Antiparasitic medication"]
    },
    "trichomoniasis": {
        "description": "Trichomoniasis is sexually transmitted parasitic infection.",
        "causes": ["Trichomonas vaginalis"],
        "remedies": ["Antibiotics"]
    },
    "toxoplasmosis": {
        "description": "Toxoplasmosis is parasitic infection from contaminated food or cats.",
        "causes": ["Toxoplasma parasite"],
        "remedies": ["Antiparasitic drugs"]
    },
    "ascariasis": {
        "description": "Ascariasis is roundworm infection of intestines.",
        "causes": ["Poor sanitation"],
        "remedies": ["Anthelmintic medication"]
    },
    "hookworm_infection": {
        "description": "Hookworm infection causes anemia and weakness.",
        "causes": ["Contact with contaminated soil"],
        "remedies": ["Anthelmintic drugs"]
    },
    "tapeworm_infection": {
        "description": "Tapeworm infection is intestinal parasitic disease.",
        "causes": ["Undercooked meat"],
        "remedies": ["Antiparasitic medication"]
    },
    "strongyloidiasis": {
        "description": "Strongyloidiasis is parasitic infection affecting intestines.",
        "causes": ["Soil exposure"],
        "remedies": ["Anthelmintic medication"]
    },
    "filariasis": {
        "description": "Filariasis is parasitic disease causing lymphatic swelling.",
        "causes": ["Mosquito bites"],
        "remedies": ["Antiparasitic drugs"]
    },
    "onchocerciasis": {
        "description": "Onchocerciasis causes skin and eye disease.",
        "causes": ["Blackfly bites"],
        "remedies": ["Ivermectin"]
    },
    "leishmaniasis": {
        "description": "Leishmaniasis is parasitic disease affecting skin or organs.",
        "causes": ["Sandfly bites"],
        "remedies": ["Antiparasitic treatment"]
    },
    "chagas_disease": {
        "description": "Chagas disease affects heart and digestive system.",
        "causes": ["Kissing bug bite"],
        "remedies": ["Antiparasitic drugs"]
    },
    "babesiosis": {
        "description": "Babesiosis is tick-borne infection affecting red blood cells.",
        "causes": ["Tick bite"],
        "remedies": ["Antiparasitic medication"]
    },
    "histoplasmosis": {
        "description": "Histoplasmosis is fungal lung infection.",
        "causes": ["Bird or bat droppings"],
        "remedies": ["Antifungal medication"]
    },
    "candidiasis": {
        "description": "Candidiasis is fungal infection caused by Candida.",
        "causes": ["Immune suppression"],
        "remedies": ["Antifungal drugs"]
    },
    "aspergillosis": {
        "description": "Aspergillosis is fungal infection affecting lungs.",
        "causes": ["Inhalation of spores"],
        "remedies": ["Antifungal therapy"]
    },
    "mucormycosis": {
        "description": "Mucormycosis is serious fungal infection.",
        "causes": ["Fungal spores in immunocompromised individuals"],
        "remedies": ["Antifungal medication", "Surgery"]
    },
    "rhinovirus_infection": {
        "description": "Rhinovirus infection causes common cold symptoms.",
        "causes": ["Viral transmission"],
        "remedies": ["Rest", "Hydration"]
    },
    "adenovirus_infection": {
        "description": "Adenovirus infection causes respiratory illness.",
        "causes": ["Viral exposure"],
        "remedies": ["Supportive care"]
    },
    "norovirus": {
        "description": "Norovirus causes acute gastroenteritis.",
        "causes": ["Contaminated food"],
        "remedies": ["Hydration"]
    },
    "rotavirus": {
        "description": "Rotavirus causes severe diarrhea in children.",
        "causes": ["Viral infection"],
        "remedies": ["ORS", "Vaccination prevention"]
    },
    "respiratory_syncytial_virus": {
        "description": "RSV causes respiratory infections in infants.",
        "causes": ["Viral transmission"],
        "remedies": ["Supportive care"]
    },
    "avian_influenza": {
        "description": "Avian influenza is bird flu infection in humans.",
        "causes": ["Contact with infected birds"],
        "remedies": ["Antiviral medication"]
    },
    "swine_flu": {
        "description": "Swine flu is influenza A H1N1 infection.",
        "causes": ["Viral infection"],
        "remedies": ["Antiviral drugs"]
    },
    "hand_dermatitis": {
        "description": "Hand dermatitis causes itchy inflamed skin.",
        "causes": ["Irritants", "Allergens"],
        "remedies": ["Moisturizers", "Topical steroids"]
    },
    "seborrheic_dermatitis": {
        "description": "Seborrheic dermatitis causes flaky scalp and skin.",
        "causes": ["Fungal overgrowth"],
        "remedies": ["Medicated shampoo"]
    },
    "dandruff": {
        "description": "Dandruff causes flaky scalp.",
        "causes": ["Seborrheic dermatitis"],
        "remedies": ["Anti-dandruff shampoo"]
    },
    "hidradenitis_suppurativa": {
        "description": "Hidradenitis causes painful skin lumps.",
        "causes": ["Blocked hair follicles"],
        "remedies": ["Medication", "Surgery"]
    },
    "rosacea": {
        "description": "Rosacea causes facial redness and bumps.",
        "causes": ["Unknown triggers"],
        "remedies": ["Topical medication"]
    },
    "keratosis_pilaris": {
        "description": "Keratosis pilaris causes small rough bumps on skin.",
        "causes": ["Keratin buildup"],
        "remedies": ["Moisturizers"]
    },
    "lichen_planus": {
        "description": "Lichen planus is inflammatory skin condition.",
        "causes": ["Autoimmune factors"],
        "remedies": ["Steroid creams"]
    },
    "lichen_sclerosus": {
        "description": "Lichen sclerosus causes white skin patches.",
        "causes": ["Autoimmune disorder"],
        "remedies": ["Topical steroids"]
    },
    "pityriasis_rosea": {
        "description": "Pityriasis rosea is temporary skin rash.",
        "causes": ["Possible viral trigger"],
        "remedies": ["Symptomatic relief"]
    },
    "erythema_nodosum": {
        "description": "Erythema nodosum causes red painful nodules.",
        "causes": ["Infection", "Autoimmune disorders"],
        "remedies": ["Treat underlying cause"]
    },
    "alopecia_areata": {
        "description": "Alopecia areata is autoimmune hair loss.",
        "causes": ["Immune attack on hair follicles"],
        "remedies": ["Steroid injections"]
    },
    "contact_dermatitis": {
        "description": "Contact dermatitis is skin irritation from substances.",
        "causes": ["Allergens", "Irritants"],
        "remedies": ["Avoid trigger", "Topical steroids"]
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
    },
    "trigeminal_neuralgia": {
        "description": "Trigeminal neuralgia is a chronic pain condition affecting the facial nerve.",
        "causes": ["Nerve compression", "Multiple sclerosis"],
        "remedies": ["Anticonvulsant medication", "Surgery"]
    },
    "guillain_barre_syndrome": {
        "description": "Guillain-Barre syndrome is an autoimmune disorder causing muscle weakness.",
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
    },
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
    },
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
    },
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
        "causes": ["Graves disease", "Thyroid nodules"],
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
        "description": "Kidney stones are hard mineral deposits in the kidneys.",
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
        "description": "Pneumonia is an infection that inflames the lungs air sacs.",
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
        "description": "Measles is a highly contagious viral infection causing fever, rash, and cough.",
        "causes": ["Measles virus", "Exposure to infected droplets"],
        "remedies": ["Vitamin A supplements", "Hydration", "Fever reducers"]
    },
    "chickenpox": {
        "description": "Chickenpox is a viral infection causing an itchy rash with fluid-filled blisters.",
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
    user_input = user_input.lower().strip()

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

    # Check for conditions in the database
    for condition, info in medical_db.items():
        # Match both underscore and spaced versions
        if condition in user_input or condition.replace("_", " ") in user_input:
            response = f"About {condition.replace('_', ' ').title()}:\n"
            response += f"Description: {info['description']}\n"
            response += f"Possible causes: {', '.join(info['causes'])}\n"
            response += f"Suggested remedies: {', '.join(info['remedies'])}\n"
            response += "Note: If symptoms persist or worsen, please consult a doctor."
            return response

    # Default response if no matches found
    return ("I'm sorry, I couldn't find information on that condition. "
            "Please try a specific condition name such as 'headache', 'diabetes', or 'fever'. "
            "For medical concerns, please consult a healthcare professional.")


def main():
    print("MediBot: Hello! I'm a simple medical chatbot providing general health information.")
    print("Type 'bye' to exit at any time.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in farewells:
            print("MediBot:", get_response(user_input))
            break
        response = get_response(user_input)
        print("MediBot:", response)
        print()


if __name__ == "__main__":
    main()