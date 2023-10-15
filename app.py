import streamlit as st
from PIL import  Image
import tempfile
from streamlit import components



def main():
   
    st.title("Object Detection with YOLO-NAS")
    st.sidebar.title("Settings")
    st.sidebar.subheader("Parameters")
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 300px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 300px;
            margin-left: -300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    app_mode = st.sidebar.selectbox('Choose the App Mode', ['About App', 'Detection'])

    if app_mode == 'About App':
        st.markdown('In this project we are using **YOLOv8** to do Object Detection on Images and Videos and we are using **StreamLit** to create a Graphical User Interface ')
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                width: 300px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 300px;
                margin-left: -300px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div style="display: flex; justify-content: center;">'
                    '<img src="https://www.linkpicture.com/q/tlogo_1.jpg" alt="Centered Image">'
                    '</div>', unsafe_allow_html=True)
        st.markdown('''
                            # About \n
                            AI based Security Camera By \n
                            **SAAHIL BARVE, AKSHAY KESARKAR,HEET GALA** \n
                            This research introduces an AI-based security camera system using **YOLO-NAS** for real-time accident and suspicious activity detection.\n
                            It integrates Google Firebase for secure access control and employs Streamlit for user-friendly interaction, offering a robust solution for enhanced security and safety.
                            ''')

    elif app_mode == 'Detection':
            # Define the URL
            url = "https://detect.roboflow.com/?model=traffic-accident-yolo8&version=1&api_key=04hq95FmAvbUh7YxNTvO"
            # Create HTML code to automatically open the URL
            html_code = f'<script>window.open("https://detect.roboflow.com/?model=traffic-accident-yolo8&version=1&api_key=04hq95FmAvbUh7YxNTvO",  "width=1100", "height=2000", "scrolling=False");</script>'
            # Display the HTML code
            st.markdown(html_code, unsafe_allow_html=True)

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
