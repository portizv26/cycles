import streamlit as st
import pandas as pd
import os

print(os.getcwd())

# Load data from local file
def load_data():
    return pd.read_csv("critical_changes_transmission_motor_with_supervised_summary.csv")  # Replace with your actual filename

def navigate(direction, df):
    print(st.session_state.index)
    if direction == "next":
        st.session_state.index += 1
    elif direction == "prev":
        st.session_state.index -= 1

df = load_data()
unique_maintenance_cycles = {cycle_id: df[df["mantention_cycle_id"] == cycle_id].shape[0] for cycle_id in df["mantention_cycle_id"].unique()}
if "index" not in st.session_state:
    st.session_state.index = 0
    
# Sidebar with metadata
with st.sidebar:
    st.header("Navigation")
    
    # Navigation buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous"):
            navigate("prev", df)
    with col2:
        if st.button("Next"):
            navigate("next", df)
            
    selected_cycle = list(unique_maintenance_cycles.keys())[st.session_state.index]
    entries = df[df.mantention_cycle_id == selected_cycle]
    n_entries = len(entries)
    
    st.write(f"**Cycle ID:** {selected_cycle}")
    st.write(f"**Date:** {df[df.mantention_cycle_id == selected_cycle].iloc[0]['Date']}")
    st.write(f"**Unit ID:** {df[df.mantention_cycle_id == selected_cycle].iloc[0]['UnitId']}")
    st.write(f"**Number of components changed:** {n_entries}")
    
    for i, entry in enumerate(entries.iterrows()):
        entry = entry[1]
        st.write(f"{i+1}. {entry['System']} -> {entry['Subsystem']} -> {entry['Component']}")

    
st.write(entry["supervised_summary"]) 
