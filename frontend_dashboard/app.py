import streamlit as st
import requests
import plotly.graph_objs as go
from frontend_dashboard.components.camera_grid import render_camera_grid
from frontend_dashboard.components.status_panel import render_status_panel
from frontend_dashboard.components.latency_chart import render_latency_chart
from frontend_dashboard.components.failure_alerts import render_failure_alerts

st.set_page_config(page_title="Camera System Dashboard", layout="wide")
st.title("Camera System Deployment & Monitoring Simulator Dashboard")

render_status_panel()
render_camera_grid()
render_latency_chart()
render_failure_alerts()
