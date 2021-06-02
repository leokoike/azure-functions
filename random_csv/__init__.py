import logging

import azure.functions as func

from random_csv.random_csv import create_random_csv


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    id = req.params.get("id")
    if not id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            id = req_body.get("id")

    if id:
        # return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
        file, filename = create_random_csv(id=id)
        return func.HttpResponse(file, status_code=200)
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully, but your request doesn't have id field. Pass an id in the query string or in the request body for a personalized response.",
            status_code=400,
        )
