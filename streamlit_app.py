import streamlit as st
import time
import random

# --- Sovereign UI Configuration ---
st.set_page_config(page_title="AUREUS: THE AWAKENING", layout="wide", initial_sidebar_state="collapsed")

# --- Advanced Living CSS ---
st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #111122 0%, #050505 100%);
        color: #D4AF37;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Floating Door Arch */
    .door-arch {
        border: 3px solid #D4AF37;
        border-radius: 150px 150px 20px 20px;
        padding: 60px;
        background: rgba(0, 0, 0, 0.6);
        text-align: center;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.2);
        margin: 20px auto;
        max-width: 500px;
        transition: 0.5s;
    }
    
    .door-arch:hover {
        box-shadow: 0 0 60px rgba(212, 175, 55, 0.5);
        border-color: #FCF6BA;
    }

    .stButton>button {
        background: linear-gradient(45deg, #BF953F, #FCF6BA, #AA771C);
        color: black !important;
        font-weight: bold;
        border-radius: 50px;
        border: none;
        letter-spacing: 2px;
        height: 3.5em;
        width: 100%;
    }
    </style>
''', unsafe_allow_html=True)

# --- State Management ---
if "door" not in st.session_state:
    st.session_state.update({"door": 1, "ars": 20400, "stage": 1})

# --- Main Interface ---
st.markdown("<h1 style='text-align: center; letter-spacing: 15px;'>🔱 AUREUS</h1>", unsafe_allow_html=True)

tabs = st.tabs(["⛩️ GATES", "🛒 ARMORY", "🎡 FATE", "💎 WALLET"])

with tabs[0]:
    if st.session_state.stage < 5:
        st.markdown(f"<p style='text-align:center;'>CHRONICLE {st.session_state.stage}: EVOLUTION</p>", unsafe_allow_html=True)
        st.markdown(f'''
            <div class="door-arch">
                <p style="color:#888; font-family: 'Orbitron';">GATEWAY</p>
                <h1 style="font-size:120px; margin:0; text-shadow: 0 0 25px #D4AF37;">{st.session_state.door}</h1>
                <p style="font-size:18px;">PROGRESS TO NEXT CHRONICLE: {st.session_state.door}/99</p>
            </div>
        ''', unsafe_allow_html=True)
        
        if st.button("✨ UNLOCK PASSAGE"):
            with st.spinner("Aligning Realities..."):
                time.sleep(0.8)
                if st.session_state.door < 99:
                    st.session_state.door += 1
                    st.session_state.ars += 500
                else:
                    st.session_state.stage += 1
                    st.session_state.door = 1
                st.rerun()
    else:
        st.success("You have reached THE SOVEREIGNTY stage.")

with tabs[3]:
    st.markdown("### 💎 TON CONNECT")
    st.write("Current Balance:", f"{st.session_state.ars:,} ARS")
    st.button("LINK WALLET")

st.divider()
st.caption("AUREUS ECOSYSTEM | AUDIT: EE41815 | POWERED BY TON")
