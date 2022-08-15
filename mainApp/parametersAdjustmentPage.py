# Library
import streamlit as st
import cv2 as cv
import numpy as np

# To adjust the parameters related to the camera and image processing
def parametersAdjustment():
    # Page title
    st.title("Parameters Adjustment")
    
    # Update the parameters when the button is pressed
    with st.form(key="form1"):
        # Create sliders for the parameters
        exposureTime = st.slider("Exposure Time (microsecond):", min_value=20, max_value=10000, value=int(st.session_state.ET), step=1)
        workingDistance = st.slider("Working Distance (mm):", min_value=181.4, max_value=1025.0, value=float(st.session_state.WD), step=0.1)
        blackLevel = st.slider("Black Level:", min_value=-2048, max_value=2047, value=int(st.session_state.BL), step=1)
        gain = st.slider("Gain:", min_value=256, max_value=2047, value=int(st.session_state.Gain), step=1)
        centerX = st.radio("Center X (T/F):", options=[True, False], index=0)
        height = st.slider("Height (pixel):", min_value=1, max_value=3780, value=int(st.session_state.Height), step=1)
        width = st.slider("Width (pixel):", min_value=1, max_value=8192, value=int(st.session_state.Width), step=1)
        triggerDelay = st.slider("Camera Trigger Delay (s):", min_value=0.1, max_value=10.0, value=float(st.session_state.triggerDelay), step=0.1)
        imgThresholding = st.selectbox('Image Thresholding?', ('Yes', 'No'))

        # Submit button
        submitButton = st.form_submit_button(label="Apply the parameters above")
        # Assign all parameters when the button is pressed
        if submitButton:
            st.session_state.WD = workingDistance
            st.session_state.ET = exposureTime
            st.session_state.BL = blackLevel
            st.session_state.Gain = gain
            st.session_state.Cx = centerX
            st.session_state.Height = height
            st.session_state.Width = width
            st.session_state.imgThresholding = imgThresholding
            st.session_state.triggerDelay = triggerDelay
            st.write(":white_check_mark:")
    
    # If the user choose to apply image thresholding, show the preview of the image processing
    if st.session_state.imgThresholding == 'Yes':
        # Create 2 columns side by side
        col1, col2 = st.columns(2)

        # Read the sample image
        sampleImage = "originalSample.png"
        originalImage = cv.imread(sampleImage,0)
        
        # Input number to adjust the threshold value
        st.session_state.pixelThreshold = st.number_input("Image Threshold Value", min_value=0, max_value=255, value=int(st.session_state.pixelThreshold), step=5)
        tImage = np.where((originalImage > st.session_state.pixelThreshold), 255, originalImage)
        tImage = np.where((tImage <= st.session_state.pixelThreshold), 0, tImage)

        # Show the image
        col1.header("Original")
        col1.image(originalImage)

        col2.header("Image Thresholding")
        col2.image(tImage)