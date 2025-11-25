from validate_excel import validate_excel_file
from pathlib import Path

def test_patient_log_valid():
    issues = validate_excel_file(Path('data/patient_log.xlsx'))
    assert issues == []

def test_med_sheet_valid():
    issues = validate_excel_file(Path('data/medication_monitor.xlsx'))
    assert issues == []
