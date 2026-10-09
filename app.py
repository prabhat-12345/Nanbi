import streamlit as st

# Premium Page Configuration
st.set_page_config(
    page_title="Happy Birthday Nandanipriyadarshini! 🌟", 
    page_icon="👑", 
    layout="centered"
)

# Premium Custom CSS for Rich Multi-Color Typography and Glowing Card Elements
st.markdown("""
    <style>
    /* Dark Premium Galactic Background */
    .stApp {
        background: linear-gradient(135deg, #090514 0%, #161233 50%, #290229 100%);
    }
    
    /* 1. Main Title - Glowing Neon Rainbow Text Style */
    .vibrant-title {
        font-family: 'Playfair Display', 'Georgia', serif;
        font-size: 38px !important;
        font-weight: 900;
        color: #FFF;
        text-align: center;
        letter-spacing: 1px;
        text-shadow: 0 0 10px #FF3366, 0 0 20px #FF9933, 0 0 30px #FFCC00;
        margin-bottom: 5px;
    }
    
    /* 2. Subtitle - Shimmering Vivid Gold */
    .vibrant-subtitle {
        font-size: 16px;
        font-weight: 700;
        text-align: center;
        color: #FFD700;
        letter-spacing: 1px;
        margin-bottom: 30px;
        text-shadow: 0 0 8px rgba(255, 215, 0, 0.6);
    }

    /* Luxury Holographic Card Container with Mobile-Friendly Padding */
    .luxury-glow-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 2px solid #FF3366;
        padding: 25px 15px;
        border-radius: 24px;
        box-shadow: 0 0 35px rgba(255, 51, 102, 0.35);
        margin-top: 25px;
        animation: smoothPop 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* 3. Birthday Quote - Electric Cyan Glow Typography */
    .animated-quote {
        font-family: 'Lora', 'Georgia', serif;
        font-size: 22px;
        font-weight: 700;
        line-height: 1.5;
        text-align: center;
        font-style: italic;
        color: #33CCFF;
        text-shadow: 0 0 10px rgba(51, 204, 255, 0.8), 0 0 20px rgba(51, 204, 255, 0.4);
        margin-bottom: 15px;
    }

    /* 4. Author Signature Tag */
    .animated-author {
        font-size: 13px;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 800;
        color: #FFCC00;
        margin-bottom: 35px;
        text-shadow: 0 0 8px rgba(255, 204, 0, 0.8);
    }

    /* 5. Main Body Message - High Contrast Radiant Styles */
    .animated-body {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        color: #FFFFFF;
        text-align: center;
        line-height: 1.8;
        font-weight: 500;
    }
    
    /* Neon Text Modifiers for Important Sentences */
    .neon-pink {
        color: #FF3366;
        font-weight: 700;
        text-shadow: 0 0 8px rgba(255, 51, 102, 0.6);
    }
    
    .neon-cyan {
        color: #00FFCC;
        font-weight: 700;
        text-shadow: 0 0 8px rgba(0, 255, 204, 0.6);
    }
    
    .neon-gold {
        color: #FFCC00;
        font-weight: 700;
        text-shadow: 0 0 8px rgba(255, 204, 0, 0.6);
    }

    /* 6. Name Spotlight Panel - Responsive Font to Force Single Line on Mobile */
    .name-spotlight-panel {
        background: linear-gradient(-45deg, #FF3366, #FF9933, #33CCFF, #AE00FF);
        background-size: 300% 300%;
        color: #FFFFFF !important;
        font-size: 16px !important; /* Made smaller for flawless mobile rendering */
        font-weight: 900;
        text-align: center;
        padding: 15px 10px;
        border-radius: 18px;
        margin-top: 35px;
        box-shadow: 0 10px 30px rgba(255, 51, 102, 0.5);
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
        animation: gradientMove 4s ease infinite;
        white-space: nowrap; /* Forces text to stay in one line */
        overflow: hidden;
        text-overflow: ellipsis;
    }
    
    @media (min-width: 480px) {
        .name-spotlight-panel {
            font-size: 24px !important;
        }
        .vibrant-title {
            font-size: 44px !important;
        }
        .animated-quote {
            font-size: 26px;
        }
        .animated-body {
            font-size: 19px;
        }
    }

    /* Smooth Entry Keyframe Animation */
    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes smoothPop {
        0% { opacity: 0; transform: scale(0.96) translateY(10px); }
        100% { opacity: 1; transform: scale(1) translateY(0); }
    }
    
    /* Elegant Button Architecture Override */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #FF3366 0%, #AE00FF 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 16px 32px !important;
        font-size: 18px !important;
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

# Main Title Framework
st.markdown('<h1 class="vibrant-title">✨ A Celebration of Excellence ✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="vibrant-subtitle">🌈 Dedicated to an exceptional mind on her special day 📚</p>', unsafe_allow_html=True)

# Main Action Button for Celebration
if st.button("🎁 Open Your Magical Birthday Surprise 🌟", use_container_width=True):
    st.balloons() 
    st.snow()     
    
    # Pure High-Contrast Multi-Color Structured Text Layout
    card_html = (
        '<div class="luxury-glow-card">'
        '    <p class="animated-quote">"The future belongs to those who believe in the beauty of their dreams."</p>'
        '    <p class="animated-author">🏆 — Eleanor Roosevelt</p>'
        '    <div class="animated-body">'
        '        <span class="neon-pink" style="font-size: 22px;">Happy Birthday! 🎉🎂🎈</span><br><br>'
        '        It is a profound privilege to guide a student with your '
        '        <span class="neon-cyan">brilliant intellect</span>, '
        '        relentless dedication, and unwavering curiosity. Your potential is absolutely limitless, '
        '        and I have no doubt that your journey ahead will be nothing short of extraordinary.🚀<br><br>'
        '        May this wonderful year unlock <span class="neon-gold">dazzling new opportunities</span>, '
        '        profound happiness, and the spectacular success you so deeply deserve. '
        '        Keep shining like the bright star you are!🌟⭐'
        '    </div>'
        '    <div class="name-spotlight-panel">👑 Happy Birthday Nandanipriyadarshini! 👑</div>'
        '</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)
    st.toast("Success! Birthday Portal Unlocked! 🥳🧁🎉", icon="💖")
else:
    st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 16px; margin-top: 60px; font-weight: 500;'>👉 Click the magical glowing portal above to reveal your message!</p>", unsafe_allow_html=True)
    
