# codebase-cleanup-template
(Worked with Krish Sarawgi)

To get started with the ["Codebase Cleanup" Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/codebase-cleanup/README.md).

## Setup

Create virtual environment:

```sh
conda create -n cleanup-env python=3.8
```

```sh
conda activate cleanup-env
```

Install packages:

```sh
pip install -r requirements.txt
```


## Configuration

Obtain a premium AlphaVantage API Key [here](https://www.alphavantage.co/).

Sign up for a [SendGrid Account](https://sendgrid.com/), verify single sender, then obtain a Sendgrid API Key. 


Set environment variables using a ".env" file approach:

```sh
ALPHAVANTAGE_API_KEY="..."

SENDER_ADDRESS="example@gmail.com"
SENDGRID_API_KEY="SG...."
```


## Usage

Run the game:

```sh
python app/game.py
```

Run the inventory report: 

```sh

python -m app.groceries
```

Run the stocks report: 

```sh

python -m app.stocks
```

Run the crypto report: 

```sh

python -m app.crypto
```

Run the utils unofficial to_usd test:

```sh

python -m app.utils
```

Run the unemployment report: 

```sh

python -m app.unemployment
```

Run the unemployment email app: 

```sh 

python -m app.unemployment_email
```

Run the email app: 

```sh

python -m app.email_me 
```

## Testing 

Run Tests:

```sh 

pytest
```

