# TEXT-SUMMARIZATION-TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*:  NALLAGATLA ADITHYA

*INTERN ID*: CT04DM719

*DOMAIN*: Artificial intelligence

*DURATION*:  4 weeks

*MENTOR*:  Neela Santhosh

#discription: This Python code demonstrates how to perform extractive text summarization using the spaCy natural language processing library, executed on the Google Colab platform. The objective of this script is to automatically condense a long piece of text into a shorter, meaningful summary by identifying and ranking the most significant sentences. It leverages spaCy’s built-in linguistic capabilities, including tokenization, lemmatization, stop word removal, and sentence segmentation, to understand and process the structure of natural language text.

At the core, the script uses the lightweight English language model en_core_web_sm from spaCy, which provides a reliable foundation for processing English text. The summary is generated using a simple but effective scoring mechanism. First, the script processes the input text and creates a frequency dictionary of all non-stopword, alphabetical tokens. These word frequencies represent the relative importance of each word in the text. Next, each sentence is evaluated by summing the frequencies of the relevant words it contains. The heapq library’s nlargest function is then used to extract the top n sentences with the highest scores, resulting in a concise extractive summary that retains the most meaningful content from the original passage.

The execution of this code on Google Colab offers several advantages. Colab is a cloud-based, Jupyter-style environment that supports Python development with zero configuration and provides free access to powerful computing resources, including GPUs. This is especially useful for developers, students, and researchers who want to experiment with natural language processing models without needing to install libraries or configure environments locally. In this case, installing and running spaCy in Colab makes it easy to perform large-scale text analysis from any device with internet access.

The primary applications of this summarization approach span multiple domains. In journalism and content creation, it can be used to quickly summarize lengthy news articles or reports. In academia, it helps students and researchers digest large volumes of scholarly material. Businesses can use such tools to automatically distill insights from meeting transcripts, customer reviews, and internal reports. In customer support, summarization can aid in ticket analysis and automated response generation. Additionally, educators and learning platforms may adopt this technique to build simplified or abridged versions of complex reading materials, enabling more inclusive and accessible learning.

Although this implementation uses a basic word-frequency-based scoring algorithm, it is quite effective for smaller texts and real-time applications where speed and simplicity are crucial. More advanced approaches, like neural text summarization using transformer models, offer higher accuracy at the cost of complexity and resource demands.

Overall, this code showcases the practical use of spaCy and Python for natural language summarization in a lightweight yet powerful manner. By running it on Google Colab, users can immediately harness the benefits of cloud-based NLP and explore further enhancements to build more intelligent, real-world text processing solutions.

#OUTPUT

Original Text:
 In recent years, the global conversation around climate change has intensified, driven by increasingly frequent extreme weather events, rising sea levels, and growing scientific consensus about the human impact on the environment. Governments, corporations, and individuals are being urged to take immediate and meaningful action to reduce carbon emissions and transition to more sustainable practices. Renewable energy sources such as solar, wind, and hydroelectric power are gaining traction as viable alternatives to fossil fuels, while innovations in electric vehicles and energy-efficient technologies are reshaping industries. However, the path to a greener future is fraught with challenges, including political resistance, economic constraints, and the need for widespread behavioral change. Education and awareness play a crucial role in mobilizing public support and encouraging environmentally responsible choices. At the same time, international cooperation is essential, as climate change knows no borders and requires a unified global response. The urgency of the situation has led to the emergence of youth-led climate movements, demanding accountability and long-term thinking from world leaders. As the world grapples with the consequences of decades of environmental neglect, the choices made today will determine the health and stability of the planet for generations to come.




Summary:
 In recent years, the global conversation around climate change has intensified, driven by increasingly frequent extreme weather events, rising sea levels, and growing scientific consensus about the human impact on the environment. Renewable energy sources such as solar, wind, and hydroelectric power are gaining traction as viable alternatives to fossil fuels, while innovations in electric vehicles and energy-efficient technologies are reshaping industries. The urgency of the situation has led to the emergence of youth-led climate movements, demanding accountability and long-term thinking from world leaders.
