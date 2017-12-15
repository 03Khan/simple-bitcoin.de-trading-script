#! /usr/bin/env python
import btcde
import sys
import tkinter.messagebox
# connection settings
api_key = 'your API Key goes here'
api_secret = 'your API Secret goes here'
# trade data
dic = 0
iRow = 0
current_trading_pair = 'empty'

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
	

new_order_for_remaining_amount = 1

def KaufOrder():
  global current_trading_pair
  conn = btcde.Connection(api_key, api_secret)
  order = btcde.createOrder(conn, OrderType = 'buy', trading_pair = current_trading_pair, max_amount = float(Mengeeingabe.get()), price = float(Preiseingabe.get()), min_amount = float(Minmenge.get()), new_order_for_remaining_amount = new_order_for_remaining_amount)
  OrderIDInput.delete(0, END)
  OrderIDInput.insert(0,str(order.get('order_id')))

def VerkaufOrder():
  global current_trading_pair
  conn = btcde.Connection(api_key, api_secret)
  order = btcde.createOrder(conn, OrderType = 'sell', trading_pair = current_trading_pair, max_amount = float(Mengeeingabe.get()), price = float(Preiseingabe.get()), min_amount = float(Minmenge.get()), new_order_for_remaining_amount = new_order_for_remaining_amount, payment_option = 3)
  OrderIDInput.delete(0, END)
  OrderIDInput.insert(0,str(order.get('order_id')))
	
def  DeleteOrder():
	global current_trading_pair
	conn = btcde.Connection(api_key, api_secret)
	order = btcde.deleteOrder(conn, order_id = OrderIDInput.get(), trading_pair = current_trading_pair)
	OrderIDInput.delete(0, END)
	
def  ExsellOrder():
	global current_trading_pair
	conn = btcde.Connection(api_key, api_secret)
	order = btcde.executeTrade(conn, order_id = OrderIDInput.get(), OrderType = 'sell', trading_pair = current_trading_pair, amount = float(Mengeeingabe.get())) 	

def  ExbuyOrder():
	global current_trading_pair
	conn = btcde.Connection(api_key, api_secret)
	order = btcde.executeTrade(conn, order_id = OrderIDInput.get(), OrderType = 'buy', trading_pair = current_trading_pair, amount = float(Mengeeingabe.get())) 	
		
def  AvAmount():
	global dic
	conn = btcde.Connection(api_key, api_secret)
	account = btcde.showAccountInfo(conn)
	dic= (account.get('data'))
	#AvAmount = ((dic['balances'][symbol]['available_amount']))
	#Mengeeingabe.delete(0, END)
	#Mengeeingabe.insert(0,AvAmount)


def AmountUpd():
	AvAmount()	
	BTCGuthaben.config(text= 'BTC: '+ balance('btc'))
	BCHGuthaben.config(text= 'BCH: '+ balance('bch'))
	ETHGuthaben.config(text= 'ETH: '+ balance('eth'))

def balance(symbol):
	global dic
	return dic['balances'][symbol]['available_amount']
	
def setTradingPair():
	global current_trading_pair
	pairno = vAuswahl.get()
	if (pairno == 1):
		current_trading_pair = 'btceur'
	elif (pairno ==2):
		current_trading_pair = 'bcheur'
	elif (pairno ==3):
		current_trading_pair = 'etheur'
	
	Handelssymbol.config(text= current_trading_pair)	
	return current_trading_pair
	
window = Tk()
window.title('Bitcoin.de Trading')
window.geometry('600x400')

vAuswahl = IntVar()
vAuswahl.set(1)  # initializing the choice, i.e. BTC - Bitcoin

trading_pairs = [
    ("BTC - Bitoin",1),
    ("BCH - Bitcoin Cash",2),
    ("ETH - Ethereum",3),
]

HandelspaareLabel = Label(window, 
      text="""Handelswährung wählen:""",
      justify = LEFT,
      padx = 20).grid(row=iRow,column=2)

i=0
for txt, val in trading_pairs:
	i +=1
	Radiobutton(window, 
                text=txt,
                padx = 2, 
                variable=vAuswahl, 
                command=setTradingPair,
                value=val).grid(row=iRow+i,column=2)

i +=1
Handelssymbol = Label(window, text= current_trading_pair)
Handelssymbol.grid(row=iRow+i,column=2)

setTradingPair()
				
