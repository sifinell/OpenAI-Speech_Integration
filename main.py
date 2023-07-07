import streamlit as st
from speech import text_to_speech, recognize_from_microphone
from open_ai import prompt_open_ai

# Create a boolean flag to keep track of button state
button_start = False

#tokens = st.slider('Tokens to be used?', 0, 2000, 100)

context = st.text_area("Inizia la tua conversazione con un messaggio!")
#context_2 = "Riassumi la risposta in massimo 150 parole"

# Create a button
if st.button("Start conversation!"):
    button_start = True

if button_start:
    # Use the OpenAI API to get a response based on the provided context
    response_open_ai = prompt_open_ai(context, "")

    st.write(response_open_ai)
    text_to_speech(response_open_ai)

    while button_start:
        st.write("\n")
        st.write("Vocal command:\n")

        # Use the speech recognition library to convert spoken commands to text
        input_vocal = recognize_from_microphone()
        #input_vocal = st.text_area("What do you want to ask?")
        st.write(input_vocal)

        if input_vocal == "Stop.":
            break
        else:
            # Use the OpenAI API to get a response based on the user's input
            response_open_ai = prompt_open_ai(input_vocal, "")
            st.write(response_open_ai)
            text_to_speech(response_open_ai)
