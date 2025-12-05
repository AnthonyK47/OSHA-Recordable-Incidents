import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load and clean OSHA data
df = pd.read_csv('src/dataset/January2015toFebruary2025.csv')
df = df.drop_duplicates()
df_clean = df.dropna(subset=['State'])

# Injury count by state
state_counts = df_clean['State'].value_counts()

# Visualization: Top 15 States Bar Chart
plt.figure(figsize=(12, 8))
state_counts.head(15).plot(kind='bar', color='steelblue')
plt.title('Top 15 States by Severe Injury Count (2015-2025)', fontsize=16, fontweight='bold')
plt.xlabel('State', fontsize=12)
plt.ylabel('Number of Severe Injuries', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('state_injury_counts.png', dpi=300, bbox_inches='tight')
plt.show()

