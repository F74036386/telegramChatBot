##start
python app.py

#fsm
show-fsm.png

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "92"
		* Reply: "you need 92"

	* Input: "95"
		* Reply: "you need 95"
	* Input: "98"
		* Reply: "you need 98"
*92,*95,*98
	*Input : full 
		*reply : "you need to full"
	*input : amount
		*reply :"you need some oil"
*credit,*cash
	*input:cash
		*reply :"you need to pay by cash"
	*input:credit
		*replay:"you need to pay by credit"

## Author
[linChangHan]
