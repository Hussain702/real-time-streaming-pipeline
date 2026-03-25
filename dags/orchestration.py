from airflow.decorators import dag, task
from datetime import datetime
import subprocess


@dag(
    dag_id="user_automation",
    start_date=datetime(2023, 9, 3, 10, 0),
    schedule="@daily",
    catchup=False,
    tags=["kafka", "stream"]
)
def user_automation_dag():

    @task()
    def run_producer():
        subprocess.run(["python", "/opt/airflow/producer/producer.py"], check=True)

    run_producer()

user_automation_dag()