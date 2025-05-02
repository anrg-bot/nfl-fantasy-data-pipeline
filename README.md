# 🏈 NFL Fantasy Football Edition - dbt™ Data Modeling

Personal Portfolio Project

*by [Anuraag Macha](https://anrg-portfolio.vercel.app/)*

This project explores how to extract hidden value from NFL player performance by bridging real-world football stats with fantasy football insights. Built using **Power BI**, **Snowflake**, and **dbt**, the dashboard highlights key metrics like consistency, red zone efficiency, injury trends, and return on investment (ROI).

## Tech Stack

- **Data Ingestion**: VS Code, MiniConda, Python scripting
- **Data Warehouse**: Snowflake  
- **Transformations**: dbt  
- **Visualization**: Power BI  
- **Source Data**: `nfl_data_py` library, injury reports, salary files  

## Data Ingestion Workflow

Getting raw NFL data into Snowflake required a custom pipeline built from scratch:

1. **Extract with `nfl_data_py`**  
   Used Python to download historical NFL data for the 2022–2024 seasons, including weekly stats, snap counts, and player metadata.

2. **Save Locally in CSV Format**  
   Created a custom Python script and ran it in **VS Code** inside a **MiniConda environment** to save clean `.csv` files.

3. **Upload to Snowflake**  
   Loaded files into Snowflake manually using the **PUT command** and Snowflake Web UI for full control over the staging process.

4. **Structure with dbt**  
   Used **dbt** to build a modular and reusable transformation layer:
   - **Staging models** (`stg_`) organized by source and cleaned up fields (renaming, casting, trimming).
   - **Dimension tables** (`dim_`) such as `dim_players` and `dim_teams` provided enriched context with consistent keys and attributes (e.g., experience level, position, team).
   - **Fact tables** (`fct_`) like `fct_player_stats` and `fct_red_zone` stored aggregated performance metrics per game or play situation.
   - **Mart models** (`mrt_`) combined dimensions and facts for dashboard-ready analysis. Examples include:
     - `mrt_consistency_score`: takes into account variance of weekly fantasy points for volatility analysis.
     - `mrt_red_zone_efficiency`: tracks red zone targets and touchdowns to calculate TD conversion rates by player.
     - `mrt_roi`: joins salary data to scoring outputs to calculate return on investment.

## Dashboard Features

### Overview Page  
Foundational layout of player experience levels, team distribution, and season structure.

### Consistency vs. Average Fantasy Points  
Compare player output against standard deviation. Identifies **reliable starters** vs. **volatile scorers**.

### Positional Breakdown  
A scatter plot that shows which players combine **high scoring** with **low weekly variance**—fantasy gold.

### Red Zone Efficiency  
Reveals who’s converting targets into TDs inside the 20. Mark Andrews and Rashod Bateman stood out for elite efficiency.

### Injury Impact  
Over **2,800 injuries** tracked across **305 players**. See which teams were most affected and which body parts were most vulnerable (knees, hamstrings, and ankles top the list).

### ROI Insights  
Who actually earned their fantasy paycheck?  
- Compare **top-paid vs. top-scoring players**  
- Highlight **value stars** like **Jayden Daniels**, **Geno Smith**, and **Baker Mayfield**

### Salary by Position  
Breakdown of total salary by position—**QBs consumed 39%** of team payroll, making them the highest-risk investments.

## Key Takeaways

- **High production ≠ high value** — ROI reveals cost-efficiency blind spots.
- Players like **Jayden Daniels**, **Jared Goff**, and **Geno Smith** massively outperformed their cost.
- **Tight ends** delivered surprising red zone value at lower salary brackets.
- Injury-prone teams like **New England** and **Carolina** impacted fantasy stability and opportunity.

## Future Enhancements

- Add DFS-specific ROI metrics based on cost-per-point  
- Integrate waiver-wire trends and ownership % filters  
- Build “value tiers” by position for draft strategy

## Related Links

- [My Medium Article](#) *(https://medium.com/@macha.anrg/from-the-field-to-the-dashboard-engineering-fantasy-football-analytics-5560ff5ddd65)* 
- [dbt Model Repo](https://github.com/anrg-bot/nfl-fantasy-data-pipeline)
- [NFL Data Source - `nfl_data_py`](https://nfl-data-py.readthedocs.io/)

Thanks for checking out this project! Whether you're optimizing lineups or building data pipelines, **smart value wins games**—in fantasy and in code.
