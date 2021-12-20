import json 


def handler(context, inputs):
    callUrl = inputs['callUrlIN']
    
    resp_call = context.request(callUrl, 'GET', '')
    
    resp_json = {}
    resp_json = json.loads(resp_call['content'])
    
    outputs = {
        "response": resp_json,
        "status": resp_call['status'],
        "trigger": context.action_trigger
    }

    print(json.dumps(outputs))

    return outputs
