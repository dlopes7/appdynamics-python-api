def map_from_json(operation, response_array):
    for response in response_array:
        yield operation.model.build_from_json(response, operation)
