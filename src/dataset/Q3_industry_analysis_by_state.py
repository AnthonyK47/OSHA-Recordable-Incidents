
import pandas as pd

# Load and clean OSHA data
df = pd.read_csv('src/dataset/January2015toFebruary2025.csv')
df = df.drop_duplicates()
df_clean = df.dropna(subset=['State', 'Primary NAICS'])

print("Total records for analysis:", len(df_clean))
print("\n")

# Get top 10 states by injury count
top_states = df_clean['State'].value_counts().head(10).index

# Analyze top industry for each of the top 10 states
print("=== TOP INDUSTRY BY STATE ===")
print("(Top 10 States by Total Injuries)")
print("\n")

for state in top_states:
    state_data = df_clean[df_clean['State'] == state]
    
    # Get top 3 NAICS codes for this state
    top_3_industries = state_data['Primary NAICS'].value_counts().head(3)
    
    total_injuries = len(state_data)
    
    print(state + ":")
    print("  Total injuries:", total_injuries)
    print("  Top 3 Industries (NAICS):")
    for rank, (naics_code, count) in enumerate(top_3_industries.items(), 1):
        percentage = (count / total_injuries) * 100
        print("    " + str(rank) + ". NAICS " + str(int(naics_code)) + ": " + 
              str(count) + " injuries (" + str(round(percentage, 1)) + "%)")
    print("\n")

# Healthcare analysis across states
healthcare_naics = 622110
print("=== HEALTHCARE (NAICS 622110) ANALYSIS ===")
print("\n")

for state in top_states:
    state_data = df_clean[df_clean['State'] == state]
    healthcare_count = len(state_data[state_data['Primary NAICS'] == healthcare_naics])
    total_count = len(state_data)
    percentage = (healthcare_count / total_count) * 100
    
    print(state + ": " + str(healthcare_count) + " healthcare injuries (" + 
          str(round(percentage, 1)) + "% of state total)")