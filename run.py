from eve import Eve
#from tendo import singleton
#me = singleton.SingleInstance()

app = Eve()

if __name__ == '__main__':
    app.run(debug=True)