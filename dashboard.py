# Import Libraries
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from functions import *
import requests
from io import StringIO
import os
os.environ['R_HOME'] = 'C:\Program Files\R\R-4.2.2'
import shutil
import rpy2.robjects as robjects
import streamlit as st

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

#Import cleaned dataset
atlas=pd.read_csv('atlas.csv', low_memory=False)
#More data preprocessing
atlas['Antibiotics'] = atlas['Antibiotics'].fillna('Unknown')
atlas['Country'] = atlas['Country'].fillna('Unknown')
atlas.rename(columns = {'COncentration':'Concentration'},inplace=True)

Species__=['Pseudomonas aeruginosa', 'Serratia marcescens',
       'Acinetobacter pitii', 'Acinetobacter baumannii',
       'Enterobacter cloacae', 'Escherichia coli',
       'Haemophilus influenzae', 'Staphylococcus aureus',
       'Enterococcus faecium', 'Enterococcus faecalis',
       'Streptococcus agalactiae', 'Klebsiella pneumoniae',
       'Klebsiella aerogenes', 'Acinetobacter junii',
       'Klebsiella oxytoca', 'Enterobacter kobei',
       'Streptococcus pneumoniae', 'Acinetobacter, non-speciated',
       'Acinetobacter lwoffii', 'Serratia liquefaciens',
       'Enterobacter asburiae', 'Citrobacter freundii',
       'Serratia fonticola', 'Serratia rubidaea',
       'Acinetobacter schindleri', 'Acinetobacter guillouiae',
       'Clostridium perfringens', 'Clostridioides difficile',
       'Clostridium tertium', 'Clostridium butyricum',
       'Clostridium hathewayi', 'Clostridium barati',
       'Bacteroides fragilis', 'Parabacteroides distasonis',
       'Bacteroides nordii', 'Prevotella denticola',
       'Bacteroides vulgatus', 'Bacteroides thetaiotaomicron',
       'Bacteroides uniformis', 'Prevotella buccae', 'Prevotella oris',
       'Prevotella bivia', 'Peptostreptococcus anaerobius',
       'Stenotrophomonas maltophilia', 'Lelliottia amnigena',
       'Acinetobacter calcoaceticus', 'Acinetobacter nosocomialis',
       'Enterococcus, non-speciated', 'Pluralibacter gergoviae',
       'Acinetobacter radioresistens', 'Acinetobacter johnsonii',
       'Enterococcus avium', 'Staphylococcus haemolyticus',
       'Acinetobacter ursingii', 'Acinetobacter haemolyticus',
       'Enterococcus raffinosus', 'Staphylococcus epidermidis',
       'Enterococcus casseliflavus', 'Enterococcus hirae',
       'Serratia odorifera', 'Enterococcus gallinarum',
       'Staphylococcus hominis', 'Staphylococcus lugdunensis',
       'Staphylococcus simulans', 'Proteus vulgaris',
       'Citrobacter koseri', 'Morganella morganii',
       'Providencia stuartii', 'Streptococcus bovis',
       'Streptococcus pyogenes', 'Proteus mirabilis',
       'Staphylococcus saprophyticus', 'Streptococcus constellatus',
       'Haemophilus parainfluenzae', 'Streptococcus dysgalactiae',
       'Streptococcus anginosus', 'Streptococcus gallolyticus',
       'Streptococcus sanguinis', 'Staphylococcus warneri',
       'Aeromonas caviae', 'Citrobacter braakii', 'Enterobacter ludwigii',
       'Acinetobacter parvus', 'Acinetobacter tjernbergiae',
       'Klebsiella, non-speciated', 'Serratia, non-speciated',
       'Serratia ficaria', 'Enterobacter, non-speciated',
       'Klebsiella ozaenae', 'Peptostreptococcus magnus',
       'Parvimonas micra', 'Anaerococcus tetradius',
       'Prevotella loescheii', 'Bacteroides ovatus',
       'Clostridium clostridiiformis', 'Prevotella oralis',
       'Clostridium subterminale', 'Prevotella intermedia',
       'Clostridium ramosum', 'Bacteroides caccae',
       'Campylobacter ureolyticus', 'Clostridium paraputrificum',
       'Anaerococcus prevotii', 'Clostridium limosum',
       'Streptococcus castoreus', 'Providencia rettgeri',
       'Staphylococcus capitis', 'Citrobacter farmeri',
       'Enterobacter cancerogenus', 'Pseudomonas putida',
       'Citrobacter gillenii', 'Citrobacter murliniae',
       'Klebsiella variicola', 'Haemophilus parahaemolyticus',
       'Streptococcus, viridans group', 'Serratia ureilytica',
       'Streptococcus oralis', 'Acinetobacter baylyi',
       'Enterobacter agglomerans', 'Pseudomonas nitroreducens',
       'Citrobacter sedlakii', 'Prevotella buccalis',
       'Peptostreptococcus hydrogenalis', 'Bacteroides salersyae',
       'Bacteroides massiliensis', 'Prevotella nanceinsis',
       'Prevotella nigrescens', 'Parabacteroides goldsteinii',
       'Anaerococcus lactolyticus', 'Peptoniphilus harei',
       'Prevotella melaninogenica', 'Clostridium aldenense',
       'Prevotella disiens', 'Clostridium citroniae',
       'Peptoniphilus gorbachii', 'Clostridium innocuum',
       'Clostridium scindens', 'Streptococcus salivarius',
       'Raoultella ornithinolytica', 'Raoultella planticola',
       'Enterococcus durans', 'Staphylococcus cohnii',
       'Clostridium septicum', 'Clostridium sporogenes',
       'Clostridium sordellii', 'Enterobacter sakazakii',
       'Staphylococcus sciuri', 'Serratia plymuthica', 'Hafnia alvei',
       'Clostridium celerecrescens', 'Anaerococcus hydrogenalis',
       'Anaerococcus vaginalis', 'Bacteroides pyogenes',
       'Prevotella baroniae', 'Bacteroides intestinalis',
       'Prevotella histicola', 'Anaerococcus murdochii',
       'Clostridium symbiosum', 'Bacteroides stercosis',
       'Peptoniphilus indolicus', 'Prevotella spp', 'Prevotella pallens',
       'Prevotella bergensis', 'Prevotella salivae',
       'Prevotella maculosa', 'Citrobacter amalonaticus',
       'Citrobacter, non-speciated', 'Staphylococcus caprae',
       'Neisseria gonorrhoeae', 'Proteus penneri', 'Streptococcus mitis',
       'Pseudomonas monteilii', 'Proteus hauseri',
       'Streptococcus intermedius', 'Staphylococcus pseudointermedius',
       'Pantoea agglomerans', 'Pseudomonas stutzeri', 'Anaerococcus spp',
       'Clostridium sphenoides', 'Parabacteroides johnsonii',
       'Staphylococcus schleiferi', 'Clostridium cadaveris',
       'Staphylococcus auricularis', 'Providencia alcalifaciens',
       'Streptococcus parasanguinis', 'Enterobacter hormaechi',
       'Escherichia hermanii', 'Providencia, non-speciated',
       'Raoultella terrigena', 'Burkholderia cepacia',
       'Streptococcus sanguis', 'Staphylococcus pasteuri',
       'Staphylococcus Coagulase Negative', 'Serratia grimesii',
       'Acinetobacter towneri', 'Streptococcus suis',
       'Staphylococcus xylosus', 'Pseudomonas alcaliphila',
       'Klebsiella ornithinolytica', 'Proteus rettgeri',
       'Peptoniphilus spp', 'Clostridium spp', 'Clostridium bifermentans',
       'Pseudomonas otitidis', 'Bacteroides spp', 'Clostridium bolteae',
       'Anaerococcus octavius', 'Prevotella corporis',
       'Clostridium disporicum', 'Clostridium histolyticum',
       'Clostridium beijerinckii', 'Clostridium glycolicum',
       'Prevotella oulorum', 'Clostridium cochlearium',
       'Staphylococcus intermedius', 'Enterobacter intermedium',
       'Klebsiella planticola', 'Burkholderia cenocepacia',
       'Bacteroides coagulans', 'Bacteroides cellulosilyticus',
       'Prevotella heparinolytica', 'Acinetobacter anitratus',
       'Cronobacter sakazakii', 'Streptococcus canis',
       'Staphylococcus pettenkoferi', 'Pseudomonas mendocina',
       'Aeromonas hydrophila', 'Pantoea septica',
       'Streptococcus lutetiensis', 'Citrobacter youngae',
       'Peptostreptococcus spp', 'Finegoldia magna', 'Aeromonas veronii',
       'Pseudomonas mosselii', 'Bacteroides faecis', 'Kluyvera ascorbata',
       'Enterobacter taylorae', 'Prevotella timonensis',
       'Peptoniphilus olsenii', 'Bacteroides eggerthii',
       'Prevotella veroralis', 'Enterobacter gergoviae',
       'Peptoniphilus lacrimalis', 'Prevotella amnii',
       'Enterococcus mundtii', 'Streptococcus massiliensis',
       'Clostridium colicanis', 'Acinetobacter bereziniae',
       'Staphylococcus spp', 'Aeromonas spp', 'Proteus spp',
       'Escherichia vulneris', 'Acinetobacter dijkshoorniae',
       'Pantoea dispersa', 'Pseudomonas pseudoalcaligenes',
       'Citrobacter diversus', 'Pseudomonas spp',
       'Streptococcus, Beta Hemolytic', 'Achromobacter xylosoxidans',
       'Acinetobacter seifertii', 'Staphylococcus argenteus',
       'Pseudomonas alcaligenes', 'Pseudomonas citronellolis',
       'Staphylococcus condimenti', 'Pantoea spp', 'Salmonella spp',
       'Enterobacter bugandensis', 'Acinetobacter beijerinckii',
       'Klebsiella spp', 'Acinetobacter spp', 'Enterobacter spp',
       'Citrobacter spp', 'Providencia spp',
       'Enterobacter xiangfangensis', 'Acinetobacter courvalinii',
       'Pseudomonas putida/fluorescens Group', 'Bordetella trematum',
       'Myroides odoratimimus', 'Achromobacter insolitus',
       'Acinetobacter proteolyticus', 'Staphylococcus arlettae',
       'Pseudomonas fulva', 'Staphylococcus saccharolyticus',
       'Ochrobactrum anthropi', 'Staphylococcus petrasii',
       'Alcaligenes faecalis', 'Cronobacter spp',
       'Pseudomonas guariconensis', 'Acinetobacter tandoii',
       'Bordetella spp', 'Providencia rustigianii',
       'Pseudomonas graminis', 'Acinetobacter dispersus',
       'Acidaminococcus fermentans', 'Enterococcus canintestini',
       'Enterococcus Group D', 'Serratia spp', 'Enterococcus spp',
       'Haemophilus spp', 'Peptoniphilus coxii', 'Escherichia spp',
       'Acinetobacter soli', 'Acinetobacter lactucae',
       'Acinetobacter colistiniresistens', 'Acinetobacter variabilis',
       'Paeniclostridium sordelli', 'Paraclostridium bifermentans',
       'Bacteroides capsillosis', 'Clostridium novyia',
       'Bacteroides bivius', 'Peptoniphilus asaccharolyticus',
       'Bacteroides merdeae', 'Prevotella tannerae',
       'Clostridium hastiforme', 'Fusobacterium nucleatum',
       'Anaerovorax spp', 'Clostridium scatalogenes',
       'Clostridium putrificum', 'Enterobacter liquifaciens',
       'Enterococcus flavescens', 'Eubacterium lentum',
       'Peptostreptococcus lactolyticus', 'Bacteroides dorei',
       'Prevotella multiformis', 'Bacteroides splanchnicus',
       'Peptostreptococcus indolicus', 'Eubacterium aerofaciens',
       'Veillonella parvula', 'Acinetobacter alcaligenes',
       'Clostridium rectum', 'Peptostreptococcus tetradius',
       'Klebsiella rhinoscleromatis', 'Streptococcus equi',
       'Haemophilus pittmaniae', 'Staphylococcus vitulinus',
       'Escherichia fergusonii', 'Staphylococcus hyicus',
       'Streptococcus gordonii', 'Pseudomonas fluorescens',
       'Enterococcus malodoratus', 'Pseudomonas stewartii']

