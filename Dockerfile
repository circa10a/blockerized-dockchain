FROM python:3-alpine

COPY *.py .

CMD ["python3", "-u", "chain.py"]
