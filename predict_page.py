import pandas as pd
import numpy as np
import streamlit as st





def  load_model():
    import pickle
    data=pickle.load(open('model_step.pkl','rb'))
    return data

data = load_model()

clf_model= data['model']
scaler= data['scaler']

def show_predict_page():

                    
    st.title('BREAST CANCER DETECTION WEB APP')
    st.write("""If you find a breast tumor or other change in your breast, you might worry about breast cancer.""")
     
    st.write("""That's understandable, most often they're noncancerous (benign). A **Fine-needle aspiration biopsy**
                may help diagnose the type of cancer.The data collected from the FNA examination maybe used to determine
                the type of cancer(Malignant or Benign)
            """)



    test_data=pd.DataFrame({'mean radius':[0.0000],
           'mean compactness':[0.0000],
           'mean concavity':[0.0000],
           'mean concave points':[0.00000],
           'radius error':[0.00000],
           'worst compactness':[0.0000],
           'worst concavity':[0.0000],
           'worst concave points':[0.0000]})


    

    
    with st.sidebar:
        st.write('**Give the required information about the breast lump**')

        mean_radius= st.slider('Radius',6.0,30.0,step=0.1 )
        test_data['mean radius']= mean_radius

        feature= ['mean radius']
        test_data[feature] = scaler.transform(test_data[feature])
        
        test_data['mean concavity']= st.slider('Concativity',0.0,0.5,step=0.001 )
        test_data['mean compactness']= st.slider('Compactness',0.0,0.5,step=0.001 )


        test_data['mean concave points']= st.slider('Concave point',0.0,0.3,step=0.001 )
        test_data['radius error']= st.slider('Radius error',0.0,3.0,step=0.01 )
        
        test_data['worst compactness']= st.slider('Worst compactness',0.0,1.5,step=0.01 )
        test_data['worst concave points']= st.slider('Worst concave point',0.0,0.5,step=0.01 )
        test_data['worst concavity']= st.slider('Worst concativity',0.0,1.5,step=0.01 )

    # CREATING NEW TABLE
    disp_table= pd.DataFrame({'Raduis':mean_radius,
                             'Concativity':test_data['mean concavity'],
                             'Compactness':test_data['mean compactness'],
                             'Concave point':test_data['mean concave points'],
                             'Radius error':test_data['radius error'],
                             'Worst compactness':test_data['worst compactness'],
                             'Worst concave point':test_data['worst concave points'],
                             'Worst concativity':test_data['worst concavity']})
    
    
    rad= st.radio('show input table',['yes','no'])
    if rad == 'yes':
        st.dataframe(disp_table)

    ok = st.button('Check type of Tumor')
    if ok:
        x=clf_model.predict(test_data)
        # st.write(x)        
        if x==1:
            st.subheader(f'Breast tumor  is Malignant')
        else:
            st.subheader(f'Breast tumor is Benign')
        



