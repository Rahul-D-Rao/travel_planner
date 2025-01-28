# AI-Powered Travel Planner

## Overview

This is a travel planner that uses Amazon Bedrock's AI models to generate a personalized travel itinerary. The app gathers user inputs, refines preferences, and generates a day-by-day trip plan. It integrates AWS Bedrock for advanced AI capabilities.

## File Structure

- `app.py`: Main application code.
- `credentials.py`: Consist of AWS Credentials.
- `prompts.py`: Contains prompt templates.
- `requirements.txt`: Dependencies.

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Rahul-D-Rao/travel_planner.git
   cd travel_planner
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up AWS Credentials**:
   Create a `credentials.py` file with your AWS access key, Model ARN, AWS Region and secret key:

   ```python
   AWS_ACCESS_KEY_ID = "your_access_ID"
   AWS_SECRET_ACCESS_KEY = "your_secret_access_key"
   AWS_REGION = "your_aws_region"
   MODEL_ARN = "your_model_arn"
   ```

4. **Run the application**:

   ```bash
   streamlit run app.py
   ```

5. **Access the app**:
   Open your browser and go to `http://localhost:8501`.

## Testing

- Enter trip details, refine preferences, and see a complete, personalized itinerary.

## Example Usage

**Input**:

- Destination: Paris
- Duration: 5 days
- Budget: Moderate
- Purpose: Cultural Experience
- Preferences: Art, history, and relaxation.

**Output**:

- A detailed day-by-day itinerary with activities and recommendations.

## Hosting on Streamlit Cloud

1. Push the project to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Link your repository and deploy.
4. Share the live app link for users to access.

## Credits

Built using:

- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Streamlit](https://streamlit.io/)
