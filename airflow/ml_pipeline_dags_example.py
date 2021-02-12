import xgboost as xgb
from sklearn.datasets import load_boston

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import ariflow.utils

from datetime import timedelta


default_args = {
	'owner': 'airflow',
	'depends_on_past': False,
	'email': ['airflow@example.com'],
	'email_on_failure': False,
	'email_on_retry': False,
	'retries': 1,
	'retry_delay': timedelta(minutes=5),
	'start_date': days_ago(2),

	# 'queue': 'bash_queue',
	# 'pool': 'backfill',
	# 'priority_weight': 10,
	# 'end_date': datetime(2022,1,1),
	# 'wait_for_downstream': False,
	# 'dag': dag,
	# 'sla': timedelta(hours=2),
	# 'execution_timeout': timedelta(seconds=300),
	# 'on_failure_callback': some_function,
	# 'on_success_callback': some_other_function,
	# 'on_retry_callback': another_function,
	# 'sla_miss_callback': yet_another_function,
	# 'trigger_rule': 'all_success'
}


dag = DAG(
	dag_id='boston_house_price_workflow',
	default_args=default_args
	)


def load_boston_data(**context):
	boston = load_boston()
	print("data loaded successfully")
	return boston


# task for load data
load_data = PythonOperator(
	task_id='load_data',
	python_callable=load_boston_data,
	dag=dag,
	retries=2,
	provide_context=True,
	)


def train(**context):
	boston = context['task_instance'].xcom_pull(task_ids='load_data')
	gbm - xgb.XGBRegressor()
	gbm.fit(boston.data, boston.target, eval_set=[(boston.data, boston.target)])
	print("Training done!")


# task for model training
train_model = PythonOperator(
	task_id='train_model',
	python_callable=train,
	dag=dag,
	retries=2,
	provide_context=True,
	)


def dummy_end(**context):
	print("dummy task indicating end of pipeline")


dummy = PythonOperator(
	task_id='dummy',
	python_callable=dummy_end,
	dag=dag,
	retries=2,
	provide_context=True,
	)


def ml_workflow_pipeline():
	train_model << load_data
	train_model >> dummy


ml_workflow_pipeline()


if __name__ == "__main__":
	dag.cli()