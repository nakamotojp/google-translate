import mistune

def translate_text_with_model(target, text, model=translate.NMT):
    """Translates text into the target language.

    Make sure your project is whitelisted.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target, model=model)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))

# google-translation
# send sentence
# recv response
# edit response
# commit response

# markdown loader
# init
# next_sentence
# prev_sentence
# pretty-print

# output markdown object
# vector of hash_tags, 1020141215125, "this is a test"
# add_sentence
# remove_sentence
# overwrite_sentence

# translation_manager
# load existing translation
# create markdown loader
# create google translation client
# create output markdown object
# check for google credentials
# event loop
# - wait for user command
# - handle user command
# user commands
# - translate(confirmation=true)
# -- read sentence
# -- send to google
# -- recv response
# -- display response
# -- wait for confirmation
# -- commit change
# - backtrack
# -- read backtrack #
# -- lookup sentence
# -- translate(confirmation=true)
# - fast-forward
# -- read #
# -- translate(confirmation=false)

# dump translated object as json??

# support collaborative editing
# divide-and-conquer
# - load 0-100, 100-200, 200-300
# - load chapter 1, 2, 3
# - load page 1 - 20, 20 - 40?

# re-translate particular sentence
# grep "sentence" -> hash-tag (hide)
# translate hash-tag (hide)
# user enters index.

if __name__ == '__main__':
    mistune = mistune.Markdown()
    mistune("")
    translate_text_with_model('zh', 'test')