MengeeingabeLabel = Label(window, text='Max. Menge')
MengeeingabeLabel.grid(row=iRow,column=0)
Mengeeingabe = Entry(window)
Mengeeingabe.grid(row=iRow,column=1)

iRow +=1
PreiseingabeLabel = Label(window, text='Preis in €')
PreiseingabeLabel.grid(row=iRow,column=0)
Preiseingabe = Entry(window)
Preiseingabe.grid(row=iRow,column=1)

iRow +=1
MinmengeLabel = Label(window, text='Min. Menge')
MinmengeLabel.grid(row=iRow,column=0)
Minmenge = Entry(window)
Minmenge.insert(0,0.02)
Minmenge.grid(row=iRow,column=1)
#Die Mindestmenge muss mindestens einem Wert von 60,00 € entsprechen
#(ca. 0,02 BTC bei dem von Ihnen vorgegebenen Kurs von 3.000,00 € / BTC).
#Falls der Preis unter 3000€ liegt muss die Mindest Menge angepasst werden.

iRow +=1
Kaufenbutton = Button(window, text='Kaufen / Kauforder einstellen', command= lambda: KaufOrder())
Kaufenbutton.grid(row=iRow,column=0)
Verkaufenbutton = Button(window, text='Verkaufen / Verkaufsorder einstellen', command= lambda: VerkaufOrder())
Verkaufenbutton.grid(row=iRow,column=1)

iRow +=1
OrderIDLabel = Label(window, text='Order ID')
OrderIDLabel.grid(row=iRow,column=0)
OrderIDInput = Entry(window)
OrderIDInput.grid(row=iRow,column=1)

iRow +=1
DeleteOrderbutton = Button(window, text='Kauf-/Verkaufsorder löschen', command= lambda: DeleteOrder())
DeleteOrderbutton.grid(row=iRow,column=1)

iRow +=1
ExecutesellOrderbutton = Button(window, text='Verkaufen / Verkauforder ausführen', command= lambda: ExsellOrder())
ExecutesellOrderbutton.grid(row=iRow,column=0)
ExecutebuyOrderbutton = Button(window, text='Kaufen / Kauforder ausführen', command= lambda: ExbuyOrder())
ExecutebuyOrderbutton.grid(row=iRow,column=1)

iRow +=1
i =0
BTCGuthabenbutton = Button(window, text='Guthaben updaten', command= lambda: AmountUpd())
BTCGuthabenbutton.grid(row=iRow,column=2)
i +=1
BTCGuthaben = Label(window, text='BTC Guthaben')
BTCGuthaben.grid(row=iRow+i,column=2)

i +=1
BCHGuthaben = Label(window, text='BCH Guthaben')
BCHGuthaben.grid(row=iRow+i,column=2)

i +=1
ETHGuthaben = Label(window, text='ETH Guthaben')
ETHGuthaben.grid(row=iRow+i,column=2)

Hinweis = """
Verwendung auf eigene Gefahr! Ich übernehme keine Haftung!

Funktionen der Buttons:
BTC kaufen/Kauforder einstellen: Bei ausreichender Reservierung wird eine Kauforder mit angegebener Max.Menge, Min.Menge und Preis pro BTC eingestellt.

BTC verkaufen/Verkauforder einstellen: Bei ausreichendem BTC Guthaben wird eine Verkauforder mit angegebener Max.Menge, Min.Menge und Preis pro BTC eingestellt.

Order-ID: Hier wird entweder die Order-ID der Kauf bzw Verkauforder angezeigt oder es kann eine beliebige Order-ID eingegeben werden.

Kauf-/Verkaufoder löschen: Löscht Order mit der in Order-ID eingegebenen Order-ID

BTC kaufen / Kauforder ausführen: Sie müssen Max.Menge die Sie kaufen möchten und Order-ID der gewünschten Order eingeben. Mit klicken auf den Button wird die gewünschte Order ausgeführt.

BTC verkaufen/ Verkauforder ausführen: Sie müssen Max.Menge die Sie verkaufen möchten und Order-ID der gewünschten Verkauforder eingeben. Mit klicken auf den Button wird die gewünschte Order ausgeführt.

BTC-Guthaben: verfügbares Guthaben auf Ihrem Bitcoin.de Account wird angezeigt.
"""

tkinter.messagebox.showinfo("Hinweis", Hinweis)

window.mainloop()
