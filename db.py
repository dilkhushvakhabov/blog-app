import psycopg2




def get_posts():
    try:
        conn = psycopg2.connect(dbname="blog_app", user="postgres", password="123", host='localhost', port=5432)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM posts')
        
        posts = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return [{'id': post[0], 'title': post[1], 'content': post[2]} for post in posts]
    except Exception as e:
        print('DB ERROR')