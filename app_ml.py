import streamlit as st
import joblib

def run_ml():
    #pass
    st.subheader('자동차 구매 가능 금액 예측')

    #예측하기 위해서는 필요한 파일들을 불러와야 한다.
    #이 예에서는 인공지능파일, x스케일러파일, y스케일러파일
    #인공지능을 불러온다.
    regressor=joblib.load('data/regressor.pkl')
    #x,y스케일러를 불러온다.
    scaler_X=joblib.load('data/x_scaler.pkl')
    scaler_y=joblib.load('data/y_scaler.pkl')

    #예측할 정보를 받는다.
    #성별, 나이, 연봉, 카드빚, 자산 을 입력 받는다.
    gender_list=['남자','여자']
    #choice_gender=st.selectbox('성별 선택',gender_list)
    choice_gender=st.radio('성별 선택',gender_list)
    if choice_gender==gender_list[0]:
        choice_gender=1
    elif choice_gender==gender_list[1]:
        choice_gender=0

    age=st.number_input('나이 입력',min_value=1, max_value=120,value=30)

    salary=st.number_input('연봉 입력',min_value=0)
    
    card_debt=st.number_input('카드빚 입력',min_value=0)

    worth=st.number_input('자산 입력',min_value=0)
