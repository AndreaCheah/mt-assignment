from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # return "Flask heroku app :)"
    # Table 1
    table1_data = {
        "Index #": ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18", "A19", "A20"],
        "Value": [41, 18, 21, 63, 2, 53, 5, 57, 60, 93, 28, 3, 90, 39, 80, 88, 49, 60, 26, 28]
    }
    df = pd.DataFrame(table1_data)
    # print(df)
    
    # Table 2
    # Alpha value
    A5 = df.loc[df["Index #"] == "A5", "Value"].values[0]
    A20 = df.loc[df["Index #"] == "A20", "Value"].values[0]
    alpha_value = A5 + A20
    print(alpha_value)

    # Beta value
    A15 = df.loc[df["Index #"] == "A15", "Value"].values[0]
    A7 = df.loc[df["Index #"] == "A7", "Value"].values[0]
    beta_value = A15 / A7 if A7 != 0 else "undefined"
    print(beta_value)

    # Charlie value
    A13 = df.loc[df["Index #"] == "A13", "Value"].values[0]
    A12 = df.loc[df["Index #"] == "A12", "Value"].values[0]
    charlie_value = A13 * A12
    print(charlie_value)

    table_1 = df.to_html(index=False)
    table_2 = [
        {"Category": "Alpha", "Value": alpha_value},
        {"Category": "Beta", "Value": beta_value},
        {"Category": "Charlie", "Value": charlie_value}
    ]

    print(render_template('index.html', table_1=table_1, table_2=table_2))
    return render_template('index.html', table_1=table_1, table_2=table_2)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()

# index()