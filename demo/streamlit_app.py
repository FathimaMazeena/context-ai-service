import httpx
import streamlit as st


API_URL = "http://127.0.0.1:8000/api/v1/chat"


st.set_page_config(
    page_title="E-Commerce AI Assistant",
    page_icon="🛍️",
    layout="centered"
)

st.title("E-Commerce AI Assistant")

st.caption(
    "Ask questions about products, delivery, "
    "returns, payments and store policies."
)


def ask_ai(message: str) -> dict:
    response = httpx.post(
        API_URL,
        json={
            "message": message
        },
        timeout=60.0
    )

    response.raise_for_status()

    return response.json()


# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display existing conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and message.get("sources")
        ):
            with st.expander("Sources"):
                for source in message["sources"]:
                    st.write(
                        f"{source['source']} "
                        f"({source['document_type']})"
                    )


# Get a new user message
prompt = st.chat_input(
    "Ask a question about our products or policies..."
)


if prompt:
    # Save and display the user's message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the question to FastAPI
    try:
        with st.spinner(
            "Searching our knowledge base..."
        ):
            result = ask_ai(prompt)

        answer = result["answer"]
        sources = result["sources"]

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(answer)

            if sources:
                with st.expander("Sources"):
                    for source in sources:
                        st.write(
                            f"{source['source']} "
                            f"({source['document_type']})"
                        )

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": sources
            }
        )

    except httpx.ConnectError:
        st.error(
            "Unable to connect to the AI service. "
            "Please make sure the FastAPI server is running."
        )

    except httpx.HTTPStatusError:
        st.error(
            "The AI service returned an error."
        )

    except httpx.RequestError:
        st.error(
            "A network error occurred while contacting "
            "the AI service."
        )