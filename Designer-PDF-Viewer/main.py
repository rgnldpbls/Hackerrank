def designerPdfViewer(h, word):
    max_height = 0
    for letter in word:
        height = h[ord(letter) - ord('a')]
        max_height = max(max_height, height)
    return max_height * len(word)