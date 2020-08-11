FROM python:3.6-slim
WORKDIR /usr/src/app

ARG TARGET
COPY src/iteration_1.py .
CMD python iteration_1.py ${TARGET}

