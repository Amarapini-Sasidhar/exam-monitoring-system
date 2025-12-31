import json
import pandas as pd
from fpdf import FPDF

def export_to_csv():
    with open("suspicion_log.json", "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df.to_csv("../data/suspicion_log.csv", index=False)
    print("✅ Exported to CSV")

def export_to_pdf():
    with open("suspicion_log.json", "r") as f:
        data = json.load(f)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Suspicion Report", ln=True, align='C')
    pdf.ln()

    for entry in data:
        pdf.cell(200, 10, txt=f"{entry['timestamp']}s | Score: {entry['score']}", ln=True)

    pdf.output("../data/suspicion_log.pdf")
    print("✅ Exported to PDF")
