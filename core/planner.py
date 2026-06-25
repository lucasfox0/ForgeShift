import os
from dotenv import load_dotenv
from openai import OpenAI
from data.models import ShiftInput

# Get OPENAI API key
load_dotenv()
key = os.getenv("OPENAI_API_KEY")
if not key:
    raise ValueError("API key not found")

client = OpenAI()

def generate_plan(shift_input):
    plan = client.responses.create(
        model="gpt-4o-mini",
        input=f"The user is a retail professional looking for help with prioritizing their shift. Their shift starts at {shift_input.shift_start} and ends at {shift_input.shift_end}. The context they provided today is {shift_input.context}. The list of tasks they have to do are {shift_input.tasks}. I would like you to prioritize this list and return it with simply just the tasks in order of importance, and then also predict the time it will take per task."
    )

    return plan

if __name__ == "__main__":
    from cli.input import get_input
    shift_input = get_input()
    result = generate_plan(shift_input)
    print(result.output_text)