import sys, types
if 'cgi' not in sys.modules:
    sys.modules['cgi'] = types.ModuleType('cgi')
import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()

# 🌟 Interfaz inspirada en Taylor Swift
st.title('Taylor Analyzer 🎤✨')
st.subheader("Escribe una frase o un fragmento de letra y descubre cómo Taylor la interpretaría emocionalmente 💌")

with st.sidebar:
    st.subheader("💫 Polaridad y Subjetividad en el universo de Taylor")
    st.markdown("""
    **Polaridad** → Indica si la emoción es triste, nostálgica o esperanzadora,  
    como cuando una canción pasa de *All Too Well* a *Shake It Off*.  
    Su valor va de -1 (muy triste 💔) a 1 (muy feliz 💖).

    **Subjetividad** → Mide cuánto de lo que escribes es una historia personal o una reflexión objetiva.  
    Va de 0 (hechos) a 1 (emociones puras).
    """)

# 🎶 Análisis emocional tipo "Taylor"
with st.expander('Analiza la emoción de tu texto'):
    text1 = st.text_area('Escribe tu frase o verso:')
    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        st.write('**Polaridad:**', round(blob.sentiment.polarity, 2))
        st.write('**Subjetividad:**', round(blob.sentiment.subjectivity, 2))
        x = round(blob.sentiment.polarity, 2)

        if x >= 0.5:
            st.success('✨ Suena a un verso alegre — energía *Lover*. 💕')
        elif x <= -0.5:
            st.error('💔 Tiene la vibra melancólica de *All Too Well*. 😢')
        else:
            st.info('😐 Neutral, como si fuera un puente esperando su emoción.')

# ✍️ Corrección gramatical
with st.expander('Reescribe tu letra en inglés con estilo perfecto 🎼'):
    text2 = st.text_area('Escribe tu texto en inglés:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write("**Versión corregida:**")
        st.write(blob2.correct())
