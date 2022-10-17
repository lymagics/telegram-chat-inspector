FROM python:slim

COPY requirements.txt ./
RUN pip install -r requirements.txt 

COPY bot bot 
COPY words words 
COPY run.py ./

CMD ["python3", "run.py"]