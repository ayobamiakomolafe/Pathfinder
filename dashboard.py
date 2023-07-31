# Import Libraries
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from functions import *
import requests
from io import StringIO
import shutil
import rpy2.robjects as robjects
import streamlit as st
from annotated_text import annotated_text
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

#Import cleaned dataset
atlas=pd.read_csv('atlas.csv', low_memory=False)
#More data preprocessing
atlas['Antibiotics'] = atlas['Antibiotics'].fillna('Unknown')
atlas['Country'] = atlas['Country'].fillna('Unknown')
atlas.rename(columns = {'COncentration':'Concentration'},inplace=True)

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
    ("About PATHFINDER", "Interactive Dashboard", "Decision Support Tool")
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
    annotated_text(("PATH", "Python"), ("FINDER", "R"))
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
        
        
    
            

    
from streamlit.web import cli as stcli
from streamlit import runtime
import sys

if __name__ == '__main__':
    if runtime.exists():
        pass
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())

