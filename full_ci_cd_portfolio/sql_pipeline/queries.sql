-- Example queries
-- 1 Monthly admissions by department
SELECT substr(admission_date,1,7) AS month, department, COUNT(*) AS admissions
FROM hospital_activity
GROUP BY month, department
ORDER BY month DESC;

-- 2 Average LOS
SELECT department, AVG(length_of_stay_days) AS avg_los FROM hospital_activity GROUP BY department;
