# Import libraries
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


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

# Function to Clean ATLAS Zipped file and save as dataframe (ensure to add .csv extension to save_cleaned_file_path e.g dir/cleaned.csv)
def Clean_ATLAS(zipped_file_path, save_cleaned_file_path):
  from zipfile import ZipFile
  zf=ZipFile(zipped_file_path, 'r')
  zf.extractall()
  zf.close()

  import pandas as pd
  import seaborn as sns
  import matplotlib.pyplot as plt

  df=pd.read_csv('2023_06_15 atlas_antibiotics.csv')

  new_list=[]
  for i in range(df.shape[0]):
    new_list.append(df.loc[i,'Amikacin': 'Meropenem vaborbactam_I'].dropna().to_dict())

  df=df.loc[:, :'Phenotype']
  df['Antibiotics']= new_list

  big_list=[]
  for i in range(df.shape[0]):
    for row in df['Antibiotics'][i].keys():
      if row.endswith('_I'):
        x=row.split('_')[0]
        big_list.append([i, x, df['Antibiotics'][i][row], df['Antibiotics'][i][x] ])

  Antibiotics=pd.DataFrame(big_list)

  clean_df=df.merge(Antibiotics, left_index=True, right_on=0, how='left').drop(['Antibiotics', 0], axis=1).rename(columns={1:"Antibiotics", 2:"Status", 3:"COncentration"})

  clean_df.to_csv(save_cleaned_file_path, sep=',', index=False)

# Function to get status report plot
def status(atlas, country, year, antibiotics, species):
    filtered_atlas = atlas[(atlas['Country'] == country) & (atlas['Year'] == year) & (atlas['Antibiotics'] == antibiotics) & (atlas['Species'] == species)]
    title = species + ' against ' + antibiotics + ', ' + country + ' (' + str(year) + ')'
    fig = px.histogram(filtered_atlas, x='Status', color='Concentration', barmode='stack', title=title)
    return fig

# Function to get percentage_resistance_plots
def percentage_resistance_plots(atlas, species, year, antibiotics_group, infection_type, countries):
    
    selected_antibiotics = antibiotics_group
    selected_countries =  countries
  

    if infection_type == 'All':
        filtered_atlas = atlas[(atlas['Species'] == species) & (atlas['Year'] == year) & (atlas['Antibiotics'].isin(selected_antibiotics)) & (atlas['Country'].isin(selected_countries))]
    else:
        filtered_atlas = atlas[(atlas['Species'] == species) & (atlas['Year'] == year) & (atlas['Antibiotics'].isin(selected_antibiotics)) & (atlas['Country'].isin(selected_countries)) & (atlas['Infection Type'] == infection_type)]

    resistance_atlas = (
        filtered_atlas[filtered_atlas['Status'] == 'Resistant']
        .groupby(['Country', 'Antibiotics'])
        .size() / filtered_atlas.groupby(['Country', 'Antibiotics']).size() * 100
    )
    resistance_atlas = resistance_atlas.reset_index(name='Percentage Resistance')

    resistance_atlas['Antibiotics'] = resistance_atlas['Antibiotics'].map(antibiotics_groups)

    resistance_grouped = resistance_atlas.groupby(['Country', 'Antibiotics'])['Percentage Resistance'].mean().reset_index()
    sorted_groups = sorted(set(resistance_grouped['Antibiotics']))
    resistance_grouped['Antibiotics'] = pd.Categorical(resistance_grouped['Antibiotics'], categories=sorted_groups, ordered=True)

    resistance_grouped.sort_values(by=['Antibiotics'], inplace=True)

    fig = px.bar(
        resistance_grouped,
        x='Antibiotics',
        y='Percentage Resistance',
        color='Country',
        barmode='group',
        title='Average Percentage Resistance by Antibiotics Group and Country',
        category_orders={"Antibiotics": sorted_groups}
    )
    
    

    return fig

# Function to get MIC Distribution plots
def MIC_distribution(atlas, country, year, antibiotics, species):
    filtered_atlas = atlas[(atlas['Country'] == country) & (atlas['Year'] == year) & (atlas['Antibiotics'] == antibiotics) & (atlas['Species'] == species)]
    filtered_atlas = filtered_atlas.sort_values('Concentration')
    title = antibiotics + ' MIC distribution on ' + species + ', ' + country + ' (' + str(year) + ')'
    fig = px.histogram(filtered_atlas, x='Concentration', color='Status', barmode='stack', title=title)
    return fig

