import streamlit as st
import plotly.graph_objs as go

def render_latency_chart():
    st.subheader("Network Latency (Simulated)")
    # Placeholder chart
    latency_data = [50, 60, 55, 70, 65, 80, 75]
    fig = go.Figure(data=[go.Scatter(y=latency_data, mode='lines+markers')])
    fig.update_layout(title='Simulated Latency (ms)', xaxis_title='Time', yaxis_title='Latency (ms)')
    st.plotly_chart(fig, use_container_width=True)
