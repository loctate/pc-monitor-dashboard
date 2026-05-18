import streamlit as st
import psutil
import platform

st.title("PC Monitoring Dashboard")

# System Info
st.header("System Information")

st.write(f"OS: {platform.system()} {platform.release()}")
st.write(f"Processor: {platform.processor()}")

# CPU
st.header("CPU Usage")
cpu_usage = psutil.cpu_percent(interval=1)
st.progress(cpu_usage / 100)
st.write(f"CPU Usage: {cpu_usage}%")

# RAM
st.header("RAM Usage")
ram = psutil.virtual_memory()
st.progress(ram.percent / 100)
st.write(f"RAM Usage: {ram.percent}%")

# Disk
st.header("Disk Usage")
disk = psutil.disk_usage('/')
st.progress(disk.percent / 100)
st.write(f"Disk Usage: {disk.percent}%")

from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, key="refresh")

# temps = psutil.sensors_temperatures()
# st.write(temps)

net = psutil.net_io_counters()

st.header("Network Usage")
st.write(f"Bytes Sent: {net.bytes_sent}")
st.write(f"Bytes Received: {net.bytes_recv}")