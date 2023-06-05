import streamlit as st
import requests
import json
import os
import sounddevice as sd
import wavio

st.set_page_config(
    page_title="Speech-to-Text Transcription App", page_icon="👄", layout="wide"
)

def _max_width_():
    max_width_str = f"max-width: 1200px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

_max_width_()

# logo and header -------------------------------------------------

c30, c31, c32 = st.columns([2.5, 1, 3])

with c30:
    st.image("logo.png", width=350)
    st.header("")

with c32:
    st.title("")
    st.title("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")

st.text("")
st.text("")

def main():
    pages = {
        "👾 Free mode (2MB per API call)": demo,
        "🤗 Full mode (with your API key)": API_key,
    }

    if "page" not in st.session_state:
        st.session_state.update(
            {
                # Default page
                "page": "Home",
            }
        )

    with st.sidebar:
        page = st.radio("Select your mode", tuple(pages.keys()))

    pages[page]()

# Free mode -------------------------------------------------

def demo():
    c1, c2, c3 = st.columns([1, 4, 1])
    with c2:
        with st.form(key="my_form"):
            st.info("👆 Record an audio")
            submit_button = st.form_submit_button(label="Record")

            if submit_button:
                # Set the audio parameters
                duration = 5  # Recording duration in seconds
                sample_rate = 44100  # Sample rate of the audio

                # Record audio
                recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
                sd.wait()  # Wait for recording to complete

                # Save the recorded audio as a WAV file
                file_name = "recording.wav"
                wavio.write(file_name, recording, sample_rate, sampwidth=2)

            #submit_button = st.form_submit_button(label="Record and Transcribe")

        if submit_button and os.path.exists(file_name):
            # Load your API key from an environment variable or secret management service
            api_token = st.secrets["api_token"]

            headers = {"Authorization": f"Bearer {api_token}"}
            API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"

            def query(data):
                response = requests.request("POST", API_URL, headers=headers, data=data)
                return json.loads(response.content.decode("utf-8"))

            with open(file_name, "rb") as f:
                bytes_data = f.read()

            data = query(bytes_data)

            values_view = data.values()
            value_iterator = iter(values_view)
            text_value = next(value_iterator)
            text_value = text_value.lower()

            st.success(text_value)

            c0, c1 = st.columns([2, 2])

            with c0:
                st.download_button(
                    "Download the transcription",
                    text_value,
                    file_name=None,
                    mime=None,
                    key=None,
                    help=None,
                    on_click=None,
                    args=None,
                    kwargs=None,
                )

# Custom API key mode -------------------------------------------------

def API_key():
    # ... Rest of the code ...
        c1, c2, c3 = st.columns([1, 4, 1])
        with c2:
            with st.form(key="my_form"):
                text_input = st.text_input("Enter your HuggingFace API key")
                st.info("👆 Record an audio")
                submit_button = st.form_submit_button(label="Record")
                
                if submit_button:
                    # Set the audio parameters
                    duration = 20  # Recording duration in seconds
                    sample_rate = 44100  # Sample rate of the audio
                    # Record audio
                    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
                    sd.wait()  # Wait for recording to complete
                    # Save the recorded audio as a WAV file
                    file_name = "recording.wav"
                    wavio.write(file_name, recording, sample_rate, sampwidth=2)
                    #submit_button = st.form_submit_button(label="Record and Transcribe")
            if submit_button and os.path.exists(file_name):
                # Load your API key from an environment variable or secret management service
                api_token = st.secrets["api_token"]
                headers = {"Authorization": f"Bearer {api_token}"}
                API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"
                
                def query(data):
                    response = requests.request("POST", API_URL, headers=headers, data=data)
                    return json.loads(response.content.decode("utf-8"))
                
                with open(file_name, "rb") as f:
                   bytes_data = f.read()
                   data = query(bytes_data)
                   values_view = data.values()
                   value_iterator = iter(values_view)
                   text_value = next(value_iterator)
                   text_value = text_value.lower()
                   st.success(text_value)
                   c0, c1 = st.columns([2, 2])
                   
                with c0:
                    st.download_button(
                    "Download the transcription",
                    text_value,
                    file_name=None,
                    mime=None,
                    key=None,
                    help=None,
                    on_click=None,
                    args=None,
                    kwargs=None,
                )

# Notes about the app -------------------------------------------------

with st.expander("FREE MODE AND FULL MODE", expanded=False):
    st.write("""     
-   Free mode is limited to 2MB. You can subscribe and extend the file to 30MB!
    """)
    st.markdown("")

if __name__ == "__main__":
    main()