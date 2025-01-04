#!/bin/bash

# To create the containers
docker build -t music-generator /aimusicmatch/Music_Generator/
docker build -t youtube-uploader /aimusicmatch/YouTube_Uploader/
docker build -t suno-api /aimusicmatch/Suno_API/