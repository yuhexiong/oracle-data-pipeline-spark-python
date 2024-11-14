FROM apache/spark:3.5.1

USER root

# Install Python
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y python3 python3-pip

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Install tzdata to set the timezone
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/UTC /etc/localtime && \
    echo "UTC" > /etc/timezone

# Install Doris
RUN wget -qO /opt/spark/jars/spark-doris-connector-3.3_2.12-1.3.1.jar https://repo1.maven.org/maven2/org/apache/doris/spark-doris-connector-3.3_2.12/1.3.1/spark-doris-connector-3.3_2.12-1.3.1.jar  

# Install Oracle JDBC
RUN wget -qO /opt/spark/jars/ojdbc8.jar https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc8/19.16.0.0/ojdbc8-19.16.0.0.jar

# mkdir checkpoint and chmod
RUN mkdir -p /app/checkpoint && \
    chmod -R 777 /app/checkpoint