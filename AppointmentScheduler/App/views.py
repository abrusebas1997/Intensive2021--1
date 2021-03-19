from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

client = FaunaClient(secret="fnAEEpXoUEACANrA9kCkDGRnaTM0De2OHmQMFgVS")

indexes = client.query(q.paginate(q.indexes()))

print(indexes)
