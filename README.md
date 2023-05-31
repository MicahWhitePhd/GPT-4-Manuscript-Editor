# GPT-4 Manuscript Editor

## Overview

The Manuscript Editor is a Python-based application that utilizes the GPT-4 API to edit and improve the content of a manuscript. It reads a manuscript, processes it in chunks, and sends it to the GPT-4 API for editing. The edited text is then saved to a new file.

## Code Structure

The code consists of four Python files and one text file:

1. **manuscript_editor.py**: The main script that ties everything together.
2. **manuscript_reader.py**: Contains the `ManuscriptReader` class, which is responsible for reading the input manuscript and dividing it into chunks.
3. **manuscript_writer.py**: Contains the `ManuscriptWriter` class, which is responsible for writing the edited text to a new document.
4. **gpt_api_handler.py**: Contains the `GPTAPIHandler` class, which handles interaction with the GPT-4 API.
5. **prompt.txt**: A text file containing the prompt to be sent to the GPT-4 API, which instructs it on how to edit the text.

## How the Code Works

1. The `main` function in **manuscript_editor.py** takes three arguments - the input file, the output file, and the prompt file. It then initializes three objects:
    - `reader`: an instance of the `ManuscriptReader` class to read the input manuscript.
    - `gpt_api`: an instance of the `GPTAPIHandler` class to send text chunks to the GPT-4 API.
    - `writer`: an instance of the `ManuscriptWriter` class to write the edited text to a new document.

2. The code iterates through the chunks of text returned by `reader.get_chunks()` and sends each chunk to the GPT-4 API for editing.

3. The edited text is added to the output document using the `writer.add_paragraph()` method.

4. The output document is saved after processing each chunk by calling the `writer.save()` method.

## How to Run the Code

1. Set up a Python 3 environment with the required packages installed. The packages needed are `docx` and `openai`. You can install them using pip:

   ```
   pip install python-docx openai
   ```

2. Set the `OPENAI_API_KEY` environment variable to your OpenAI API key.

3. Run the script with the following command:

   ```
   python3 manuscript_editor.py <input_directory> <output_directory> <prompt_file> --start_text "TEXT TO START FROM (OPTIONAL)"
   ```

   Replace `<input_directory>` with the path to the directory with the manuscripts you want to edit, `<output_directory>` with the desired path for the edited manuscripts, and `<prompt_file>` with the path to the prompt text file (in this case, `prompt.txt`). Include the optional --start_text parameter if you'd like the editor to start from a specific part in the text

## Example

To edit a manuscript called `input_manuscript.docx` in the raw/ directory and save the edited version as `edited_manuscript.docx` in the edited/ directory, use the following command:

```
python3 manuscript_editor.py raw edited prompt.txt --start_text "Once upon a time"
```

## License

Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

This is a human-readable summary of (and not a substitute for) the license, which can be found at https://creativecommons.org/licenses/by-nc/4.0/legalcode.

You are free to:

* Share — copy and redistribute the material in any medium or format
* Adapt — remix, transform, and build upon the material

The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:

* Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

* NonCommercial — You may not use the material for commercial purposes.

* No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Notices:

* You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.

* No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.
