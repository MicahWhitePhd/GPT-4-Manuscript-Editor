import docx

class ManuscriptReader:
    def __init__(self, file_path, start_text=None, chunk_size=3000):
        self.start_text = start_text
        self.chunk_size = chunk_size
        self.file_path = file_path

    def get_chunks(self):
        raise NotImplementedError

class DocxManuscriptReader(ManuscriptReader):
    def __init__(self, file_path, start_text=None, chunk_size=3000):
        super().__init__(file_path, start_text, chunk_size)
        self.doc = docx.Document(file_path)

    def get_chunks(self):
        paragraphs = []
        start_processing = not bool(self.start_text)

        for paragraph in self.doc.paragraphs:
            if self.start_text and self.start_text in paragraph.text:
                start_processing = True

            if start_processing:
                paragraphs.append(paragraph.text)

        return self._split_into_chunks(paragraphs)

class TxtManuscriptReader(ManuscriptReader):
    def __init__(self, file_path, start_text=None, chunk_size=3000):
        super().__init__(file_path, start_text, chunk_size)
        with open(file_path, "r") as file:
            self.text = file.read()

    def get_chunks(self):
        return self._split_into_chunks(self.text)


    def _split_into_chunks(self, text):
        words = text.split()
        chunks = []
        current_chunk = []
        current_token_count = 0

        for word in words:
            word_token_count = len(word)

            if current_token_count + word_token_count > self.chunk_size:
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_token_count = word_token_count
            else:
                current_chunk.append(word)
                current_token_count += word_token_count

        if current_chunk:
            chunks.append(' '.join(current_chunk))

        return chunks
