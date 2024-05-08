from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def task1():
    print('Task 1: Started')
    # Perform some meaningful operation, such as data processing
    result = 10 + 20
    print('Task 1: Completed with result:', result)

def task2():
    print('Task 2: Started')
    # Perform another meaningful operation, such as data validation
    data = [1, 2, 3, 4, 5]
    if len(data) > 3:
        print('Data has more than 3 elements')
    else:
        print('Data has 3 or fewer elements')
    print('Task 2: Completed')

def task3():
    print('Task 3: Started')
    # Perform another meaningful operation, such as data transformation
    data = [1, 2, 3, 4, 5]
    transformed_data = [x * 2 for x in data]
    print('Transformed data:', transformed_data)
    print('Task 3: Completed')

def task4():
    print('Task 4: Started')
    # Perform another meaningful operation, such as data loading
    data_to_load = [6, 7, 8, 9, 10]
    print('Data loaded:', data_to_load)
    print('Task 4: Completed')

with DAG(
    dag_id='question_3',
    description='This DAG is created for question 3',
    start_date=datetime(2024, 5, 8),
    schedule_interval=None
) as dag:
    task1 = PythonOperator(
        task_id='task1',
        python_callable=task1,
        #"First stage: Perform data processing"
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=task2,
        #"Second stage: Perform data validation"
    )

    task3 = PythonOperator(
        task_id='task3',
        python_callable=task3,
        #"Third stage: Perform data transformation"
    )

    task4 = PythonOperator(
        task_id='task4',
        python_callable=task4,
        #"Fourth stage: Perform data loading"
    )

    # Define task dependencies
    task1 >> task2>>[task3,task4]

