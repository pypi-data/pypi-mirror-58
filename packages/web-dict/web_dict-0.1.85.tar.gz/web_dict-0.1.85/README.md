# Parser for Web dictionaries

# Installation
```bash
pip install web-dict
```
# Bilingual sites

## Collinsdictionary.com
- class `CollinsDictionary` supports below languages, respectively call method `.en2es` or `.es2en` etc. 

```json
{
    "es": "spanish",
    "zh": "chinese",
    "de": "german",
    "fr": "french",
    "en": "english"
}
```
```python
from web_dict import CollinsDictionary
dict_ = CollinsDictionary()
defs = dict_.es2en(word='hacer')
```

returns 
```json
{
    "audio": "https://www.collinsdictionary.com/sounds/hwd_sounds/ES-419-W0025780.mp3",
    "defs": [
        {
            "senses": [
                {
                    "senses": [],
                    "examples": [
                        {
                            "sent": "¿qué haces?",
                            "trans": "what are you doing?"
                        },
                        {
                            "sent": "¿qué haces ahí?",
                            "trans": "what are you doing there?"
                        },
                        {
                            "sent": "no sé qué hacer",
                            "trans": "I don’t know what to do"
                        },
                        {
                            "sent": "hace y deshace las cosas a su antojo",
                            "trans": "she does as she pleases"
                        },
                        {
                            "sent": "¡eso no se hace!",
                            "trans": "that’s not done!"
                        },
                        {
                            "sent": "no hizo nada por ayudarnos",
                            "trans": "she didn’t do anything to help us"
                        },
                        {
                            "sent": "haz todo lo posible por llegar a tiempo",
                            "trans": "do everything possible to arrive on time"
                        },
                        {
                            "sent": "no tiene sentido hacer las cosas por hacerlas",
                            "trans": "there’s no point doing things just for the sake of it"
                        }
                    ],
                    "exp": "to do",
                    "syn": {
                        "syn": "",
                        "geo": null
                    },
                    "idioms": [
                        {
                            "orth": "¡qué le vamos a hacer!",
                            "trans": "what can you do?"
                        },
                        {
                            "orth": "hacer algo por hacer",
                            "trans": "there’s no point doing things just for the sake of it"
                        },
                        {
                            "orth": "¡la hemos hecho buena!",
                            "trans": "we’ve really gone and done it now! (informal)"
                        },
                        {
                            "orth": "ya ha hecho otra de las suyas",
                            "trans": "he’s been up to his old tricks again"
                        }
                    ]
                },
                {
                    "senses": [],
                    "examples": [
                        {
                            "sent": "él protestó y yo hice lo mismo",
                            "trans": "he protested and I did the same"
                        },
                        {
                            "sent": "no viene tanto como lo solía hacer",
                            "trans": "he doesn’t come as much as he used to"
                        }
                    ],
                    "exp": "to do",
                    "syn": {
                        "syn": "",
                        "geo": null
                    },
                    "idioms": []
                }]
        }
    ],
    "rank": 5,
    "head_word": "hacer"
}

```


## Lexico.com
- en-es
- es-en
- en
- es
# Monolingual sites
use `.do_search` method as which supports mono-language
## Vocabulary.com
- class `VocabularyDictionary` supports `English` only

```python
from web_dict import VocabularyDictionary
dict_ = VocabularyDictionary()
defs = dict_.do_search(word='python')
```

