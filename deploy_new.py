import numpy as np
import pickle
import pandas as pd
import streamlit as st


pickle_in = open("new_model.pkl","rb")
classifier=pickle.load(pickle_in)

if 'abtest' not in st.session_state:
    st.session_state.abtest = 0
if 'year_reg' not in st.session_state:
    st.session_state.year_reg = 0
if 'power_ps' not in st.session_state:
    st.session_state.power_ps = 0
if 'kilometer' not in st.session_state:
    st.session_state.kilometer = 0
if 'repaired' not in st.session_state:
    st.session_state.repaired = 0
if 'vehicle_type_Other' not in st.session_state:
    st.session_state.vehicle_type_Other = 0
if 'vehicle_type_bus' not in st.session_state:
    st.session_state.vehicle_type_bus = 0
if 'vehicle_type_cabrio' not in st.session_state:
    st.session_state.vehicle_type_cabrio = 0
if 'vehicle_type_coupe' not in st.session_state:
    st.session_state.vehicle_type_coupe = 0
if 'vehicle_type_kleinwagen' not in st.session_state:
    st.session_state.vehicle_type_kleinwagen = 0
if 'vehicle_type_kombi' not in st.session_state:
    st.session_state.vehicle_type_kombi = 0
if 'vehicle_type_limousine' not in st.session_state:
    st.session_state.vehicle_type_limousine = 0
if 'vehicle_type_suv' not in st.session_state:
    st.session_state.vehicle_type_suv = 0
if 'fuel_type_Other' not in st.session_state:
    st.session_state.fuel_type_Other = 0
if 'fuel_type_benzin' not in st.session_state:
    st.session_state.fuel_type_benzin = 0
if 'fuel_type_cng' not in st.session_state:
    st.session_state.fuel_type_cng = 0
if 'fuel_type_diesel' not in st.session_state:
    st.session_state.fuel_type_diesel = 0
if 'fuel_type_elektro' not in st.session_state:
    st.session_state.fuel_type_elektro = 0
if 'fuel_type_hybrid' not in st.session_state:
    st.session_state.fuel_type_hybrid = 0
if 'fuel_type_lpg' not in st.session_state:
    st.session_state.fuel_type_lpg = 0
if 'gearbox_Other' not in st.session_state:
    st.session_state.gearbox_Other = 0
if 'gearbox_automatik' not in st.session_state:
    st.gearbox_automatik = 0
if 'gearbox_manuell' not in st.session_state:
    st.session_state.gearbox_manuell = 0
if 'fuel_type' not in st.session_state:
    st.session_state.fuel_type = "Other"
if 'vehicle_type' not in st.session_state:
    st.session_state.vehicle_type = "Other"
if 'gearbox_type' not in st.session_state:
    st.session_state.gearbox_type = "Other"



def welcome():
    return "Welcome All"

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


#@app.route('/predict',methods=["Get"])
#def predict_note_authentication():
def predict_note_authentication(abtest_a,year_reg,power_ps,kilometer,repaired,vehicle_type_Other,vehicle_type_bus,vehicle_type_cabrio,vehicle_type_coupe,vehicle_type_kleinwagen,vehicle_type_kombi,vehicle_type_limousine,vehicle_type_suv,gearbox_Other,gearbox_automatik,gearbox_manuell,fuel_type_Other,fuel_type_benzin,fuel_type_cng,fuel_type_diesel,fuel_type_elektro,fuel_type_hybrid,fuel_type_lpg):
#def predict_note_authentication(abtest,year_reg,power_ps,kilometer,repaired,vehicle_type_Other,vehicle_type_andere,vehicle_type_bus,vehicle_type_cabrio,vehicle_type_coupe,vehicle_type_kleinwagen,vehicle_type_kombi,vehicle_type_limousine,vehicle_type_suv,gearbox_Other,gearbox_automatik,gearbox_manuell,fuel_type_Other,fuel_type_andere,fuel_type_benzin,fuel_type_cng,fuel_type_diesel,fuel_type_elektro,fuel_type_hybrid,fuel_type_lpg):


    print(st.session_state.kilometer)
    print(vehicle_type_coupe)
    print(gearbox_automatik)
    print(year_reg)
    print(power_ps)
    #prediction = classifier.predict([[0,2000,200,8000,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0]])
    #prediction=classifier.predict([[abtest,year_reg,power_ps,kilometer,repaired,vehicle_type_Other,vehicle_type_andere,vehicle_type_bus,vehicle_type_cabrio,vehicle_type_coupe,vehicle_type_kleinwagen,vehicle_type_kombi,vehicle_type_limousine,vehicle_type_suv,gearbox_Other,gearbox_automatik,gearbox_manuell,fuel_type_Other,fuel_type_andere,fuel_type_benzin,fuel_type_cng,fuel_type_diesel,fuel_type_elektro,fuel_type_hybrid,fuel_type_lpg]])
    prediction=classifier.predict([[abtest_a,year_reg,power_ps,kilometer,repaired,vehicle_type_Other,vehicle_type_bus,vehicle_type_cabrio,vehicle_type_coupe,vehicle_type_kleinwagen,vehicle_type_kombi,vehicle_type_limousine,vehicle_type_suv,gearbox_Other,gearbox_automatik,gearbox_manuell,fuel_type_Other,fuel_type_benzin,fuel_type_cng,fuel_type_diesel,fuel_type_elektro,fuel_type_hybrid,fuel_type_lpg]])



    print(prediction)

    return prediction



