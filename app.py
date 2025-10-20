import streamlit as st
import requests

st.set_page_config(page_title="Excel-Report-Agent", layout="centered")

st.title("📊 Excel-Report-Agent (Demo)")

st.write("Lade eine Excel-Datei hoch (Spalten: Umsatz, Kosten).")
uploaded_file = st.file_uploader("Excel hochladen", type=["xlsx"])

BACKEND_URL = "https://DEINE-BACKEND-URL.onrender.com/upload_excel/"

if uploaded_file is not None:
    st.info("Sende Datei an Backend...")
    try:
        files = {
            "file": (uploaded_file.name, uploaded_file, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        }
        resp = requests.post(BACKEND_URL, files=files, timeout=120)
        if resp.status_code == 200:
            st.success("✅ Report erstellt!")
            st.download_button(
                label="📥 Report herunterladen",
                data=resp.content,
                file_name="Report.pdf",
                mime="application/pdf"
            )
        else:
            st.error(f"Fehler vom Backend (Status {resp.status_code}).")
            st.write(resp.text)
    except requests.exceptions.RequestException as e:
        st.error("Fehler beim Verbinden mit dem Backend.")
        st.write(str(e))
