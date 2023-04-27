import argparse
import os
from datetime import datetime

import arxiv
from langchain import LLMChain, OpenAI, PromptTemplate
from tqdm import tqdm

# Load environment variables
key = os.getenv("OPENAI_API_KEY")
if key is None:
    raise ValueError("No OpenAI API key found")


template = """
Suppose you are a good researcher in machine learning,
I’ll give you a paper from arXiv, the title is: {title} 
and summary is: {summary}, please use simple and concise word (no more than 3 sentences)
 to tell me the main methodology and contribution.
"""

prompt = PromptTemplate(input_variables=["title", "summary"], template=template)

parser = argparse.ArgumentParser()
parser.add_argument("--number", type=int, default=30)
parser.add_argument("--temperature", type=float, default=0)
parser.add_argument("--cat", type=str, default="stat.ML")
parser.add_argument("--output_dir", type=str)
args = parser.parse_args()

# print(args.number, args.area, args.temperature)

query = f"cat:{args.cat}"
papers = arxiv.Search(
    query=query,
    max_results=args.number,
    sort_by=arxiv.SortCriterion.SubmittedDate,
)

llm = LLMChain(
    prompt=prompt,
    llm=OpenAI(temperature=args.temperature, n=1),
)
time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
directory = args.output_dir or os.getcwd()
file_name = time + ".md"
full_path = os.path.join(directory, file_name)
with open(full_path, "w") as output_file:
    for paper in tqdm(papers.results(), total=args.number):
        res = llm.predict(
            title=paper.title,
            summary=paper.summary,
        )
        authors = [author.name for author in paper.authors]
        output = f"## [{paper.title}]({paper.pdf_url})\n\nPublished at: {paper.published}\n\nAuthors: {authors}\n\n{res}\n\n{'-' * 200}\n\n"
        # print(output)  # This will print the results on the screen
        output_file.write(output)  # This will write the results to the output.md file

print("Done! Results are saved as", file_name)
