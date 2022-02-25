# Infinity Influencer API

Implementation of Infinity Influencer web service

## Usage
1. Download files in repository 
2. Install dependencies in requirements.txt
3. Open two cmd/bash terminals and move to directory where files are located. 
4. Run python InfinityInfluencer_api.py on one terminal and test.py on another. 
```bash
python InfinityInfluencer_api.py
```
```bash
python test.py
```
5. Results will be displayed in terminal where test.py is ran. 

Any of the requests in test.py can be changed and new requests can be added.

Alternatively, requests can also be made to the web service through a third party website or software such as [Reqbin](https://reqbin.com/) or [Postman](https://www.postman.com/). If using this method, only InfinityInfluencer_api.py needs to be ran in the terminal. 

Use link: http://127.0.0.1:5000 when accessing from a third party method 

## Endpoints 

#### /api/vocab

Accepts a GET request. Returns all vocab words in the database

Response 
```json
{
  "vocab":[
     "#ad",
     "#sponsored",
     "advertisement"
   ]
}
```

Accepts a POST request. Adds a new vocab word to the database and returns the current words. Does not add duplicate words. Can accept multiple words

Request
```json
{
  "vocab":[
     "blogger",
     "influencer"
   ]
}
```

Response
```json
{
  "vocab":[
     "#ad",
     "#sponsored",
     "advertisement",
     "blogger",
     "influencer"
   ]
}

```

#### /api/prediction

Accepts a POST request. Will make a prediction if post_text is sponsored or non-sponsored based on vocab words in database and returns prediction.

Request
```json
{
  "post_text":"#ad This text is paid for"
}
```

Response
```json
{
  "prediction":"sponsored"
}
```

Request
```json
{
  "post_text":"This text is not paid for"
}
```

Response
```json
{
  "prediction":"non-sponsored"
}
```