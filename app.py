import streamlit as st

st.set_page_config(
    page_title="Rama Krishna | AI Systems Builder",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

/* Dark theme */
.stApp {
    background-color: #0E1117;
    color: #FAFAFA;
}

/* fade animation */
.fade-in {
    animation: fadeIn 1.2s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

/* gradient name */
.gradient-text {
    background: linear-gradient(90deg, #00F5A0, #00D9F5, #7A5FFF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}

/* profile image */
img {
    border-radius: 50%;
    border: 3px solid rgba(0,255,200,0.6);
    object-fit: cover;
    aspect-ratio: 1 / 1;
}

/* glass cards */
.glass {
    background: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.08);
    transition: 0.3s ease;
    margin-bottom: 16px;
}

.glass:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,255,200,0.25);
}

/* buttons */
.custom-btn {
    padding: 8px 18px;
    border-radius: 10px;
    border: 1px solid rgba(0,255,200,0.4);
    background: transparent;
    color: white !important;
    text-decoration: none !important;
    transition: 0.3s ease;
}

.custom-btn:hover {
    background: rgba(0,255,200,0.2);
    border-color: rgba(0,255,200,0.8);
    transform: translateY(-2px);
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
col1, col2 = st.columns([1, 2])

with col1:
    st.image("profile.jpg", width=220)

with col2:
    st.markdown('<h1 class="gradient-text fade-in">Rama Krishna Vullaganti</h1>', unsafe_allow_html=True)
    st.markdown('<div class="fade-in">AI Product Builder • Agentic Systems Architect • Senior AI Tech Manager</div>', unsafe_allow_html=True)
    st.write("I design intelligent systems that **think, decide, and automate real business workflows.**")

    st.markdown("""
    <div style="display:flex; gap:10px; margin-top:10px;">
        <a href="https://www.linkedin.com/in/ramakrishnavullaganti" target="_blank" class="custom-btn">🔗 LinkedIn</a>
        <a href="https://github.com/ramakrishna2512" target="_blank" class="custom-btn">💻 GitHub</a>
        <a href="mailto:ramakrishnavullaganti@gmail.com" class="custom-btn">✉️ Email</a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------- PROBLEM ----------
st.markdown('<h2 class="fade-in">⚡ The Problem I Solve</h2>', unsafe_allow_html=True)

st.write("""
Businesses don’t need more chatbots.

They need intelligent systems that:

✔ reduce operational load  
✔ automate workflows  
✔ assist decision making  
✔ scale intelligence across teams  
""")

st.divider()

# ---------- AI SYSTEMS ----------
st.markdown('<h2 class="fade-in">⚙️ AI Systems I Build</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="glass fade-in">
🧠 <b>AI Agents</b><br>
Autonomous decision systems with memory & tools
</div>

<div class="glass fade-in">
⚡ <b>Automation Intelligence</b><br>
Workflow automation & operational optimization
</div>

<div class="glass fade-in">
📊 <b>LLM Business Systems</b><br>
AI-powered analytics & decision support
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------- SIGNATURE PROJECTS ----------
st.markdown('<h2 class="fade-in"> Signature Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "title": "Smart Navigation AI Chatbot",
        "problem": "Users struggled to find relevant information quickly.",
        "solution": "Built an NLP-powered routing chatbot to guide users intelligently.",
        "impact": "Achieved 98% routing accuracy and improved conversions.",
        "tech": "NLP • Decision Logic • zapier"
    },
    {
        "title": "AI Email Intelligence System",
        "problem": "Manual email triage slowed response times.",
        "solution": "Developed NLP classification to prioritize emails automatically.",
        "impact": "Reduced manual workload by 50%.",
        "tech": "NLP • Automation • zapier"
    },
    {
        "title": "AI Marketing Intelligence Engine",
        "problem": "Campaign planning required heavy manual research.",
        "solution": "Built AI assistant generating insights from market data.",
        "impact": "Accelerated planning workflows by 40%.",
        "tech": "LLMs • Data Synthesis • Automation"
    },
]

for p in projects:
    st.markdown(f"""
    <div class="glass fade-in">
        <h4>{p['title']}</h4>
        <p><b>Problem:</b> {p['problem']}</p>
        <p><b>Solution:</b> {p['solution']}</p>
        <p><b>Impact:</b> {p['impact']}</p>
        <small>{p['tech']}</small>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------- GITHUB PROJECTS ----------
st.markdown('<h2 class="fade-in"> GitHub Projects</h2>', unsafe_allow_html=True)

repos = [
    ("AI Agents Hub",
     "Collection of local AI agents for workflow automation.",
     "Build and test autonomous AI workflows locally.",
     "Python • AI Agents",
     "https://github.com/ramakrishna2512/ai-agents-hub"),

    ("Prompt Rewriter",
     "Improves prompt clarity for better AI responses.",
     "Enhances accuracy of AI outputs.",
     "JavaScript • Cloudflare",
     "https://github.com/ramakrishna2512/prompt-rewriter-cloudflare"),

    ("Email Writer",
     "AI system that generates professional email drafts.",
     "Improves communication productivity.",
     "AI • Automation",
     "https://github.com/ramakrishna2512/email-writer-cloudflare-backend"),

    ("Prompt Playground",
     "Environment for saving and testing prompts.",
     "Speeds up prompt experimentation.",
     "Python • Prompt Engineering",
     "https://github.com/ramakrishna2512/Prompt-playground"),
]

for name, desc, value, tech, link in repos:
    st.markdown(f"""
    <div class="glass fade-in">
        <h4>{name}</h4>
        <p><b>Overview:</b> {desc}</p>
        <p><b>Value:</b> {value}</p>
        <small>{tech}</small><br><br>
        <a href="{link}" target="_blank" class="custom-btn">View Repository</a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------- CONTACT ----------
st.markdown('<h2 class="fade-in">Let’s Build Intelligence That Works</h2>', unsafe_allow_html=True)

st.write("""
If you're building AI products, scaling automation, or exploring agentic systems — let’s collaborate.
""")

st.link_button("Connect on LinkedIn", "https://www.linkedin.com/in/ramakrishnavullaganti")