import streamlit as st
from llm import get_sql, get_schema
from db import run_query
from safety import UnsafeSQLError, MAX_ROWS
from pandas.errors import DatabaseError

def app():
    st.title("Its a SQL From Prompt beta version!")
    st.write("Do you want to answer your questions about your dataframe (or bunch of them)? "
             "Then write it down and I will look it up for you!")
    
    with st.form("ask_form", clear_on_submit=True):
        col_input, col_button = st.columns([5, 1], vertical_alignment="bottom")
        with col_input:
            question = st.text_input(label="Search query")
        with col_button:    
            apply = st.form_submit_button("Apply")


    if question.strip() and apply:
        st.toast("Question sent!", icon="✅")
        st.markdown(f"**Question:** {question}")
        try:
            with st.spinner("Asking LLM model..."):
                sql = get_sql(question, get_schema())

            st.code(sql, language="sql")
            df = run_query(sql)
            st.dataframe(df)

            if len(df) >= MAX_ROWS:
                st.caption(f"The result is limited to {MAX_ROWS} rows.")
            
        except DatabaseError: 
            st.error("The generated SQL could not be executed. Try rephrasing the question.")
        except UnsafeSQLError as e:
            st.error(f"Query rejected: {e}")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
    
    
    
    

if __name__ == "__main__":
    app()