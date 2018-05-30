FROM python:2
RUN mkdir /input
RUN mkdir /output
COPY script/docker-backup-restore.py /home
ENTRYPOINT ["python", "/home/docker-backup-restore.py"]
CMD [""]