import requests

headers = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtkbXBocnh6amt5c3Z6bGFoamZjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5ODU1ODM1MywiZXhwIjoyMDE0MTM0MzUzfQ.t7zpcCOk8PwNBfDO8kk-_gAc6BvCokymgsEmk9SuGGQ",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtkbXBocnh6amt5c3Z6bGFoamZjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5ODU1ODM1MywiZXhwIjoyMDE0MTM0MzUzfQ.t7zpcCOk8PwNBfDO8kk-_gAc6BvCokymgsEmk9SuGGQ",
    "Content-Type": "application/json",
    "Prefer": "return=minimal",
}

response = requests.get(
    "https://kdmphrxzjkysvzlahjfc.supabase.co/rest/v1/students?select=*",
    headers=headers,
)
print(response.text)

# json_data = {
#     "firstname": "Dichill",
#     "lastname": "Tomarong",
#     "status": "Logged In",
#     "section": "Grade 12 - Hawking",
#     "phone_number": "2137320694",
#     "rfid": "12345678",
# }

# response = requests.post(
#     "https://kdmphrxzjkysvzlahjfc.supabase.co/rest/v1/students",
#     headers=headers,
#     json=json_data,
# )

# print(response.text)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{ "some_column": "someValue", "other_column": "otherValue" }'
# response = requests.post('https://kdmphrxzjkysvzlahjfc.supabase.co/rest/v1/students', headers=headers, data=data)
