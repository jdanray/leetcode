/* https://leetcode.com/problems/swap-salary/ */ 

UPDATE salary
   SET sex = (case when sex = 'm' then 'f'
                   when sex = 'f' then 'm'
              end)
