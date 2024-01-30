import streamlit as st
import urllib.parse
from main import pdf_extraction

def st_main():
	params = st.experimental_get_query_params()
	print('params : ',params)
	pdf_info = params.get("pdf_info", str)[0]
	print("pdf_info : ", str(pdf_info))

	try:
		trail = pdf_extraction(pdf_info)
		return trail
	except Exception as e:
		print("error from app", e)
		return 

if __name__ == "__main__":
    st_main()
