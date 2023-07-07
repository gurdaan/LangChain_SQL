

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain import SQLDatabase, SQLDatabaseChain

# Storing the response
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

def generate_response(message):

    # Database connection string
    dburi = r"mssql+pyodbc:///?odbc_connect=driver=ODBC+Driver+17+for+SQL+Server;" \
            r"Server=localhost\SQLEXPRESS;Database=Student;Trusted_Connection=yes"


    db = SQLDatabase.from_uri(dburi)

    # LLM Instance
    llm = ChatOpenAI(openai_api_key='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')

    # Create an SQLDatabaseChain using the ChatOpenAI model and the database
    db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db)
    response = db_chain.run(message)

    return response

def get_input():
    # Input field for user
    input_text = st.text_input("You: ", "", key="input")
    return input_text  

def main():
    # Load environment variables
    load_dotenv()

    # Display header
    st.header('Answer Questions to Database 🤩🤩')

    # Show image
    st.image('Sql.png',width=100)

    # Get user input
    user_input = get_input()

    if user_input:
        # Generate response for the user input
        st.session_state["generated"] = generate_response(user_input)

    if st.session_state['generated']:
        # Display the generated response
        st.write(st.session_state['generated'])

if __name__ == '__main__':
    main()