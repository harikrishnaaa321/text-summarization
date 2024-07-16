#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
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}
data= ''' 
the former captain of the Indian national cricket team.
 He is a right-handed batsman and an occasional
 medium-fast bowler. He currently represents Royal Challengers Bangalore 
 in the IPL and Delhi in domestic cricket. Kohli is widely regarded as one of the greatest 
 batsmen of all time.[3] He holds the record as the highest run-scorer in T20I and IPL
'''
minL = 20
maxL = 30
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": data,
    "parameters":{"min_length":minL,"max_length":maxL},
})
print(output)

