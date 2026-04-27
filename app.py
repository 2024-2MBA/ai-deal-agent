import streamlit as st
import re

# Page config
st.set_page_config(page_title="AI Deal Agent", layout="wide")

# ------------------ UI STYLING ------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

/* Headings */
h1, h2, h3 {
    color: #ffffff !important;
}

/* Cards */
.card {
    background: rgba(30, 41, 59, 0.95);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.6);
    margin-bottom: 20px;
}

/* Highlight */
.highlight {
    color: #22c55e;
    font-size: 22px;
    font-weight: bold;
}

/* Button */
.stButton > button {
    background: #22c55e;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

/* Inputs */
input, textarea {
    background-color: #1e293b !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.title("🚀 AI Deal Discovery & Marketing Agent")
st.caption("Simulating AI-powered personalization for e-commerce")

# ------------------ INPUTS ------------------
col1, col2 = st.columns(2)

with col1:
    user_type = st.selectbox("👤 User Type", ["gamer", "student", "fashion", "tech"])

with col2:
    budget = st.slider("💰 Budget (₹)", 500, 10000, 3000)

product = st.text_input("🔍 What are you looking for?", "shoes")
products = [
    {"name": "Casual Shirt", "price": 1200, "category": "fashion"},
    {"name": "Formal Shirt", "price": 2500, "category": "fashion"},
    {"name": "Nike Sneakers", "price": 2800, "category": "fashion"},
    {"name": "Gaming Headset", "price": 1999, "category": "gamer"},
    {"name": "Laptop Stand", "price": 1500, "category": "student"},
]

# ------------------ GENERATE DEAL ------------------
if st.button("🚀 Generate Smart Deal"):

    deal = ""
    price = ""
    marketing = ""
    insight = ""

    # Deal logic
    products = [
    {"name": "Casual Shirt", "price": 1200, "keywords": ["shirt", "fashion"]},
    {"name": "Formal Shirt", "price": 2500, "keywords": ["shirt", "fashion"]},
    {"name": "Sports Shoes", "price": 2499, "keywords": ["shoes", "fashion"]},
    {"name": "Gaming Headset", "price": 1999, "keywords": ["gaming", "gamer"]},
    {"name": "Smart Gadget", "price": 2199, "keywords": ["gadget", "tech"]},
]

results = []

for p in products:
    if p["price"] <= budget:
        for k in p["keywords"]:
            if k in product.lower():
                results.append(p)

if results:
    selected = results[0]
    deal = f"🔥 {selected['name']}"
    price = f"₹{selected['price']}"
else:
    deal = "❌ No matching product found"
    price = ""

    # Marketing content
    marketing = f"""
📢 Instagram: Don’t miss this! {deal} now at {price} 🚀  
🔔 Push: Limited Deal! Grab {deal} at {price}  
📧 Email: Exclusive Deal Alert – {deal} at {price}  
🌐 SEO: Best {product} under ₹{budget}. Limited offer!
"""

    # Insight
    insight = f"""
This deal targets **{user_type} users**, increasing engagement.

📈 CTR Boost: +18% to +25%  
💰 Conversion Increase: +8% to +12%  
🎯 Strong price-value perception drives clicks
"""

    # ------------------ OUTPUT ------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
        <h3>🔥 Recommended Deal</h3>
        <p>{deal}</p>
        <p class="highlight">{price}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
        <h3>📢 Marketing Content</h3>
        <p>{marketing}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
        <h3>📊 AI Insights</h3>
        <p>{insight}</p>
        </div>
        """, unsafe_allow_html=True)

# ------------------ AI ASSISTANT ------------------
st.markdown("## 🤖 AI Deal Assistant")

user_query = st.text_input("Ask something (e.g., best shoes under 3000)")

if user_query:

    response = ""

    # Extract budget
    match = re.search(r'\d+', user_query)
    if match:
        query_budget = int(match.group())
        response += f"💡 Showing deals under ₹{query_budget}\n\n"

    # Smart recommendations
    if "shoes" in user_query.lower():
        response += "👟 Best Pick: Sports Shoes at ₹2,499\n"
    elif "gaming" in user_query.lower():
        response += "🎧 Best Pick: Gaming Headset at ₹1,999\n"
    elif "fashion" in user_query.lower():
        response += "🧥 Best Pick: Jacket at ₹2,799\n"
    else:
        response += "✨ Try searching: gaming, shoes, fashion\n"

    response += "\n📈 High CTR expected due to pricing + demand."

    st.success(response)

# ------------------ EXTRA AI INSIGHT ------------------
st.markdown("### 🧠 Why this works")

st.info("""
This app simulates **AI-driven personalization engines** used by platforms like Amazon & Flipkart.

✔ User segmentation  
✔ Budget-based filtering  
✔ Dynamic marketing content generation  
✔ Conversion-focused recommendations  
""")

