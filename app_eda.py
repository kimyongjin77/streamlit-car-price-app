from sqlalchemy import column
import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def run_eda():
    #pass
    st.subheader('데이터 분석')
    
    car_df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')
    #st.dataframe(car_df)

    #라디오버튼을 이용해서, 데이터프레임과, 통계치를 선택해서
    #보여줄수 있도록 만든다.
    radio_menu=['데이터프레임','통계치']
    selected=st.radio('선택하세요.',radio_menu)

    if selected==radio_menu[0]:
        st.dataframe(car_df)
    elif selected==radio_menu[1]:
        st.dataframe(car_df.describe())
    
    #컬럼을 선택하면 해당 컬럼값의 최대값 데이터와 최소값 데이터를 보여준다.
    columns=car_df.columns[4:]
    choice_col=st.selectbox('컬럼을 선택하면 Max/Min 데이터를 보여줍니다.',columns)
    st.text(choice_col + ' 컬럼값이 Max인 데이터')
    st.dataframe(car_df.loc[car_df[choice_col]==car_df[choice_col].max(),])
    st.text(choice_col + ' 컬럼값이 Min인 데이터')
    st.dataframe(car_df.loc[car_df[choice_col]==car_df[choice_col].min(),])

    #컬럼을 선택하면 해당 컬럼들의 pairplot를 그리고
    #그 아래, 상관계수를 보여준다.
    choice_cols=st.multiselect('컬럼을 선택하면 선택된 컬럼들의 pairplot그래프와 상관계수를 보여줍니다.',columns)
    if len(choice_cols) > 1:
        fig1=sb.pairplot(data=car_df, vars=choice_cols)
        st.pyplot(fig1)
        st.text('상관계수')
        st.dataframe(car_df[choice_cols].corr())

        fig2=plt.figure()
        sb.heatmap(data=car_df[choice_cols].corr(),annot=True,fmt='.2f',vmin=-1,vmax=1,cmap='coolwarm',linewidths=0.5)
        st.pyplot(fig2)
    
    #고객 이름 컬럼을 검색할 수 있도록 만듭니다.
    #he라고 넣으면, he가 이름에 있는 고객들의 데이터를 가져옵니다.
    #1.유저한테 검색어를 입력받는다.
    search_word=st.text_input('찾을 고객명를 입력하세요')
    #2.검색어를 고객이름 컬럼에 들어 있는 데이터 가져온다.
    if len(search_word) > 0:
        search_df=car_df.loc[car_df['Customer Name'].str.lower().str.contains(search_word.lower()),]
        #3.화면에 보여준다.
        st.dataframe(search_df)