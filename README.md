# inkscape-server

curl --output - -X  POST "http://localhost:2003/convert" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@test.svg"
