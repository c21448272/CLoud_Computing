import requests
import json


url = "https://management.azure.com/subscriptions/38111b20-4eae-407d-a4cf-2e1a5211e1bb/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/nic4?api-version=2023-05-01"
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzJkN2FmZjY4LTk0MDQtNDFhNi1iODJhLTY3YjkxMzBkNmEwYy8iLCJpYXQiOjE3MDAxNTU5MjQsIm5iZiI6MTcwMDE1NTkyNCwiZXhwIjoxNzAwMTYxMTE3LCJhY3IiOiIxIiwiYWlvIjoiQVdRQW0vOFZBQUFBUDJkN0Z5RFM4SWNHUEZnOFpyWjJNZ0tLRzRsUlFaTDlKNmh2RnZ1a2lMZjJvY1o0eFV5b1BMSC81NDJhd0EzMjBrTUJQNUlrRU0zcnVHaitVWlJybUdzOTFKaHRhUUFDRXA3eEFBTGF6eEpnZmh5VysxUnplQUJYNGthcnFPL3UiLCJhbHRzZWNpZCI6IjE6bGl2ZS5jb206MDAwMzQwMDE2M0MwQkE0QiIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJlbWFpbCI6InNhbXVlbG9taXNha2luMjE3QG91dGxvb2suY29tIiwiZmFtaWx5X25hbWUiOiJPbWkiLCJnaXZlbl9uYW1lIjoiU2FtIiwiZ3JvdXBzIjpbIjFlY2U2NmQ5LWJjYzAtNDRkMy1iMDFjLWMwODI0ZjY3Mzg3NyJdLCJpZHAiOiJsaXZlLmNvbSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE0Ny4yNTIuMTkuMjE5IiwibmFtZSI6IlNhbSBPbWkiLCJvaWQiOiIzYTM5N2Q1My1mNTQyLTRkNjctOWEzZS0xNTBhZDk4MjE1MzQiLCJwdWlkIjoiMTAwMzIwMDMwRjA1QzM2NyIsInJoIjoiMC5BYTRBYVA5NkxRU1Vwa0c0S21lNUV3MXFERVpJZjNrQXV0ZFB1a1Bhd2ZqMk1CT3JBUDguIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiOEtPTmdMcWtfUUJEaVFNVUF6LVExeUpLa0ZlbXRaOGhkOEhmQ29QRXFYSSIsInRpZCI6IjJkN2FmZjY4LTk0MDQtNDFhNi1iODJhLTY3YjkxMzBkNmEwYyIsInVuaXF1ZV9uYW1lIjoibGl2ZS5jb20jc2FtdWVsb21pc2FraW4yMTdAb3V0bG9vay5jb20iLCJ1dGkiOiJVZFpJaEVlOUVrLU1MbFBnNmNVVEFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyI2MmU5MDM5NC02OWY1LTQyMzctOTE5MC0wMTIxNzcxNDVlMTAiLCJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTY5OTExNzEwMX0.JFSsNPn769NO6xaDZ_j7UIP3wuTgY4rx2Ygco0RyMnGzM5-ffDGwBYcw4-x6nKQXsJEdAhwN_7j1WYHFOlxE5D0U_EiDLET2u4VCHtRZ2wdQ0DyeRwtekoz4PFtYXkNArpBFJ1zMyewieKUuMgo49Ga4QrlQyB4Jj0RQU5STxt2XtPWsjQqYqWrnkzivYts9vKrocHI6Hq1HGRbPhuP03RqDL-3az-Z_UZ5aTnqsjWw0e5y6Xvub4ARcjP-RJ658gkAVeItncr8uBaY1L-Aan3nFN4nJ9Z15Wq2q8PSfFP80q1tv0_cFEr8B7PyvFT4FjdXmSD4lj31_jn67ihtq_g',
    'Content-type': 'application/json'
}

data = {
  "properties": {
    "ipConfigurations": [
      {
        "name": "ipconfig1",
        "properties": {
          "publicIPAddress": {
            "id": "/subscriptions/38111b20-4eae-407d-a4cf-2e1a5211e1bb/resourceGroups/lab4/providers/Microsoft.Network/publicIPAddresses/ip4"
          },
          "subnet": {
            "id": "/subscriptions/38111b20-4eae-407d-a4cf-2e1a5211e1bb/resourceGroups/lab4/providers/Microsoft.Network/virtualNetworks/net4/subnets/snet4"
          }
        }
      }
    ]
  },
  "location": "westeurope"
}


response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())