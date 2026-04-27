import streamlit as st

# ---------------- TITLE ----------------
st.title("🛒 StudX AI Deal Marketplace")
st.write("Find the best student deals based on your needs & budget")

# ---------------- INPUTS ----------------
user_type = st.selectbox("User Type", ["student", "gamer", "shopper"])
product_input = st.text_input("What are you looking for?")
budget = st.slider("Budget", 500, 5000, 3000)

# ---------------- STUDX PRODUCT DATABASE ----------------
products = [
    {"name": "Casual Shirt (Student Seller)", "price": 1200, "original": 2000, "keywords": ["shirt", "fashion"]},
    {"name": "Formal Shirt (Campus Sale)", "price": 2500, "original": 3500, "keywords": ["shirt", "fashion"]},
    {"name": "Sports Shoes (Used - Good Condition)", "price": 2499, "original": 4000, "keywords": ["shoes", "fashion"]},
    {"name": "Gaming Headset (Student Deal)", "price": 1999, "original": 3000, "keywords": ["gaming", "gamer"]},
    {"name": "Smart Gadget (Tech Club Sale)", "price": 2199, "original": 3200, "keywords": ["gadget", "tech"]},
]

# ---------------- BUTTON ----------------
if st.button("🚀 Generate Smart Deal"):

    results = []
    query = product_input.lower()

    # ---------------- MATCHING LOGIC ----------------
    for p in products:
        if p["price"] <= budget:
            if any(k in query or query in k for k in p.get("keywords", [])):
                results.append(p)

    # ---------------- OUTPUT ----------------
    if results:
        st.success("🎯 Deals Found!")

        # Sort by best price
        results = sorted(results, key=lambda x: x["price"])

        for p in results:
            st.markdown("---")

            discount = int((p["original"] - p["price"]) / p["original"] * 100)

            st.write(f"🛒 **{p['name']}**")
            st.write(f"💰 Price: ₹{p['price']}")
            st.write(f"🔥 {discount}% OFF (₹{p['original']} → ₹{p['price']})")

            # Why this deal
            st.write(f"💡 Matches your search '{product_input}' under ₹{budget}")

        # ---------------- MARKETING CONTENT ----------------
        best = results[0]

        st.markdown("## 📢 Marketing Content")
        st.write(f"Instagram: Don’t miss this {best['name']} now at ₹{best['price']} 🚀")
        st.write(f"Push: Limited Deal! Grab {best['name']} at ₹{best['price']}")
        st.write(f"Email: Exclusive Deal Alert – {best['name']} at ₹{best['price']}")
        st.write(f"SEO: Best {product_input} under ₹{budget}")

        # ---------------- INSIGHT ----------------
        st.markdown("## 📊 Insight")
        st.write(f"This deal targets **{user_type} users**, increasing engagement.")

    else:
        st.error("❌ No deals found within your budget")