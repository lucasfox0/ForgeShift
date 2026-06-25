from cli.input import get_input
from cli.output import remove_formatting
from core.planner import generate_plan

if __name__ == "__main__":
    shift_input = get_input()
    result = generate_plan(shift_input)
    print(remove_formatting(result.output_text))