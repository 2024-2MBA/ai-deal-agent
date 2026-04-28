import streamlit as st

# Page config
st.set_page_config(page_title="StudX AI Marketplace", layout="centered")

# Title
st.title("🛒 StudX AI Deal Marketplace")
st.write("Find the best student deals based on your needs & budget")

# Inputs
user_type = st.selectbox("User Type", ["student", "gamer", "shopper"])
product_input = st.text_input("What are you looking for?")
budget = st.slider("Budget", 500, 5000, 3000)

# Product database (with images + original price)
products = [
    {
        "name": "Casual Shirt",
        "price": 1200,
        "original": 2000,
        "keywords": ["shirt", "fashion"],
        "seller": "Student Seller",
        "image": "https://via.placeholder.com/150"
    },
    {
        "name": "Formal Shirt",
        "price": 2500,
        "original": 3500,
        "keywords": ["shirt", "fashion"],
        "seller": "Campus Sale",
        "image": "https://via.placeholder.com/150"
    },
    {
        "name": "Sports Shoes",
        "price": 2499,
        "original": 4000,
        "keywords": ["shoes", "fashion"],
        "seller": "Senior Seller",
        "image": "https://via.placeholder.com/150"
    },
    {
        "name": "Gaming Headset",
        "price": 1999,
        "original": 3000,
        "keywords": ["gaming", "gamer"],
        "seller": "Tech Club",
        "image": "https://via.placeholder.com/150"
    },
    {
        "name": "Smart Gadget",
        "price": 2199,
        "original": 3500,
        "keywords": ["gadget", "tech"],
        "seller": "Student Store",
        "image": "https://via.placeholder.com/150"
    }
]

# Button
if st.button("🚀 Generate Smart Deal"):

    if not product_input:
        st.warning("⚠️ Please enter what you're looking for")
    else:
        results = []

        # Matching logic
        for p in products:
            if p["price"] <= budget:
                if any(k in product_input.lower() for k in p["keywords"]):
                    results.append(p)

        # Output
        if results:
            st.success("🎯 Best Deals Found!")

            for p in results:
                discount = int(((p["original"] - p["price"]) / p["original"]) * 100)
                savings = p["original"] - p["price"]

                # Card layout
                st.markdown("---")
                col1, col2 = st.columns([1, 2])

                with col1:
                    st.image(p["image"], width=120)

                with col2:
                    st.subheader(f"{p['name']} ({p['seller']})")
                    st.write(f"💰 Price: ₹{p['price']}")
                    st.write(f"🔥 {discount}% OFF (₹{p['original']} → ₹{p['price']})")
                    st.write(f"💸 You save ₹{savings}")
                    st.write(f"💡 Matches your search '{product_input}' under ₹{budget}")

            # Marketing Content
            best = results[0]
            st.markdown("---")
            st.subheader("📢 Marketing Content")

            st.write(f"Instagram: Don’t miss this {best['name']} now at ₹{best['price']} 🚀")
            st.write(f"Push: Limited Deal! Grab {best['name']} at ₹{best['price']}")
            st.write(f"Email: Exclusive Deal Alert – {best['name']} at ₹{best['price']}")
            st.write(f"SEO: Best {product_input} under ₹{budget}")

            # Insight
            st.markdown("---")
            st.subheader("📊 Insight")
            st.write(f"This deal targets **{user_type} users**, increasing engagement.")

        else:
            st.error("❌ No matching deals found")