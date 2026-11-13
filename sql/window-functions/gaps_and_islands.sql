/*
Problem: Identify consecutive activity periods for each user.

Requirements:
1. Extract activity dates from event_time.
2. Count each user's activity once per calendar day.
3. Identify the previous activity date using LAG().
4. Detect gaps between consecutive activity dates.
5. Generate island IDs using a cumulative SUM().
6. Group activity dates into consecutive periods.

Expected output:
- user_id
- start_date
- end_date
- activity_days

Concepts:
- DISTINCT
- CTEs
- LAG()
- PARTITION BY
- Date arithmetic
- CASE WHEN
- Cumulative SUM()
- Window frames
- Gaps and Islands pattern

Revision status:
Completed once; independent revision pending.
*/

with cte_1 as (SELECT distinct user_id,
                               event_time::date AS activity_date
               FROM activity_events),
     cte_2 as (select user_id,
                      activity_date,
                      lag(activity_date) over (partition by user_id order by activity_date) as previous_activity_date
               from cte_1),
     cte_3 as (select user_id,
                      activity_date,
                      previous_activity_date,
                      (activity_date - previous_activity_date) day_difference
               from cte_2),
     cte_4 as (select user_id,
                      activity_date,
                      previous_activity_date,
                      day_difference,
                      case
                          when previous_activity_date is null then 1
                          when day_difference > 1 then 1
                          else 0
                          end as is_new_island
               from cte_3),
     cte_5 as (select user_id,
                      activity_date,
                      is_new_island,
                      sum(is_new_island)
                      over (partition by user_id order by activity_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as island_id
               from cte_4)
select user_id,
       min(activity_date) as start_date,
       max(activity_date) as end_date,
       count(*)           as activity_days
from cte_5
group by user_id, island_id
ORDER BY user_id, start_date;