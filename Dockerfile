
FROM continuumio/miniconda3

# OS installs
RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get install -y build-essential

# add the app directory
COPY ./app /app

# python package installs
RUN pip install -r /app/requirements.txt

# generate gRPC classes from proto files
RUN cd /app/ && bash shell_scripts/gen_grpc_classes.sh

# spin-up python gRPC server
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["server.py"]
