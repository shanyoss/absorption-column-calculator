# Absorption Column Design Calculator

An interactive chemical engineering tool that calculates the required tower height for gas-liquid absorption based on Henry’s Law, midpoint integration, and mass transfer theory. Built using Python and Streamlit.

---

## Description 

This app dynamically computes the total tower height (Z) for a packed absorption column given user-defined process inputs:

- Gas and liquid flowrates  
- Overall mass transfer coefficient (KGa)  
- Henry’s constant (m)  
- Inlet and outlet compositions

It also visualizes segment-wise mass transfer resistance (Δy / (y − y*)) to provide insight into column performance and driving force distribution.

---

## Live Demo

Click here to try the app: (https://absorption-column-calculator-5p4unw3raqhtyhnfm5bbxc.streamlit.app)


---

## Method

1. Uses midpoint integration to divide the column into uniform segments  
2. Computes driving force and resistance per segment  
3. Calculates number of overall gas transfer units (N_OG)  
4. Estimates tower height using:  
   Z = HOG × NOG, where HOG = G / KGa

---


## Purpose

This project was developed as an independent engineering application to reinforce:
- Separation process modeling concepts  
- Mass transfer fundamentals  
- Use of Python and Streamlit for interactive engineering tools  
- Visualization of theoretical principles

---

## Technologies Used

- Python 3.11  
- Streamlit  
- NumPy  
- Matplotlib

---

## Author

Gurkirat Singh  
BSc Chemical Engineering, University of Alberta

