API GPT : Quelques infos
==

Sources
--
<https://platform.openai.com/account/usage>

<https://24pm.com/gpt/900-s-abonner-a-chatgpt-plus-et-gpt3-tarifs-formules-d-abonnement-reductions>

<https://www.blogdumoderateur.com/gpt-3-gpt-4-tout-savoir/>

<https://www.commentcoder.com/api-chatgpt/>

#### Limites : <https://platform.openai.com/docs/guides/rate-limits/overview>


Variables d'environnement
--
Pour charger votre clé API depuis une variable d'environnement ou un service de secret management :   
1. Depuis un fichier .env   
Shell CLI :   
`pip install python-dotenv`
`echo 'OPENAI_API_KEY=Y0uR_OP3N@i_@P1_K3Y' > .env`
`source .env`
Script Python :   
`
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')
`
2. Depuis un export manuel :   
Shell Cli :
`export OPENAI_API_KEY="Y0uR_OP3N@i_@P1_K3Y"`
Script Python :
`openai.api_key = os.getenv('OPENAI_API_KEY')`

Contrat
--
### Argument
En entrée, le script prend une liste de chaine de caractères.   
Exemple : `['robot needs', 'robot position', 'itself robot', 'robot experiments', 'robot interaction', 'robot experimental']`
### Résultat
En sortie, lescript renvoie un dictionnaire de la forme suivante
`{'topic': 'string', 'tokens': {'completion': int, 'prompt': int}}`
* topic : le sujet déterminé d'après la liste de mots en entrée.
* tokens.completions : le cout du résultat en 'tokens' de GOT.
* tokens.prompt : le cout généré par la requête en 'token' de GPT.   
Exemple : `{'topic': ' "Robotics"', 'tokens': {'completion': 4, 'prompt': 216}}`

Modèles disponibles
--
GPT-3 signifie Generative Pre-trained Transformer 3. Cette technologie se décline en une série de 4 modèles (A, B, C, D) 
plus ou moins rapides et performants.

1. Davinci (text-davinci-003) :   
    c’est le modèle le plus avancé. Davinci est particulièrement adapté aux intentions complexes, 
    aux relations de cause à effet et à la création de résumés de contenus.
2. Curie (text-curie-001) :    
    performant et beaucoup plus rapide. Idéal pour la traduction, la classification complexe, 
    l’analyse de texte et les résumés.
3. Babbage (text-babbage-001) :    
    un modèle efficace pour les catégorisations plus simples et la classification sémantique.
4. Ada (text-ada-001) :    
    très rapide et peu coûteux, à privilégier pour les classifications les plus simples, 
    l’extraction de texte et la correction d’adresses.


OpenAI propose également les modèles spécifiques Codex pour la compréhension et la génération de code informatique 
(code-davinci-002 et code-cushman-001). Pour la modération des contenus, 
l’éditeur invite les développeurs à privilégier un nouvel endpoint permettant de déterminer ( avec des filtres personnalisés)
si un contenu est :
* safe, 
* sensitive 
* ou unsafe.


Coût
--
L'utilisateur paye les "tokens" consommés et non le volume de textes générés.
Les "tokens" (ou jetons en français) correspondent aux unités de puissance de calcul consommés.
#### En résumé
* Plus long est le texte demandé est long (en nombre de mots), plus grande est la quantité de tokens consommées
* Plus le texte à produire et compliqué à généré pour GPT, plus important est le nombre de tokens consommés
* Plus long est le prompt soumis, plus important est le nombre de tokens consommés
Concrètement, un texte de qualité moyenne de 400 à 500 mots coûte au moment de l'écriture de cet article entre 0,01 € et 0,025€


Le coût d’utilisation de l’API de ChatGPT est d’environ un centime de dollars américains (USD) pour 5000 tokens. 
OpenAI offre 5 dollars de crédits gratuits pendant 30 jours quand vous ouvrez un nouveau compte. 
C’est plus qu’assez pour faire toutes les requêtes que vous voulez pendant un mois.


Température
--
Si vous soumettez une même requête 4 fois avec une température définie sur 0, le modèle renverra toujours la même réponse
(parce qu'elle a la probabilité la plus élevée).    
Si vous augmentez la température, le modèle prendra plus de risques et considérer des réponses avec des probabilités plus faibles.