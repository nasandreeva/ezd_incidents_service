from flask import Response


def response(code: int, payload: any):
    resp = Response(response=payload,
                    status=code,
                    mimetype="application/json")

    return resp
