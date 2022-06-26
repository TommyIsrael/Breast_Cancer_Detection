import streamlit as st
import sklearn
from predict_page import show_predict_page
from explore_page import show_explore_page



# st.set_page_config(layout='wide')
st.set_page_config(
    page_title= 'Predict your heart condition',
    layout='wide',
    page_icon='🩸',
    initial_sidebar_state='auto',
    menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"
                }
)



page= st.sidebar.selectbox('Navigation',['predict page','explore page'])
if page == 'predict page':
    show_predict_page()
else:
    show_explore_page()
    

