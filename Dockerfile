#Deriving the latest base image
FROM python:3.8.10

# Any working direcrtory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY ./pysqltocsv/pysqltocsv.py ./
COPY ./sice-devops/db/development.sqlite3 ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
RUN ["pip3", "install", "pandas"]
RUN ["pip3", "install", "mega.py"]

CMD [ "python3", "./pysqltocsv.py"]
