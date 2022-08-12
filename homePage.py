# Library
import streamlit as st

# Provide some basic informations about the camera
def createHomePage():
    st.title("Basler raL8192 - 12gm Camera")
    line1 = "**Sensor**: 8K Monochrome"
    line2 = "**Pixel Size**: 3.5 x 3.5 micrometer"
    line3 = "**Max Line Rate**: 12kHz"
    line4 = "**Power requirement (typical)**: 5.5W"
    st.write("Basler raL8192 - 12gm is a line scan cammera with:")
    st.write("1. ", line1, "  \n2. ", line2, "  \n3. ", line3, "  \n4. ", line4)
    st.write("[Product Page](https://www.baslerweb.com/en/products/cameras/line-scan-cameras/racer/ral8192-12gm/)")

    st.title("VS-L5028/F Lens")
    line1 = "**Focal Length**: 50mm"
    line2 = "**Optical Maginification**: x0.05 to x0.3"
    line3 = "**Working Distance**: 181.4 - 1025.0mm"
    st.write("Basler raL8192 - 12gm is a line scan cammera with:")
    st.write("1. ", line1, "  \n2. ", line2, "  \n3. ", line3)
    st.write("[Product Page](https://vitalvisiontechnology.com/machine-vision-lenses/large-format-lenses/vs-l-f-series/vs-l5028f/#1629878382741-0fe26a50-e8b1)")