import streamlit as st

st.title("동주 첫 Streamlit 웹 앱")
st.write("GitHub Codespaces에서 작성 중입니다.")

name = st.text_input("이름을 입력하세요:")
if name:
    st.write(f"환영합니다, {name}님!")