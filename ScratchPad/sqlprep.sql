-- SQL Question 1: Energy Consumption Analysis
-- Given a table `energy_consumption` with columns `timestamp`, `device_id`, and `consumption` (in kWh),
-- write a query to find the average hourly consumption for each device over the past 7 days.

-- Solution:
SELECT
    device_id,
    EXTRACT(YEAR FROM timestamp) AS year,
    EXTRACT(MONTH FROM timestamp) AS month,
    EXTRACT(DAY FROM timestamp) AS day,
    EXTRACT(HOUR FROM timestamp) AS hour,
    AVG(consumption) AS avg_hourly_consumption
FROM
    energy_consumption
WHERE
    timestamp >= NOW() - INTERVAL '7 days'
GROUP BY
    device_id,
    EXTRACT(YEAR FROM timestamp),
    EXTRACT(MONTH FROM timestamp),
    EXTRACT(DAY FROM timestamp),
    EXTRACT(HOUR FROM timestamp)
ORDER BY
    device_id,
    year,
    month,
    day,
    hour;

-- Explanation:
-- 1. EXTRACT Function: Extracts the year, month, day, and hour from the `timestamp` column.
-- 2. WHERE Clause: Filters the records to include only those from the past 7 days.
-- 3. GROUP BY Clause: Groups the records by `device_id` and the extracted year, month, day, and hour.
-- 4. AVG Function: Calculates the average consumption for each group.
-- 5. ORDER BY Clause: Orders the results by `device_id`, year, month, day, and hour.


-- SQL Question 2: Peak Usage Detection
-- Given a table `energy_usage` with columns `timestamp`, `device_id`, and `usage` (in kWh),
-- write a query to find the top 3 devices with the highest peak usage in any single hour over the past month.

-- Solution:
WITH HourlyUsage AS (
    SELECT
        device_id,
        EXTRACT(YEAR FROM timestamp) AS year,
        EXTRACT(MONTH FROM timestamp) AS month,
        EXTRACT(DAY FROM timestamp) AS day,
        EXTRACT(HOUR FROM timestamp) AS hour,
        SUM(usage) AS total_usage
    FROM
        energy_usage
    WHERE
        timestamp >= NOW() - INTERVAL '1 month'
    GROUP BY
        device_id,
        EXTRACT(YEAR FROM timestamp),
        EXTRACT(MONTH FROM timestamp),
        EXTRACT(DAY FROM timestamp),
        EXTRACT(HOUR FROM timestamp)
)
SELECT
    device_id,
    MAX(total_usage) AS peak_usage
FROM
    HourlyUsage
GROUP BY
    device_id
ORDER BY
    peak_usage DESC
LIMIT 3;

-- Explanation:
-- 1. HourlyUsage CTE: Calculates the total usage for each device in each hour.
--    - EXTRACT Function: Extracts the year, month, day, and hour from the `timestamp` column.
--    - WHERE Clause: Filters the records to include only those from the past month.
--    - GROUP BY Clause: Groups the records by `device_id` and the extracted year, month, day, and hour.
--    - SUM Function: Calculates the total usage for each group.
-- 2. Final SELECT: Finds the top 3 devices with the highest peak usage.
--    - MAX Function: Finds the maximum usage for each device.
--    - ORDER BY Clause: Orders the results by peak usage in descending order.
--    - LIMIT Clause: Limits the results to the top 3 devices.


-- SQL Question 3: Device Efficiency
-- Given a table `device_efficiency` with columns `device_id`, `timestamp`, `input_energy` (in kWh), and `output_energy` (in kWh),
-- write a query to calculate the efficiency (output/input) of each device for each day over the past month.

-- Solution:
SELECT
    device_id,
    EXTRACT(YEAR FROM timestamp) AS year,
    EXTRACT(MONTH FROM timestamp) AS month,
    EXTRACT(DAY FROM timestamp) AS day,
    SUM(output_energy) / SUM(input_energy) AS efficiency
FROM
    device_efficiency
WHERE
    timestamp >= NOW() - INTERVAL '1 month'
