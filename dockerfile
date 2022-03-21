FROM python:3.10-buster

## elasticsearch logging install
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN apt-get install apt-transport-https
RUN echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list

# added tools
RUN apt-get update && apt-get install -y \
    filebeat \
    libssl-dev \
    default-mysql-client \
    default-libmysqlclient-dev \
    vim \
    supervisor \
    libgl1-mesa-glx \
    locales \
    net-tools

ENV PYTHONUNBUFFERED=1
# poetry install
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /home/code
# poetry dependencies install
COPY poetry.lock pyproject.toml /home/code/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi
RUN mkdir -p logs data

COPY . /home/code/

# setup all the configfiles
COPY app/conf/supervisor-app.conf /etc/supervisor/conf.d/
COPY app/conf/filebeat.yml /etc/filebeat/filebeat.yml

ENV TZ Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 8080
STOPSIGNAL SIGINT

# fastapi uvicorn run   
CMD ["uvicorn", "main:app", "--host 0.0.0.0", "--port 8080" ,"/home/code/start_up.sh"]