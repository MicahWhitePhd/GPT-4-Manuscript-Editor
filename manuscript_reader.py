import docx
import csv

class ManuscriptReader:
    def __init__(self, file_path, start_text=None, chunk_size=3000):
        self.start_text = start_text
        self.chunk_size = chunk_size
        self.file_path = file_path

    def get_chunks(self):
        raise NotImplementedError

import csv

class CsvManuscriptReader(ManuscriptReader):
    def __init__(self, file_path, start_text=None, chunk_size=5):  # 5 rows at a time
        super().__init__(file_path, start_text, chunk_size)
        
    def get_chunks(self):
        rows = []
        start_processing = not bool(self.start_text)

        with open(self.file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                # Check if we found the start_text
                if self.start_text and self.start_text in row:
                    start_processing = True
                
                # Add the row to rows list
                if start_processing:
                    rows.append(', '.join(row))

        return self._split_into_chunks(rows)
    
    def _split_into_chunks(self, rows):
        chunks = []
        current_chunk = []
        current_row_count = 0

        for row in rows:
            current_row_count += 1

            if current_row_count > self.chunk_size:
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                current_chunk = [row]
                current_row_count = 1
            else:
                current_chunk.append(row)

        if current_chunk:
            chunks.append('\n'.join(current_chunk))

        return chunks

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
        paragraphs = text.split('\n\n')  # split text into paragraphs
        chunks = []
        current_chunk = []
        chunk_text_length = 0

        for paragraph in paragraphs:
            paragraph_length = len(paragraph)

            # Add complete paragraphs not exceeding the chunk_size
            if chunk_text_length + paragraph_length > self.chunk_size:
                if current_chunk:
                    chunks.append('\n\n'.join(current_chunk))
                current_chunk = [paragraph]
                chunk_text_length = paragraph_length
            else:
                current_chunk.append(paragraph)
                chunk_text_length += paragraph_length

        if current_chunk:
            chunks.append('\n\n'.join(current_chunk))

        return chunks

