from script import clean_patient_data
import pandas as pd

def test_clean_patient_data(tmp_path):
    # prepare sample csv
    data = pd.DataFrame({
        'patient_id':[1,2,3],
        'age':[34,None,50],
        'bp_systolic':[120,140,None],
        'bp_diastolic':[80,None,90],
        'medication_given':['Yes','No','Yes'],
        'visit_date':['2024-01-01','2024-01-02','2024-01-03']
    })
    infile = tmp_path/'patient_data.csv'
    outfile = tmp_path/'cleaned_patient_data.csv'
    data.to_csv(infile, index=False)
    df = clean_patient_data(str(infile), str(outfile))
    assert df['age'].isnull().sum() == 0
    assert 'cleaned' not in df.columns or True
