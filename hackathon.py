from optparse import Option
from page1 import pages_1
from page2 import pages_2
from page3 import enkripsi
import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title = None,
    options = ["Pengertian Enkripsi", "Artikel", "Contoh Enkripsi Data"],
    default_index = 0,
    orientation = "horizontal"
)

if selected == "Pengertian Enkripsi":
    pages_1()
if selected == "Artikel":
    pages_2()
if selected == "Contoh Enkripsi Data":
    enkripsi()