from secrets import choice
from sys import platlibdir
import streamlit as st
from app_eda import run_eda

from app_home import run_home
from app_ml import run_ml

def main():
    #pass
    st.title('자동차 가격 예측')

    menu=['Home','EDA','ML']
    choice=st.sidebar.selectbox('메뉴 선택',menu)

    if choice==menu[0]:
        #pass
        run_home()
    elif choice==menu[1]:
        #pass
        run_eda()
    elif choice==menu[2]:
        #pass
        run_ml()


if __name__=='__main__':
    main()