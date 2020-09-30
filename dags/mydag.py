from datetime import datetime, timedelta
import airflow
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    "owner": "airflow",
    "depend_on_past": "False",
    "start_date": datetime.utcnow(),
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

def get_activated_sources():
    request = "SELECT * FROM public.links"
    pg_hook = PostgresHook(postgre_conn_id="airflow_db1")
    connection = pg_hook.get_conn()
    cursor = connection.cursor()
    cursor.execute(request)
    sources = cursor.fetchall()
    for source in sources:
        print("Source {0} - activated: {1}".format(source[0],source[1]))
    return sources

with DAG("hook_dag",
    default_args=default_args,
    schedule_interval="@once",
    catchup=False) as dag:

    #start_task = DummyOperator(task_id="start_task")
    hook_task = PythonOperator(task_id="hook_task", python_callable=get_activated_sources)
    hook_task


