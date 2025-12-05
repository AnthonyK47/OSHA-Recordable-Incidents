### Author

Anthony Konas  
University of Colorado Boulder  
CSPB 4502 - Data Mining

# OSHA Recordable Incidents: An Analysis on State by State Safety Regulations

## Final Project Links

- Final Paper: [Click Here](https://drive.google.com/file/d/1HupHuz4yS_UjRdjURtk2p0S6EZzIQXU3/view?usp=sharing)
- Project Presentation: [Click Here](https://drive.google.com/file/d/1yZ9WhRKRnjjWliTSd1rX4bq9b2qf0pqZ/view?usp=sharing)

## Project Description

This project analyzes workplace safety patterns across the United States using OSHA's Severe Injury Reports dataset from 2015-2025. The goal is to understand how severe workplace injuries vary by state, industry, and time period, and to explore whether geographic location and industry type can help predict where workplace safety efforts should be focused.

As someone working in the Environmental Health and Safety software industry, I wanted to dive deeper into the data behind workplace injuries to better understand the challenges my clients face. This analysis examines nearly 100,000 severe injury reports to identify patterns that could inform safety policy and resource allocation.

## Dataset

- **Source:** OSHA Severe Injury Reports (https://www.osha.gov/severe-injury-reports)
- **Records:** 98,801 severe workplace injuries
- **Time Period:** January 2015 - February 2025 (**Update, as of 12/1/25, it looks like the March data is included now**)
- **Attributes:** 27 fields including geographic coordinates, industry codes (NAICS), injury type, employer information, and detailed incident narratives

## Research Questions & Findings Summary

### Question 1: Do certain states have higher injury rates than others, and what might explain these differences?

**Answer:** Yes, there are significant geographic disparities in severe workplace injuries. The top 5 states by injury count are:
- Texas: 16,234 injuries (16.43%)
- Florida: 10,789 injuries (10.92%)
- Pennsylvania: 7,839 injuries (7.93%)
- Ohio: 7,699 injuries (7.79%)
- Illinois: 5,936 injuries (6.01%)

These five states alone account for nearly half of all severe injuries in the dataset. States with their own OSHA programs (State Plans) tend to show lower rates of injury compared to states who follow just the federal OSHA guidelines. Further analysis with workforce size data would be needed to calculate true injury rates per worker, but it was difficult to find good census data that shows the amount of workers per NAICS code per state.

### Question 2: Which specific industries drive the highest injury rates in different states?

**Answer:** Healthcare facilities consistently rank as the most dangerous industry across multiple states, with NAICS 622110 (General Medical/Surgical Hospitals) recording 1,534 severe injuries nationally. The top 5 industries overall are:
1. General Medical/Surgical Hospitals (622110): 1,534 injuries
2. Supermarkets/Grocery Stores (445110): 1,333 injuries
3. Electrical Contractors (238210): 1,259 injuries
4. Commercial Building Construction (236220): 1,188 injuries
5. Oil and Gas Operations (213112): 1,102 injuries

Industry patterns vary by state. For example, oil and gas operations dominate in Texas, while warehousing is more prominent in Pennsylvania and Ohio. This challenges the common assumption that heavy industrial work is always the most dangerous, as service sectors like healthcare and retail show surprisingly high injury counts.

### Question 3: Are there temporal trends in workplace injuries over the 2015-2025 period?

**Answer:** Yes, there are some clear temporal patterns. Injuries increased from 2015 (9,838) to a peak in 2018 (11,156), then dropped sharply in 2020 (8,915) which was a 19.5% decrease likely due to COVID-19 workplace shutdowns. Since 2020, injury counts have remained relatively stable in the 8,700-9,100 range. Year-over-year analysis reveals:
- 2015-2018: Steady increase (+13.4% overall)
- 2020: Sharp drop (-19.5%) coinciding with pandemic
- 2021-2024: Gradual stabilization around 9,000 injuries per year
- 2025: Incomplete data (only through February)

The data suggests that while pandemic-related workplace closures temporarily reduced severe injuries, rates have not returned to pre-pandemic levels, possibly indicating lasting changes in workplace practices or reporting.



