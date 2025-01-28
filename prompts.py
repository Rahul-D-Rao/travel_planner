# prompts.py

def get_initial_prompt(destination, trip_duration, budget, purpose, preferences):
    """Generates the initial prompt for basic trip details."""
    return f"""
    I am planning a trip. Here are the details:
    - Destination: {destination}
    - Duration: {trip_duration} days
    - Budget: {budget}
    - Purpose: {purpose}
    - Preferences: {preferences}
    
    Can you suggest a personalized travel itinerary?
    """

def refine_input_prompt(dietary_preferences, mobility_concerns, accommodation, specific_interests):
    """Generates the prompt for refining user inputs."""
    return f"""
    Here are additional preferences for my trip:
    - Dietary Preferences: {dietary_preferences}
    - Mobility Concerns: {mobility_concerns}
    - Accommodation: {accommodation}
    - Specific Interests: {specific_interests}
    
    Please use these details to refine my itinerary.
    """

def generate_itinerary_prompt():
    """Final step for generating the day-by-day itinerary."""
    return "Using all provided details, generate a detailed, day-by-day travel itinerary."