import pandas as pd
from nfl_data_py import import_weekly_data
from sqlalchemy import create_engine

# 1. Pull NFL data for seasons 2022-2024
seasons = [2022, 2023, 2024]
print(f"Pulling data for seasons: {seasons}")

nfl_df = import_weekly_data(seasons)
print(f"Pulled data with shape: {nfl_df.shape}")

# 2. Select relevant columns
nfl_df = nfl_df[[
    'season', 'week', 'player_name', 'position', 'recent_team',
    'passing_yards', 'rushing_yards', 'receiving_yards', 'fantasy_points'
]]
print(f"Data after selecting columns: {nfl_df.shape}")

# 3. Snowflake connection setup
engine = create_engine(
    'snowflake://{user}@{account}/{database}/{schema}?warehouse={warehouse}&role={role}&authenticator=externalbrowser'.format(
        user='001800416',
        account='NORTHEASTERN-MAIN',
        database='DZ_ENRA_DEV',
        schema='SANDBOX_AM',
        warehouse='ENRA_WH',
        role='R_AMACHA'
    )
)

# 4. Load data into Snowflake table
nfl_df.to_sql('NFL_WEEKLY_STATS', engine, if_exists='append', index=False, method='multi')
print("Data loaded successfully into Snowflake!")