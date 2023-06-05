                                                           Voice_To_Text_Converter

It is a website created using Hugging Face Interface and hosted using Streamlit. In the website, you have 2 versions: 
           1: Free Mode(where you can record only 5 seconds of audio and that will be converted/ transcribed to text) 
           2: Full Mode(where you can record upto 15 seconds of audio to be transcribed. It requires your API key on subscription)

Steps to run the project:
1. Install pyaudio, huggingface, streamlit using pip install command.
2. Start the AudioToTextConverter.py file on your environment.
3. Create your api from Hugging Face cloud and note your API key.
4. Create a toml file for storing your api from hugging face cloud interface in Step 2.
5. Remember to update the key location used in the main .py file precisely. It is suggested to store the secrets.toml file at the same location as the main file.
6. Also download the logo.png file for the image.
7. Run the command on the terminal : streamlit run AudioToTextConvertor.py
8. It will run on a local server with all the functionality.
