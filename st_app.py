import streamlit as st
import urllib.parse
from main import pdf_extraction

def st_main():
	params = st.query_params.to_dict()

	print('params : ',params)
	pdf_info = params.get("pdf_info", [""])
	print("pdf_info : ", str(pdf_info))
	st.query_params.clear()
	cors_enabled = st.get_option("server.enableCORS")
	if pdf_info:
		try:	
			st.write("Streamlit Configuration:")
			st.write("Current value of enableCORS:", cors_enabled)
			trail = pdf_extraction(pdf_info)
			return trail
		except Exception as e:
			print("error from app", e)
			return 

if __name__ == "__main__":
    st_main()
