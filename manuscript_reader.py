import docx

class ManuscriptReader:
    def __init__(self, file_path, chunk_size=3000):
        self.doc = docx.Document(file_path)
        self.chunk_size = chunk_size

    def get_chunks(self):
        paragraphs = []
        start_processing = False

        for paragraph in self.doc.paragraphs:
            if "BOOK 1: THE CAVE" in paragraph.text:
                start_processing = True

            if start_processing:
                paragraphs.append(paragraph.text)

        chunks = []
        current_chunk = []
        current_token_count = 0

        for paragraph in paragraphs:
            paragraph_tokens = paragraph.split()
            paragraph_token_count = len(paragraph_tokens)

            if current_token_count + paragraph_token_count <= self.chunk_size:
                current_chunk.extend(paragraph_tokens)
                current_token_count += paragraph_token_count
            else:
                chunks.append(' '.join(current_chunk))
                current_chunk = paragraph_tokens
                current_token_count = paragraph_token_count

        if current_chunk:
            chunks.append(' '.join(current_chunk))

        return chunks

