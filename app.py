## MEAL PLANNER APP

import streamlit as st
import pandas as pd
import streamlit_calendar as calendar


#---------------SETTINGS--------------------
page_title = "Meal Planner App"
page_icon = ":cook:"  #https://www.webfx.com/tools/emoji-cheat-sheet/
layout= "centered"
initial_sidebar_state="expanded"
#-------------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout, initial_sidebar_state=initial_sidebar_state)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title(f'{page_title} {page_icon}')

# Functionality
st.header("Functionality")
meal_data = st.file_uploader("Upload CSV of meals and ingredients", type=["csv"])
if meal_data:
    meals_df = pd.read_csv(meal_data)
    st.write(meals_df)

meal_url = st.text_input("Upload website URL for meal")
my_meals = st.text_area("Upload my meals")

st.subheader("Settings")
planning_period = st.number_input("Length of meal planning period", 1, 30, 7)
num_people = st.number_input("Number of people", 1, 10, 4)
leftovers = st.checkbox("Use leftovers?")

st.subheader("Meal Options")
lunch_options = st.checkbox("Include lunch options")
breakfast_options = st.checkbox("Include breakfast options")



if st.button("Generate Shopping List"):
    # Placeholder for the algorithm
    st.text("Shopping list based on input data...")


def main():
    print('yes')
if __name__ == "__main__":
    main()