# Function to get AMR Trends
def AMR_trend(atlas, antibiotics_groupss, infection_type, species, country):
    atlas['Infection Type'] = atlas['Source'].map(source_to_infection)
    atlas.dropna(subset=['Infection Type'], inplace=True)
    atlas['Antibiotics_']= atlas['Antibiotics'].map(antibiotics_groups)
    selected_antibiotics=antibiotics_groupss
    if infection_type == 'All':
        filtered_atlas = atlas[
            (atlas['Country'] == country) &
            (atlas['Species'] == species)
        ]
    else:
        filtered_atlas = atlas[
            (atlas['Country'] == country) &
            (atlas['Species'] == species) &
            (atlas['Infection Type'] == infection_type)
        ]    # Grouping by year and calculatimg the percentage resistance and total isolates
    resistance_atlas = (
        filtered_atlas.groupby(['Country', 'Year', 'Antibiotics'])
        .agg(
            Percentage_Resistance=('Status', lambda x: (x == 'Resistant').mean() * 100),
            Total_Isolates=('Status', 'count'),
            Resistant_Isolates=('Status', lambda x: (x == 'Resistant').sum())
        )
        .reset_index()
    )
    title = f"Percentage Resistance of {species} to Selected Antibiotics in {country}"

    fig = go.Figure()

    # sorting years in ascending order
    years = sorted(resistance_atlas['Year'].unique())

    # Add traces for each antibiotic
    color_palette = px.colors.qualitative.Plotly
    for i, antibiotic in enumerate(selected_antibiotics):
        data = resistance_atlas[resistance_atlas['Antibiotics'] == antibiotic]

        # Initialize y-values with NaN for all years
        y_values = [None] * len(years)

        # Fill in the y-values for available years
        for year in data['Year']:
            index = years.index(year)
            y_values[index] = data[data['Year'] == year]['Percentage_Resistance'].values[0]

        fig.add_trace(go.Scatter(
            x=years,
            y=y_values,
            mode='lines+markers',
            name=antibiotic,
            line=dict(color=color_palette[i % len(color_palette)]),
            hovertemplate='Year: %{x}<br>Antibiotic: ' + antibiotic + '<br>Percentage Resistance: %{y:.2f}%<br>Total Isolates: %{customdata[0]}<br>Resistant Isolates: %{customdata[1]}<extra></extra>',
            customdata=data[['Total_Isolates', 'Resistant_Isolates']],
        ))

    fig.update_layout(
        title=title,
        xaxis_title='Year',
        yaxis_title='Percentage Resistance',
        legend_title='Antibiotics',
        hovermode='closest',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    # Update x-axis range if there are data points available
    if len(years) > 0:
        fig.update_xaxes(range=[min(years), max(years)])
    return fig


# Function to get World Maps

def world_map(atlas, species, year, antibiotics):
    filtered_atlas = atlas[
        (atlas['Species'] == species) &
        (atlas['Year'] == year) &
        (atlas['Antibiotics'] == antibiotics)
    ]

    total_isolates = filtered_atlas.groupby(['Country']).size().reset_index(name='Total Isolates')
    resistance_atlas = filtered_atlas[filtered_atlas['Status'] == 'Resistant'].groupby(['Country', 'Antibiotics']).size() / filtered_atlas.groupby(['Country', 'Antibiotics']).size() * 100
    resistance_atlas = resistance_atlas.reset_index(name='Percentage Resistance')

    country_data = pd.merge(resistance_atlas, total_isolates, on='Country', how='left')
    country_data['Percentage Resistance'] = country_data['Percentage Resistance'].round(2)

    fig = px.choropleth(
        country_data,
        locations='Country',
        locationmode='country names',
        color='Percentage Resistance',
        hover_name='Country',
        hover_data=['Antibiotics', 'Total Isolates'],
        color_continuous_scale='turbo',
        projection='natural earth',
        title=f'Percentage Resistance of {species} to Antibiotics in {year}',
    )

    fig.update_layout(
        coloraxis_colorbar=dict(title='Resistance Rate (%)'),
        annotations=[
            dict(
                x=0.5,
                y=-0.15,
                text=f"Year = {year}, Antibiotics = {antibiotics}",
                showarrow=False,
                font=dict(size=12)
            )
        ]
    )

    return fig


# Function to get MIC Scatter Plots
def MIC_scatter_plots(atlas, country, species, antibiotics):
    selected_antibiotics=antibiotics
  
    filtered_atlas = atlas[(atlas['Country'] == country) & (atlas['Species'] == species) & (atlas['Antibiotics'].isin(selected_antibiotics))]
    title = f"MIC Comparison for {species} in {country} (All Years)"


    fig = px.scatter(filtered_atlas, x='Antibiotics', y='Concentration', color='Status', title=title)
    fig.update_layout(
        xaxis_title='Antibiotics',
        yaxis_title='MIC <μg/ml>',
        showlegend=True,
        hovermode='closest',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )
    return fig
    
