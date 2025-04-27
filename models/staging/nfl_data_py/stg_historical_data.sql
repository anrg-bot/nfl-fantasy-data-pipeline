WITH historical_data AS (
    SELECT
        PLAYER_ID,
        PLAYER_NAME,
        RECENT_TEAM,
        POSITION,
        SEASON,
        WEEK,
        PASSING_YARDS,
        PASSING_TDS,
        COMPLETIONS,
        ATTEMPTS,
        INTERCEPTIONS,
        SACKS,
        RUSHING_YARDS,
        CARRIES,
        RUSHING_TDS,
        RUSHING_FIRST_DOWNS,
        RECEIVING_YARDS,
        RECEPTIONS,
        TARGETS,
        RECEIVING_TDS,
        RECEIVING_FIRST_DOWNS,
        FANTASY_POINTS,
        FANTASY_POINTS_PPR
    FROM
        {{ source('nfl_data_py', 'HISTORICAL_DATA') }}
)

SELECT
    *
FROM
    historical_data