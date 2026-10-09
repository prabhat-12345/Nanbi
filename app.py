import streamlit as st

# Premium Page Configuration
st.set_page_config(
    page_title="Happy Birthday Nandanipriyadarshini! 🌟", 
    page_icon="👑", 
    layout="centered"
)

# Premium Custom CSS for Multi-Color Animated Texts & Shimmering Gradients
st.markdown("""
    <style>
    /* Premium Cosmic Space Background */
    .stApp {
        background: linear-gradient(135deg, #090514 0%, #161233 50%, #290229 100%);
    }
    
    /* 1. Main Title - Mega Rainbow Glow Animation */
    .vibrant-title {
        font-family: 'Playfair Display', 'Georgia', serif;
        font-size: 46px !important;
        font-weight: 900;
        background: linear-gradient(45deg, #FF3366, #FF9933, #FFCC00, #33CCFF, #AE00FF);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: 2px;
        animation: rainbowShift 6s ease infinite, glowPulse 2s infinite alternate;
    }
    
    /* 2. Subtitle - Elegant Gold Shimmer */
    .vibrant-subtitle {
        font-size: 19px;
        font-weight: 600;
        text-align: center;
        background: linear-gradient(to right, #FFD700, #FFA500, #FFD700);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
        margin-bottom: 30px;
        animation: shineText 3s linear infinite;
    }

    /* Luxury Card Design with Neon Borders */
    .luxury-glow-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 2px solid transparent;
        border-image: linear-gradient(45deg, #FF3366, #33CCFF) 1;
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0 0 35px rgba(255, 51, 102, 0.2);
        margin-top: 25px;
        animation: smoothPop 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* 3. Main Birthday Quote - Neon Cyberpunk Pink-Blue Polish */
    .animated-quote {
        font-family: 'Lora', 'Georgia', serif;
        font-size: 26px;
        font-weight: 700;
        line-height: 1.6;
        text-align: center;
        font-style: italic;
        background: linear-gradient(90deg, #33CCFF, #FF3366, #33CCFF);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 15px;
        animation: shineText 4s linear infinite;
    }

    /* 4. Author Name - Gold Radiant Pulse */
    .animated-author {
        font-size: 15px;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 4px;
        font-weight: 800;
        color: #FFCC00;
        margin-bottom: 35px;
        text-shadow: 0 0 8px rgba(255, 204, 0, 0.6);
    }

    /* 5. Main Body Message - Clean Pastel Vibrant Style */
    .animated-body {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        color: #F3F4F6;
        text-align: center;
        line-height: 1.9;
        background: linear-gradient(120deg, #FFFFFF 0%, #E2E8F0 50%, #CBD5E1 100%);
        -webkit-background-clip: text;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    
    .highlight-word {
        background: linear-gradient(to right, #00FFCC, #33CCFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }

    /* 6. Student Name Spotlight Panel - Mega Colorful Moving Wave */
    .name-spotlight-panel {
        background: linear-gradient(-45deg, #FF3366, #FF9933, #33CCFF, #AE00FF);
        background-size: 300% 300%;
        color: white !important;
        font-size: 28px !important;
        font-weight: 900;
        text-align: center;
        padding: 18px;
        border-radius: 15px;
        margin-top: 35px;
        box-shadow: 0 10px 30px rgba(255, 51, 102, 0.4);
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.4);
        animation: gradientMove 4s ease infinite;
    }

    /* Keyframe Animations Engine */
    @keyframes rainbowShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes shineText {
        to { background-position: 200% center; }
    }
    @keyframes glowPulse {
        0% { filter: drop-shadow(0px 0px 5px rgba(255,51,102,0.4)); }
        100% { filter: drop-shadow(0px 0px 20px rgba(51,204,255,0.8)); }
    }
    @keyframes smoothPop {
        0% { opacity: 0; transform: scale(0.96) translateY(10px); }
        100% { opacity: 1; transform: scale(1) translateY(0); }
    }
    
    /* Grand Golden Interactive Button Overrides */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #FF3366 0%, #AE00FF 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 16px 32px !important;
        font-size: 21px !important;
        font-weight: 800 !important;
        border-radius: 50px !important;
        box-shadow: 0 6px 25px rgba(174, 0, 255, 0.5) !important;
        transition: all 0.4s ease !important;
        letter-spacing: 1px;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.04) translateY(-3px) !important;
        box-shadow: 0 10px 35px rgba(255, 51, 102, 0.7) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Layout Structure
st.markdown('<h1 class="vibrant-title">✨ A Celebration of Excellence ✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="vibrant-subtitle">🌈 Dedicated to an exceptional mind on her special day 📚</p>', unsafe_allow_html=True)

# Main Action Button for Celebration
if st.button("🎁 Open Your Magical Birthday Surprise 🌟", use_container_width=True):
    st.balloons() 
    st.snow()     
    
    # Fully Compiled HTML Layout with Explicit Text Classes
    card_html = (
        '<div class="luxury-glow-card">'
        '    <p class="animated-quote">"The future belongs to those who believe in the beauty of their dreams."</p>'
        '    <p class="animated-author">🏆 — Eleanor Roosevelt</p>'
        '    <div class="animated-body">'
        '        <strong>Happy Birthday! 🎉🎂🎈</strong><br><br>'
        '        It is a profound privilege to guide a student with your <span class="highlight-word">brilliant intellect</span>, '
        '        relentless dedication, and unwavering curiosity. Your potential is absolutely limitless, '
        '        and I have no doubt that your journey ahead will be nothing short of extraordinary.🚀<br><br>'
        '        May this wonderful year unlock dazzling new opportunities, profound happiness, '
        '        and the spectacular success you so deeply deserve. Keep shining like the bright star you are!🌟⭐'
        '    </div>'
        '    <div class="name-spotlight-panel">👑 Happy Birthday Nandanipriyadarshini! 👑</div>'
        '</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)
    st.toast("Success! Birthday Portal Unlocked! 🥳🧁🎉", icon="💖")
else:
    st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 16px; margin-top: 60px; font-weight: 500;'>👉 Click the magical glowing portal above to reveal your message!</p>", unsafe_allow_html=True)
    
