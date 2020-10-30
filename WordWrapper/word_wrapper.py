class Wrapper:
    @staticmethod
    def wrap(words: str, column_number: int) -> str:
        if len(words) < column_number:
            return words
        outside, space_index = Wrapper.index(words, column_number)
        if len(words) <= space_index + outside:
            return words[:space_index]
        return words[:space_index] + "\n" + Wrapper.wrap(words[space_index + outside:], column_number)

    @staticmethod
    def index(strng, column_number):
        outside = 1
        try:
            space_index = strng.index(" ")
        except ValueError:
            space_index = column_number
            outside = 0
        return outside, space_index
