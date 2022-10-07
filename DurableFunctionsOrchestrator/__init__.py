import logging
import json
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
 result = yield context.call_activity('Hello', 'some_input')
 result = json.loads(result)
 logging.info(result)

main = df.Orchestrator.create(orchestrator_function)