import unicodedata
from ftfy import fix_text
from . import const

def fix_quotes(text):
    text = const.SINGLE_QUOTE_REGEX.sub("'", text)
    text = const.DOUBLE_QUOTE_REGEX.sub('"', text)
    return text


def normalize(
    text,
    unicode_norm="NFKC",
    punct_replacement=None,
    url_replacement=None,
    emoji_replacement=None,
    apply_unicode_norm_last=True
):
    # fix encoding related issues first
    # and group characters for future
    # char replacements to work
    text = fix_text(
        text,
        normalization="NFC",
        explain=False,

    )

    # normalize variations of quotes
    text = fix_quotes(text)

    # replace URLS in text with specified replacement (if any)
    if url_replacement is not None:
        text = const.URL_HANDLER_REGEX.sub(url_replacement, text)

    # replace punctuations with specified replacement (if any)
    if punct_replacement is not None:
        text = const.PUNCT_HANDLER_REGEX.sub(punct_replacement, text)
        
    # replace emojis in text with specified replacement (if any)
    if emoji_replacement is not None:
        text = const.EMOJI_HANDLER_REGEX.sub(emoji_replacement, text)

    # apply char replacements
    text = text.translate(const.CHAR_REPLACEMENTS)
    
    if not apply_unicode_norm_last:
        text = unicodedata.normalize(text, unicode_norm)

    # apply unicode replacements    
    text = const.UNICODE_REPLACEMENTS_REGEX.sub(
        lambda match: const.UNICODE_REPLACEMENTS.get(match.group(0), f"{match.group(1)}\u09cc"), 
        text
    )

    if apply_unicode_norm_last:
        text = unicodedata.normalize(unicode_norm, text)

    # finally clean up extra whitespaces
    text = const.WHITESPACE_HANDLER_REGEX.sub(" ", text)

    return text

