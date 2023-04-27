# arxiv-gpt-summary

This repository contains a Python script to automatically generate summaries of machine learning research papers from the arXiv platform, using OpenAI's GPT-4 model. The generated summaries are concise and limited to a maximum of 3 sentences, providing a quick understanding of the main methodology and contributions of each paper.

## Dependencies

To run the script, you need to have the following packages installed:

- `arxiv`: To fetch papers from the arXiv platform.
- `langchain`: A library to create language model chains.
- `tqdm`: To display progress bars.

You can install these dependencies using pip:

```
pip install -r requirements.txt
```

Additionally, you need to have an OpenAI API key to use the GPT-4 model. Set the key as an environment variable `OPENAI_API_KEY`.

## Usage

To use the script, simply run it with the desired arguments:

```
python arxiv-gpt-summarize.py --number 30 --temperature 0 --cat stat.ML --output_dir /path/to/output/directory
```

The script accepts the following arguments:

- `--number`: The number of papers to fetch and summarize (default: 30).
- `--temperature`: The temperature value for GPT-4, controlling the randomness of the output (default: 0).
- `--cat`: The category of the papers to fetch from arXiv (default: "stat.ML").
- `--output_dir`: The directory where the summarized papers will be saved in a Markdown file (default: current working directory).

The script will save the summarized papers in a Markdown file named with the current timestamp, e.g., `2023-04-27-18-30-45.md`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
