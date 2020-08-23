FROM python:3-alpine

COPY glouton2.py /glouton2.py

ENV CPUS 1
ENV MEM 256
ENV STEP 10

CMD ["python","/glouton2.py"]
