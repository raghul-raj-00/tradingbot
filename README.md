🔑 Setup Instructions
1. Clone the repository
git clone https://github.com/raghul-raj-00/tradingbot.git
cd tradingbot
2. Install dependencies
pip install -r requirements.txt
3. Create Binance Testnet API Keys
Go to: https://testnet.binancefuture.com
Login / Register
Navigate to API Management
Create a new API key
4. Create .env file

Create a .env file in the root directory:

BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here

⚠️ Important:

Do NOT add quotes
Do NOT share this file
Ensure .env is in .gitignore
5. Add Test Funds
Open: https://testnet.binancefuture.com/en/futures/BTCUSDT
Use the Faucet / Get Test Funds option
▶️ How to Run
🔹 MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.1
🔹 LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.1 --price 30000
📊 Sample Output
=== ORDER SUMMARY ===
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.1

=== RESPONSE ===
Order ID: 12345678
Status: FILLED
Executed Qty: 0.1
Avg Price: 29850

✅ SUCCESS
📁 Logs

Logs are stored in:

logs/app.log

Includes:

API requests
API responses
Errors
