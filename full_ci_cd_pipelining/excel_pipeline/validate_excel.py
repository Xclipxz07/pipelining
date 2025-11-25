import pandas as pd
from pathlib import Path
import sys

REQUIRED_SHEETS = {
    "patient_log.xlsx": {"DailyNotes": ["patient_id","date","vital_bp","notes"]},
    "medication_monitor.xlsx": {"MedicationLog": ["patient_id","medication","dose_time","administered"]}
}

def validate_excel_file(path):
    p = Path(path)
    if not p.exists():
        return [f"File not found: {path}"]
    xls = pd.ExcelFile(p)
    issues = []
    req = REQUIRED_SHEETS.get(p.name, {})
    for sheet, cols in req.items():
        if sheet not in xls.sheet_names:
            issues.append(f"Missing sheet: {sheet} in {p.name}")
            continue
        df = pd.read_excel(p, sheet_name=sheet)
        for c in cols:
            if c not in df.columns:
                issues.append(f"Missing column: {c} in sheet {sheet} of {p.name}")
    return issues

def main():
    base = Path('data')
    all_issues = []
    for fname in REQUIRED_SHEETS.keys():
        issues = validate_excel_file(base/fname)
        all_issues.extend(issues)
    if all_issues:
        print("Validation failed with issues:")
        for i in all_issues:
            print('-', i)
        sys.exit(2)
    print("All Excel files validated successfully.")
    sys.exit(0)

if __name__ == '__main__':
    main()
