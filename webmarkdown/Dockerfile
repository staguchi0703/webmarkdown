FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /home/webmarkdown
WORKDIR  /home/webmarkdown
ADD ./requires.txt  /home/webmarkdown
RUN pip install -r requires.txt
CMD tail -f /dev/null
# CMD uwsgi --socket :8001 --module config.wsgi --py-autoreload 1
