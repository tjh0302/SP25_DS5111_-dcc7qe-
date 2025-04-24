## ERD Diagram Report

### Introduction
This report details how the raw (normalized) gainers data is tranformed into tables for use in snowflake.
The Entity Relationship Diagram (ERD) graphically conveys this structure for two use cases, 
the fields required from the raw data, and the intermediate steps required. 

### Use cases
Two likely use cases are identified based on the objectives of the investing firm. 
The first use case is to plot in a timeseries the 3 stocks that had the largest daily percentage increase, for each source - wsj and yahoo. 
This requires an intermediate table which ranks the symbols from largest to smallest daily percent changes, using the closing-gainers data for each day.
The intermediate table requires a table for each day that consists of the list of gainers symbols for each of the three time frames
 - opening, midday, and closing. 

The second use case is to plot a barchart from a final table of the most volatile stocks for the week.
The most volatile stocks are computed in an intermediate table called 'opening-list only'. 
The metric to determine a volatile stock is the number of days that particular symbol (ticker) appeared only in the opening list but not the closing list,
indicating a drop in price-percentage through the course of the day. The investing firm could choose to modify this and reverse the criteria.
For the week, and for each data source, the ten companies that meet this criteria the greatest number of days will be captured in the final table.
The intermediate table will require the list of opening gainers and closing gainers for each day, reflected in the 'day' table.


### Diagram

Below is the mermaidjs code for the ERD.

erDiagram
    SYMBOL }|--|| OPENING-PRICE-PERC-CHANGE: has
    SYMBOL }|--|| MIDDAY-PRICE-PERC-CHANGE: has
    SYMBOL }|--|| CLOSING-PRICE-PERC-CHANGE: has

    OPENING-PRICE-PERC-CHANGE ||--|| OPENING-GAINERS : in
    MIDDAY-PRICE-PERC-CHANGE ||--|| MIDDAY-GAINERS : in
    CLOSING-PRICE-PERC-CHANGE ||--|| CLOSING-GAINERS : in

    OPENING-GAINERS ||--|{ DAY: every
    MIDDAY-GAINERS ||--|{ DAY: every
    CLOSING-GAINERS ||--|{ DAY: every

    DAY }|--|{ DAILY-PERC-CHANGES : contains
    DAILY-PERC-CHANGES }|--|{ LARGEST-DAILY-INCREASES : determines
    LARGEST-DAILY-INCREASES }|--|{ TOP-3-STOCKS : determines
    TIMESERIES }|--|{ TOP-3-STOCKS : contains


    DAY }|--|| OPENING-LIST-ONLY: has
    MOST-VOLATILE-STOCKS }|--|| OPENING-LIST-ONLY : determines
    BARCHART ||--|{ MOST-VOLATILE-STOCKS : contains
