FROM python:3

RUN git clone https://github.com/lucasfozzatti/Final_Computaci-n1.git

WORKDIR /Final_Computaci-n1

RUN pip install -r requirements.txt

CMD ["python3", "./test_musical.py"]