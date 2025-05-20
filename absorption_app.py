# -*- coding: utf-8 -*-
"""
Created on Sat May 17 10:49:21 2025

@author: vinsm
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Absorption Column Calculator", layout="centered")
st.title("Absorption Column Height Calculator")
st.markdown("This tool estimates the required tower height for gas-liquid absorption using Henry’s Law and midpoint integration.")

# User Inputs
st.sidebar.header("Input Parameters")
G = st.sidebar.number_input("Gas flow rate (G) [mol/m²·s]", value=1.0)
L = st.sidebar.number_input("Liquid flow rate (L) [mol/m²·s]", value=1.5)
KGa = st.sidebar.number_input("Overall mass transfer coeff (KGa) [mol/m³·s]", value=5.0)
m = st.sidebar.number_input("Henry’s constant (m)", value=2.0)
y1 = st.sidebar.number_input("Inlet gas composition (y₁)", value=0.5)
y2 = st.sidebar.number_input("Outlet gas composition (y₂)", value=0.2)
x2 = st.sidebar.number_input("Outlet liquid composition (x₂)", value=0.0)

# Calculations 
n = 9  
if y1 <= y2:
    st.error("Invalid input: y₁ must be greater than y₂ for absorption to occur.")
else:
    x1 = (G / L) * (y1 - y2) + x2
    y_vals = np.linspace(y1, y2, n + 1)
    x_vals = np.linspace(x1, x2, n + 1)
    y_mid = (y_vals[:-1] + y_vals[1:]) / 2
    x_mid = (x_vals[:-1] + x_vals[1:]) / 2
    y_star = m * x_mid
    dy = -np.diff(y_vals)
    driving_force = y_mid - y_star

    resistance = np.where(driving_force > 0, dy / driving_force, np.nan)
    invalid_segments = np.sum(np.isnan(resistance))

    if invalid_segments > 0:
        st.error("Invalid configuration: Driving force reversed in one or more segments.")
    else:
        N_OG = np.sum(resistance)
        H_OG = G / KGa
        Z = H_OG * N_OG

        st.subheader("Calculated Tower Height:")
        st.success(f"Z = {Z:.5f} meters")

        # Plot
        st.subheader("Mass Transfer Resistance per Segment")
        fig, ax = plt.subplots()
        ax.bar(range(1, n + 1), resistance, color="#3399ff")
        ax.set_xlabel("Segment")
        ax.set_ylabel("Δy / (y − y*)")
        ax.set_title("Resistance in Each Segment")
        st.pyplot(fig)
