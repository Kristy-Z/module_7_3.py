class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = filenames

    def get_all_words(self):
        all_words = {}

        for filename in self.file_names:
            with open(filename, encoding='utf-8') as f:
                content = f.read()

            content_lower = content.lower()

            punctuation =  [',', '.', '=', '!', '?', ';', ':', ' - ' '\n']
            for punc in punctuation:
                content_lower = content_lower.replace(punc, '')

            words = content_lower.split()

            all_words[filename] = words

        return all_words

    def find(self, word):
        result = {}
        word = word.lower()

        for filename, words in self.get_all_words().items():
            try:
                index = words.index(word)
                result[filename] = index + 1
            except ValueError:
                pass

        return result

    def count(self, word):
        result = {}
        word = word.lower()

        for filename, words in self.get_all_words().items():
            count_word = words.count(word)
            if count_word > 0:
                result[filename] = count_word

        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
