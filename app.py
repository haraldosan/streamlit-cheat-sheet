
import streamlit as st
from pathlib import Path
import base64

# Initial page config

st.set_page_config(
     page_title='Hva er det egentlig i kantina denne uken?',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    cs_body()
    return None

# Thanks to streamlitopedia for the following code snippet


##########################
# Main body of cheat sheet
##########################

def cs_body():

    st.title('Hva er det egentlig i kantina - UKE 33 edition?')

    col1 = st.container()

    #######################################
    # COLUMN 1
    #######################################
    
    # Display text

    col1.header('Mandag')
    col1.code('''Karbonader m/ løk
Allergener: Gluten / hvete, melk''')
    
    col1.header('Tirsdag')
    col1.code('''Kalkunscnitzel m/ pommes frites & béarnaisesaus
Allergener: Gluten / hvete, melk, egg''')
    
    col1.header('Onsdag')
    col1.code('''Suppe m/ tilbehør
Allergener: Gluten / hvete, melk''')

    col1.header('Torsdag')
    col1.code('''Thai kyllinggryte m/ ris
Allergener: Gluten / hvete, melk''')

    col1.header('✨ Fredag ✨')
    col1.code('''BURGER 🍔
Allergener: Gluten / hvete, melk''')

    return None

# Run main()

if __name__ == '__main__':
    main()
