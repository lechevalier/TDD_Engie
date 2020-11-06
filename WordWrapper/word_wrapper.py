class Wrapper:

    @staticmethod
    def wrap(words: str, column_number: int) -> str:
        wrapped_words = words[:]
        result = []
        while len(wrapped_words) > column_number:
            offset, space_index = Wrapper.index(wrapped_words, column_number)
            result.append(wrapped_words[:space_index])
            wrapped_words = wrapped_words[space_index + offset:]

        result.append(wrapped_words[:])
        return "\n".join(result)

    @staticmethod
    def index(strng, column_number):
        try:
            offset = 1
            space_index = strng.rindex(" ", 0, column_number+1)
        except ValueError:
            offset = 0
            space_index = column_number
        return offset, space_index
