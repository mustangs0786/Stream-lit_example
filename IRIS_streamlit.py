# Importing important libaries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.datasets import load_boston

# title
st.title('IRIS EDA APP')
st.header('Built WIth Love')

#Eda

my_dataset = 'Iris.csv'

# Load Dataset
@st.cache(persist=True,suppress_st_warning=True)
def load_datset(dataset):
    st.write('d')
    df = pd.read_csv(os.path.join(my_dataset))
    return df


# Loading of dataset

data = load_datset(my_dataset)




# Welcome to my world
def main():
        

    if st.checkbox('Preview Dataset'):
        
        # preview of dataset
        # checkbox
        if st.button('Head'):
            st.write(data.head())
        elif st.button('Want to see Tail also'):
            st.write(data.tail())

        else:
            st.write(data.head(3))

        # Radio buttons
        s = st.radio('Want to see head or tail',('head','tail'))
        if s == 'head':
            st.write(data.head())
        elif s == 'tail':
            st.write(data.tail())

        # selectbox

        s = st.selectbox('SElect head or tail',('head','tail'))

        if s == 'head':
            st.write(data.head())
        elif s == 'tail':
            st.write(data.tail())

        # show full dataset

        if st.checkbox('show full dataset'):
        # st.write(data)
            st.dataframe(data)




    # Show column name
    if st.checkbox('show columns name'):
        st.dataframe(data.columns)





    # show Dimensions
    if st.checkbox('want to seee dimesnion'):
        dim  = st.radio('what dimension to see',('rows','columns','all'))
        if dim == 'rows':
            st.write('showing rows')
            st.write(data.shape[0])

        elif dim == 'columns':
            st.write('showing columns')
            st.write(data.shape[1])

        else:
            st.write('Showing full dimension')
            st.write(data.shape)
            




    # show summary

    if st.checkbox('Show discripiton of Dataset'):
        a = st.selectbox("Catergorical and Non Catergorical discripiton",('Categorical','Non-Categorical'))
        
        if a == 'Categorical':
            st.write(data.describe(include='O'))
        elif a == 'Non-Categorical':
            st.write(data.describe())


    # Select a Columns
    if st.checkbox('want to see indivisual columns'):
        col_option = st.selectbox('Select columns',('sepal_length','sepal_width','petal_length','petal_width'))

        if col_option == 'sepal_length':
            st.write(data['SepalLengthCm'])

        elif col_option == 'sepal_width':
            st.write(data['SepalWidthCm'])

        elif col_option == 'petal_length':
            st.write(data['PetalLengthCm'])

        elif col_option == 'petal_width':
            st.write(data['PetalWidthCm'])

        else:
            st.write('Select any options ')



    # if i want them to run together

    if st.checkbox('Want all together'):
        for i in data.columns:
            st.write('preview of {}'.format(i))
            st.write(data[i])



    # plotting


    if st.checkbox('show correlation plot'):
        sm = data.corr()
        import seaborn as sns
        st.write(sns.heatmap(sm), annot=True)  
        st.pyplot() 




    # for Plotting Graph
    import plotly.express as px
    #@st.cache(suppress_st_warning=True)
    def graph(a):
        if a == 'Species':
            fig = px.bar(data, x=a,color="Species", title='{}'.format(a), hover_name='Species' )
            fig.update_xaxes(title_font_family="Arial", title="No.of observations")
            st.plotly_chart(fig)
            st.write(data.Species.value_counts())


        else:
            # st.write(data[a].plot(figsize=(10,5)))
            # st.pyplot()
            fig = px.line(data, y=a,color="Species", title='{}'.format(a), hover_name='Species' )
            fig.update_xaxes(title_font_family="Arial", title="No.of observations")
            st.plotly_chart(fig)

        


    # Select a Columns
    if st.checkbox('want to see indivisual plot'):
        col_option = st.selectbox('Select columns',('sepal_length','sepal_width','petal_length','petal_width', 'Species'))
    
        if col_option == 'sepal_length':
            graph('SepalLengthCm')


        elif col_option == 'sepal_width': 
            graph('SepalWidthCm')
            

        elif col_option == 'petal_length':
            graph('PetalLengthCm')
            

        elif col_option == 'petal_width':
            graph('PetalWidthCm')
        
        elif col_option == 'Species':
            graph('Species')
            

        else:
            st.write('Select any options ')


if __name__ == '__main__':
    main()








    
        
            

