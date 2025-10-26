import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    alumno_datos = event['body']['alumno_datos']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    # Actualización de los datos del alumno
    response = table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression="set alumno_datos = :d",
        ExpressionAttributeValues={
            ':d': alumno_datos
        },
        ReturnValues="UPDATED_NEW"
    )
    
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
