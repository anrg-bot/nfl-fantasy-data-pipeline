WITH salaries AS (
    SELECT
        p.PLAYER_ID,
        s.TEAM,
        s.SALARY
    FROM
        {{ ref('stg_nfl_salaries_2024') }} s
    JOIN
        {{ ref('dim_players') }} p
    ON
        s.PLAYER_NAME = p.PLAYER_NAME
)
SELECT
    *
FROM
    salaries