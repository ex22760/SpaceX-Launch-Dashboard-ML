# SpaceX Launch Success Prediction & Dashboard 

A complete end-to-end data science project focused on analysing and predicting SpaceX Falcon 9 rocket launch success. Includes data collection, SQL querying, preprocessing, EDA, machine learning, and an interactive dashboard built with Folium and Plotly Dash.

---

## Project Overview

This project was developed as part of the IBM Data Science Professional Certificate capstone. It explores historical launch data to identify trends, evaluate success rates, and build a predictive model to classify future launch outcomes.

---

## Tech Stack

- **Languages**: Python, SQL
- **Libraries**: Pandas, NumPy, Scikit-learn, Plotly, Folium, Dash, Seaborn, Matplotlib
- **Tools**: Jupyter Notebook, IBM Cloud, Git/GitHub

---

## Workflow

1. **Data Collection**  
   - Launch data obtained via API and CSV
   - SQL used to query IBM DB2 warehouse

2. **Data Wrangling & Cleaning**  
   - Removed nulls and filtered for Falcon 9 launches
   - Converted categorical features and engineered new ones

3. **Exploratory Data Analysis (EDA)**  
   - Analyzed launch sites, payload ranges, and booster versions  
   - Visualized patterns using histograms, scatter plots, and maps

4. **Machine Learning**  
   - Compared SVM, Decision Trees, KNN, and Logistic Regression  
   - Evaluated models using accuracy, precision, and confusion matrix  
   - SVM achieved highest accuracy: **83.3%**

5. **Interactive Dashboard**  
   - **Folium** used to map global launch sites  
   - **Plotly Dash** app to visualize success rates by payload, site, and booster version

---

## Results

- CCAFS LC-40 had the most launches (46.4%)
- KSC LC-39A was the most reliable site (76.9% success rate)
- Payloads of 2500–7000 kg showed highest success rates
- Dash app enables dynamic filtering and data exploration

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/ex22760/spacex-launch-dashboard-ml.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the dashboard locally:
```bash
python app.py
```
---

## Screenshots

![Dashboard-Overview1](https://github.com/user-attachments/assets/8a8873df-a164-43c7-98fb-db4e3cc7d259)
![Dashboard-Overview2](https://github.com/user-attachments/assets/690e8948-7638-4450-86dd-aaf2e74df77c)
![image](https://github.com/user-attachments/assets/1acf9b59-c5c4-4e8b-be5f-9494aab4c8de)
![image](https://github.com/user-attachments/assets/6bf3c4e2-50ee-4ec8-a203-c9fdf7cacec5)

---

## Folder Structure

├── Datasets/               # Cleaned and raw datasets for the notebooks
├── notebooks/              # Jupyter Notebooks for Data Collection, Wrangling, EDA, ML
├── Dashboard/              # Dash app files
├── ds-capstone.pptx        # Final Presentation (Results and Analysis)
├── requirements.txt
├── README.md

---

## Acknowledgements

Developed as part of the [IBM Data Science Certificate capstone]((https://www.coursera.org/professional-certificates/ibm-data-science?utm_medium=sem&utm_source=gg&utm_campaign=b2c_emea_multi_ibm_ftcof_multi_cx_dr_bau_gg_sem_pr_gb_en_m_hyb_25-04_x&campaignid=22465908183&adgroupid=176821228725&device=c&keyword=ibm%20data%20science%20professional%20certificate&matchtype=e&network=g&devicemodel=&creativeid=747841919499&assetgroupid=&targetid=kwd-652307688950&extensionid=&placement=&gad_source=1&gad_campaignid=22465908183&gbraid=0AAAAADdKX6Ygr8LzanRz_BKD5CQSiIqBj&gclid=CjwKCAjwuIbBBhBvEiwAsNypvdJl4BBIfaCRHuc2Wg_9tut_QDXTTspID8kfQ8CFtn-toGkJ92mK6BoCOncQAvD_BwE)) project.

![image](https://github.com/user-attachments/assets/ce5d99c5-fb81-4c24-a0a6-8aecb1630401)

---

## Contact

**Sujin Subanthran**
[LinkedIn Profile](https://www.linkedin.com/in/sujin-subanthran-b44512226/)
