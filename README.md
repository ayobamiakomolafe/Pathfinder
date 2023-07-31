# Pathfinder

The translation of available antimicrobial resistance (AMR) surveillance data to observe trends and evolving patterns of microbial resistance to antimicrobial agents while forecasting and identifying regions at high risk of resistant cases and also serving as a decision support tool is an aspect of AMR surveillance and interpretation that is sparsely explored nationwide and uncommon on a global scale (Dewar et al., 2021). We aim to provide revolutionary insights that can inform targeted interventions, guide antimicrobial stewardship efforts nationally, promote appropriate antibiotic use and reduce the risk of resistance development.
Our objectives are:
1.	To analyze the Antimicrobial Testing Leadership and Surveillance (ATLAS) dataset and observe evolving global spatiotemporal patterns of AMR and AMR percentage, visualise the minimum inhibitory concentrations (MICs) as distribution plots to understand resistance level of different antibiotics, and portray a choropleth map to reveal real-time resistant pattern across different geolocations (Pfizer, 2023).
2.	To develop a workflow that integrates local AMR gene resources to identify functional AMR determinant genes and antibiotic classes from query organism genome.
3.	To develop a decision support tool that assists healthcare providers in making evidence-based conclusions regarding genomic susceptibility status and antibiotic selection.
4.	To integrate a conversational AI component that can interpret the decision support output, and provide insights concerning the significance of specific resistance patterns for a patient’s query condition (Bahrini et al., 2023).
5.	To develop and deploy an interactive web app to access this application (the ‘PATHFINDER’ app).


How to Run The App:
1. The App run on the web app interface via this link:
ALTERNATIVELY TO RUN LOCALLY
1. Download all files in the repository
2. Install Dependencies found in the requirements and packages file
3. The code runs on both python and R so make sure both languages are installed on your device
4. DOwnload Zipped Atlas dataset
5. Use the "Clean Atlas" Function found on the function.py file to unzip and clean the atlas file
6. Replace input dataset in dashboard.py with the csv output from "Clean Atlas"   Function ran above
7. RUn dashboard.py
