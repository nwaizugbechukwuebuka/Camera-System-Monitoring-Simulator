import streamlit as st
import requests

def render_camera_grid():
    st.subheader("Camera Grid")
    # Placeholder for camera grid
    cameras = requests.get("http://localhost:8000/cameras/").json()
    cols = st.columns(2)
    for idx, cam in enumerate(cameras):
        with cols[idx % 2]:
            st.markdown(f"**{cam['id']}** - {cam['location']}")
            st.text(f"Status: {cam['status']}")
