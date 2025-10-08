import os
import streamlit as st

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
    # Set the title of the app
    st.title("My First Streamlit App")
    # Display a text message
    st.write("This is my first Streamlit application!")
    # Crate a bar chart table
    st.bar_chart([1, 5, 2, 6, 2, 1])