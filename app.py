# Creating the UI with Streamlit alternative would be Gradio
# I will be wrapping everything in an API later in PHase 2 with HTML to learn FASTAPI and production
import streamlit as st
from src.retriever import answer_question as a_q
# This has to be done first otherwise there will be an error from Streamlit
st.set_page_config(
    page_title= "Manufacturing AI Assistant", # tab title
   # page_icon= "🔧", # icon on the tab
    layout= "wide" # uses full width of the screen instead of narriow centered column

)

st.title("Manufacturing AI Assistant")
st.caption("Ask questions about machine faults, error codes and maintenance procedures.")

# session state is a dictionary kept alive as logs, we create a list in that dictionary
#loop thru messages list and display it in a chat setting with either user or assistant role no matter bold or anhything
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])    
    # default text for the chat input box if empty using walrus operator to check and assign        
if prompt:= st.chat_input("Describe fault and or error ...."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt) # renders in the user bubble
    with st.spinner("Thinking....."):
        result = a_q(prompt)
    answer = result["answer"] # acesssing dictionary for respective answer
    sources = result["sources"] # acesssing dictionary for respective source

    response = f"{answer}\n\n--Sources:--\n" # Displaying the answer in a formatted line with a new line whilst lopping thru soruces and displayinh
    for source in sources:
         response += f"- {source}\n"
    st.session_state.messages.append({"role": "user", "content": response})
    with st.chat_message("assistant"):
         st.markdown(response)