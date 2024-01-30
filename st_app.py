import streamlit as st
import urllib.parse
from main import pdf_extraction

def st_main():
	params = st.query_params.get_all("pdf_info")

	print('params : ',params)
	pdf_info = params.get("pdf_info", [""])[0]
	print("pdf_info : ", str(pdf_info))

	try:
		trail = pdf_extraction(pdf_info)
		return trail
	except Exception as e:
		print("error from app", e)
		return 

if __name__ == "__main__":
    st_main()
