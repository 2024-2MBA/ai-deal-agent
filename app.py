import streamlit as st

# Title
st.title("🚀 AI Deal Discovery & Marketing Agent")

# Inputs
user_type = st.selectbox("User Type", ["student", "gamer", "shopper"])
product_input = st.text_input("What are you looking for?")
budget = st.slider("Budget", 500, 5000, 3000)

# Product database
products = [
    {"name": "Casual Shirt", "price": 1200, "keywords": ["shirt", "fashion"]},
    {"name": "Formal Shirt", "price": 2500, "keywords": ["shirt", "fashion"]},
    {"name": "Sports Shoes", "price": 2499, "keywords": ["shoes", "fashion"]},
    {"name": "Gaming Headset", "price": 1999, "keywords": ["gaming", "gamer"]},
    {"name": "Smart Gadget", "price": 2199, "keywords": ["gadget", "tech"]},
]

# Button
if st.button("🚀 Generate Smart Deal"):

    results = []

    query = product_input.lower()

    # Matching logic (fixed + improved)
    for p in products:
        if p["price"] <= budget:
            if any(k in query or query in k for k in p.get("keywords", [])):
                results.append(p)

    # Output
    if results:
        # Sort by price (best deal first)
        results = sorted(results, key=lambda x: x["price"])
        best = results[0]

        deal = best["name"]
        price = f"₹{best['price']}"

        st.success("🎯 Best Deal Found!")
        st.write(f"**Product:** {deal}")
        st.write(f"**Price:** {price}")

        # Marketing Content
        st.subheader("📢 Marketing Content")
        st.write(f"Instagram: Don’t miss this {deal} now at {price} 🚀")
        st.write(f"Push: Limited Deal! Grab {deal} at {price}")
        st.write(f"Email: Exclusive Deal Alert – {deal} at {price}")
        st.write(f"SEO: Best {product_input} under ₹{budget}")

        # Insight
        st.subheader("📊 Insight")
        st.write(f"This deal targets **{user_type} users**, increasing engagement.")

    else:
        st.error("❌ No deals found within your budget")
        