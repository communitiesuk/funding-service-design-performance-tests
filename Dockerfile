FROM locustio/locust:2.17.0

WORKDIR /app    
COPY . .
CMD ["--users", "2", "--spawn-rate", "1","--run-time", "10s"]
