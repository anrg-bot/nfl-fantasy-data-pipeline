import nfl_data_py as nfl
import pandas as pd

# Load datasets
years = range(2020, 2024)
weekly_data = nfl.import_weekly_data(years)

print(weekly_data.columns)

hist_data = weekly_data.groupby(
    ['season', 'week', 'player_id', 'player_name', 'position', 'recent_team']
).agg({
    'passing_yards': 'sum',
    'passing_tds': 'sum',
    'completions': 'sum',
    'attempts': 'sum',
    'interceptions': 'sum',
    'sacks': 'sum',
    'rushing_yards': 'sum',
    'carries': 'sum',
    'rushing_tds': 'sum',
    'rushing_first_downs': 'sum',
    'receiving_yards': 'sum',
    'receptions': 'sum',
    'targets': 'sum',
    'receiving_tds': 'sum',
    'receiving_first_downs': 'sum',
    'fantasy_points': 'sum',  # Standard scoring
    'fantasy_points_ppr': 'sum'  # PPR scoring
}).reset_index()

# Save data to CSV (for loading into Snowflake)
hist_data.to_csv("hist_data.csv", index=False)