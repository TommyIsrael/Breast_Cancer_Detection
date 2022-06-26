
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import streamlit as st


def show_explore_page():
    # load data set
    from sklearn.datasets import load_breast_cancer
    breast_cancer_df= load_breast_cancer()
    df= pd.DataFrame(breast_cancer_df.data,columns=breast_cancer_df.feature_names)
    df['diagnosis']= breast_cancer_df.target
    
    # making dynamic  scatter plot

    st.sidebar.markdown('### Scatter Chart: *Explore relationship between features*')
    label_feature= df.drop(labels=['diagnosis'],axis=1).columns.tolist()

    container_0= st.container()
    col_0,col_01= st.sidebar.columns(2)

    with container_0:
        with col_0:
            x_axis= st.selectbox('X Axis',label_feature)
        with col_01:
            y_axis= st.selectbox('Y Axis',label_feature,index=1)

    
    if x_axis and y_axis:

        # SCATTER PLOT ........................................
        # fig_1 = figure for scatter plot.............

        fig_1,ax1=plt.subplots(nrows=1,ncols=1,figsize=(5,5))
        var=ax1.scatter(df[x_axis],df[y_axis],c=df['diagnosis'])
        ax1.set_title('{} vs {}'.format(x_axis.capitalize(),y_axis.capitalize()))
        ax1.set_xlabel(x_axis)
        ax1.set_ylabel(y_axis)
        ax1.legend(*var.legend_elements(), title= "diagnosis",)


    # HISTOGRAM PLOT...............................
    # fig_2: figure for histogram plot

    st.sidebar.markdown('### Histogram chart: *Explore Distribution of features*')
    fig_2,ax2= plt.subplots(nrows=1,ncols=1,figsize=(5,5))
    hist_axis= st.sidebar.multiselect('Select features',
                                        options= label_feature,
                                        default=['mean radius','mean texture'])
    ax2.set_xlabel(' ')
                                        

    bins= st.sidebar.radio('No of Bins',options= [10,20,30,40,50],index=4)

    if hist_axis:
        sub_df= df[hist_axis]
        sub_df.plot.hist(bins=bins,alpha=0.8,ax=ax2,title= 'Distribution of features')
    else:
        sub_df= df[['mean radius','mean texture']] 
        sub_df.plot.hist(bins=bins,alpha=0.8,ax=ax2,title= 'Distribution of features') 

    # HEXABIN CHART...............................
    # fig_3: figure of hexabin chart

    st.sidebar.markdown('### Hexabin chart: *Explore concentration of features*')
    fig_3,ax_3=plt.subplots(figsize=(5,5))

    
    container_01= st.container()
    col_00,col_001= st.sidebar.columns(2)
    with container_01:
        with col_00:
            hex_x_axis= st.selectbox('HX Axis',options= label_feature,index=0)
        with col_001:
            hex_y_axis= st.selectbox('HY Axis',options= label_feature,index=1)
    
    if hex_x_axis and hex_y_axis:
        df.plot.hexbin(x= hex_x_axis, y= hex_y_axis,
                cmap='BuGn',
                gridsize= 25,
                title= 'Concentration of feature',
                ax=ax_3)

    else:
        df.plot.hexbin(x='mean texture',y='mean area',
                cmap='BuGn',
                gridsize= 25,
                title= 'Concentration of feature',
                ax=ax_3)
    

    # BARPLOT CHART............................
    # fig_4: figure of barplot chart
    fig_4,ax4= plt.subplots(figsize=(5,5))
    st.sidebar.markdown('### Barchart: *Shows average feature per tumor type*')
    df_avg= df.groupby('diagnosis').mean()
    sub_df_avg= st.sidebar.multiselect('Select features',
                        options= label_feature,
                        default=['mean radius','mean texture','worst texture'])

    df_avg[sub_df_avg].plot.bar(ax= ax4,)
    ax4.set_title('Average feature per tumor type')
    plt.xticks(ticks=[0,1],labels=['Benign','Malignant'],rotation=0)


    # PAGE LAYOUT...............

    container_1= st.container()
    container_2= st.container()

    col1,col2=st.columns(2)

    with container_1:
        with col1:
            st.pyplot(fig_1)
        with col2:
            st.pyplot(fig_2)
    with container_2:
        with col1:
            st.pyplot(fig_3)
        with col2:
            st.pyplot(fig_4)




        





    