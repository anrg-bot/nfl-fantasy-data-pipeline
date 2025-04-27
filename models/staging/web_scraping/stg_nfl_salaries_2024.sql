WITH nfl_salaries AS (
    SELECT
        NAME AS PLAYER_NAME,
        TEAM,
        SALARY
    FROM
        {{ source('web_scraping', 'SALARIES_2024') }}
        
    WHERE TEAM IS NULL
)
SELECT
    *
FROM
    nfl_salaries