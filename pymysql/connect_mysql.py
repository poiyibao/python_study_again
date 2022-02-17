from typing import ItemsView, List
import pymysql
db = pymysql.connect(
    host='sh-cynosdbmysql-grp-815ahyxk.sql.tencentcdb.com',
    port=20301,
    user='root',
    passwd='Yb1612409282',
    db='shop'
)
cursor = db.cursor(pymysql.cursors.DictCursor)
def select(sql, args):
    cursor.execute(sql, args)
    result = cursor.fetchall()
    #print(result)
    #db.commit()
    cursor.close()
    db.close()
    return result

def clearData(li):
    clearLi = []
    for item in li:
        #print(item.values())
        clearLi.append(item['Concat(`学号`,`姓名`, `成绩`)']) 
    return clearLi


if __name__ == "__main__":
    #sql = 'UPDATE Product SET product_id = %s WHERE sale_price = %s;'
    sql = 'SELECT DISTINCT Concat(`学号`,`姓名`, `成绩`) FROM Courses ORDER BY %s'
    re = select(sql, ('学号'))
    li = clearData(re)
    print(li)