Family__=['Non-Enterobacteriaceae', 'Enterobacteriaceae', 'Haemophilus spp',
       'Staphylococcus spp', 'Enterococcus spp',
       'Streptococcus spp (no S. pneumo)', 'Streptococcus pneumoniae',
       'Gram Positive Anaerobes', 'Gram Negative Anaerobes',
       'Neisseria gonorrhoeae']

Country__=['France', 'Spain', 'Belgium', 'Italy', 'Germany', 'Canada',
       'United States', 'Ireland', 'Portugal', 'Israel', 'Greece',
       'China', 'United Kingdom', 'Kuwait', 'Poland', 'Switzerland',
       'Hungary', 'Austria', 'Colombia', 'Chile', 'Finland', 'Australia',
       'Mexico', 'Denmark', 'Sweden', 'Hong Kong', 'Japan', 'Croatia',
       'Malaysia', 'Nigeria', 'Kenya', 'Czech Republic', 'Netherlands',
       'Russia', 'Romania', 'Venezuela', 'Thailand', 'Philippines',
       'Turkey', 'Korea, South', 'South Africa', 'Argentina', 'Taiwan',
       'Brazil', 'Panama', 'Jordan', 'Saudi Arabia', 'Pakistan',
       'Guatemala', 'Morocco', 'India', 'Singapore', 'Vietnam', 'Latvia',
       'Lithuania', 'Serbia', 'Dominican Republic', 'Costa Rica',
       'Ukraine', 'Lebanon', 'New Zealand', 'Qatar', 'Jamaica',
       'Ivory Coast', 'Cameroon', 'Slovenia', 'Norway', 'Honduras',
       'Puerto Rico', 'Nicaragua', 'Slovak Republic', 'Oman', 'Uganda',
       'Ghana', 'Malawi', 'Namibia', 'Indonesia', 'Bulgaria', 'Mauritius',
       'Estonia', 'El Salvador', 'Tunisia', 'Egypt']
