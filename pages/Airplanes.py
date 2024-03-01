import streamlit as st
st.title("Airplanes")
t1,t2,t3 = st.tabs(["Boeing 737 MAX","X-43","Antonov An-225 Mriya"])
with t1:
    st.header("Boeing 737 MAX")
    st.subheader("Is it the future, or the end?")
    a,b = st.columns([1,0.433])
    a.image("images/istockphoto-1399587359-612x612.jpg")
    b.image("images/TUXZ23BYXRFF4CTHG42CKBXC6Q.JPG")
with t2:
    st.header("X-43")
    st.subheader("Faster than fast")
    st.image("images/357521main_ED99-45243-01_full.jpg.webp")
with t3:
    st.header("Antonov An-225 Mriya")
    st.subheader("The big daddy of planes")
    st.image("images/Antonov_An-225_Beltyukov-1.jpg")