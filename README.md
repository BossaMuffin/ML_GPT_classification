Clusters' Topics by GPT : Quelques infos
==
Abstract
--

Ce document "README" a pour vocation de vous guider dans l'utilisation du module "Clusters' Topics by GPT", 
inclus au module de TLA du projet "CS/SIO/22-23/Fil_rouge".    
Rappel "module TLA":
1. extraire les mots clefs d'un corpus de document (une dizaine par document)
2. regrouper ces mots clefs en des groupes de mots proches sémantiquement (environ 500 mots)
3. déterminer la thématique globale de chacun de ces groupes (une expression de 1 à 3 mots cohérents par groupe)

Objet : Générer les grandes thématiques des mots-clefs extraits d'un corpus de documents.    
Objectif : Compléter la chaine de traitement du module de TLA (3ème point décrit ci-dessus).      
Enjeux : Proposer un ensemble 10 en 50 thématiques (dans le module "ontologie") permettant de faire des recherches (filtres) dans le corpus de document.    
Fonctionnalité principale : nommer une liste de mots par une expression le représentant le mieux possible.

Plans
--
* Pour démarrer : générer une API key 
* Intégrer l'API key dans le module
* Contrat 
* Modèles disponibles 
* Coût d'utilisation
* Le paramètre "température"
* Sources



Pour démarrer : générer une API Key
--
Pour faire fonctionner ce sript, vous aurez besoin d'une clé API GPT. 
Il suffit de vous rendre sur votre compte OpenAI (chatGPT) et depuis le menu en haut à droite de demander la génération
d'une clé pour votre API. Cette clé doit rester secrète puisqu'elle donne accès aux capacités de votre compte OpenAI.
Alors, comment intégrer cette clé dans notre présent script ? Réponse au paragraphe suivant.

Intégrer l'API key dansle module
--
Pour charger votre clé API nous avons choisi la méthode "variables d'environnement", pour respecter les bonnes pratiques.
Donc, pour manipuler votre clé comme variable d'environnement, nous vous proposons deux méthodes. 
Soit avec la méthode "automatique" avec un fichier .env (solution recommandée), soit avec un export manuel dans l'OS.

1. Méthode "automatique" : Fichier .env (recommandée)
D'abord
Shell CLI :   
`pip install python-dotenv`   
`echo 'OPENAI_API_KEY=Y0uR_OP3N@i_@P1_K3Y' > .env`   
`source .env`   
Script Python :   
`import os`
`from dotenv import load_dotenv`
`load_dotenv()`
`openai.api_key = os.environ.get('OPENAI_API_KEY')`

2. Méthode "manuelle" : Commande "export"

Shell CLI :     
`export OPENAI_API_KEY="Y0uR_OP3N@i_@P1_K3Y"`   

Script Python :   
`openai.api_key = os.getenv('OPENAI_API_KEY')`   

Contrat
--
Lancer le script depuis un shell : `python main.py [-h] [-m] [-t] [-d] "words1, words2, ..., wordsN"`   


### Argument
En entrée, le script prend une liste de chaine de caractères.
Exemple : `['robot needs', 'robot position', 'itself robot', 'robot experiments', 'robot interaction', 'robot experimental']`
Pour plus d'information `python main.py -h`
### Résultat
En sortie, le script renvoie un dictionnaire de la forme suivante   
`{'topic': 'string', 'tokens': {'completion': int, 'prompt': int}}`   
* topic : le sujet déterminé d'après la liste de mots en entrée.
* tokens.completions : le cout du résultat en 'tokens' de GOT.
* tokens.prompt : le cout généré par la requête en 'token' de GPT.   
Exemple : `{'topic': ' "Robotics"', 'tokens': {'completion': 4, 'prompt': 216}}`   

### If you want to test it
* X1 : `"robot needs, robot position, itself robot, robot experiments, robot interaction, robot experimental"`     
  Y1 = `Robotic Experimentation`    
* X2 : `"training with, training dynamics, adversarial training, training accuracy, longer training"`
  Y2 = `Machine Learning Training`
* X3 : `"taxing process, reconstruction process, mri reconstruction, reconstruction benchmarks"`     
  Y3 = `Image Reconstruction`
* X4 : `"learning dexterous, learning linear, robust learning, in learning, learning combined, prototypes learning, organizing learning, improved learning, learning networks, learning properties, generalized learning"`      
  Y4 = `Machine Learning`
