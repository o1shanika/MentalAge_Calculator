import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Sri Lankan Mental Age Test", layout="centered")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.title("🧠 Mental Age Checker 🇱🇰")

    # Safe Lottie animation
    lottie_url = "https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json"
    lottie_json = load_lottieurl(lottie_url)

    if lottie_json:
        st_lottie(lottie_json, speed=1, width=250, height=250, key="safe_brain_animation")
    else:
        st.image("https://media.giphy.com/media/fAMd9YJlsO2S1Irs5I/giphy.gif", width=250)

    st.markdown("""
        ### Welcome to the Mental Age Checker!
        Ever wondered if your mind is younger or older than you are? This short, fun quiz is designed to give you an estimate of your "mental age" based on your lifestyle, preferences, and outlook on life.

        **Ready to start? Select "📝 Questions" from the sidebar on the left!**
    """)

if __name__ == "__main__":
    main()
