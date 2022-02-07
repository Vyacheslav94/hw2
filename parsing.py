# Imports
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
# Retrieve page text
url = 'https://www.npr.org/2019/07/10/740387601/university-of-texas-austin-promises-free-tuition-for-low-income-students' \
      '-in-2020'
page = requests.get(url).text
# Turn page into BeautifulSoup object to access HTML tags
soup = BeautifulSoup(page)
# Get headline
headline = soup.find('h1').get_text()
print(headline)
# Get text from all <p> tags.
p_tags = soup.find_all('p')
# Get the text from each of the "p" tags and strip surrounding whitespace.
p_tags_text = [tag.get_text().strip() for tag in p_tags]
p_tags_text
# Filter out sentences that contain newline characters '\n' or don't contain periods.
sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
sentence_list
# Combine list items into string.
article = ' '.join(sentence_list)
summary = summarize(article, ratio=0.3)
print(f'Length of original article: {len(article)}')
print(f'Length of summary: {len(summary)} \n')
print(f'Headline: {headline} \n')
print(f'Article Summary:\n{summary}')
