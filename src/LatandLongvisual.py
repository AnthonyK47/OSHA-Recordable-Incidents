import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('src/dataset/January2015toFebruary2025.csv')

# Clean data for geographic plotting
df_clean = df.dropna(subset=['Latitude', 'Longitude'])

# Geographic Distribution of Injuries
plt.figure(figsize=(15, 10))

plt.scatter(df_clean['Longitude'], df_clean['Latitude'], alpha=0.4, s=3, color='red')
plt.title('Geographic Distribution of Severe Workplace Injuries (2015-2025)', fontsize=16, fontweight='bold')
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12)
plt.grid(True, alpha=0.3)


plt.xlim(-130, -65)  # Continental US longitude range
plt.ylim(20, 50)     # Continental US latitude range

plt.tight_layout()
plt.savefig('geographic_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Print geographic insights
print(f"Geographic coverage:")
print(f"Latitude range: {df_clean['Latitude'].min():.2f} to {df_clean['Latitude'].max():.2f}")
print(f"Longitude range: {df_clean['Longitude'].min():.2f} to {df_clean['Longitude'].max():.2f}")
print(f"Total plotted points: {len(df_clean):,}")