import requests
import json


url = "https://management.azure.com/subscriptions/38111b20-4eae-407d-a4cf-2e1a5211e1bb/resourceGroups/lab4/providers/Microsoft.Network/virtualNetworks/net4?api-version=2023-05-01"
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzJkN2FmZjY4LTk0MDQtNDFhNi1iODJhLTY3YjkxMzBkNmEwYy8iLCJpYXQiOjE3MDAxNTU0NTIsIm5iZiI6MTcwMDE1NTQ1MiwiZXhwIjoxNzAwMTU5ODc3LCJhY3IiOiIxIiwiYWlvIjoiQVdRQW0vOFZBQUFBZERsZDhyaHQ0Z0dYR0dGcjloc2FpZTk4OXRGQ2c3UFVvNTFNNFZyZnhPZDkrbWhYVHB5dmZHdEx3QWhiUnhxVDVjc0JpcTRDdndVTytzRTZQYlpETThkSE1scC9UaXdQZkh5VHVrVHg1WmltaXVWdzJzQ0F1bXBITVM1ckI5dk0iLCJhbHRzZWNpZCI6IjE6bGl2ZS5jb206MDAwMzQwMDE2M0MwQkE0QiIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJlbWFpbCI6InNhbXVlbG9taXNha2luMjE3QG91dGxvb2suY29tIiwiZmFtaWx5X25hbWUiOiJPbWkiLCJnaXZlbl9uYW1lIjoiU2FtIiwiZ3JvdXBzIjpbIjFlY2U2NmQ5LWJjYzAtNDRkMy1iMDFjLWMwODI0ZjY3Mzg3NyJdLCJpZHAiOiJsaXZlLmNvbSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE0Ny4yNTIuMTkuMjE5IiwibmFtZSI6IlNhbSBPbWkiLCJvaWQiOiIzYTM5N2Q1My1mNTQyLTRkNjctOWEzZS0xNTBhZDk4MjE1MzQiLCJwdWlkIjoiMTAwMzIwMDMwRjA1QzM2NyIsInJoIjoiMC5BYTRBYVA5NkxRU1Vwa0c0S21lNUV3MXFERVpJZjNrQXV0ZFB1a1Bhd2ZqMk1CT3JBUDguIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiOEtPTmdMcWtfUUJEaVFNVUF6LVExeUpLa0ZlbXRaOGhkOEhmQ29QRXFYSSIsInRpZCI6IjJkN2FmZjY4LTk0MDQtNDFhNi1iODJhLTY3YjkxMzBkNmEwYyIsInVuaXF1ZV9uYW1lIjoibGl2ZS5jb20jc2FtdWVsb21pc2FraW4yMTdAb3V0bG9vay5jb20iLCJ1dGkiOiJ6ZUpZV3kzUG8weUlxZ1hBTTFvUEFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyI2MmU5MDM5NC02OWY1LTQyMzctOTE5MC0wMTIxNzcxNDVlMTAiLCJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTY5OTExNzEwMX0.lW-FJLh7jCGykAPRmAliJV7XvUMiR1gzgoYSsm2rbacjbNTAJumg0H7ExAm5PK5l9EH18l27KtCk6Oc0pMfraA4c4wBIomKsXGB5K8idcxTsD11likrI9CvAIYyI6ZKZi1Oq3RKWSTfi4ZhQU-gEyU0UA8gfPZhR-LN-y_8vtSI5gTij0MKHFSR-81CcH9FofGOGNzqkQhBSjjXcr1goYDh1Xy2Xfp70NSq90dL4tnSAuy7HpKdReSF4MomPJeA8F9VvdNuvUZShszDRD-SzkOjD_5S3O4pbYEKGD15Gjp_28YGPk2cnKZRG_g_Q617LffOjAGRRuZ6ttnjBFPxEsg',
    'Content-type': 'application/json'
}

data = {
  "properties": {
    "addressSpace": {
      "addressPrefixes": [
        "10.0.0.0/16"
      ]
    },
    "flowTimeoutInMinutes": 10
  },
  "location": "westeurope"
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())