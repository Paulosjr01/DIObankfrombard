from flask import Flask, render_template, request
from datetime import datetime



app = Flask(__name__, template_folder="templates")
#app.debug = True

# Initialize account balance and transaction history (empty list)
balance = 0
transactions = []
now = datetime.now()

@app.route("/")
def index():
  return render_template("index.html", now=now, balance=balance, transactions=transactions)

@app.route("/process", methods=["POST"])
def process():
  global balance, transactions
  operation = request.form["operation"]
  amount = float(request.form["amount"]) if request.form["amount"] else 0

  if operation == "deposit":
    balance += amount
    transactions.append(f"Deposit: ${amount:.2f}")
  elif operation == "withdraw" and balance >= amount:
    balance -= amount
    transactions.append(f"Withdrawal: -${amount:.2f}")
  else:
    # Handle insufficient funds for withdrawal
    transactions.append("Insufficient Funds")

  return render_template("index.html", balance=balance, transactions=transactions)

if __name__ == "__main__":
  app.run(debug=True)