#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 22:46:37 2022
https://www.geeksforgeeks.org/read-json-file-using-python/
https://discuss.streamlit.io/t/how-to-increment-a-function-to-a-button/15177/2
https://superuser.com/questions/273797/convert-mp3-to-ogg-vorbis        

very important : did not work as expected 
        https://blog.streamlit.io/introducing-submit-button-and-forms/

https://www.i2symbol.com/symbols/arrows

@author: mohamed
"""

import json
# Opening JSON file
f = open('cs2r-97c92-SentencesV6Game-export.json')
data = json.load(f)
# for i in data:
#     print(i["text"])
#     print("*"*20)
# Closing file
f.close()

import streamlit as st
# from annotated_text import annotated_text
Next_Text=" التالي ➡ "
Previous_Text= " ⬅ السابق"
Title="مشروع تصحيح نطق اللغة العربية للاطفال"
st.markdown("<h1 style='font-family:traditional.ttf;text-align: center; color: red; font-size:25px'>"+Title+"</h1>", unsafe_allow_html=True)
if 'i' not in st.session_state:
	st.session_state.i = -1

def write_text(Text):
    k=data[st.session_state.i]["code"]
    mylist_id=" : القائمة "+k
    st.markdown("<h2 style='font-family:traditional.ttf; text-align: center; color: blue; font-size: 22px;'>"+mylist_id+"</h2>", unsafe_allow_html=True)    
    # annotate(Text)
    Text=Text.split("\n")
    for t in Text:
        t=t.strip()
        if len(t)>0:
            st.markdown("<h2 style='font-family:traditional; text-align: center; color: blue; font-size: 22px;'>"+t+"</h2>", unsafe_allow_html=True)    

def play_audio():
    k=data[st.session_state.i]["code"]
    audio_file = open('CAPT_AUDIOS_6G/sattam/'+str(k)+".ogg", 'rb')
    audio_bytes = audio_file.read()
    # st.write("k "+k)
    st.audio(audio_bytes, format='audio/ogg', start_time=0)
    text_version="نسخة تجريبية"
    st.markdown("<h3 style='font-family:traditional; text-align: center; color: black; font-size: 18px;'>"+text_version+"</h3>", unsafe_allow_html=True)    
    
def button_right_click():
    st.session_state.i-=1
    if st.session_state.i<0:
        st.session_state.i=31
    # text1=st.write(data[st.session_state.i])
    write_text(data[st.session_state.i]["text"])
    
def button_left_click():
    st.session_state.i+=1
    if st.session_state.i>31:
        st.session_state.i=0
    # text1=st.write(data[st.session_state.i])
    write_text(data[st.session_state.i]["text"])
    

button_left  = st.button(label=Next_Text)
button_right = st.button(label=Previous_Text)

if st.session_state.i==-1:
    button_left_click()
    play_audio()

if button_left:
    button_left_click()        
    play_audio()
    
if button_right:
    button_right_click()
    play_audio()
    

# # def annotate(Text):
# #     Text=Text.split("\n")
# #     for j, t in enumerate(Text):
# #         t=t.strip()
# #         if len(t)>0:
# #             if j % 2:
# #                 annotated_text((t,"","#afa") )    
# #             else :
# #                 annotated_text((t,"","#8ef"))    
