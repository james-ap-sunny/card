from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# 连接到云数据库 MySQL
conn = mysql.connector.connect(
    host='card.corebanking.com',
    user='root',
    password='Areuok222',
    database='test'
)
cursor = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def display_card_info():
    if request.method == 'POST':
        card_number = request.form['card_number']
        
        # 查询数据库中对应卡号的记录
        cursor.execute("SELECT * FROM card WHERE card_number=%s", (card_number,))
        record = cursor.fetchone()
        
        if record:
            # 获取记录的其他字段
            account_date = record[1]
            balance = record[2]
            
            return render_template('result.html', account_date=account_date, balance=balance)
        else:
            return render_template('result.html', error_message='Card not found')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
# 关闭数据库连接
conn.close()
