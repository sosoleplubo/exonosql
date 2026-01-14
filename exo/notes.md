apt install curl
curl -L "https://att.ovh/1j6jn" -o /tmp/data1.json
curl -L "https://att.ovh/8yced" -o /tmp/data.json


docker cp data/arbres.json IABDNOSQL:/tmp/data.json
docker exec -it IABDNOSQL bash  
mongoimport --uri "mongodb://localhost:27017" --db exo --collection arbres --file /tmp/data.json --jsonArray
