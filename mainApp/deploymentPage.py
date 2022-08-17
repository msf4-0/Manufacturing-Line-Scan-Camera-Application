# Library
import streamlit as st
from pypylon import pylon
import numpy as np
import time
import paho.mqtt.client as mqtt
from PIL import Image as im
import cv2 as cv
from streamlit.script_run_context import add_script_run_ctx

# Deployment page
def deployment():
    # Main container
    mainContainer = st.container()
    
    # on_connect callback; when connected to a broker, subscribe to the desired topic
    def on_connect(client,userdata,flags,rc):
        """
        on_connect callback; when connected to a broker, subscribe to the desired topic
        """
        print("Connected with result code " + str(rc))
        # rc code meaning:
        #   0: Connection successful
        #   1: Connection refused – incorrect protocol version
        #   2: Connection refused – invalid client identifier
        #   3: Connection refused – server unavailable
        #   4: Connection refused – bad username or password
        #   5: Connection refused – not authorised
        #   6-255: Currently unused.
        client.subscribe(st.session_state.subTopic, qos=2)

    def on_message(client,userdata,msg):
        """
        on_message callback; when a publish message is received from the server, assign the payload to the message variable.
        """
        st.session_state.message = msg.payload.decode("UTF-8")

    # Page title
    mainContainer.title("Deployment")
    
    # Variable to store the connect button
    if 'connectButton' not in st.session_state:
        st.session_state.connectButton = None

    # Create a connect and disconnect button
    connectButton = mainContainer.button(label="Connect")
    disconnectButton = mainContainer.button(label="Disconnect")
    
    mainContainer.markdown("""---""")

    # Update the valriable if the button is pressed
    if connectButton:
        st.session_state.connectButton = True

    if disconnectButton:
        st.session_state.connectButton = False
        st.warning("The camera has been disconnected!")

    # If the user chooses to connect to a camera
    if st.session_state.connectButton:
        # Printing name of the connected camera
        tl_factory = pylon.TlFactory.GetInstance()
        devices = tl_factory.EnumerateDevices()
        st.session_state.connected = False
        for device in devices:
            st.session_state.connected = True
            mainContainer.warning(":white_check_mark: " + device.GetFriendlyName() + " has been connected!")
        
        # Create a new InstantCamera object, apply the pamareters, and print a warning if no camera is connected
        try:
            tl_factory = pylon.TlFactory.GetInstance()
            camera = pylon.InstantCamera()
            camera.Attach(tl_factory.CreateFirstDevice())

            camera.Open()
            # Assigning the camera parameters with the selected value (will be assigned with default value if the user didn't set any value)
            camera.BlackLevelRaw.SetValue(st.session_state.BL)
            camera.ExposureTimeAbs.SetValue(st.session_state.ET)
            camera.GainRaw.SetValue(st.session_state.Gain)
            camera.CenterX.SetValue(st.session_state.Cx)
            camera.Width.SetValue(st.session_state.Width)
            camera.Height.SetValue(100)
            camera.MaxNumBuffer = 20
            camera.Close()
        except:
            st.warning(":x:No camera detected")

        # If there is a camera connected
        if st.session_state.connected:
            # Create the deployment button
            st.session_state.deployButton = mainContainer.checkbox("Deploy", value=False)

            # Create a MQTT client, connect to the desired broker, and start the loop (waiting if the sensor is triggered)
            client = mqtt.Client()
            try:
                client.connect(st.session_state.brokerIP, st.session_state.port)
            except:
                st.warning("Couldn't find the broker!")
            
            client.on_connect = on_connect
            client.on_message = on_message
            client.loop_start()
            add_script_run_ctx(client._thread)

            # If user wants to deploy
            while st.session_state.deployButton:
                # To avoid the error when dealing with while loop in streamlit
                with st.session_state.temp1.container():
                    st.write("")
                    time.sleep(0.1)

                st.session_state.temp1.empty()

                # If the message received from the sensor is true, start the image aquisition
                if st.session_state.message == "true":
                    # To avoid the effect of the container above
                    with st.session_state.temp.container():
                        camera.Open()

                        # Wait for the object to reach the camera's FOV
                        time.sleep(st.session_state.triggerDelay)

                        # Start to aquire the frame
                        camera.StartGrabbing(pylon.GrabStrategy_OneByOne)
                        i = 0
                        print('Starting to acquire')
                        # t0 = time.time()
                        img = []
                        while camera.IsGrabbing():
                            grab = camera.RetrieveResult(2000, pylon.TimeoutHandling_ThrowException)
                            if grab.GrabSucceeded():
                                i += 1
                                img.append(grab.GetArray())
                            if i == (st.session_state.Height / 100):
                                camera.StopGrabbing()
                                break
                        
                        camera.Close()

                        # Combine the frames into 1 image
                        with st.container():
                            combinedImg = img[0]
                            for imgIndex in range(len(img) - 1):
                                combinedImg = np.concatenate((combinedImg, img[imgIndex+1]), axis=0)
                            st.image(combinedImg)
                            st.write(f'Size of the image: {combinedImg.shape}')
                        
                        # Resize the combined image
                        combinedImg = cv.resize(combinedImg, (512,512))
                        
                        # If user chose to use image thresholding, apply the method
                        if st.session_state.imgThresholding == 'Yes':
                            combinedImg = np.where((combinedImg > st.session_state.pixelThreshold), 255, combinedImg)
                            combinedImg = np.where((combinedImg <= st.session_state.pixelThreshold), 0, combinedImg)

                        # Preview the image after the thresholding
                        st.image(combinedImg)
                        st.write(f'Size of the image: {combinedImg.shape}')
                        
                        # Saving the image in PNG format
                        data = im.fromarray(combinedImg)

                        # Save the image
                        pathName = "img.png"
                        data.save(pathName)

                        # Loading the image and encode it to bytearray to be sent through MQTT
                        with open(pathName, 'rb') as img_file:
                            byteArrayImage = bytearray(img_file.read())

                        # Connect and publish the image
                        client = mqtt.Client()
                        client.connect("localhost",1883,60)
                        client.publish("cvsystem/main/recv_frame", byteArrayImage)
                        time.sleep(0.01)
                        client.disconnect()
                        
                        # Clear the message
                        st.session_state.message = ""