## Techstore Project with dbt, Snowflake and Prefect
This repository consists of a [dbt](https://www.getdbt.com/) project that transforms raw data sources into clear, formatted models for Analytics.

### Sources:
_All source data is loaded to the `RAW` database._
- `tech_store` - An internal company database
- `payment_app` - A third party payment processing application
- `ad_platform` - A third party advertisement platform which conatains data of ads and their performance metrics
- `accounting_app` - A third party accounting application which consists of invoice data

### Target Environments:
_All transformed data models are deployed to the `ANALYTICS` database._
- **Development**
   - Schema: `dbt_jpatel`
     - One per developer _(first initial, last name)_
- **Production**
   - Schema: `STAGING`
     - 1:1 with each soure-system table
   - Schema: `MARTS`
     - Fully transformed and joined models ready for analytics

### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
