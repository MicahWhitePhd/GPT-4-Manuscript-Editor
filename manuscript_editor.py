import os
import sys
import argparse
from manuscript_reader import ManuscriptReader
from gpt_api_handler import GPTAPIHandler
from manuscript_writer import ManuscriptWriter
import docx

def read_prompt_file(prompt_file):
    with open(prompt_file, 'r') as file:
        return file.read()

def main(input_file, output_file, prompt_file, start_text=None):
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        sys.exit(1)

    # Read the content of the prompt file
    with open(prompt_file, 'r') as file:
        prompt = file.read()

    reader = ManuscriptReader(input_file, start_text=start_text)
    gpt_api = GPTAPIHandler(prompt, api_key)
    writer = ManuscriptWriter(output_file)

    chunks = list(reader.get_chunks())
    total_chunks = len(chunks)

    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1} of {total_chunks}")
        print(f"Sending text to GPT API: {chunk[:100]}...")

        edited_text = gpt_api.get_edited_text(chunk)

        print(f"Received edited text: {edited_text[:100]}...")

        writer.add_paragraph(edited_text)
        writer.save()  # Save the document after processing each chunk

    print(f"Edited manuscript saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manuscript Editor")
    parser.add_argument("input_file", help="Input manuscript file path")
    parser.add_argument("output_file", help="Output edited manuscript file path")
    parser.add_argument("prompt_file", help="Prompt file path")
    parser.add_argument("--start_text", help="Optional start text to process the input manuscript from", default=None)

    args = parser.parse_args()

    main(args.input_file, args.output_file, args.prompt_file, args.start_text)
