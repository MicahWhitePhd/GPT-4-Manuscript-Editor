import docx

class ManuscriptWriter:
    def __init__(self, file_path):
        self.doc = docx.Document()
        self.file_path = file_path

    def add_paragraph(self, text):
        self.doc.add_paragraph(text)

    def save(self):
        self.doc.save(self.file_path)
