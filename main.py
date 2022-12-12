from fastapi import FastAPI, Response, Header
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

authDemo = [
   {
      "access_token":"eyJ0eX...",
      "expires_on":"2022-11-28T11:29:36.8601739Z",
      "id_token":"eyJ0...",
      "provider_name":"aad",
      "user_claims":[
         {
            "typ":"aud",
            "val":"X"
         },
         {
            "typ":"iss",
            "val":"X"
         },
         {
            "typ":"iat",
            "val":"1669630716"
         },
         {
            "typ":"nbf",
            "val":"1669630716"
         },
         {
            "typ":"exp",
            "val":"1669634616"
         },
         {
            "typ":"aio",
            "val":"X"
         },
         {
            "typ":"c_hash",
            "val":"X"
         },
         {
            "typ":"cc",
            "val":"X"
         },
         {
            "typ":"name",
            "val":"DUMMY"
         },
         {
            "typ":"nonce",
            "val":"X"
         },
         {
            "typ":"http:\/\/schemas.microsoft.com\/identity\/claims\/objectidentifier",
            "val":"X"
         },
         {
            "typ":"preferred_username",
            "val":"DUMMY USERNAME"
         },
         {
            "typ":"rh",
            "val":"X"
         },
         {
            "typ":"http:\/\/schemas.xmlsoap.org\/ws\/2005\/05\/identity\/claims\/nameidentifier",
            "val":"X"
         },
         {
            "typ":"http:\/\/schemas.microsoft.com\/identity\/claims\/tenantid",
            "val":"X"
         },
         {
            "typ":"uti",
            "val":"X"
         },
         {
            "typ":"ver",
            "val":"2.0"
         }
      ],
      "user_id":"DUMMY"
   }
]

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/.auth/me")
async def login(Authorization: str | None = Header(default=None)):
    print(Authorization)
    return authDemo

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=82, reload=True)
