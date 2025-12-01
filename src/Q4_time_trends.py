import pandas as pd

# Load and clean data
df = pd.read_csv('src/dataset/January2015toFebruary2025.csv')
df = df.drop_duplicates()

# Convert EventDate to datetime
df['EventDate'] = pd.to_datetime(df['EventDate'])

# Extract year
df['Year'] = df['EventDate'].dt.year

print("=== YEARLY INJURY TRENDS (2015-2025) ===")
print("\n")

# Count injuries by year
yearly_counts = df['Year'].value_counts().sort_index()

print("Injuries by Year:")
for year, count in yearly_counts.items():
    print(str(year) + ": " + str(count) + " injuries")

print("\n")

# Calculate year-over-year changes
print("=== YEAR-OVER-YEAR CHANGES ===")
print("\n")

previous_year = None
previous_count = None

for year, count in yearly_counts.items():
    if previous_year is not None:
        change = count - previous_count
        percent_change = ((count - previous_count) / previous_count) * 100
        
        direction = "increase" if change > 0 else "decrease"
        print(str(year) + " vs " + str(previous_year) + ": " + str(abs(change)) + " " + direction + " (" + str(round(abs(percent_change), 1)) + "%)")
    
    previous_year = year
    previous_count = count

print("\n")

# Summary statistics
print("=== SUMMARY STATISTICS ===")
print("Total years analyzed:", len(yearly_counts))
print("Average injuries per year:", round(yearly_counts.mean(), 2))
print("Highest year:", yearly_counts.idxmax(), "(" + str(yearly_counts.max()) + " injuries)")
print("Lowest year:", yearly_counts.idxmin(), "(" + str(yearly_counts.min()) + " injuries)")
print("Total injuries:", yearly_counts.sum())