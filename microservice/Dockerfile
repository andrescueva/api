FROM python:3.9-slim-buster
RUN useradd -m nonroot
ENV API_KEY=secret
WORKDIR /src
COPY . /src
RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R nonroot:nonroot /src
EXPOSE 8000
USER nonroot
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000" ]

