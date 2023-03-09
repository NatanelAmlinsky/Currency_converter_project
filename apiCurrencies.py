import requests

try:
    base = input("I can show you the latest currencies."
                 "\n Please enter what type of currency you would like to know(for example from: USD, to ILS) from: ")
    rate = input("Convert to: ")
    url = f"https://api.apilayer.com/fixer/latest?symbols={rate}&base={base}"

    payload = {}
    headers = {
        "apikey": "SNtRFTb0ugdyfFcnQMY1t5qnzOAPMQBw"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # response: This variable will store the response object returned by the API endpoint.
    # requests.request(): This function is used to send an HTTP request to a server. It takes several arguments to configure the request, including the HTTP method, the URL, request headers, and data to be sent with the request.
    # "GET": This string specifies the HTTP method used for the request. In this case, it is the GET method, which is used to retrieve data from the server.
    # url: This variable contains the URL of the API endpoint that we want to send the request to.
    # headers=headers: This specifies the headers to be included in the request. In this case, it is the headers dictionary containing the "apikey" header with the API key.
    # data=payload: This specifies the data to be sent with the request. In this case, it is an empty dictionary because we are not sending any data with the request.
    # So, overall, this line of code is sending an HTTP GET request to the specified API endpoint with the "apikey" header included in the request header, and no data included in the request body. The response object returned by the API endpoint will be stored in the response variable for further processing.
    data = response.json()
    ils_rate = data["rates"]["ILS"]

    print(f"The exchange rate for 1 USD to ILS is: {ils_rate}")

except:
    print("Could not get rate from API using default rate...")
