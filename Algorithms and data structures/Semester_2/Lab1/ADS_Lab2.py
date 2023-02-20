import wikipedia
import docx

def naive(text, summary):
    checked = []
    for i in range(2, len(summary)):
        stroka = summary[i-2] + summary[i-1] + summary[i]
        if not(stroka in checked) and stroka in text:
            checked.append(stroka)
    return checked


def remover(text):
    symbols = ['.', ',', ':', '\n', '-', ')', '1', '2',
                    '3', '4', '5', '6', '7', '8', '9', '0',
                    ';', '(', '-', '«', '»', '—', '?', '=' , '==',
                    '  ', '–']
    for i in symbols:
        if i == "  ":
            text = text.replace(i, ' ')
        elif i == "\n":
            text = text.replace(i, "\n")
        else:
            text = text.replace(i, ' ')
    return text

def text_get(file_name):
    f = docx.Document(file_name)
    text = ""
    for i in f.paragraphs:
        text += i.text
    return text

wikipedia.set_lang("ru")
text = remover(wikipedia.page("Стресс").content).split()
summary = remover(text_get("Стресс.docx"))
summary_len = len(summary)
summary = summary.split()

text_triple = [text[i-2]+text[i-1]+text[i] for i in range(2, len(text))]

pl_len = len("".join(naive(text_triple, summary)))

print("В реферате присутствует примерно %.4f" % ((pl_len/summary_len)*100), "% плагиата", sep="")
