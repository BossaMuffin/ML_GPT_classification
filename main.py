# pip install --upgrade openai
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')
# or
# in shell CLI : export OPENAI_API_KEY="<OPENAI_API_KEY>"
# openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_prompt(words_list: list):
    words_str: str = " ".join(words_list)
    return """As the examples below, name the last list of words with a topic that represents them :
    Example 1 :
        Words: "Algorithm robots", "Uploading patients", "Driving scenario", "Facial animation", "Prototype hybrid", "Planar robots"
        Expression: "Robotics"
    Example 2 :
        Words: "Learn noisy", "Learning safe", "Enables models", "Efficiently eliciting", "Extrapolation errors", "Proposed model", "Robustly learning"
        Expression: "Machine Learning"
    Example 3 :
        Words: "Quantum algorithmic", "Selection algorithm", "Neuromorphic chips", "Quantum gates", "Algorithms hard", "Deep autoencoders", "Accelerating convolutional", "Android malware"
        Expression: "Computer Science"
    Your job :
        Words: {}
        Them:""".format(words_str)


def find_closest_word(context: str, words_list: list, temperature: int):
    answer = {
        "topic": "default",
        "tokens": {}
    }
    query = context + generate_prompt(words_list)
    response = openai.Completion.create(
        model="text-davinci-003",
        # model="text-babbage-001",
        prompt=query,
        temperature=temperature,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    answer["topic"] = response.choices[0].text
    answer["tokens"]["completion"] = response.usage.completion_tokens
    answer['tokens']["prompt"] = response.usage.prompt_tokens
    #return re.sub('[^a-zA-Z0-9 \n\.]', '', answer).strip()
    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Permet de définir le comportement que l'assistant doit adopter
    context = "Tu es un développeur Python"

    # To name
    # X1
    lists_to_name = [
        ["robot needs", "robot position", "itself robot", "robot experiments", "robot interaction", "robot experimental"],  # Y1 = Robotic Experimentation
        ["training with", "training dynamics", "adversarial training", "training accuracy", "longer training"], # Y2 = Machine Learning Training
        ["taxing process", "reconstruction process", "mri reconstruction", "reconstruction benchmarks"], # Y3 = Image Reconstruction
        ["learning dexterous", "learning linear", "robust learning", "in learning", "learning combined", "prototypes learning", "organizing learning", "improved learning", "learning networks", "learning properties", "generalized learning"], # Y4 = Machine Learning
        ["new scenes", "new approaches", "new spectralnet", "new demands"] # Y5 = New Technology
    ]
    for list_of_words in lists_to_name[:1]:
        print(f"X{1} ={list_of_words}")
        closest_words = find_closest_word(context, list_of_words, temperature=0)
        print(f"Y{1} ={closest_words}")

    print("__EOF")

