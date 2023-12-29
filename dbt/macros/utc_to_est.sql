-- '-' before/after % is used to remove whitespaces
{% macro utc_to_est(column_name) -%}

convert_timezone('UTC', 'America/New_York', {{ column_name }})

{%- endmacro %}