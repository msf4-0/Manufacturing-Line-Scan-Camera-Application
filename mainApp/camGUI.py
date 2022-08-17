# Library 
import streamlit as st

# Modules
from homePage import createHomePage
from calculatorPage import createCalculatorPage
from parametersAdjustmentPage import parametersAdjustment
from deploymentPage import deployment

# Create the page title, icon, and layout 
st.set_page_config(page_title = "MLSCA", page_icon = 'resources/logos/shrdc-logo_no-bg.png', layout = "wide")

# Global Variable (saved in the session state)
# Camera parameters
if 'Vr' not in st.session_state:
    st.session_state.Vr = 26.19

if 'WD' not in st.session_state:
    st.session_state.WD = 260

if 'ET' not in st.session_state:
    st.session_state.ET = 98

if 'BL' not in st.session_state:
    st.session_state.BL = 50

if 'Gain' not in st.session_state:
    st.session_state.Gain = 2047

if 'Cx' not in st.session_state:
    st.session_state.Cx = True

if 'Width' not in st.session_state:
    st.session_state.Width = 8000

if 'Height' not in st.session_state:
    st.session_state.Height = 8000

# Camera trigger delay
if 'triggerDelay' not in st.session_state:
    st.session_state.triggerDelay = 1.3

# Deployment page buttons
if 'connectButton' not in st.session_state:
    st.session_state.connectButton = False

if 'connected' not in st.session_state:
    st.session_state.connected = False

# MQTT
if 'brokerIP' not in st.session_state:
    st.session_state.brokerIP = "192.168.0.129"

if 'port' not in st.session_state:
    st.session_state.port = 1883

if 'subTopic' not in st.session_state:
    st.session_state.subTopic = "sensorRead"

if 'message' not in st.session_state:
    st.session_state.message = ""

if 'temp' not in st.session_state:
    st.session_state.temp = st.empty()

if 'temp1' not in st.session_state:
    st.session_state.temp1 = st.empty()

# Other Variable
if 'imgThresholding' not in st.session_state:
    st.session_state.imgThresholding = 'Yes'

if 'pixelThreshold' not in st.session_state:
    st.session_state.pixelThreshold = 110

if 'count' not in st.session_state:
    st.session_state.count = 0

# Create the sidebar for navigation 
logo = "resources/logos/MSF-logo.gif"
st.sidebar.image(logo)
st.sidebar.title("Navigation")  
navOption = st.sidebar.radio("Pages:", options=['Home', 'Calculator', 'Parameters Adjustment', 'Deployment'])

# ---------------------------------- Home page -----------------------------------
if navOption == "Home":
    createHomePage()

# -------------------------------- Calculator page -------------------------------
elif navOption == "Calculator":
    createCalculatorPage()

# -------------------------- Parameters adjustment page --------------------------
elif navOption == "Parameters Adjustment":
    parametersAdjustment()

# ------------------------------- Deployment page --------------------------------
else: 
    deployment()