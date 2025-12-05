import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv('src/dataset/January2015toFebruary2025.csv')
df = df.drop_duplicates()

# Convert EventDate to datetime
df['EventDate'] = pd.to_datetime(df['EventDate'])

# Extract year
df['Year'] = df['EventDate'].dt.year

# Count injuries by year
yearly_counts = df['Year'].value_counts().sort_index()

# Create line chart
plt.figure(figsize=(12, 6))
plt.plot(yearly_counts.index, yearly_counts.values, marker='o', linewidth=2, markersize=8, color='purple')
plt.title('Severe Workplace Injuries by Year (2015-2025)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Injuries', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(yearly_counts.index, rotation=45)

# Add value labels on points
for year, count in yearly_counts.items():
    plt.text(year, count + 100, str(count), ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('time_trends_simple.png', dpi=300, bbox_inches='tight')
plt.show()


print("Visualization saved as 'time_trends.png'")
