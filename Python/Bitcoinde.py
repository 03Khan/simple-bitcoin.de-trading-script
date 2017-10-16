#! /usr/bin/env python
import btcde
import sys
import tkinter.messagebox
# connection settings
api_key = 'DEIN API KEY'
api_secret = 'DEIN API SECRET'
# trade data

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
	

new_order_for_remaining_amount = 1

def KaufOrder():
  conn = btcde.Connection(api_key, api_secret)
  order = btcde.createOrder(conn, OrderType = 'buy', max_amount = float(Mengeeingabe.get()), price = float(Preiseingabe.get()), min_amount = float(Minmenge.get()), new_order_for_remaining_amount = new_order_for_remaining_amount)
  OrderIDInput.delete(0, END)
  OrderIDInput.insert(0,str(order.get('order_id')))

def VerkaufOrder():
  conn = btcde.Connection(api_key, api_secret)
  order = btcde.createOrder(conn, OrderType = 'sell', max_amount = float(Mengeeingabe.get()), price = float(Preiseingabe.get()), min_amount = float(Minmenge.get()), new_order_for_remaining_amount = new_order_for_remaining_amount, payment_option = 3)
  OrderIDInput.delete(0, END)
  OrderIDInput.insert(0,str(order.get('order_id')))
  
def  DeleteOrder():
	conn = btcde.Connection(api_key, api_secret)
	order = btcde.deleteOrder(conn, order_id = OrderIDInput.get())
	OrderIDInput.delete(0, END)
	
def  ExsellOrder():
	conn = btcde.Connection(api_key, api_secret)
	order = btcde.executeTrade(conn, order_id = OrderIDInput.get(), OrderType = 'sell', amount = float(Mengeeingabe.get())) 	

def  ExbuyOrder():
	conn = btcde.Connection(api_key, api_secret)
	order = btcde.executeTrade(conn, order_id = OrderIDInput.get(), OrderType = 'buy', amount = float(Mengeeingabe.get())) 	
		
def  AvAmount():
	conn = btcde.Connection(api_key, api_secret)
	account = btcde.showAccountInfo(conn)
	dic= (account.get('data'))
	AvAmount = ((dic['btc_balance']['available_amount']))
	Mengeeingabe.delete(0, END)
	Mengeeingabe.insert(0,AvAmount)
		
	
window = Tk()
window.title('Bitcoin.de Trading')
window.geometry('600x400')

Mengeeingabe = Entry(window)
Mengeeingabe.grid(row=0,column=0)
MengeeingabeLabel = Label(window, text='Max.Menge in Bitcoin')
MengeeingabeLabel.grid(row=0,column=1)

Preiseingabe = Entry(window)
Preiseingabe.grid(row=1,column=0)
PreiseingabeLabel = Label(window, text='Preis in €/Bitcoin')
PreiseingabeLabel.grid(row=1,column=1)

Minmenge = Entry(window)
Minmenge.insert(0,0.02)
Minmenge.grid(row=2,column=0)
#Die Mindestmenge muss mindestens einem Wert von 60,00 € entsprechen
#(ca. 0,02 BTC bei dem von Ihnen vorgegebenen Kurs von 3.000,00 € / BTC).
#Falls der Preis unter 3000€ liegt muss die Mindest Menge angepasst werden.

MinmengeLabel = Label(window, text='Min.Menge in Bitcoin')
MinmengeLabel.grid(row=2,column=1)

Kaufenbutton = Button(window, text='BTC kaufen / Kauforder einstellen', command= lambda: KaufOrder())
Kaufenbutton.grid(row=3,column=0)
Verkaufenbutton = Button(window, text='BTC verkaufen / Verkaufsorder einstellen', command= lambda: VerkaufOrder())
Verkaufenbutton.grid(row=3,column=1)

OrderIDInput = Entry(window)
OrderIDInput.grid(row=4,column=0)

OrderIDLabel = Label(window, text='Order ID')
OrderIDLabel.grid(row=4,column=1)

DeleteOrderbutton = Button(window, text='Kauf-/Verkaufsorder löschen', command= lambda: DeleteOrder())
DeleteOrderbutton.grid(row=5,column=1)

ExecutesellOrderbutton = Button(window, text='BTC verkaufen / Verkauforder ausführen', command= lambda: ExsellOrder())
ExecutesellOrderbutton.grid(row=6,column=0)

ExecutebuyOrderbutton = Button(window, text='BBTC kaufen / Kauforder ausführen', command= lambda: ExbuyOrder())
ExecutebuyOrderbutton.grid(row=6,column=1)

BTCGuthabenbutton = Button(window, text='BTC Guthaben', command= lambda: AvAmount())
BTCGuthabenbutton.grid(row=8,column=0)

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