import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('src/dataset/January2015toFebruary2025.csv')

print(f"Original dataset: {len(df)} records")

# Removing duplicates
df = df.drop_duplicates()

# Remove records with missing NAICS code
df_clean = df.dropna(subset=['Primary NAICS'])

print(f"After cleaning: {len(df_clean)} records")
print(f"Removed {len(df) - len(df_clean)} records with missing NAICS codes")

# Top Industries by Severe Injury Count (NAICS)
naics_counts = df_clean['Primary NAICS'].value_counts().head(10)

plt.figure(figsize=(12, 8))

# Create bar chart
naics_counts.plot(kind='bar', color='firebrick')
plt.title('Top 10 Industries by Severe Injury Count (NAICS Codes)', fontsize=16, fontweight='bold')
plt.xlabel('NAICS Industry Code', fontsize=12)
plt.ylabel('Number of Severe Injuries', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('naics_pattern_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Print insights
print("\nPattern Analysis Results:")
print("Top 5 NAICS codes with most injuries:")
for i, (naics, count) in enumerate(naics_counts.head(5).items(), 1):

    print(f"{i}. NAICS {naics}: {count} injuries")
