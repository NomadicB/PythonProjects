def text_to_string(text):
    split_text = len(text.split())
    return split_text

def text_to_count(text):
    count = {}
    for i in text.lower():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

def sort_on(items):
    return items["num"]

def sorted_list(text):
    sorted = []
    for i in text:
        sorted.append({"char": i, "num": text[i]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted