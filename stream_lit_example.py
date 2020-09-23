import streamlit as st

st.title('IRIS EDA App')
st.text('built with love')


# header and subheader
st.header('EDA APP')
st.subheader('Iris Dataset')


# checkbox

if st.checkbox('Show Dataset'):
    st.text('Showing Dataset')
    

# radio buttons


gender = st.radio('What is your agender?',('Male','Female'))

if gender == 'Male':
    st.text('hello guy')

else:
    st.text('hello mam')


# Selection

occupation = st.selectbox('OCcupation',('programmer','data Sceintist'))


# sliders
import numpy as np

age = st.slider('Your age',1,10)


# buttons


if st.button('About me'):
    st.text('hello Deepak')




# Write

st.write('Hello world')

# data

st.date_input('Today date', datetime.now())



EDA
