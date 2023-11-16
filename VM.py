import requests
import json


url = "https://management.azure.com/subscriptions/38111b20-4eae-407d-a4cf-2e1a5211e1bb/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/nic4?api-version=2023-05-01"
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzJkN2FmZjY4LTk0MDQtNDFhNi1iODJhLTY3YjkxMzBkNmEwYy8iLCJpYXQiOjE3MDAxNTYxMDYsIm5iZiI6MTcwMDE1NjEwNiwiZXhwIjoxNzAwMTYwMzc4LCJhY3IiOiIxIiwiYWlvIjoiQVdRQW0vOFZBQUFBUDJkN0Z5RFM4SWNHUEZnOFpyWjJNZ0tLRzRsUlFaTDlKNmh2RnZ1a2lMZjJvY1o0eFV5b1BMSC81NDJhd0EzMjBrTUJQNUlrRU0zcnVHaitVWlJybUdzOTFKaHRhUUFDRXA3eEFBTGF6eEpnZmh5VysxUnplQUJYNGthcnFPL3UiLCJhbHRzZWNpZCI6IjE6bGl2ZS5jb206MDAwMzQwMDE2M0MwQkE0QiIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJlbWFpbCI6InNhbXVlbG9taXNha2luMjE3QG91dGxvb2suY29tIiwiZmFtaWx5X25hbWUiOiJPbWkiLCJnaXZlbl9uYW1lIjoiU2FtIiwiZ3JvdXBzIjpbIjFlY2U2NmQ5LWJjYzAtNDRkMy1iMDFjLWMwODI0ZjY3Mzg3NyJdLCJpZHAiOiJsaXZlLmNvbSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE0Ny4yNTIuMTkuMjE5IiwibmFtZSI6IlNhbSBPbWkiLCJvaWQiOiIzYTM5N2Q1My1mNTQyLTRkNjctOWEzZS0xNTBhZDk4MjE1MzQiLCJwdWlkIjoiMTAwMzIwMDMwRjA1QzM2NyIsInJoIjoiMC5BYTRBYVA5NkxRU1Vwa0c0S21lNUV3MXFERVpJZjNrQXV0ZFB1a1Bhd2ZqMk1CT3JBUDguIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiOEtPTmdMcWtfUUJEaVFNVUF6LVExeUpLa0ZlbXRaOGhkOEhmQ29QRXFYSSIsInRpZCI6IjJkN2FmZjY4LTk0MDQtNDFhNi1iODJhLTY3YjkxMzBkNmEwYyIsInVuaXF1ZV9uYW1lIjoibGl2ZS5jb20jc2FtdWVsb21pc2FraW4yMTdAb3V0bG9vay5jb20iLCJ1dGkiOiI3WnhLUmZTY1RrLUE3Nmt0dDJBWkFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyI2MmU5MDM5NC02OWY1LTQyMzctOTE5MC0wMTIxNzcxNDVlMTAiLCJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTY5OTExNzEwMX0.djuLn-GJ-C-vuROc0sfyV69QNFcsW_sWSeposNdtsbCWL2GBV34vm_om9EkqPMyua6wIcGMxWeo8NzByl6IT9KF0uacsH-uGB25ZKPTV4PH97MDfS6a157PyIUExwEpQy1iq8ra-EYAi7MbyIF2DyO4INwTssLBDxQchyhkKaSusMnvzsM-6jDRMVrve6NNklZ53sZcsn-Su7P88nGh0SV1KBC_Bf7GH3zNgWkjolm5idqGDG5tTmJzNWcBaMnZJ6YWm5ijzOE3gbhWuIbgO4hGzV9iaburFuOtaEZtLadgzUJX5GgfQB4FhwI7rdB3TjgK1fxR_MDUwPFJtgPgMwA',
    'Content-type': 'application/json'
}

data = {
  "id": "/subscriptions/38111b20-4eae-407d-a4cf-2e1a5211e1bb/resourceGroups/lab4/ providers/Microsoft.Compute/virtualMachines/vm4",
  "type": "Microsoft.Compute/virtualMachines",
  "properties": {
    "osProfile": {
      "adminUsername": "driz",
      "secrets": [
        
      ],
      "computerName": "vm4",
      "linuxConfiguration": {
        "ssh": {
          "publicKeys": [
            {
              "path": "/home/driz/.ssh/authorized_keys",
              "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCnC8J4Z+OXyWxOmezFIUuRtFhUCbaiyV8obNMM2m13xfPp9Kxy9KG4PC2DnJdfEmptwvx1nIal0lqJSre6OI33Doo9B53LMirCZhV77lrity2jS7dwV4/QVzu8VINRQsqZqzXqKtIVgzqUzNuUSKwRX1hjJkv7W3fx9kNVCZ8K/Bf376cFKOxCfHTl4YLFd+oq4WxRnaH1xNG3PmEvgHA7P9AETHbALz/UvidzjuIQjyKJTN8XbQXrjPGETc9aFw0GkphFzZunk1sQqSJBJUbcam//e2lzTBmfkR6Q+6Na77fx55FxzqfqmENgeufEztXIrO2Jm2DscxfZ3R7WXX/9d2sU8QdybZOFX4tz65eCeXuBZcPqjBR2VhPe4oQ3d6gKzcverKcm5HaSbvTXOJ4sMjnkHpXADWjDL8qwthyxRjtlIBun0EmCmGSEXYtqhI0+XQd6ut6JkS+tLM5Y4GzMttuQKogHcIDp8eRxEJgB3v1zGrkuK+j253/E9fDjsq0= driz@driz "
            }
          ]
        },
        "disablePasswordAuthentication": 'true'
      }
    },
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/38111b20-4eae-407d-a4cf-2e1a5211e1bb/resourceGroups/lab4/ providers/Microsoft.Network/networkInterfaces/nic4",
          "properties": {
            "primary": 'true'
          }
        }
      ]
    },
    "storageProfile": {
      "imageReference": {
        "sku": "16.04-LTS",
        "publisher": "Canonical",
        "version": "latest",
        "offer": "UbuntuServer"
      },
      "dataDisks": [
        
      ]
    },
    "hardwareProfile": {
      "vmSize": "Standard_D1_v2"
    },
    "provisioningState": "Creating"
  },
  "name": "vm4",
  "location": "westeurope"
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())