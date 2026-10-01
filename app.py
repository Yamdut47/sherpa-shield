"""
SherpaShield — Premium Password Security Analyzer
Inspired by the legendary Sherpas of the Himalayas.
"""

import streamlit as st
from utils.password_checker import analyze_password, get_recommendations
from utils.entropy import calculate_entropy
from utils.crack_time import estimate_crack_time
from utils.generator import generate_password

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="SherpaShield",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# Premium Custom CSS — Himalayan Cyber Theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background: linear-gradient(160deg, #060b18 0%, #0c1529 40%, #0a1628 100%);
    color: #e8edf5;
}
#MainMenu, footer, header {visibility: hidden;}
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a1225 0%, #07101f 100%) !important;
    border-right: 1px solid rgba(59, 130, 246, 0.15);
}
section[data-testid="stSidebar"] .stRadio label {
    background: transparent;
    border-radius: 10px;
    padding: 0.6rem 0.9rem;
    margin-bottom: 0.3rem;
    transition: all 0.25s ease;
    font-weight: 500;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(59, 130, 246, 0.12);
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.6rem;
    font-weight: 700;
    background: linear-gradient(135deg, #60a5fa 0%, #38bdf8 40%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    letter-spacing: -0.5px;
}
.hero-sub {
    color: #94a3b8;
    font-size: 1.05rem;
    font-weight: 400;
    margin-top: 0.3rem;
}

.glass {
    background: rgba(15, 23, 42, 0.65);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(148, 163, 184, 0.12);
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    transition: all 0.3s ease;
}
.glass:hover {
    border-color: rgba(96, 165, 250, 0.3);
    box-shadow: 0 0 30px rgba(59, 130, 246, 0.08);
}
.glass-label {
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #64748b;
    margin-bottom: 0.4rem;
}
.glass-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.7rem;
    font-weight: 700;
    color: #f1f5f9;
}
.glass-sub {
    font-size: 0.8rem;
    color: #64748b;
    margin-top: 0.25rem;
}

.s-weak   { color: #f87171 !important; }
.s-medium { color: #fbbf24 !important; }
.s-strong { color: #34d399 !important; }
.s-vstrong{ color: #22d3ee !important; }

.pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 0.4rem 0.85rem;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 500;
    margin: 0.25rem 0.3rem 0.25rem 0;
}
.pill-yes {
    background: rgba(52, 211, 153, 0.12);
    color: #34d399;
    border: 1px solid rgba(52, 211, 153, 0.25);
}
.pill-no {
    background: rgba(248, 113, 113, 0.1);
    color: #f87171;
    border: 1px solid rgba(248, 113, 113, 0.2);
}

.section-h {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.15rem;
    font-weight: 600;
    color: #e2e8f0;
    margin: 1.8rem 0 0.8rem 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-h::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(96,165,250,0.3), transparent);
}

.rec-item {
    background: rgba(30, 41, 59, 0.5);
    border-left: 3px solid #3b82f6;
    border-radius: 0 10px 10px 0;
    padding: 0.7rem 1rem;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
    color: #cbd5e1;
}
.rec-good {
    border-left-color: #34d399;
}

.score-big {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    background: linear-gradient(135deg, #60a5fa, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.gen-box {
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(96, 165, 250, 0.25);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    font-family: 'Space Grotesk', monospace;
    font-size: 1.35rem;
    letter-spacing: 1.5px;
    color: #38bdf8;
    text-align: center;
    word-break: break-all;
}

.stTextInput > div > div > input {
    background: rgba(15, 23, 42, 0.7) !important;
    border: 1px solid rgba(96, 165, 250, 0.2) !important;
    border-radius: 12px !important;
    color: #f1f5f9 !important;
    font-size: 1.05rem !important;
    padding: 0.85rem 1.1rem !important;
}
.stTextInput > div > div > input:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
}

.stButton > button {
    background: linear-gradient(135deg, #2563eb, #7c3aed) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 0.65rem 1.5rem !important;
    transition: all 0.25s ease !important;
    font-family: 'Inter', sans-serif !important;
}
.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.35) !important;
}

div[data-testid="stMetric"] {
    background: rgba(15, 23, 42, 0.55);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 14px;
    padding: 1rem 1.2rem;
}
div[data-testid="stMetric"] label {
    color: #64748b !important;
    font-size: 0.75rem !important;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4rem !important;
    color: #f1f5f9 !important;
}

.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #2563eb, #7c3aed, #22d3ee) !important;
    border-radius: 99px;
}
.stProgress > div > div {
    background: rgba(30, 41, 59, 0.6) !important;
    border-radius: 99px;
}

.streamlit-expanderHeader {
    background: rgba(15, 23, 42, 0.5) !important;
    border-radius: 10px !important;
    color: #94a3b8 !important;
}

