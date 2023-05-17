## Setup
1. To run the project/code please clone the two files together into the same folder along with the .env file using the following command git clone https://github.com/PaulyMac/ChatBot.git
2. Python is needed to run this project so visit the www.python.org website to download.
3. The code requires an openai_api_key to run to get this please create an account on https://openai.com.
4. Then navigate to the API section and click the personal tab in the top right
5. Click view api keys and then navigate to the create new secret key button. You will name the key and be provided with an api key.
6. Store this api key in a new file called .env like the sample provided.
7. Before running the code please make sure to download the required python packages using pip install python-dotenv faiss-cpu langchain PyPDF2 openai pytesseract tiktoken (There may be other packages required upon running however on a fresh virtual environment these were the packages needed to install)
8. To run the code simply navigate to the directory the code is stored and run the command py Chatbot.py
9. The application should pop up and you can begin asking the bot questions regarding the documentation
10. The Bot will only answer questions based on the documentation and will prompt the user to ask another question upon answering the first. Please fill in your question in the shown text box and click the Ask button or hit enter to receive a response.
11. To close the application simple type exit or close the application by clicking the x.

## Difficulties in Creating project
1. While langchain provides great tools and accesibilty to other packages such as Pinecone and OpenAI, the documentation on implementing certain tools such as Chromadb/pinecone and certain embedding tools was lacking. Due to this along with a time limit of Wednesday due to other interviews I had to stick with what was easiest to implement. After managing to set up Pinecone and store the vectors, for testing different models and manipulations of the data chunks it would take too long for each new test. This is why I stuck with a quick and easy implementation of the vector database using FAISS along with using openai embeddings as they were the easiest to change and implement. If working on this over a longer timeframe I would like to look into using a lot more variations of language models along with different vector databases to compare speeds and efficiency.
2. Another difficulty I encountered during the implementation was the large amount of conflicts between certain packages, this led to having to either having to use different packages or downgrading them to meet requirements. Thankfully after a lot of trial and error I found a solution that had minimal conflicts and was easiest to set up.
3. The final difficulty I encountered was cleaning the json file provided, I tested working solely with the Json file however from testing with other pieces of text I found converting it to a PDF was by far the easiest solution, I used an online PDF converter after cleaning the data of html and processing it into a format that would be accepted.

## Improvements to be made

1. I would like to make the code more modular and to be able to create the vector database and store it as a global variable so after first use of the application the database will not have to be created a second time.
2. I would like to add a better gui interface using a package such as streamlit however when using it to build an interface there were a large amount of conflicts which I did not have time to resolve.
3. I would like to implement a better llm using some of the more complex models and testing the Prompt formatting for the Chatbot.
