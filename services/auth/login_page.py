import streamlit as st 
from services.persistence.exercise_repository import get_or_create_user

def render_login_page():

    if st.session_state.get("logged_in", False):
        return True

    st.title("🏋️ AI GYM TRAINER ")
    st.markdown("### Welcome! Please enter a username to start.")


    with st.form("login-form", clear_on_submit=False):
        username = st.text_input("Username" , placeholder="Enter your username")
        submit_button = st.form_submit_button("Start Your Session", width='stretch')

   
    if submit_button:
        if not username:
            st.error("Username cannot be emply")
            return False

        user = get_or_create_user(username) 

        st.session_state["logged_in"] = True
        st.session_state['username'] = user["username"]
        st.session_state["user_id"] = user["id"]
        st.toast(f"welcome! {username}")
        st.rerun()


    return False