.stSlider > div > div > div {
    background: #3b82f6 !important;
}
.stCheckbox label span {
    color: #cbd5e1 !important;
}
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(96,165,250,0.2), transparent);
    margin: 1.5rem 0;
}
.tip-box {
    background: rgba(59, 130, 246, 0.08);
    border: 1px solid rgba(59, 130, 246, 0.18);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    font-size: 0.85rem;
    color: #94a3b8;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.image("assets/logo.png", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["Analyze", "Generator", "About"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("""
    <div class="tip-box">
        <b style="color:#60a5fa">Quick Tips</b><br>
        • Use 16+ characters<br>
        • Mix upper, lower, digits & symbols<br>
        • Avoid dictionary words<br>
        • Never reuse passwords
    </div>
    """, unsafe_allow_html=True)

# ═════════════════════════════════════════════
# PAGE: ANALYZE
# ═════════════════════════════════════════════
if page == "Analyze":

    c1, c2 = st.columns([1, 5])
    with c1:
        st.image("assets/logo.png", width=90)
    with c2:
        st.markdown('<p class="hero-title">SherpaShield</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-sub">Evaluate • Entropy • Crack Time • Recommendations</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter or paste a password to analyze…",
        label_visibility="collapsed",
        key="pwd",
    )
    show = st.checkbox("Show password", value=False)
    if show and password:
        st.code(password, language=None)

    if password:
        analysis = analyze_password(password)
        entropy = calculate_entropy(password)
        crack = estimate_crack_time(password, entropy["entropy_bits"])
        recs = get_recommendations(analysis)

        strength = analysis["strength"]
        s_class = {
            "Weak": "s-weak",
            "Medium": "s-medium",
            "Strong": "s-strong",
            "Very Strong": "s-vstrong",
        }.get(strength, "s-weak")

        st.markdown("<br>", unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.markdown(f"""
            <div class="glass">
                <div class="glass-label">Strength</div>
                <div class="glass-value {s_class}">{strength}</div>
            </div>
            """, unsafe_allow_html=True)

        with m2:
            st.markdown(f"""
            <div class="glass">
                <div class="glass-label">Security Score</div>
                <div class="score-big">{analysis['score']}<span style="font-size:1rem;color:#64748b"> /100</span></div>
            </div>
            """, unsafe_allow_html=True)
            st.progress(analysis["score"] / 100)

        with m3:
            st.markdown(f"""
            <div class="glass">
                <div class="glass-label">Entropy</div>
                <div class="glass-value">{entropy['entropy_bits']} <span style="font-size:0.9rem;color:#64748b">bits</span></div>
                <div class="glass-sub">{entropy['classification']}</div>
            </div>
            """, unsafe_allow_html=True)

        with m4:
            st.markdown(f"""
            <div class="glass">
                <div class="glass-label">Crack Time</div>
                <div class="glass-value" style="font-size:1.3rem">{crack['primary']}</div>
                <div class="glass-sub">Offline GPU cluster</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-h">Complexity Checks</div>', unsafe_allow_html=True)

        pills_html = ""
        for label, passed in analysis["checks"].items():
            cls = "pill-yes" if passed else "pill-no"
            icon = "✓" if passed else "✗"
            pills_html += f'<span class="pill {cls}">{icon} {label}</span>'
        st.markdown(pills_html, unsafe_allow_html=True)

        st.markdown('<div class="section-h">Attack Scenarios</div>', unsafe_allow_html=True)
        scen = crack["scenarios"]
        t1, t2, t3, t4 = st.columns(4)
        with t1:
            st.metric("Online (throttled)", scen["online_throttled"]["readable"])
        with t2:
            st.metric("Online (no limit)", scen["online_unthrottled"]["readable"])
        with t3:
            st.metric("Offline (bcrypt)", scen["offline_slow_hash"]["readable"])
        with t4:
            st.metric("Offline (GPU)", scen["offline_fast_hash"]["readable"])

        st.markdown('<div class="section-h">Recommendations</div>', unsafe_allow_html=True)
        is_strong = analysis["score"] >= 80
        for r in recs:
            cls = "rec-good" if is_strong else ""
            st.markdown(f'<div class="rec-item {cls}">{r}</div>', unsafe_allow_html=True)

        with st.expander("Technical Details"):
            st.json({
                "Length": analysis["length"],
                "Charset size": entropy["charset_size"],
                "Entropy (bits)": entropy["entropy_bits"],
                "Keyspace": f"{crack['keyspace']:.2e}",
                "Uppercase": analysis["has_upper"],
                "Lowercase": analysis["has_lower"],
                "Digits": analysis["has_digit"],
                "Symbols": analysis["has_symbol"],
                "No common patterns": analysis["no_common_patterns"],
            })

    else:
        st.markdown("""
        <div class="glass" style="text-align:center; padding:2.5rem; margin-top:1rem">
            <p style="font-size:1.1rem; color:#64748b; margin:0">
                Enter a password above to unlock the full security report
            </p>
        </div>
        """, unsafe_allow_html=True)

# ═════════════════════════════════════════════
# PAGE: GENERATOR
# ═════════════════════════════════════════════
elif page == "Generator":

    c1, c2 = st.columns([1, 5])
    with c1:
        st.image("assets/logo.png", width=80)
    with c2:
        st.markdown('<p class="hero-title">Password Generator</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-sub">Cryptographically secure • Built for strength</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown('<div class="section-h">Options</div>', unsafe_allow_html=True)
        length = st.slider("Length", 8, 64, 16)
        include_upper = st.checkbox("Uppercase (A-Z)", value=True)
        include_lower = st.checkbox("Lowercase (a-z)", value=True)
        include_digits = st.checkbox("Numbers (0-9)", value=True)
        include_symbols = st.checkbox("Symbols (!@#$…)", value=True)

        if st.button("Generate Secure Password", use_container_width=True):
            if not any([include_upper, include_lower, include_digits, include_symbols]):
                st.error("Select at least one character type.")
            else:
                pwd = generate_password(length, include_upper, include_lower, include_digits, include_symbols)
                st.session_state["gen_pwd"] = pwd

    with right:
        st.markdown('<div class="section-h">Result</div>', unsafe_allow_html=True)
        if "gen_pwd" in st.session_state:
            pwd = st.session_state["gen_pwd"]
            st.markdown(f'<div class="gen-box">{pwd}</div>', unsafe_allow_html=True)
            st.caption("Select & copy the password above")

            a = analyze_password(pwd)
            e = calculate_entropy(pwd)
            c = estimate_crack_time(pwd, e["entropy_bits"])

            st.markdown("<br>", unsafe_allow_html=True)
            r1, r2 = st.columns(2)
            with r1:
                st.metric("Strength", a["strength"])
                st.metric("Entropy", f"{e['entropy_bits']} bits")
            with r2:
                st.metric("Score", f"{a['score']}/100")
                st.metric("Crack Time", c["primary"])
        else:
            st.markdown("""
            <div class="glass" style="text-align:center; padding:2rem">
                <p style="color:#64748b; margin:0">Configure options and hit Generate</p>
            </div>
            """, unsafe_allow_html=True)

# ═════════════════════════════════════════════
# PAGE: ABOUT
# ═════════════════════════════════════════════
else:
    c1, c2 = st.columns([1, 5])
    with c1:
        st.image("assets/logo.png", width=80)
    with c2:
        st.markdown('<p class="hero-title">About SherpaShield</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-sub">English name. Nepali soul.</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass">
        <p style="font-size:1.05rem; line-height:1.7; color:#cbd5e1; margin:0">
            <b style="color:#60a5fa">Sherpas</b> are the legendary mountain guides of the Himalayas —
            known for unmatched strength, resilience, and protection of those who journey through
            the world's highest peaks.<br><br>
            <b style="color:#60a5fa">SherpaShield</b> carries that same spirit into the digital world:
            guiding users to stronger passwords and shielding them from cyber threats.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-h">Core Modules</div>', unsafe_allow_html=True)

    mods = [
        ("Strength Analysis", "Length, character classes & common patterns"),
        ("Security Score", "0–100 score from multiple criteria"),
        ("Entropy Calculator", "Randomness measured in bits"),
        ("Crack Time Estimator", "Brute-force time under 4 attack scenarios"),
        ("Password Generator", "Cryptographically secure random passwords"),
        ("Recommendations", "Actionable advice tailored to your password"),
    ]
    cols = st.columns(3)
    for i, (title, desc) in enumerate(mods):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="glass" style="margin-bottom:0.8rem; min-height:100px">
                <div style="font-weight:600; color:#e2e8f0; margin-bottom:0.3rem">{title}</div>
                <div style="font-size:0.85rem; color:#64748b">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-h">Stack & Roadmap</div>', unsafe_allow_html=True)
    s1, s2 = st.columns(2)
    with s1:
        st.markdown("""
        <div class="glass">
            <div class="glass-label">Technology</div>
            <p style="color:#cbd5e1; font-size:0.9rem; margin:0.5rem 0 0 0">
                Python 3 · Streamlit · secrets · math · re
            </p>
        </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown("""
        <div class="glass">
            <div class="glass-label">Coming Next</div>
            <p style="color:#cbd5e1; font-size:0.9rem; margin:0.5rem 0 0 0">
                Pwned check · History analysis · AI advisor
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("SherpaShield · Educational cybersecurity project · Built with Python & Streamlit")
