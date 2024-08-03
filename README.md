# Pathfinder

The translation of available antimicrobial resistance (AMR) surveillance data to observe trends and evolving patterns of microbial resistance to antimicrobial agents while forecasting and identifying regions at high risk of resistant cases and also serving as a decision support tool is an aspect of AMR surveillance and interpretation that is sparsely explored nationwide and uncommon on a global scale (Dewar et al., 2021). We aim to provide revolutionary insights that can inform targeted interventions, guide antimicrobial stewardship efforts nationally, promote appropriate antibiotic use and reduce the risk of resistance development.
Our objectives are:
1.	To analyze the Antimicrobial Testing Leadership and Surveillance (ATLAS) dataset and observe evolving global spatiotemporal patterns of AMR and AMR percentage, visualise the minimum inhibitory concentrations (MICs) as distribution plots to understand resistance level of different antibiotics, and portray a choropleth map to reveal real-time resistant pattern across different geolocations (Pfizer, 2023).
2.	To develop a workflow that integrates local AMR gene resources to identify functional AMR determinant genes and antibiotic classes from query organism genome.
3.	To develop a decision support tool that assists healthcare providers in making evidence-based conclusions regarding genomic susceptibility status and antibiotic selection.
4.	To integrate a conversational AI component that can interpret the decision support output, and provide insights concerning the significance of specific resistance patterns for a patient’s query condition (Bahrini et al., 2023).
5.	To develop and deploy an interactive web app to access this application (the ‘PATHFINDER’ app).


How to Run the App LOCALLY:
1. Download the repository as a folder.
2. The code requires both python and R to run so make sure both languages are installed on your device.
3. Install Dependencies found in the requirements.txt and packages.txt file.  
4. Download the Zipped Atlas dataset.
5. Use the "Clean Atlas" function found on the function.py file to unzip and clean the atlas dataset downloaded in step 4 above; this returns a dataset in csv which is a cleaned and reformated format of the downloaded dataset in step 4.
6. Replace input dataset in dashboard.py (line 17) with the csv output from running "Clean Atlas" function from step 5 above.
7. Run dashboard.py.
