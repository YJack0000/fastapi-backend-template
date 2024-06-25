FROM python:3.12

WORKDIR /workspace

COPY ./requirements.txt /workspace/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /workspace/requirements.txt

COPY ./ /workspace

CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "8000"]