Gender__=['Female', 'Male']
Age_Group__=  ['85 and Over', '13 to 18 Years', '65 to 84 Years',
       '19 to 64 Years', 'Unknown', '0 to 2 Years', '3 to 12 Years']

Speciality__=['Emergency Room', 'Nursing Home / Rehab', 'Medicine General',
       'Medicine ICU', 'Surgery General', 'None Given',
       'Pediatric General', 'Pediatric ICU', 'Clinic / Office',
       'Surgery ICU', 'General Unspecified ICU', 'Other']

Source__=['Urine', 'Ear', 'Skin', 'Blood', 'Bronchus', 'Sputum',
       'Peritoneal Fluid', 'Bone', 'Wound', 'Placenta', 'Gastric Abscess',
       'Stomach', 'Vagina', 'Lungs', 'Nose', 'Catheters', 'Exudate',
       'Throat', 'CNS: Other', 'Peripheral Nerves', 'Eye', 'Decubitus',
       'Ulcer', 'Synovial Fluid', 'Genitourinary: Other', 'Tissue Fluid',
       'Respiratory: Other', 'Trachea', 'Drains', 'Rectum', 'Bile',
       'Feces/Stool', 'Skin: Other', 'Bodily Fluids', 'Lymph Nodes',
       'Spinal Cord', 'Abdominal Fluid', 'None Given', 'Pleural Fluid',
       'Aspirate', 'Kidney', 'Instruments: Other', 'HEENT: Other',
       'Intestinal: Other', 'Mouth', 'Penis', 'Thoracentesis Fluid',
       'Pancreas', 'Gall Bladder', 'CSF', 'Head', 'Muscle', 'Urethra',
       'Liver', 'Brain', 'Burn', 'Nails', 'Bone Marrow',
       'Respiratory: Sinuses', 'Heart', 'Colon', 'Skeletal: Other',
       'Endotracheal aspirate', 'Bladder', 'Abscess',
       'Bronchoalveolar lavage', 'Circulatory: Other', 'Ureter',
       'Appendix', 'Impetiginous lesions', 'Furuncle', 'Carbuncle',
       'Prostate', 'Uterus', 'Integumentary (Skin Nail Hair)',
       'Cellulitis', 'Blood Vessels', 'Diverticulum', 'Fallopian Tubes',
       'Vas Deferens', 'Spleen', 'Ovary', 'Cervix', 'Lymphatic Fluid',
       'Testis', 'Hair', 'Esophagus', 'Vomit', 'Thymus',
       'Nasopharyngeal Aspirate', 'Transtracheal Aspirate',
       'Paracentesis Fluid', 'Ascetic Fluid', 'Nasotracheal Aspirate',
       'Bronchiole', 'Ileum', 'Pyoderma Lesion']

