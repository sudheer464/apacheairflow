
To generate fernet_key: 

docker run puckel/docker-airflow python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)"


use fernet_key as an evnrionemnt variable while running docker:

 docker run -itd -p 8082:8080 -v /root/dags:/usr/local/airflow/dags -e FERNET_KEY=nY-VFkjHQYXpW-HoLVtIXQT8wkznL1NVmTCf6ew7khw= puckel/docker-airflow webserver


docker-compose up -d
