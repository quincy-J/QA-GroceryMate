def count_word_matches(text, target):
    if not text or not target:
        return 0
    words = text.lower().split()
    target = target.lower()
    return words.count(target)