Patient__=['Other', 'Inpatient', 'Outpatient']

Antibiotics__=['Amikacin', 'Cefepime', 'Ceftazidime', 'Levofloxacin', 'Meropenem',
       'Piperacillin tazobactam', 'Amoxycillin clavulanate', 'Ampicillin',
       'Ceftriaxone', 'Minocycline', 'Tigecycline', 'Linezolid',
       'Vancomycin', 'Penicillin', 'Azithromycin', 'Clarithromycin',
       'Clindamycin', 'Erythromycin', 'Metronidazole', 'Cefoxitin',
       'Imipenem', 'Aztreonam', 'Ceftaroline', 'Ceftazidime avibactam',
       'Doripenem', 'Ertapenem', 'Daptomycin', 'Moxifloxacin',
       'Oxacillin', 'Teicoplanin', 'Ampicillin sulbactam',
       'Quinupristin dalfopristin', 'Colistin', 'Gentamicin',
       'Trimethoprim sulfa', 'Cefixime', 'Ciprofloxacin', 'Tetracycline',
       'Ceftolozane tazobactam', 'Meropenem vaborbactam']

antibiotics_groups = {
    'Amikacin': 'Aminoglycosides', 
    'Cefepime': 'Cephalosporins', 
    'Ceftazidime': 'Cephalosporins', 
    'Levofloxacin': 'Fluoroquinolones', 
    'Meropenem': 'Carbapenems',
    'Piperacillin tazobactam': 'Penicillins', 
    'Amoxycillin clavulanate': 'Penicillins', 
    'Ampicillin': 'Penicillins',
    'Ceftriaxone': 'Cephalosporins', 
    'Minocycline': 'Tetracycline', 
    'Tigecycline': 'Tetracycline', 
    'Linezolid': 'Oxazolidinones',
    'Vancomycin': 'Glycopeptides', 
    'Penicillin': 'Penicillins', 
    'Azithromycin': 'Macrolides', 
    'Clarithromycin': 'Macrolides',
    'Clindamycin': 'Lincosamide', 
    'Erythromycin': 'Macrolides', 
    'Metronidazole': 'Nitroimidazole', 
    'Cefoxitin': 'Cephalosporins',
    'Imipenem': 'Carbapenems', 
    'Ceftaroline': 'Cephalosporins', 
    'Ceftazidime avibactam': 'Cephalosporins',
    'Doripenem': 'Carbapenems', 
    'Ertapenem': 'Carbapenems', 
    'Moxifloxacin': 'Fluoroquinolones',
    'Oxacillin': 'Penicillins', 
    'Teicoplanin': 'Glycopeptides',
    'Ampicillin sulbactam':'Penicillins', 
    'Colistin': 'Colistin', 
    'Gentamicin': 'Aminoglycosides',
    'Cefixime': 'Cephalosporins', 
    'Ciprofloxacin': 'Fluoroquinolones', 
    'Tetracycline': 'Tetracycline',
    'Ceftolozane tazobactam': 'Cephalosporins', 
    'Meropenem vaborbactam': 'Carbapenems',
    'Aztreonam': "Monobactams (Aztreonam)", 
    'Daptomycin': 'Cyclic lipopeptides (Daptomycin)', 
    'Trimethoprim sulfa': 'Sulfonamides (Cotrimoxazole)',
    'Quinupristin dalfopristin': 'Streptogramin (Quinupristin dalfopristin)',
}

