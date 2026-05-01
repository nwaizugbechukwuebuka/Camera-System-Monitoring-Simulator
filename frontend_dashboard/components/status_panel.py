import streamlit as st
import requests

def render_status_panel():
    st.subheader("System Status")
    health = requests.get("http://localhost:8000/health/").json()
    st.metric("Total Cameras", health['total_cameras'])
    st.metric("Online", health['online'])
    st.metric("Offline", health['offline'])
