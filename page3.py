from hashlib import new
from typing import final
from unittest import result
import streamlit as st

def enkripsi():

    def encrypt(text, s):
        result = ""

        for i in range(len(text)):  
            char = text[i]  
        # encypt_func uppercase characters in plain txt  
  
            if (char.isupper()):  
                result += chr((ord(char) + s - 64) % 26 + 65)  
        # encypt_func lowercase characters in plain txt  
            else:  
                result += chr((ord(char) + s - 96) % 26 + 97) 

        return result  

    text = st.text_input("Masukkan plain text: ")
    s = st.number_input("Shift: ", 0)
    st.write("Hasil Enkripsi: ", encrypt(text, s))
                