source_to_infection = {
    'Urine': 'Urinary Tract Infections (UTIs)',
    'Ear': 'Ear Infections',
    'Skin': 'Skin Infections',
    'Blood': 'Blood Infections',
    'Bronchus': 'Respiratory Infections',
    'Sputum': 'Respiratory Infections',
    'Lungs': 'Respiratory Infections',
    'Trachea': 'Respiratory Infections',
    'Respiratory: Other': 'Respiratory Infections',
    'Bronchiole': 'Respiratory Infections',
    'Endotracheal aspirate': 'Respiratory Infections',
    'Nasopharyngeal Aspirate': 'Respiratory Infections',
    'Transtracheal Aspirate': 'Respiratory Infections',
    'Nasotracheal Aspirate': 'Respiratory Infections',
    'Bronchoalveolar lavage': 'Respiratory Infections',
    'Brain': 'Central Nervous System (CNS) Infections',
    'Spinal Cord': 'Central Nervous System (CNS) Infections',
    'CSF': 'Central Nervous System (CNS) Infections',
    'Heart': 'Cardiovascular Infections',
    'Kidney': 'Urinary Tract Infections (UTIs)',
    'Bladder': 'Urinary Tract Infections (UTIs)',
    'Ureter': 'Urinary Tract Infections (UTIs)',
    'Urethra': 'Urinary Tract Infections (UTIs)',
    'Stomach': 'Intra-abdominal Infections',
    'Gastric Abscess': 'Intra-abdominal Infections',
    'Peritoneal Fluid': 'Intra-abdominal Infections',
    'Abdominal Fluid': 'Intra-abdominal Infections',
    'Pancreas': 'Intra-abdominal Infections',
    'Gall Bladder': 'Intra-abdominal Infections',
    'Liver': 'Intra-abdominal Infections',
    'Spleen': 'Intra-abdominal Infections',
    'Colon': 'Intra-abdominal Infections',
    'Wound': 'Soft Tissue Infections',
    'Decubitus': 'Soft Tissue Infections',
    'Ulcer': 'Soft Tissue Infections',
    'Cellulitis': 'Soft Tissue Infections',
    'Pyoderma Lesion': 'Soft Tissue Infections',
    'Genitourinary Infections': 'Genitourinary Infections',
}


