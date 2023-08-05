from odooapiclient.client import Client


client = Client(host='andriisem.odoo.com', dbname='andriisem', ssl=True)
client.authenticate(login='semko.andrey.i@gmail.com', pwd='audi100')
print(client.search('res.partner'))

