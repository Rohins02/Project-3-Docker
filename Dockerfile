#light-weight image < 200MB
FROM python:3.9-slim

WORKDIR /home/data

COPY scripts.py /home/data/
COPY IF-1.txt /home/data/
COPY AlwaysRememberUsThisWay-1.txt /home/data/

RUN pip install --no-cache-dir nltk

RUN mkdir -p /root/nltk_data \
    && python -c "import nltk; \
                  nltk.data.path.append('/root/nltk_data'); \
                  nltk.download('punkt', download_dir='/root/nltk_data'); \
                  nltk.download('stopwords', download_dir='/root/nltk_data'); \
                  nltk.download('wordnet', download_dir='/root/nltk_data'); \
                  nltk.download('omw-1.4', download_dir='/root/nltk_data'); \
                  nltk.download('punkt_tab', download_dir='/root/nltk_data')"

# Define the entry point
CMD ["python", "/home/data/txtProcess.py"]
