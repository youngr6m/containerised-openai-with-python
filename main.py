import streamlit as st
import pandas as pd

def main():
    st.write("# Hello, world!")
    st.write("## My first streamlit app")

    dataframe = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })

    st.dataframe(dataframe.style.highlight_max(axis=0))
    

if __name__ == "__main__":
    main()

