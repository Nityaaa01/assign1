import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------------------------
# PRODUCT DATA
# --------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2499,
        "description": "Premium noise-cancelling headphones with crystal-clear sound.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 3999,
        "description": "Track fitness, notifications, and health metrics on the go.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 2999,
        "description": "Lightweight and comfortable shoes for everyday training.",
        "category": "Fashion"
    },
    {
        "name": "Backpack",
        "price": 1499,
        "description": "Durable travel backpack with multiple storage compartments.",
        "category": "Accessories"
    },
    {
        "name": "Coffee Maker",
        "price": 3499,
        "description": "Brew fresh coffee at home with one-touch convenience.",
        "category": "Home"
    },
    {
        "name": "Bluetooth Speaker",
        "price": 1999,
        "description": "Portable speaker with rich bass and long battery life.",
        "category": "Electronics"
    }
]

# Store products for chatbot access
st.session_state["products"] = products

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "cart_count" not in st.session_state:
    st.session_state.cart_count = 0

if "cart_total" not in st.session_state:
    st.session_state.cart_total = 0

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>
/* Lava Lamp Background */
.stApp {
    background: linear-gradient(
        -45deg,
        #ff9ff3,
        #d980fa,
        #c56cf0,
        #7d5fff,
        #18dcff
    );
    background-size: 400% 400%;
    animation: lavaGradient 15s ease infinite;
}

@keyframes lavaGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero {
    background: linear-gradient(135deg,#4f46e5,#7c3aed);
    padding:40px;
    border-radius:15px;
    color:White;
    text-align:center;
    margin-bottom:25px;
}

.product-card{
    background:linear-gradient(135deg, #667eea, #764ba2 100%);
    padding:20px;
    border-radius:12px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.support-button{
    position:fixed;
    bottom:20px;
    right:20px;
    background:#4f46e5;
    color:white;
    padding:15px 20px;
    border-radius:50px;
    font-weight:bold;
    z-index:999;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set(p["category"] for p in products))
)

selected_category = st.sidebar.selectbox(
    "Categories",
    categories
)

st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Cart Summary")
st.sidebar.write(f"Items: {st.session_state.cart_count}")
st.sidebar.write(f"Total: ₹{st.session_state.cart_total}")

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown("""
<div class='hero'>
<h1>🛒 Welcome to MiniStore</h1>
<p>Discover premium products at affordable prices.</p>
</div>
""", unsafe_allow_html=True)

st.header("⭐ Featured Products")

# --------------------------------------------------
# FILTER PRODUCTS
# --------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# --------------------------------------------------
# PRODUCT GRID
# --------------------------------------------------
cols = st.columns(3)

for i, product in enumerate(filtered_products):

    with cols[i % 3]:

        st.markdown(f"""
        <div class='product-card'>
            <h3>{product['name']}</h3>
            <h4>₹{product['price']}</h4>
            <p>{product['description']}</p>
            <small>{product['category']}</small>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            f"Add to Cart",
            key=product["name"]
        ):
            st.session_state.cart_count += 1
            st.session_state.cart_total += product["price"]
            st.success("Added to cart!")

# --------------------------------------------------
# FLOATING SUPPORT BUTTON
# --------------------------------------------------
st.markdown("""
<a href="/Support_Chatbot" target="_self">
    <div class="support-button">
        💬 Support
    </div>
</a>
""", unsafe_allow_html=True)
