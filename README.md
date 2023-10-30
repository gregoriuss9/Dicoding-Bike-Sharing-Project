# Dicoding-Bike-Sharing-Project

This repository is used to finish Dicoding certification **"Belajar Analis Data dengan Python"**. The datasets talk about bike rent activites during 2011 and 2012 by Capital Bikeshare which the daatasets consist of 2 file, `hour.csv` and `day.csv` that explain the rent activities hourly and daily, respectively. There is Jupyter Notebook file to analyze the dataset and Python file to deploy the dashboard using streamlit package. 

## Repository Structure
Please understand this structure so you could explore this repo easily
```
├── dashboard
│   ├── dashboard.py
│   └── final_hour_data.csv
├── data
│   ├── day.csv
|   └── hour.csv
├── image
│   ├── 2E-N0B6u_400x400.jpg
|   └── Screenshot 2011_1.png
│   ├── Screenshot 2011_2.png
|   └── Screenshot 2012_1.png
|   └── Screenshot 2012_2.png
├── README.md
├── final_project.ipynb
├── requirements.txt
```
## Analysis Insights
There are several insights obtained from the dataset. They are: 
1. The bike rent trend **has increased generally** by **806473** activites from 2011 to 2012. In same month and day, the bike rent activites increased and the most significant values for month and day is **September** and **17** respectively. Both of 2011 and 2012 show same pattern that peak activities occurs in the **middle of year** and it's related to the season so in the begin and end of year it show low activites.  
2. People prefer to rent bike during the **weekday** instead of weekend/holiday although the activites during the weekday and weekend have no significant difference. This happens because people **might be** awared to use eco-friendly vehicle for their daily routinity and choose **rent a bike as an alternative**.
3. Both of 2011 and 2012 show people pretend to rent bike in **Fall** season which provide clear with few clouds although weather condition is unpredictable. **Clear with flew clouds** is the favourite condition so many people do bike rent activities and this condition show 'best spot' that is **25-32 &deg;C**.
4.  In 2011, **June** show most users to rent bike while in 2012 there is an enhancement and the highest count of bike rent users is in **September**. From July to September it shows a positive trend line in count of bike rent.
5.  The best time to rent bike is at **17 or 5 p.m**. In 2011 **Tuesday** and **Friday** are 2 favourite days to rent bike while in 2012 it's on **Thursday**.
6.  Generally, ratio between casual user to registered user is **1:4**. The number of registered bike rent users increased **1.7%** or about **680960 users** from 2011 to 2012.

## Dashboard Deployment
The dashboard should be deploy globally or locally. Here the picture about the dashboard. 

Here if you select **2011** `year` as time filter.
<p align="center">
  <img src="/image/Screenshot 2011_1.png" />
<p align="center">
  <img src="/image/Screenshot 2011_2.png" />
  
You may choose **2012** as the time filter too.

<p align="center">
  <img src="/image/Screenshot 2012_1.png" />
<p align="center">
  <img src="/image/Screenshot 2012_2.png" />

### Run globally
You may visit ........... to access the online dashboard 

## Run locally
Follow this steps to run the dashboard locally
1. Clone this repository
   ```
   git clone https://github.com/kamandanu9/Dicoding-Bike-Sharing-Project.git
   ```
2. Install the `requirements.txt`
   ```
   pip install -r requirements.txt
   ```
3. Go to **dashboard** directory
     ```
   cd dashboard
   ```
7. Run the `dashboard.py`
     ```
   streamlit run .\dashboard.py
   ```
