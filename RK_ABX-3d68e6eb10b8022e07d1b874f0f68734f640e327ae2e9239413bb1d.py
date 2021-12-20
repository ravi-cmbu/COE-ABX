def handler(context, inputs):
    print("Changing hostname from ABX")
    
    newName = "namedbyABX"
    outputs={}
    outputs["customProperties"] = inputs["customProperties"]
    outputs["customProperties"]["name"] = newName
    
    print("The new name is : " + newName)
    
    return outputs