GROUP BY
    device_id,
    EXTRACT(YEAR FROM timestamp),
    EXTRACT(MONTH FROM timestamp),
    EXTRACT(DAY FROM timestamp)
ORDER BY
    device_id,
    year,
    month,
    day;

-- Explanation:
-- 1. EXTRACT Function: Extracts the year, month, and day from the `timestamp` column.
-- 2. WHERE Clause: Filters the records to include only those from the past month.
-- 3. GROUP BY Clause: Groups the records by `device_id` and the extracted year, month, and day.
-- 4. SUM Function: Calculates the total output and input energy for each group.
-- 5. Efficiency Calculation: Calculates the efficiency as the ratio of total output energy to total input energy.
-- 6. ORDER BY Clause: Orders the results by `device_id`, year, month, and day.


-- SQL Question 4: Anomalous Consumption Detection
-- Given a table `energy_data` with columns `timestamp`, `device_id`, and `consumption` (in kWh),
-- write a query to identify devices that had a consumption spike (more than double the average consumption) in any hour over the past week.

-- Solution:
WITH ConsumptionData AS (
    SELECT
        device_id,
        EXTRACT(HOUR FROM timestamp) AS hour,
        SUM(consumption) OVER (PARTITION BY device_id, EXTRACT(HOUR FROM timestamp)) AS total_consumption,
        AVG(consumption) OVER (PARTITION BY device_id) AS avg_consumption
    FROM
        energy_data
    WHERE
        timestamp >= NOW() - INTERVAL '1 week'
)
SELECT
    device_id,
    hour,
    total_consumption,
    avg_consumption
FROM
    ConsumptionData
WHERE
    total_consumption > 2 * avg_consumption
ORDER BY
    device_id,
    hour;

-- Explanation
-- ConsumptionData CTE:
-- This CTE calculates both the total consumption for each hour and the average consumption over the past week for each device.
-- EXTRACT Function: Extracts the year, month, day, and hour from the timestamp column.
-- SUM Function with Window: Calculates the total consumption for each hour using the SUM function with a window partitioned by device_id, year, month, day, and hour.
-- AVG Function with Window: Calculates the average consumption over the past week for each device using the AVG function with a window partitioned by device_id.
-- WHERE Clause: Filters the records to include only those from the past week.

-- Final SELECT:
-- The final query selects the device_id, year, month, day, hour, total_consumption, and avg_consumption from the ConsumptionData CTE.
-- WHERE Clause: Filters the records to include only those where the total consumption in any hour is more than double the average consumption.
-- ORDER BY Clause: Orders the results by device_id, year, month, day, and hour.

-- Why Use a Window Function? Using window functions here is beneficial because:

-- Efficiency: It allows us to calculate both the total consumption for each hour and the average consumption over the past week in a single pass through the data, reducing the number of scans needed.
-- Simplicity: It simplifies the query by combining the calculations into a single CTE, making the logic easier to follow and maintain.
-- Flexibility: Window functions provide a powerful way to perform calculations across different partitions of the data without needing to use multiple subqueries or CTEs.
-- By using window functions, we can efficiently and effectively identify devices that had a consumption spike in any hour over the past week.


-- SQL Question 5: Energy Savings Calculation
-- Given a table `energy_savings` with columns `timestamp`, `device_id`, `baseline_consumption` (in kWh), and `actual_consumption` (in kWh),
-- write a query to calculate the total energy savings for each device over the past year.

-- Solution:
SELECT
    device_id,
    SUM(baseline_consumption - actual_consumption) AS total_savings
FROM
    energy_savings
WHERE
    timestamp >= NOW() - INTERVAL '1 year'
GROUP BY
    device_id
ORDER BY
    total_savings DESC;

-- Explanation:
-- 1. SUM Function: Calculates the total energy savings for each device as the difference between baseline consumption and actual consumption.
-- 2. WHERE Clause: Filters the records to include only those from the past year.
-- 3. GROUP BY Clause: Groups the records by `device_id`.
-- 4. ORDER BY Clause: Orders the results by total savings in descending order.