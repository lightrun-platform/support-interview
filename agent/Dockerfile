FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./

COPY agent.py ./

ENTRYPOINT ["/bin/bash"]
CMD ["./agent.py" ]
