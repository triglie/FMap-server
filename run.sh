#!/bin/bash
docker build --tag=fmap.server:stream ./data-enrichment
docker-compose up