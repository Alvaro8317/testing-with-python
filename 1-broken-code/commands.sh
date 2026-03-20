# Happy path

curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "supersecret123"}'

# User does not exists
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "noexiste", "password": "cualquiercosa"}'

# Password invalid
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": 12345, "password": null}'
