import streamlit as st
from openai import OpenAI

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support Assistant")

# --------------------------------------------------
# OPENAI CLIENT
# --------------------------------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# --------------------------------------------------
# PRODUCT CATALOG
# --------------------------------------------------
products = st.session_state.get(
    "products",
    [
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
)

# --------------------------------------------------
# BUILD PRODUCT CATALOG TEXT
# --------------------------------------------------
catalog_text = ""

for product in products:
    catalog_text += f"""
Product: {product['name']}
Category: {product['category']}
Price: ₹{product['price']}
Description: {product['description']}
"""

# --------------------------------------------------
# SYSTEM PROMPT
# --------------------------------------------------
SYSTEM_PROMPT = f"""
You are MiniStore's professional customer support assistant.

Your role is to help customers with:
- Products
- Product pricing
- Product information
- Orders
- Order status
- Delivery and shipping
- Returns
- Refunds
- Payment methods

Store Product Catalog:
{catalog_text}

Rules:
1. Only answer questions related to MiniStore.
2. If a user asks unrelated questions such as:
   - coding
   - math
   - politics
   - celebrities
   - general knowledge
   - school assignments
   politely explain that you can only assist with MiniStore support.

3. Be concise and professional.
4. Always prioritize customer support.
5. If information is unavailable, say so clearly.
"""

# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------
user_input = st.chat_input(
    "Ask about products, orders, delivery, refunds..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        messages.extend(st.session_state.messages)

        try:

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.3
            )

            assistant_reply = (
                response.choices[0]
                .message
                .content
            )

            response_placeholder.markdown(
                assistant_reply
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": assistant_reply
                }
            )

        except Exception as e:

            error_message = (
                f"Error contacting OpenAI API:\n\n{e}"
            )

            response_placeholder.error(
                error_message
            )