returns:
```json
{
    "audio": "https://audio.vocab.com/1.0/us/P/6XU2813JWEQB.mp3",
    "long_def": "A python will grab smaller animals with its sharp teeth and then use its powerful coils to constrict the prey until it stops breathing. Pythons can also eat animals larger than they are — occasionally, pythons have been known to eat antelope and deer. The word python comes from Greek mythology, in which Python was a dragon or serpent who guarded the Delphic oracle until he was eventually killed by Apollo.",
    "head_word": "python",
    "short_def": "A python is a very large, nonvenomous snake. Instead of injecting poison through their fangs, pythons kill by wrapping around and asphyxiating their prey. You certainly wouldn't want to be a python's main squeeze.",
    "defs": {
        "primary": [
            {
                "exp": "large Old World boas",
                "pos": [
                    "n"
                ]
            },
            {
                "exp": "a soothsaying spirit or a person who is possessed by such a spirit",
                "pos": [
                    "n"
                ]
            }
        ],
        "full": [
            {
                "examples": [],
                "exp": "large Old World boas",
                "pos": "n"
            },
            {
                "examples": [],
                "exp": "a soothsaying spirit or a person who is possessed by such a spirit",
                "pos": "n"
            }
        ]
    }
}
```
- class `VocabularySuggestionDictionary`
```json
{
    "suggestion": [
        {
            "phrase": "python",
            "freq": 18497.57,
            "exp": "large Old World boas"
        },
        {
            "phrase": "Python",
            "freq": 25364.33,
            "exp": "Greek mythology"
        },
        {
            "phrase": "pythoness",
            "freq": 262652.35,
            "exp": "a witch with powers of divination"
        },
        {
            "phrase": "Pythoness",
            "freq": 90918.78,
            "exp": "Greek mythology"
        },
        {
            "phrase": "Pythonidae",
            "freq": -1,
            "exp": "in some classifications a family separate from Boidae comprising Old World boas"
        },
        {
            "phrase": "Pythoninae",
            "freq": -1,
            "exp": "Old World boas: pythons"
        },
        {
            "phrase": "Python molurus",
            "freq": 5909656.39,
            "exp": "very large python of southeast Asia"
        },
        {
            "phrase": "Python reticulatus",
            "freq": 1477414.85,
            "exp": "of southeast Asia and East Indies"
        },
        {
            "phrase": "Python sebae",
            "freq": -1,
            "exp": "very large python of tropical and southern Africa"
        },
        {
            "phrase": "Python variegatus",
            "freq": -1,
            "exp": "Australian python with a variegated pattern on its back"
        }
    ]
}
```
## cn.Bing.com
- class `CNBingDictionary` supports `English > Simplified Chinese` only
- class `CNBingSuggestion` 
```json
{
    "suggestion": [
        {
            "exp": "蟒; 蚺蛇",
            "phrase": "python"
        },
        {
            "exp": "女巫; 希腊达尔菲地方祀奉阿波罗神的...",
            "phrase": "pythoness"
        },
        {
            "exp": "女巫; 希腊达尔菲地方祀奉阿波罗神...",
            "phrase": "pythonesses"
        },
        {
            "exp": "神托的; 蚒蛇的",
            "phrase": "pythonic"
        }
    ]
}

```

## UrbanDictionary.com
- class `UrbanDictionary`

```json 
{
    "definitions": [
        "To be totally honest about something.",
        "A song released in 1994 by a rapper named Jeru the Damaja. This song has one of the greatest beats ever composed for rap music. The beat has which has been widely compared to dripping water and hammers banging on pipes. That, and a scratch of Onyx screaming \"Uh-oh! HEADS UP cause we're dropping some shit\" It was also laced with tight lyrics by Jeru, a great song on a great album.",
        "A song written by Billie Joe Armstrong and played by Green Day. It is a song about how a teenage boy has turned seventeen, who has secrets just like anybody. He is wondering if he should tell people about his secrets. His secrets are possibly concering his sexuality. He has also found out how to be a man.",
        "(v) The act of shoving everything in a closet and calling it decent.",
        "describing an item that looks really nice.",
        "Having stopped taking drugs.",
        "Referring to some new or icy attire. Usually directed toward shoes.",
        "Exceedingly attractive, in an overtly sexual way.",
        "in runescape when you lose all your money staking because of pid.",
        "1.Action that people do when bored. Involve taking a pile of junk and moving it to somewhere else in the house. 2.Removing all useless part of a whole so that it is better."
    ]
}
```

## SpanishDict.com
- class `SpanishDictDictionary` supports `Spanish > English` only

