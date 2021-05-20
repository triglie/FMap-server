#!/bin/bash
docker build -t fmap-kafka-consumer .
docker rm fmap-kafka-consumer
docker run --network fmap-int -e PYTHON_APP=app.py --name kafka-test-consumer fmap-kafka-consumer