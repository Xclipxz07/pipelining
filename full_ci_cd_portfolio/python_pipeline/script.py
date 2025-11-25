import pandas as pd

def clean_patient_data(infile='data/patient_data.csv', outfile='data/cleaned_patient_data.csv'):
    df = pd.read_csv(infile, parse_dates=['visit_date'])
    df['age'] = df['age'].fillna(df['age'].median())
    df['bp_systolic'] = df['bp_systolic'].fillna(df['bp_systolic'].median())
    df['bp_diastolic'] = df['bp_diastolic'].fillna(df['bp_diastolic'].median())
    df['medication_given'] = df['medication_given'].str.capitalize()
    df.to_csv(outfile, index=False)
    return df

if __name__ == '__main__':
    df = clean_patient_data()
    print('Cleaned rows:', len(df))
