#!/usr/bin/env python3
# coding: utf-8
#!/usr/bin/env python3
# coding: utf-8
"""
Created on January 20th, 2023
@title: Clusters' Topics by GPT
@version: 2
@author: Balthazar Méhus
@society: CentraleSupélec
@abstract: Nommer une liste de mots par une expression le représentant le mieux possible - main script
"""

# pip install --upgrade openai
import openai
import os
import re
from dotenv import load_dotenv


from args import Args

load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')


# or
# in shell CLI : export OPENAI_API_KEY="<OPENAI_API_KEY>"
# openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_prompt(words_list: list):
    words_str: str = " ".join(words_list)
    return """As the examples below, name the last list of words with a topic that represents them :
    Example 1 :
        Words: robot needs, robot position, itself robot, robot experiments, robot interaction, robot experimental
        Expression: Robotic Experimentation
    Example 2 :
        Words: learning dexterous, learning linear, robust learning, in learning, learning combined, prototypes learning, organizing learning, improved learning, learning networks, learning properties, generalized learning
        Expression: Machine Learning
    Example 3 :
        Words: taxing process, reconstruction process, mri reconstruction, reconstruction benchmarks
        Expression: Image Reconstruction
    Your job :
        Words: {}
        Them:""".format(words_str)


def find_closest_word(context: str, words_list: list, temperature: float, model: str):
    # Prepare the answer schema
    answer = {
        "topic": "default",
        "tokens": {}
    }
    # Add the historical context to the query prompt
    query = context + generate_prompt(words_list)
    response = openai.Completion.create(
        model=model,
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
    return answer


def clean_special_chars(string_to_clean: str):
    # Keep only few special chars, plus spaces and comas
    return re.sub(r"[^a-zéèêëâàùûüôöîïA-ZÉÈÊËÂÀÛÜÙÔÖÎÏ0-9 ,']", "", str(string_to_clean))


if __name__ == '__main__':

    try:
        # --------------------------------------- MANAGE ARGS ----------------------------------------
        manage_args = Args()
        argues = {
            # LIST OF WORDS : Cleaned Coma separated words to list
            "words": (clean_special_chars(manage_args.parsed_args.words)).split(","),
            # OPTIONAL MODEL
            "model": str(manage_args.parsed_args.model),
            # OPTIONAL TEMPERATURE
            "temperature": float(manage_args.parsed_args.temperature),
            # OPTIONAL DOMAIN
            "domain": clean_special_chars(str(manage_args.parsed_args.domain))
        }

        # --------------------------------------- RUN ----------------------------------------
        # Permet de définir le comportement que l'assistant doit adopter
        closest_words = find_closest_word(
            context=f"You have been a scientist specializing in {argues['domain']} for 20 years",
            words_list=argues["words"],
            temperature=argues["temperature"],
            model=argues["model"])

        print(closest_words)

    except KeyboardInterrupt:
        print('\n\n[CRITICAL]\tClosing: cause of an unexpected interruption order by keyboard (err: KeyboardInterrupt)')
    except openai.error.APIConnectionError:
        print('\n\n[CRITICAL]\tClosing: check your connexion (network or GPT API')
