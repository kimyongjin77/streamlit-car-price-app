import streamlit as st
import joblib
import numpy as np

def run_ml():
    #pass
    st.subheader('자동차 구매 가능 금액 예측')

    #예측하기 위해서는 필요한 파일들을 불러와야 한다.
    #이 예에서는 인공지능파일, x스케일러파일, y스케일러파일
    #인공지능을 불러온다.
    regressor=joblib.load('data/regressor.pkl')
    #x,y스케일러를 불러온다.
    x_scaler=joblib.load('data/x_scaler.pkl')
    y_scaler=joblib.load('data/y_scaler.pkl')

    #예측할 정보를 받는다.
    #여자, 나이=38, 연봉=78000, 카드빚=15000, 자산=480000
    #성별, 나이, 연봉, 카드빚, 자산 을 입력 받는다.
    gender_list=['남자','여자']
    #choice_gender=st.selectbox('성별 선택',gender_list)
    choice_gender=st.radio('성별 선택',gender_list)
    if choice_gender==gender_list[0]:
        gender=1
    elif choice_gender==gender_list[1]:
        gender=0

    age=st.number_input('나이 입력',min_value=1, max_value=120,value=38)
    salary=st.number_input('연봉 입력',min_value=0,value=78000) 
    card_debt=st.number_input('카드빚 입력',min_value=0,value=15000)
    worth=st.number_input('자산 입력',min_value=0,value=480000)

    if st.button('예측하기'):
        #1.신규고객의 정보를 넘파이 어레이로 만든다.
        new_data=np.array([gender,age,salary,card_debt,worth])
        #2.학습할때 사용한 X의 피처스케일러를 이용해서, 피처스케일링한다.
        #먼저, 데이터를 2차원으로 만들어 준다.
        new_data=new_data.reshape(1,5)
        new_data=x_scaler.transform(new_data)
        #3.인공지능에게 예측 해 달라고 한다.
        new_data_pred=regressor.predict(new_data)
        #4.예측한 값은 스케일링된 값이므로 역으로 원래 값으로 바뀐다.
        y_pred=y_scaler.inverse_transform(new_data_pred)
        
        st.write('이 사람의 구매 가능 금액은 {} 달러입니다.'.format(str(round(y_pred[0,0],2))))