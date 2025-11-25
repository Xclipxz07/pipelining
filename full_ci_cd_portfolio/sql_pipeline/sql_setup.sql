-- create tables and insert sample data (sqlite compatible)
CREATE TABLE hospital_activity (
  activity_id INTEGER PRIMARY KEY,
  patient_id INTEGER,
  admission_date TEXT,
  discharge_date TEXT,
  department TEXT,
  length_of_stay_days INTEGER,
  diagnosis_code TEXT,
  bed_id INTEGER
);

.mode csv
.import data/hospital_activity.csv hospital_activity
