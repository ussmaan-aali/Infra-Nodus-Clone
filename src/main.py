import streamlit as st
from fileHandler import handleFile

# @st.cache_data()
def main():   
        graph = handleFile(uploaded_file)
        if graph:
                st.title("Graph Generated")


if __name__=="__main__":
        st.title('InfraNodus Clone')
        uploaded_file = st.file_uploader('Upload file')
        
        if uploaded_file:
                main()