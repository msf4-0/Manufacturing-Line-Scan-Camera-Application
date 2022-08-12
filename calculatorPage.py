# Library
import streamlit as st
# import math

# Assign the parameters to the session state
def submitParamForm(requiredSpeed, workingDistance, exposureTime):
    """
    To assign the following parameters to the session state when the button is pressed:
    1. The required conveyor speed
    2. The required working distance
    3. The required exposure time
    """
    # Assign only when the form button is pressed
    with st.form(key="form1"):
        submitButton = st.form_submit_button(label="Apply the parameters above")
        st.session_state.Vr = requiredSpeed
        st.session_state.WD = workingDistance
        st.session_state.ET = exposureTime

        # Indicate the user that the assignment is done
        if submitButton:
            st.write(":white_check_mark:")

# Calculate one of the missing parameters
def createCalculatorPage():
    # Fix variables
    sensorSize = 3.5 * (10**-3)
    focalLength = 51.38
    tanTheta = (0.5*sensorSize)/focalLength
    # theta = math.degrees(math.atan(tanTheta))
    
    # Basic info about the calculator page
    st.title("Parameters Calculator")
    st.warning(":exclamation:**NOTE:** The parameters calculated by the calculator can only be used to estimate the required parameters value.")
    st.write("---")
    selectBoxVal = st.selectbox("What is the unknown parameter (Please choose 1)?", options=["Object Speed", "Working Distance", "Exposure Time"])
    st.write("###")
    st.write("###")

    # Calculate the required object speed
    if selectBoxVal == "Object Speed":
        workingDistance = float(st.number_input(label="Working Distance (mm) =", value=195.0, min_value=181.4, max_value=1025.0, step=0.1))
        exposureTime = float(st.number_input(label="Exposure Time (microsecond) =", value=98, min_value=20, max_value=10000))
        requiredSpeed = (2*workingDistance*tanTheta)/(exposureTime*(10**-6))
        st.write("**Required Object Speed = ** {:.2f}".format(requiredSpeed), "mm/s")
        submitParamForm(requiredSpeed, workingDistance, exposureTime)

    # Calculate the required distance from the camera to the surface of the object
    elif selectBoxVal == "Working Distance":
        requiredSpeed = float(st.text_input("Object Speed (mm/s) =", value=135.0, min_value=1.24, max_value=3491.14, step=0.1))
        exposureTime = float(st.text_input("Exposure Time (microsecond) =", value=98, min_value=20, max_value=10000))        
        workingDistance = (requiredSpeed*exposureTime*(10**-6))/(2*tanTheta)
        st.write("**Required Distance to the Object Surface = ** {:.2f}".format(workingDistance), "mm")
        submitParamForm(requiredSpeed, workingDistance, exposureTime)

    # Calculate the required exposure time
    else:
        requiredSpeed = float(st.text_input("Object Speed (mm/s) =", value=135.0, min_value=1.24, max_value=3491.14, step=0.1))
        workingDistance = float(st.text_input("Working Distance (mm) =", value=195.0, min_value=181.4, max_value=1025.0, step=0.1))
        exposureTime = (2*workingDistance*tanTheta)/(requiredSpeed*(10**-6))
        st.write("**Required Exposure Time = **{:.2f}".format(exposureTime), "microsecond")
        submitParamForm(requiredSpeed, workingDistance, exposureTime)