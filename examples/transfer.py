"""Transfer some WAX to a receiver account."""

import eospyo

data = {
    "from": "me.wam",
    "to": "receiver",
    "quantity": "55.00000000 WAX",
    "memo": "Trying EosPyo",
}

auth = eospyo.Authorization(actor="me.wam", permission="active")

action = eospyo.Action(
    account="eosio.token",
    name="transfer",
    data=data,
    authorization=[auth],
)

raw_transaction = eospyo.Transaction(actions=[action])

net = eospyo.WaxTestnet()
linked_transaction = raw_transaction.link(net=net)

key = "a_very_secret_key"
signed_transaction = linked_transaction.sign(key=key)

resp = signed_transaction.send()
