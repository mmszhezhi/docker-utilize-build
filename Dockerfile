FROM python:3
COPY . /
RUN  pip install -r req.txt
CMD  ["python","main.py"]