# Define Selection box
add_selectbox = st.sidebar.selectbox(
    "Pages",
    ("About PATHFINDER", "Interactive Dashboard", "Decision Support Tool", "AST Predictor")
)

# Home Page
if add_selectbox=='About PATHFINDER':
    st.markdown("""
    <style>
    .big-font {
        font-size:80px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    # Page Description
    st.title('Predictive Analysis of AMR Trends For Healthcare Decision Making And Forecasting (PATHFINDER)')

    st.title('What is PATHFINDER?')

    st.markdown('PATHFINDER is a two-tiered interactive dashboard application capable of presenting evolving \
                patterns of microbial resistance to antimicrobial agents while serving as a decision-support tool \
                that assists healthcare providers in making evidence-based conclusions regarding genomic susceptibility \
                status and antibiotic selection.')
    st.divider()

    st.title("PATHFINDER's Functionality")
    st.markdown('The PATHFINDER interactive dashboard presents global antimicrobial resistance (AMR) data from the \
                ATLAS surveillance dataset using interactive visualisations. Comprehensive antibiotics class, \
                bacterial species, country, and year profiles for the data were provided to filter by. Dashboards \
                are optimised for quick-run use on the web.')
    st.image("image1.png")
    st.caption("A choropleth map revealing real-time resistant pattern across different geolocations")
    st.divider()
    st.markdown('The PATHFINDER decision support tool presents a web-based, open BLAST (Basic Local Alignment Search Tool) \
                pipeline for comparing query nucleotide sequences with a curated database of antimicrobial-resistant gene determinants \
                and identifying pre-defined AMR-encoding genes in bacterial proteins. Result interpretation is made available \
                with the aid of a conversational AI assistant.')
    st.image("image2.png")
    st.caption("A BLAST run of a query genome to identify possible pre-defined AMR genes")
    
# Dashboard Page    
elif add_selectbox =="Interactive Dashboard":
    
    st.markdown("""
    <style>
    .big-font {
        font-size:80px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title('PATHFINDER Interactive Dashboard')
    st.divider()
    
    cont1=st.container()
    cont2=st.container()
    cont3=st.container()

    # Define input features for AMR Distribution and Spatiotemporal Trend widgets
    st.sidebar.subheader("AMR Distribution and Spatiotemporal Trend")
    Country = st.sidebar.selectbox('Country', atlas['Country'].unique() )
    Species = st.sidebar.selectbox('Specie', atlas['Species'].unique() )
    Antibiotics = st.sidebar.selectbox('Antibiotics', atlas['Antibiotics'].unique() )
    Year = st.sidebar.slider('Year', min_value=2004, max_value=2021, step= 1, value=2013 )
    
    # Define input features for AMR Percentage Trend widgets
    st.sidebar.write('\n\n')
    st.sidebar.subheader("AMR Percentage Trend")
    Countries_3 = st.sidebar.selectbox('Country_', atlas['Country'].unique() )
    Speciess_3= st.sidebar.selectbox('Specie_', atlas['Species'].unique() )
    Antibioticss_3 = st.sidebar.multiselect('Antibioticss', antibiotics_groups.keys(), default=['Amikacin'] )
    source_to_infection=list( source_to_infection.values() )
    source_to_infection=[*set(source_to_infection)]
    source_to_infection.append('All')
    Infection= st.sidebar.selectbox('Infections', source_to_infection)

    # Define input features for Comparative Antibiotic classes distribution widgets
    st.sidebar.write('\n\n')
    st.sidebar.subheader("Comparative Antibiotic classes distribution")
    Countries = st.sidebar.multiselect('Countries', atlas['Country'].unique(), default=['France', 'Spain', 'Belgium', 'Italy'] )
    Speciess = st.sidebar.selectbox('Species', atlas['Species'].unique() )
    Antibiotics_groups = st.sidebar.multiselect('Antibiotics Group', antibiotics_groups.keys(), default=['Amikacin'] )
    Years = st.sidebar.slider('Years', min_value=2004, max_value=2021, step= 1, value=2013 )
    Infection_= st.sidebar.selectbox('Infections_', source_to_infection)
    





 
    

    
    # Making and displaying plots to streamlit using functions on functions.py script
    with cont1:
        st.subheader('AMR Distribution and Spatiotemporal Trend')
        tab1, tab2, tab3 = st.tabs(["Susceptilibilty Status", "MIC Distribution", "Spatiotemporal Map"])
        with tab1:
            fig_status=status(atlas, Country, Year, Antibiotics, Species)
            st.plotly_chart(fig_status, theme="streamlit", use_container_width=True)
            
        with tab2:
            fig_MIC_distribution= MIC_distribution(atlas, Country, Year, Antibiotics, Species)
            st.plotly_chart(fig_MIC_distribution, theme="streamlit", use_container_width=True)

        with tab3:
            fig_world_map=world_map(atlas, Species, Year, Antibiotics)
            st.plotly_chart(fig_world_map, theme="streamlit", use_container_width=True)
            

    with cont2:
            st.subheader('AMR Percentage Trend')
            fig_AMR_trend=AMR_trend(atlas, Antibioticss_3, Infection, Speciess_3, Countries_3)
            st.plotly_chart(fig_AMR_trend, theme="streamlit", use_container_width=True)
       
            

            

    with cont3:
            st.subheader('Comparative Antibiotic classes distribution')
            fig_percentage_resistance_plots=percentage_resistance_plots(atlas, Speciess, Years, Antibiotics_groups, Infection_, Countries)
            st.plotly_chart(fig_percentage_resistance_plots, theme="streamlit", use_container_width=True)
            

            


# Decision Support page
elif add_selectbox =="Decision Support Tool":
    st.title('PATHFINDER Decision Support Tool')
    # Page Description
    st.markdown("The PATHFINDER decision support tool runs a BLAST (Basic Local Alignment Search Tool) pipeline \
                and compares uploaded nucleotide sequences (.fasta, .fsa) with a curated database of \
                antimicrobial-resistant gene determinants, and identifies pre-defined AMR-encoding genes in uploaded sequence.") 
    st.markdown("Result interpretation is also made available with the aid of our conversational AI assistant.")
    st.divider()
    # Input Organism name
    organism = st.text_input('Organism')
    # Input fasta file to blast
    uploaded_file = st.file_uploader("Upload fasta file", type = "fasta")

     # Load and blast fasta file
    if uploaded_file is not None:
        query=uploaded_file.name
        #implement R script gotten from the r_blast.txt file to run blaster a tool for blasting
        f1 = open('r_blast.txt', 'r')
        f2 = open('file2.txt', 'w')
        for line in f1:
            f2.write(line.replace("query2", query))
        f1.close()
        f2.close()
        shutil.copy2('file2.txt', 'file2.R')

        # run blaster with output result put into dataframe
        with open("file2.R", 'r') as file: 
            r_script_code = file.read()
        with st.spinner('Loading BLAST Result...'):
            result = robjects.r(r_script_code)
            df=pd.read_csv('blast_table.csv')
            df=df[['TargetId','Identity', 'NumMatches', 'NumMismatches', 'NumGaps']]
            df1=pd.read_csv('phenotypes.csv')
            df=df.merge(df1, left_on='TargetId', right_on='gene_name', how='inner').dropna(axis=1, how='all')
        st.header('BLAST Result')
        st.write(df)
        dico=str( df.to_dict('tight') )


       # Chat GPT function to get query response
        import openai
        openai.api_key = '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'
        def get_completion(prompt, model="gpt-3.5-turbo"):
          messages = [{"role": "user", "content": prompt}]
          response = openai.ChatCompletion.create(
          model=model,
          messages=messages,
          temperature=0)
          return response.choices[0].message["content"]
        # send dataframe result from blaster to Chat GPT for interpretation
        if df.empty:
            st.subheader('No Result Returned')
        else:
            # Getting responses from Chat GPT
            with st.spinner('Loading Result Interpretation...'):
                prompt = "Description: \
                You are provided with an analysis of " + organism +" resistance to certain antibiotics. Your task is to examine the data and perform the following: \
                Describe the Antibiotic Classes and List the Antibiotics: \
                Identify the antibiotic classes to which the organism shows resistance and list the specific antibiotics within each class. \
                Present your findings in a clear and organized format. \
                List Alternative Antibiotics that the organism should be suceptible to: \
                Identify and list antibiotics that are not mentioned in the provided table but could potentially be effective against the resistant organism. \
                Include a reasonable number of alternatives that could serve as potential treatment options. \
                Instructions: \
                Please carefully review the table with the information on the organism's antibiotic resistance. \
                Categorize the antibiotics based on their respective classes and create a concise summary. \
                After analysing the resistance data, research and suggest alternative antibiotics that are \
                not included in the table but could be considered as potential treatment options. \
                Note: The objective is to explore alternative antibiotics for potential treatment; therefore, \
                consider the organism's resistance patterns and make informed recommendations. \
                Note: If no resistance results/antibiotics were found, output: 'No Antimicrobial resistant genes found'" +  dico
                response = get_completion(prompt)
            st.header('Result Interpretation By Chat GPT')
            st.write(response)
        
        
    
elif add_selectbox=='AST Predictor': 
    st.title('Antimicrobial Susceptibility Test Predictor')
    with st.form("my_form"):
        Gender_=st.selectbox('Gender',Gender__)
        Age_Group_=st.selectbox('Age_Group', Age_Group__)
        Country_= st.selectbox('Country', Country__)
        Year_=st.number_input('Year', min_value=2000, step=1, value=2010)
        Speciality_=st.selectbox('Speciality', Speciality__)
        Patient_=st.selectbox('Patient', Patient__)
        Source_=st.selectbox('Source',Source__)
        Family_=st.selectbox('Family', Family__)
        Species_=st.selectbox('Species', Species__)
        Antibiotics_=st.selectbox('Antibiotics',Antibiotics__)


        submitted = st.form_submit_button("Make Prediction")
        if submitted:
            import pickle
            scalerfile = 'Dependencies/Patient.pkl'
            scaler = pickle.load(open(scalerfile, 'rb'))
            Patient= scaler.transform([Patient_])
            Patient=Patient[0]

            scalerfile = 'Dependencies/Speciality.pkl'
            scaler = pickle.load(open(scalerfile, 'rb'))
            Speciality= scaler.transform([Speciality_])
            Speciality=Speciality[0]

            scalerfile = 'Dependencies/Age Group.pkl'
            scaler = pickle.load(open(scalerfile, 'rb'))
            Age_Group= scaler.transform([Age_Group_])
            Age_Group=Age_Group[0]

            scalerfile = 'Dependencies/Gender.pkl'
            scaler = pickle.load(open(scalerfile, 'rb'))
            Gender_= scaler.transform([Gender_])
            Gender=Gender_[0]

            scalerfile = 'Dependencies/Source.pkl'
            scaler = pickle.load(open(scalerfile, 'rb'))
            Source_= scaler.transform([Source_])
            Source=Source_[0]

            scalerfile = 'Dependencies/Family.pkl'
            scaler = pickle.load(open(scalerfile, 'rb'))
            Family= scaler.transform([Family_])
            Family=Family[0]

            scalerfile = 'Dependencies/Species.pkl'
            scaler = pickle.load(open(scalerfile, 'rb'))
            Species_= scaler.transform([Species_])
            Species=Species_[0]

            scalerfile = 'Dependencies/Antibiotics.pkl'
            scaler = pickle.load(open(scalerfile, 'rb'))
            Antibiotics_= scaler.transform([Antibiotics_])
            Antibiotics=Antibiotics_[0]

            scalerfile = 'Dependencies/Country.pkl'
            scaler = pickle.load(open(scalerfile, 'rb'))
            Country_= scaler.transform([Country_])
            Country=Country_[0]

            X=[Species, Family, Country, Gender, Age_Group, Speciality,Source, Patient, Year_, Antibiotics]



            import lightgbm
            model = lightgbm.Booster(model_file='Dependencies/lgbr_base.txt')
            df=model.predict([X])
            fig = px.pie(values=df[0],names=['Susceptible', 'Resistant', 'Intermediate'], title='Result')
            st.plotly_chart(fig, use_container_width=True)   
           

    
from streamlit.web import cli as stcli
from streamlit import runtime
import sys

if __name__ == '__main__':
    if runtime.exists():
        pass
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())

