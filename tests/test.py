#%%
from normalizer import normalize
from normalizer import const

def test_url_replacements():
    data = [
        [ 
            "যেভাবে মেম্বার হবেন https://couchsurfing.com এ একটি একাউন্ট খুলুন।",
            "যেভাবে মেম্বার হবেন এ একটি একাউন্ট খুলুন।"
        ]
    ]
    
    for d in data:
        normalized_text = normalize(d[0], url_replacement="")
        assert normalized_text == d[1]

def test_char_replacements():
    data = [
        [ 
            "La retirada de Occidente de Afganistán significa que hay mucho en juego para China, Rusia, Pakistán e Irán.",
            "La retirada de Occidente de Afganistan significa que hay mucho en juego para China, Rusia, Pakistan e Iran."
        ]
    ]
    
    for d in data:
        normalized_text = normalize(d[0])
        assert normalized_text == d[1]


def test_emoji_replacements():
    data = [
        [ 
            "🗽Удачи, Любви и Счатья!🏝 Срочно👨🏻‍🎨 нужны Тайные📺 Агенты💡! В связи с расширением👩🏻‍🍳",
            "<<emoticon>>Удачи, Любви и Счатья!<<emoticon>> Срочно<<emoticon>> нужны Тайные<<emoticon>> Агенты<<emoticon>>! В связи с расширением<<emoticon>>"
        ]
    ]
    
    for d in data:
        normalized_text = normalize(d[0], emoji_replacement="<<emoticon>>")
        assert normalized_text == d[1]

def test_punct_replacements():
    data = [
        [ 
            "যেভাবে মেম্বার হবেন https://couchsurfing.com এ একটি একাউন্ট খুলুন।",
            "যেভাবে মেম্বার হবেন https<<punct>><<punct>><<punct>>couchsurfing<<punct>>com এ একটি একাউন্ট খুলুন<<punct>>"
        ]
    ]
    
    for d in data:
        normalized_text = normalize(d[0], punct_replacement="<<punct>>")
        assert normalized_text == d[1]


def test_unicode_replacements():
    data = [
        [ 
            "\u09F7",
            "\u0964"
        ],
        [
            "\u09af\u09bc",
            "\u09af\u09bc"
        ],
        [
            "\u00a0",
            " "
        ],
        [
            'েশৗ',
            'শৌ'
        ]
    ]
    
    for d in data:
        normalized_text = normalize(d[0])
        assert normalized_text == d[1], f"{normalized_text} != {d[1]}" 



if __name__ == "__main__":
    test_url_replacements()
    test_char_replacements()
    test_emoji_replacements()
    test_punct_replacements()
    test_unicode_replacements()