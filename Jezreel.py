import streamlit as st
st.title("🏆All about Jezreel🏆")
t1,t2,t3 = st.tabs(["About Me","Hobbies","Contact"])
with t1:
    st.header("Jezreel")
    st.subheader("I love anything that flies")
    st.image("images/Screenshot 2024-02-23 at 3.20.00 PM.png", width = 1000)
with t2:
    st.header("I like anything that flies")
    st.subheader("Which includes birds, planes, drones, heli's, blimps, jets, etc")
    st.image("images/1000_F_294354542_pX8tXdAGZfmwwxRpcY6KLuIRHIicFy6v.jpg",width = 1000)
with t3:
    st.header("Call 📞 000-000-000")
    st.subheader("Or email random.email@gmail.com")
    st.image("images/communication-icons-smartphone-envelope-phone-600nw-432329383.webp", width = 700)