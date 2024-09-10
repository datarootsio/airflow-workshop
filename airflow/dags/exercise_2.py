# Oh no! A pizza was baked but someone forgot to deliver it.
# Write a DAG which can be triggered manually to correct the situation.
# - Provide 2 parameters (orderId and specialGift) you can use when triggering the dag
# - orderId is an int
# - specialGift is a string but can the only allowed values are "Chocolates", "Bottle of Wine" or "Gift Voucher"
# - use the DeliverPizza operator to send out the pizza of `orderId`
# - afterwards, "send" the gift (this doesn't have to do anything, just print it)