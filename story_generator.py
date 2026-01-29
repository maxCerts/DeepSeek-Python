import ollama
import textwrap
import time

def generate_story(prompt: str, choices: int = 3) -> tuple[str, list[str]]:
    """
    Generate story segment and choices
        - current story textfont
        - list of choice prompts
    """
    response = ollama.generate(
        model="deepseek-r1:8b",
        prompt=f"""Continue this interactive story with {choices} choices:
    {prompt}
    
    Format exactly like this:
    STORY: [1 paragraph advancing the plot]
    CHOICE 1: [action]
    CHOICE 2: [action]
    CHOICE 3: [action]"""
    ).get('response', '')

    story_part = ""
    choices_list = []
    for line in response.split('\n'):
        if line.startswith("STORY:"):
            story_part = line[6:].strip()
        elif line.startswith ('CHOICE'):
            choices_list.append(line.split(':', 1)[1].strip())

    return story_part,choices_list

def display_story(text: str, width: int = 70):
    print("\n" + " STORY ".center(width, "~"))
    print(textwrap.fill(text, width=width))
    print("~" * width)

def display_choices(choices: list[str]):
    print("\n" + " WHAT WILL YOU DO? ".center(50, " "))
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    print()

def game_loop():
    print("\n" + " AI STORYTELLER ".center(50, "="))
    print("Type 'quit' anytime to exit")

    genre = input("choose genre (fantasy/sci-fi/horror): ").lower()
    character = input("Your character name: ")
    current_story = f"Genre: {genre}\nMain character: {character}"

    while True:
        story_text, choices = generate_story(current_story)
        if not story_text:
            print("Error generating story. Try again. ")
            break

        display_story(story_text)

        if not choices:
            print("\nTHE END".center(50, "*"))
            break

        display_choices(choices)

        while True:
            choice = input("Your Choice: ").strip().lower()
            if choice == 'quit':
                print("\nThanks for playing!")
                return

            if choice.isdigit() and 1 <= int(choice) <= int(choice):
                current_story += f"\nChoice: {choices[int(choice) -1]}\n"
                print("\n" + " Generating the next chapter....".center(50))
                time.sleep(1)
                break

            print(f"Please enter 1-{len(choices)}")

if __name__ == "__main__":
    game_loop()


