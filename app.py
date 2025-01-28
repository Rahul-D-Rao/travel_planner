import streamlit as st
import json
import boto3
from credentials import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, MODEL_ARN
from prompts import get_initial_prompt, refine_input_prompt, generate_itinerary_prompt

# AWS Bedrock client configuration
def interact_with_bedrock(input_text):
    """
    Interact with AWS Bedrock for generative AI tasks.
    Args:
        input_text (str): Input text to send to AWS Bedrock.
    Returns:
        str: Response from AWS Bedrock.
    """
    try:
        # Create a Bedrock Runtime client using boto3
        client = boto3.client(
            'bedrock-runtime',
            region_name=AWS_REGION,  # Ensure this is the correct region
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

        # Use the model ARN (replace with the actual ARN)
        model_arn = MODEL_ARN
        # Prepare the payload (JSON format)
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"text": input_text}
                    ]
                }
            ]
        }

        # Convert the payload to JSON
        payload_json = json.dumps(payload)

        # Invoke the Bedrock model
        response = client.invoke_model(
            modelId=model_arn,  # Using model ARN in the request
            body=payload_json,
            contentType="application/json",
            accept="application/json",
        )

        # Parse the response body
        response_body = response["body"].read().decode("utf-8")
        result = json.loads(response_body)

        # Extract the text from the result
        if 'output' in result and 'message' in result['output'] and 'content' in result['output']['message']:
            for item in result['output']['message']['content']:
                if 'text' in item:
                    return item['text']

        return "No response received from the model."

    except Exception as e:
        raise RuntimeError(f"Failed to interact with AWS Bedrock: {e}")

# Streamlit App UI
st.title("AI-Powered Travel Planner")
st.markdown("Plan your next adventure with a personalized travel itinerary!")

# Step 1: Gather Initial Inputs
st.header("Step 1: Basic Details")
destination = st.text_input("Where are you planning to go?")
trip_duration = st.number_input("How many days is your trip?", min_value=1, step=1)
budget = st.selectbox("What's your budget?", ["Budget", "Moderate", "Luxury"])
purpose = st.selectbox("What's the purpose of your trip?", ["Relaxation", "Adventure", "Cultural Experience", "Other"])
preferences = st.text_area("Any specific preferences (e.g., food, activities, pace)?")

if st.button("Submit Basic Details"):
    if not destination:
        st.warning("Please enter a destination.")
    elif trip_duration <= 0:
        st.warning("Please enter a valid trip duration.")
    else:
        initial_prompt = get_initial_prompt(destination, trip_duration, budget, purpose, preferences)
        
        try:
            # Query Amazon Bedrock and get the response
            st.session_state['response'] = interact_with_bedrock(initial_prompt)
            st.success("Basic details submitted. Refine your inputs in Step 2.")
        except RuntimeError as e:
            st.error(f"An error occurred: {e}")

# Step 2: Refine Inputs
if 'response' in st.session_state:
    st.header("Step 2: Refine Your Details")
    st.markdown(st.session_state['response'])
    dietary_preferences = st.text_input("Dietary Preferences (e.g., vegetarian, no restrictions)")
    mobility_concerns = st.text_input("Mobility Concerns (e.g., walking distance)")
    accommodation = st.selectbox("Accommodation Preference", ["Budget", "Luxury", "Central Location"])
    specific_interests = st.text_area("Specific Interests (e.g., hidden gems, landmarks)")

    if st.button("Submit Refinement"):
        if not dietary_preferences and not mobility_concerns and not specific_interests:
            st.warning("Please provide at least one refinement detail.")
        else:
            refine_prompt = refine_input_prompt(dietary_preferences, mobility_concerns, accommodation, specific_interests)
            
            try:
                # Query Amazon Bedrock and get the refined itinerary
                st.session_state['itinerary'] = interact_with_bedrock(refine_prompt)
                st.success("Refinement complete. Generate your itinerary in Step 3.")
            except RuntimeError as e:
                st.error(f"An error occurred: {e}")

# Step 3: Generate Itinerary
# Step 3: Generate Itinerary
if 'itinerary' in st.session_state:
    st.header("Step 3: Your Personalized Travel Itinerary")
    
    # The itinerary will be in Markdown format, so we use st.markdown to display it properly
    itinerary_text = st.session_state['itinerary']
    
    # Displaying the formatted itinerary text with Markdown rendering
    st.markdown(itinerary_text)

    st.success("Itinerary generated! Enjoy your trip.")

st.markdown("### Built with [Amazon Bedrock](https://aws.amazon.com/bedrock/) and [Streamlit](https://streamlit.io/)")