* X5 :  `"new scenes", new approaches, new spectralnet, new demands`
  Y5 = `New Technology`
  

Modèles disponibles
--
GPT-3 (pour Generative Pre-trained Transformer 3) se décline en une série de 4 modèles 
plus ou moins rapides et performants.    

1. Davinci (text-davinci-003) :   
    C’est le modèle le plus avancé. Davinci est particulièrement adapté aux intentions complexes, 
    aux relations de cause à effet et à la création de résumés de contenus.     
    NB : Bien qu'elle soit la plus consommatrice en ressource et donc la plus couteuse, 
    nous la recommandons dans notre cas précis, car notre opération est ponctuelle 
    et nécessite une compréhension sémantique poussée. Les tests avec les autres modèles décrits si dessous sont, certes,
    moins onéreux et bien plus rapide, toutefois leurs résultats manquent cruellement de pertinence.
2. Curie (text-curie-001) :    
    Performant et beaucoup plus rapide. Idéal pour la traduction, la classification complexe, 
    l’analyse de texte et les résumés.     
    NB : ce modèle pourrait être un compromis acceptable. Attention : les résultats sont bien moins fins qu'avec Davinci.
3. Babbage (text-babbage-001) :    
    Un modèle efficace pour les catégorisations plus simples et la classification sémantique.
4. Ada (text-ada-001) :    
    Très rapide et peu coûteux, à privilégier pour les classifications les plus simples, 
    l’extraction de texte et la correction d’adresses.

#### A toutes fins utiles 
OpenAI propose également les modèles spécifiques Codex pour la compréhension et la génération de code informatique 
(code-davinci-002 et code-cushman-001). Pour la modération des contenus, 
l’éditeur invite les développeurs à privilégier un nouvel endpoint permettant de déterminer (avec des filtres personnalisés)
si un contenu est :
* safe, 
* sensitive 
* ou unsafe.    
NB : Ces capacités n'ont pas été testées dans notre cas d'usage.

Coût d'utilisation
--
L'utilisateur paye les "tokens" consommés et non le volume de textes générés.
Les "tokens" (ou jetons en Français) correspondent aux unités de puissance de calcul consommées.
#### En résumé
* Plus le texte demandé est long (en nombre de mots, donc en complexité), plus grande est la quantité de tokens consommés ;    
NB : notre cas d'usage n'est pas concerné par ce point puisque que nous demandons une réponse de quelques mots à peine.   
* Plus le texte à produire et compliqué à générer pour GPT, plus important est le nombre de tokens consommés ;
* Plus long est le prompt soumis, plus important est le nombre de tokens consommés.    
NB : dans notre cas d'usage, le prompt en entrée a une taille

Concrètement, un texte de qualité moyenne de 400 à 500 mots coûte, en fonction du modèle choisi, entre 0,01 € et 0,025€


Le coût d’utilisation de l’API de ChatGPT est d’environ un centime de dollars américains (USD) pour 5000 tokens. 
OpenAI offre 5 dollars de crédits gratuits pendant 30 jours quand vous ouvrez un nouveau compte. 
C’est plus qu’assez pour faire toutes les requêtes que vous voulez pendant un mois.


Le paramètre "Température"
--
Float entre 0 et 1 (valeurs disponibles [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.7, 0.8, 0.9, 1]) :     
* Si vous soumettez une même requête 4 fois avec une température définie sur 0, le modèle renverra toujours la même réponse
(parce qu'elle a la probabilité la plus élevée).    
* Si vous augmentez la température, le modèle prendra plus de risques et considérer des réponses avec des probabilités plus faibles.

Sources
--
Ce README ce repose sur les sources suivantes. 
Attention néanmoins, il s'avère que les limites d'utilisation aient évolué (dans le bon sens) par rapport à nos recherches.
<https://platform.openai.com/account/usage>

<https://24pm.com/gpt/900-s-abonner-a-chatgpt-plus-et-gpt3-tarifs-formules-d-abonnement-reductions>

<https://www.blogdumoderateur.com/gpt-3-gpt-4-tout-savoir/>

<https://www.commentcoder.com/api-chatgpt/>   

Limites : <https://platform.openai.com/docs/guides/rate-limits/overview>