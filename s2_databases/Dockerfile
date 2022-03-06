FROM postgres
ENV POSTGRES_PASSWORD=postgres
RUN mkdir /opt/sql
COPY /sql/init.sql /opt/sql/init.sql
COPY /sql/query1.sql /opt/sql/query1.sql
COPY /sql/query2.sql /opt/sql/query2.sql
COPY /sql/query2.sql /opt/sql/query3.sql