def main():
    st.title("Used Car Price")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Predict Used Car Price App </h2>
    </div>
    """


    st.markdown(html_temp,unsafe_allow_html=True)

    st.session_state.abtest = st.selectbox("Insert abtest (1-Yes,0-No)",('1','0'),key='1')
    st.session_state.year_reg = st.slider("Insert Year",1935,2019)
    st.session_state.power_ps = st.text_input("power_ps","200")
    st.session_state.kilometer = st.text_input("kilometer","50000")
    st.session_state.repaired = st.selectbox("Repaird or not",("Yes","No","Other"),key="1")

    st.session_state.vehicle_type = st.radio(
         "What's your selection for Vehicle Type",
         ('Other', 'Bus', 'Cabrio', 'Coupe','Kleinwagen','Kombi','Limousine','SUV'))




    st.session_state.gearbox_type = st.radio(
         "What's your selection for Gear Box",
         ('Other', 'Automatik', 'Manuell'))




    st.session_state.fuel_type = st.radio(
         "What's your selection for Fuel Type",
         ('Other', 'Benzin', 'CNG', 'Diesel','Elektro','Hybrid','LPG'))





result=""
if st.button("Predict"):
    if st.session_state.repaired == "Yes":
        st.session_state.repaired = 0
    elif st.session_state.repaired == "No":
       st.session_state.repaired = 1
    elif st.session_state.repaired == "Other":
       st.session_state.repaired = 2

    if  st.session_state.vehicle_type == 'Other':
        st.session_state.vehicle_type_Other = 1
        st.session_state.vehicle_type_bus = 0
        st.session_state.vehicle_type_cabrio = 0
        st.session_state.vehicle_type_coupe = 0
        st.session_state.vehicle_type_kleinwagen = 0
        st.session_state.vehicle_type_kombi = 0
        st.session_state.vehicle_type_limousine = 0
        st.session_state.vehicle_type_suv = 0
    elif st.session_state.vehicle_type == 'Bus':
        st.session_state.vehicle_type_Other = 0
        st.session_state.vehicle_type_bus = 1
        st.session_state.vehicle_type_cabrio = 0
        st.session_state.vehicle_type_coupe = 0
        st.session_state.vehicle_type_kleinwagen = 0
        st.session_state.vehicle_type_kombi = 0
        st.session_state.vehicle_type_limousine = 0
        st.session_state.vehicle_type_suv = 0
    elif st.session_state.vehicle_type == 'Cabrio':
        st.session_state.vehicle_type_Other = 0
        st.session_state.vehicle_type_bus = 0
        st.session_state.vehicle_type_cabrio = 1
        st.session_state.vehicle_type_coupe = 0
        st.session_state.vehicle_type_kleinwagen = 0
        st.session_state.vehicle_type_kombi = 0
        st.session_state.vehicle_type_limousine = 0
        st.session_state.vehicle_type_suv = 0
    elif st.session_state.vehicle_type == 'Kleinwagen':
        st.session_state.vehicle_type_Other = 0
        st.session_state.vehicle_type_bus = 0
        st.session_state.vehicle_type_cabrio = 0
        st.session_state.vehicle_type_coupe = 0
        st.session_state.vehicle_type_kleinwagen = 1
        st.session_state.vehicle_type_kombi = 0
        st.session_state.vehicle_type_limousine = 0
        st.session_state.vehicle_type_suv = 0
    elif st.session_state.vehicle_type == 'Kombi':
        st.session_state.vehicle_type_Other = 0
        st.session_state.vehicle_type_bus = 0
        st.session_state.vehicle_type_cabrio = 0
        st.session_state.vehicle_type_coupe = 0
        st.session_state.vehicle_type_kleinwagen = 0
        st.session_state.vehicle_type_kombi = 1
        st.session_state.vehicle_type_limousine = 0
        st.session_state.vehicle_type_suv = 0
    elif st.session_state.vehicle_type == 'Coupe':
        st.session_state.vehicle_type_Other = 0
        st.session_state.vehicle_type_bus = 0
        st.session_state.vehicle_type_cabrio = 0
        st.session_state.vehicle_type_coupe = 1
        st.session_state.vehicle_type_kleinwagen = 0
        st.session_state.vehicle_type_kombi = 0
        st.session_state.vehicle_type_limousine = 0
        st.session_state.vehicle_type_suv = 0
    elif st.session_state.vehicle_type == 'Limousine':
        st.session_state.vehicle_type_Other = 0
        st.session_state.vehicle_type_bus = 0
        st.session_state.vehicle_type_cabrio = 0
        st.session_state.vehicle_type_coupe = 0
        st.session_state.vehicle_type_kleinwagen = 0
        st.session_state.vehicle_type_kombi = 0
        st.session_state.vehicle_type_limousine = 1
        st.session_state.vehicle_type_suv = 0
    elif st.session_state.vehicle_type == 'SUV':
        st.session_state.vehicle_type_Other = 0
        st.session_state.vehicle_type_bus = 0
        st.session_state.vehicle_type_cabrio = 0
        st.session_state.vehicle_type_coupe = 0
        st.session_state.vehicle_type_kleinwagen = 0
        st.session_state.vehicle_type_kombi = 0
        st.session_state.vehicle_type_limousine = 0
        st.session_state.vehicle_type_suv = 1

    if st.session_state.gearbox_type == 'Other':
        st.session_state.gearbox_Other = 1
        st.session_state.gearbox_automatik = 0
        st.session_state.gearbox_manuell = 0
    elif st.session_state.gearbox_type == 'Automatik':
        st.session_state.gearbox_Other = 0
        st.session_state.gearbox_automatik = 1
        st.session_state.gearbox_manuell = 0
    elif st.session_state.gearbox_type == 'Manuell':
        st.session_state.gearbox_Other = 0
        st.session_state.gearbox_automatik = 0
        st.session_state.gearbox_manuell = 1

    if st.session_state.fuel_type == 'Other':
        st.session_state.fuel_type_Other = 1
        st.session_state.fuel_type_benzin = 0
        st.session_state.fuel_type_cng = 0
        st.session_state.fuel_type_diesel = 0
        st.session_state.fuel_type_elektro = 0
        st.session_state.fuel_type_hybrid = 0
        st.session_state.fuel_type_lpg = 0
    elif st.session_state.fuel_type == 'Benzin':
        st.session_state.fuel_type_Other = 0
        st.session_state.fuel_type_benzin = 1
        st.session_state.fuel_type_cng = 0
        st.session_state.fuel_type_diesel = 0
        st.session_state.fuel_type_elektro = 0
        st.session_state.fuel_type_hybrid = 0
        st.session_state.fuel_type_lpg = 0
    elif st.session_state.fuel_type == 'CNG':
        st.session_state.fuel_type_Other = 0
        st.session_state.fuel_type_benzin = 0
        st.session_state.fuel_type_cng = 1
        st.session_state.fuel_type_diesel = 0
        st.session_state.fuel_type_elektro = 0
        st.session_state.fuel_type_hybrid = 0
        st.session_state.fuel_type_lpg = 0
    elif st.session_state.fuel_type == 'Diesel':
        st.session_state.fuel_type_Other = 0
        st.session_state.fuel_type_benzin = 0
        st.session_state.fuel_type_cng = 0
        st.session_state.fuel_type_diesel = 1
        st.session_state.fuel_type_elektro = 0
        st.session_state.fuel_type_hybrid = 0
        st.session_state.fuel_type_lpg = 0
    elif st.session_state.fuel_type == 'Elektro':
        st.session_state.fuel_type_Other = 0
        st.session_state.fuel_type_benzin = 0
        st.session_state.fuel_type_cng = 0
        st.session_state.fuel_type_diesel = 0
        st.session_state.fuel_type_elektro = 1
        st.session_state.fuel_type_hybrid = 0
        st.session_state.fuel_type_lpg = 0
    elif st.session_state.fuel_type == 'Hybrid':
        st.session_state.fuel_type_Other = 0
        st.session_state.fuel_type_benzin = 0
        st.session_state.fuel_type_cng = 0
        st.session_state.fuel_type_diesel = 0
        st.session_state.fuel_type_elektro = 0
        st.session_state.fuel_type_hybrid = 1
        st.session_state.fuel_type_lpg = 0
    elif st.session_state.fuel_type == 'LPG':
        st.session_state.fuel_type_Other = 0
        st.session_state.fuel_type_benzin = 0
        st.session_state.fuel_type_cng = 0
        st.session_state.fuel_type_diesel = 0
        st.session_state.fuel_type_elektro = 0
        st.session_state.fuel_type_hybrid = 0
        st.session_state.fuel_type_lpg = 1

    #st.write("Hi Predicted")
    result=predict_note_authentication(st.session_state.abtest,st.session_state.year_reg,st.session_state.power_ps,st.session_state.kilometer,st.session_state.repaired,st.session_state.vehicle_type_Other,st.session_state.vehicle_type_bus,st.session_state.vehicle_type_cabrio,st.session_state.vehicle_type_coupe,
                                       st.session_state.vehicle_type_kleinwagen,st.session_state.vehicle_type_kombi,st.session_state.vehicle_type_limousine,
                                       st.session_state.vehicle_type_suv,st.session_state.gearbox_Other,st.session_state.gearbox_automatik,st.session_state.gearbox_manuell,
                                       st.session_state.fuel_type_Other,st.session_state.fuel_type_benzin,st.session_state.fuel_type_cng,st.session_state.fuel_type_diesel,
                                       st.session_state.fuel_type_elektro,st.session_state.fuel_type_hybrid,st.session_state.fuel_type_lpg)
    #result=predict_note_authentication()
st.success('The Predicted Price is {}'.format(result))


if __name__=='__main__':
    main()
