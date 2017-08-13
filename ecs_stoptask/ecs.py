import boto3

client = boto3.client('ecs')
response = client.list_tasks(
    cluster='test-automation',
    desiredStatus='stopped'
)

print(response)

response = client.start_task(
    cluster='test-automation',
    taskDefinition='testapache',
    containerInstances=['2c3f3f0d-76db-42b2-8fdd-9edf1595e62e']
    
)
print(response)

response = client.stop_task(
    cluster='test-automation',
    task='ed016036-a8b6-4f83-b95c-57c59fbd02fd'
)
print(response)

